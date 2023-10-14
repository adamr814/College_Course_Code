:: 9/22/23 ::

Deadlock

Prevention:
Havender (1968)

**Avoidance**
- ostrich algo
- resource allocation graph algo
- dijkstras algorithm

**detection:**
a popular notion to use resource allocation graphs to detect deadlock. However, since these algorithms incur overhead, the question is "How often should we invoke the algorithm? possible answers include:
- every time a resource request is made and refused
- at fixed intervals
- when CPU usage is low (deadlock eventually cripples the system)

reduction of resource allocation graphs - whenever a process's resource requests are granted, the corresponding edges in the resource allocation graph are removed

**recovery:**
Deadlock must be removed from the system
    
Deadlock recovery is difficult because of:
1. it may not be clear that the system is in a state of deadlock
2. most systems have poor facilities for suspending a process, removing it from the system, and resuming it at a later time
3. Deadlock recovery facilities incur overhead and typically require a skilled operator to manage them
4. recovering from a deadlock of modest proportions requires work. Recovering from deadlock on a grand scale requires an enormous amount of work

    Deadlock recovery generally has four options:
    1. abort all deadlocked processes
    2. abort 1 process at a time until the deadlock is broken
    3. rollback deadlocked processes to some "safe" state
    4. preempt 1 resource at a time until the deadlock is broken

    However 3 and 4 require some effective suspend/resume mechanism (like databases) However, to date, few operating systems include this type of mechanism
    (suspend/resume and checkpoint/restart)

    However, aborting processes has problems also, For example:
    - the deadlocked processes may all have the same priority
    - the priorities may be muddled by special considerations

    If we could choose preemption/aborting, we still have issues:
    - how do we select a victim?
    - what do we do with the preempted process?
    - how do we guarantee that the same process will not always be preempted?

Starvation:
    Starvation (aka indefinite postponement) occurs when a process is waiting for an event that may never occur because of biases (or poor design?_ of the
    scheduling method)

    in deadlock, the process can be resolved if one of the processes terminates. in starvation, the problem is (or can be) caused by a process terminating.