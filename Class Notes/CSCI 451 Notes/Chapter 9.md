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

