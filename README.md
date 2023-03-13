# Optimal_Unlabeled_Set_Partitioning
The codes serve for my paper "Optimal Unlabeled Set Partitioning with Application to Risk-based Quarantine Policies" published in IISE transactions. 

# Description
The algorithm using a reformulation techanique in which the set partitioning problem is cast as a more tractable network flow problem.
The modified implementation of the algorithm is to find the optimal shortest path with at most K edges.

The algorithm was used to develop a Risk-based quarantine policy application. The following code was used to generate the results presented in the paper. However, it is important to note that the files provided only include the results and not the plots for illustration. Additionally, the results presented in the paper were executed by HPRC (High Performance Research Computing), using parallel computing, due to the long running time required.


# Files

## Main algorithm

File: ESP_constrained.py

The file generates the optimal solution for a given set of parameters, including the optimal partition, the optimal number of partitions, and the corresponding objective value. The results presented in Table 1 of the paper are generated based on this file.

All the results can be generated on the basis of this file by adding necessary loops and modifictaions. For example:

## Figure 2 

Simply add necessary loops to ESP_constrained.py under the entire spectrum of $\mu$ and $\beta$.

## Figure 3 & Figure 6 (Supplemental File)

File: Thresholds.py

Added necessary Use ESP_constrained.py to explore the two thresholds the entire spectrum of $\beta$ under a given $\mu$. The outputs include the optimal number of partitions and the optimal number of risk thresholds.









