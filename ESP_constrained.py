#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys;

import time
import csv
import pandas as pd

import numpy as np
import random
from random import randint
from scipy import stats
import csv 



def simu_nodes(import_risk,Simu_time,items_number):


    risk_vector=np.zeros([Simu_time,items_number])


    for k in range(Simu_time):
        risk_index=sorted([randint(0, len(import_risk)-1) for p in range(0, items_number)])

    
        for i in range(0,items_number):
            risk_vector[k][i]=import_risk[risk_index[i]]



    ###Average 
    risk_final=np.zeros(items_number)
    for i in range(items_number):
        s=0
        for k in range(Simu_time):
            s=s+risk_vector[k][i]
            #print(s)
        risk_final[i]=s/Simu_time

    return sorted(risk_final)


def CB_Partition(S,beta):
    Obj=0
    if len(S) ==1:
        Obj=-(mu*(1-S[0])+(1-mu)*(1-S[0]))**beta
    

    else:
        Prod=1
        Sum=0

        for i in range(0,len(S)):
            Prod=Prod*(1-S[i])
            Sum=Sum+(1-S[i])
        
        #print(Sum)
        #print(Prod)
        Obj=-(len(S)*mu*Prod+(1-mu)*Sum)**beta
        #print(Obj)
    return Obj



class Node(object):
    def __init__(self,name):
        self.name =name
        self.visited =False
        self.predecessor = None
        self.adjacenciesList=[]
        self.minDistance =sys.maxsize
        

class Edge(object):
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

def normalize(vector, scale):
    for i in range(0,len(vector)):
        vector[i]=vector[i]/scale
    return vector

#Data impor- random data for demonstration purpose
xk=[0.0 for i in range(25)]
xk=np.array(xk)
xk[0]=321.0
xk[1]=853.0
xk[2]=495.0
xk[3]=1507.0
xk[4]=303.0
xk[5]=1020.0
xk[6]=1010.0
xk[7]=2463.0
xk[8]=2740.0
xk[9]=1051.0
xk[10]=2240.0
xk[11]=2480.0
xk[12]=6660.0
xk[13]=7488.0
xk[14]=1720.0
xk[15]=1858.0
xk[16]=2769.0
xk[17]=3981.0
xk[18]=7887.0
xk[19]=1223.0
xk[20]=1708.0
xk[21]=2532.0
xk[22]=1078.0
xk[23]=4340.0
xk[24]=1260.0


qk=[0.000939177, 0.003834568, 0.017673612, 0.005585304, 0.04265668,
    0.002721221,0.011721494,0.017673612,0.017167917,0.133505235,
    0.0036928,0.022788632,0.025510345,0.021416087,0.242884882,
    0.002310636,0.008872188,0.017673612,0.008491278,0.22206038,
    0.00093105,0.003147995,0.017673612,0.001999607,0.147068075
    ]

custm = stats.rv_discrete(name='custm', values=(xk, qk))


Simu_time=10000 #order statistics: simulate time
N_items=100 #number of items
np.random.seed(1) 
risk_vector_simu=np.zeros([Simu_time,N_items])

for k in range(Simu_time):
    
    r = sorted(custm.rvs(size=N_items))
    #print(r)
    
    for j in range(N_items):
        risk_vector_simu[k][j]= r[j] 
    
#print(risk_vector_simu)

risk_vector=np.zeros(N_items)


for i in range(len(risk_vector)):
    sum_simu=0
    
    for k in range(Simu_time):
        sum_simu=sum_simu+risk_vector_simu[k][i]

    risk_vector[i]=(sum_simu/Simu_time)/100000


#print final risk vector as input
print(risk_vector)




#paratmeters:

#Transmission Rate
mu=0.491
#contrianed, maximum edges(subgroups) allowed <n-1
k_max=5
beta=1.15

risk_index=list(range(1, len(risk_vector)+2)) # N+1 nodes, node starts #1







#Create Node list and Edge list

node_list=[0]*(len(risk_vector)+1)
c_list=(range(1,len(risk_vector)+2))

for i in range(0,len(risk_vector)+1):
    node_list[i]=Node(c_list[i])
    #print(node_list[i].name)
    

edge_list=[0]*999999 ##define how many edges exactly later to save the running space
Q=0 # Test how many edges total 
for i in range(0,len(risk_vector)+1):
    for j in range(i+1,len(risk_vector)+1):
            #print(i)
            #print(j)
            risk_subgroup=[0]*(j-i)
            for k in range(0,j-i):
                risk_subgroup[k]=risk_vector[i+k]
            #print(risk_subgroup)
            
            weig_edge=CB_Partition(risk_subgroup,beta)

            edge_list[Q]=Edge(weig_edge,node_list[i],node_list[j])
            #print('i,j, weight', i,j,weig_edge)
            #print('#i:',i) #startnode
            #print('#j:',j) #endnode
            #print('#Q:',Q)
            node_list[i].adjacenciesList.append(edge_list[Q])
            Q=Q+1
            

            

#Algorithm Prep
k_atmost=len(risk_vector)+1
v_nodes=len(risk_vector)+1

D=[[sys.maxsize for x in range(v_nodes)] for y in range(k_atmost)]  #D List: Save the Shortest Path

P=[[-1 for x in range(v_nodes)] for y in range(k_atmost)] # P List: Store the vertex just before vertex on the shoretst path

    
edgeList=[]
for i in range(0,Q):
    edgeList.append(edge_list[i])
#print(D)     
#print(P)




         
#Algorithm

startVertex=node_list[0]
D[startVertex.name-1][0]=0


K=len(risk_vector)+1
for k in range (1,K):
    
    for i in range(0,v_nodes-1):
        D[k][i]=D[0][i]
        #print(D)
        

    for edge in edgeList:
        u= edge.startVertex.name-1
        v= edge.targetVertex.name-1
        
        #print("start:",u)
        #print("end:",v)
        #print("edge.weight:",edge.weight)
        
        newDistance=D[k-1][u]+edge.weight
        
        #print("new",newDistance)
        #print("------")
        
       

        if newDistance < D[k][v]:
            D[k][v]=newDistance
            P[k][v]=edge.startVertex.name
            #print('k,u,v;',k,u,v)
            #print(D[k][v])
            #print(k)
            #print(P)
            #print('------')

#Results Output

print("Shortest path exists with value:", D[k_max][len(risk_vector)])
V=len(risk_vector)


print("Node:",V+1)

k=0
for i in range(0,V):
        
    if V==1:
        i=i+sys.maxsize
        
    else:
        V=P[k_max-i][V-1]        
        print("Node:",V)
    
        k=k+1
        i=i+1
print("Total number of partitions:",k) 















                    