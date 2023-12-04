**Distributed Systems**
*clusters:*
an alternative to multiprocessor machines is clusters of machines. Reasons include:
- scalability - add more machines get more power
- availability - fault tolerance
- price/performance - mainframe computers simply cannot match the performance per dollar that clusters can. In many cases, mainframe computers simply cannot match the performance at any price.

Clusters have 2 major classifications:
1. passive standby - where one machine does all the processing, unless it fails.
2. Active secondary - where all of the machines share in the processing

Cluster design issues:
- fault tolerance - increased hardware increases the probability of some failure
- load balancing - data processing gets more complex (synchronization)
- Parallelizability - increased algorithm complexity (network communications)

