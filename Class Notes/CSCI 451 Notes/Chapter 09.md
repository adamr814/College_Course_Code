%% 10/2/23 %%

**Paged Memory Allocation**
paging is a method used to manage the overlay process in virtual memory systems (UNIX and Windows 10 are virtual memory systems)

paging requires the memory to be divided into equal sized chunks. Physical memory chunks are called **page frames** and logical/virtual memory chunks are called **pages**. the frames are always of equal size. a data structure is used to log the location and use of each page.
* paging allows noncontiguous memory allocation.
* paging is a form of dynamic relocation
* paging eliminates eliminates external fragmentation (any free page frame can be allocated to any waiting page).
* paging does not eliminate internal fragmentation

**Virtual Memory**
by using the hard drive as a "backing store" virtual memory makes it look like there is more random access memory (RAM) than actually exists, allowing the computer to run larger programs and multiple programs concurrently.

To support virtual memory, the memory space must be broken up into small blocks called **pages**

The key to improving access performance is to rely on locality of reference to the page tale. the translation look-aside buffer (TLB) keeps track of recently used address mappings to trey to avoid an access to the page table. The TLB includes five fields:
* valid but: ON if the page is in memory and the entry contains the physical page number
* reference bit: On every reference, the virtual page number in the TLB is checked. If it is a hit, the physical page number is used to form the address and the corresponding reference bit is turned ON.
* Dirty bit: if the processor is performing a write, the dirty bit is turned ON.
* Tag entry: because the TLB is a cache, it must have a tag field, which holds (a portion of) the virtual page number.
* Data entry: it holds a physical page number.

The page table either supplies a physical page number for the page (which can be used to build a TLB entry) or indicates that the page resides on disk (indicating a fault). Since the page table has an entry for every virtual page, no tag field is needed.

**Paging Performance:**
- page-buffering - the OS keeps a set of free pages, so it can load a page and get the process started before spending the time to write the replaced page out to disk.
- Pre-paging - The working set pages (or neighboring pages) are loaded before execution starts.
- Paging on demand - Pages are not loaded into memory until they are required.
- Proportional allocation - Allocate the number of frames based on the size of the program.
Local vs global allocation policies - When the OS chooses a page to remove does the OS only consider pages belonging to the process causing the page fault (local policy) or does the OS consider all pages (global policy)?
	Generally, global policies work better.
	Cleaning - When does the OS synchronize a page with that on the disk? Two common methods:
1. Demand Cleaning - A "dirty" page is written out only when selected for replacement
2. Pre-cleaning - writes a "dirty" pages out before selected for replacement. Allows for "batch" writes to disk.

**Thrashing:**
Thrashing - When page faults occur every few instructions. Typically, the case is that several processes will be in contention for memory space and (assuming a global allocation policy) will generate page faults that will remove each other pages. It's a vicious cycle.

We can run into a similar problem when we have a shared file system (on a server). As more and more processes request a file from the server, the server get backlogged. However, this is not the same thing as thrashing:

Methods to reduce thrashing include:
1. local allocation policy.
2. Page fault frequency (PFF) allocation - With Least-Recently-Used (LRU), increasing the number of pages available reduces the number of page faults. Therefore, if a process is generating a lot of page faults, we would remove some other processes page(s) giving problem processes more pages to work with.
3. Working-Set model allocation - we keep track of N currently active pages for each process. The OS only allows a degree of multi-programing such that each process can be allocated its working-set of pages. Prevents thrashing and provides a near optimal use of memory however it is expensive to implement and the determination of N is/can be difficult.

