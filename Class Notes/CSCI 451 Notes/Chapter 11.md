%% 10/16/23 %%

**Disk Organization:**
**DOS:**
BIOS locates the sectors by a 3D number scheme (cylinder number, head number, sector number)

DOS only uses sector numbers and numbers the sectors sequentially from outside to inside. The numbering scheme starts with cylinder 0, head 0, and sector 1 (in BIOS terms) and continues through the remainder of the disk

The boot record is always a single sectors located at cylinder 0, head 0, and sector 1. The boot record contains information on how to start the OS, All disks have a boot record even if its not used.

The FAT follows the boot record at cylinder 0 ,head 0, and sector 2, The size (# of sectors allocated to it) of the FAT may vary from drive to drive

The directory follows the FAT, The size of the directory may vary from drive to drive

**UNIX:**
BIOS locates the sectors by a 3D number scheme (cylinder number, head number, sector number)

Unix uses a file system based on blocks (each block is one or more sectors)

The first block of the **partition** is always for bootstrapping (even if its not required)

The super block follows. The superblock contains system attributes and file system metadata

The I-list follows the superblock. The size (# of blocks allocated / number of I-nodes) of the I-list may vary from drive to drive

The storage space (for file contents) follows the I-list and makes up the remainder of the drive

**Partitions**
partitions are low level structures on which directories and files reside. A single drive can be broken into several partitions or several drives can be combined into a single partition (even across networked machines)

**_File Allocation Table (FAT)_**
File-allocation table (FAT) used by dos and OS/2 is an important variation on the linked list idea
- The FAT is stored at the beginning of each partition
- The FAT has one entry for each disk block and is indexed by block number
- The directory entry contains the block number on the first block of the file
- The FAT entry (indexed by that block number) contains the block number of the next block of the file
- Unused blocks have a FAT entry of 0
- Bad blocks are also recorded in the FAT
*Read a file* - search directory for the file. Use directory's start value to determine where the FAT the file starts. Use  the FAT to determine which disk blocks hold the file.
Write a new file - search the directory for the file. Append the name, start block, etc on directory. Search the FAT to find enough unused disk blocks to hold the file.
*Erase a file* - search the directory for the file. Use directory's start value to determine where in the FAT the file starts. Use FAT to determine which other FAT entries are used by the file. We then remove these entries and the file data from the directory.
*Overwrite a file* - search the directory for the file. Use the directory's start vale to determine where in the FAT the file starts. use the FAT to determine which other FAT entries are used by the file. We then:
- remove the entries from the FAT and write the file as if it were a new file.
- leave the FAT alone. Replace the disk blocks with new data.

I-Node:
I-NODE used by UNIX is a variation on the indexed idea:
- each file has its own I-node. Unlike DOS's FAT, the I-nodes only exist for files Empty blocks do not have an I-node
- The directory entry (a simple file in UNIX) contains the I-node number for each file
- The I-node contains information about the file. It also contains an index (multi-)
The i-node can directly hold up to 10 disk block locations. Making small files (< 10 blocks) efficient to load

The size of the i-node (size of the disk block) determines how big a file can be.

UNIX links: 
in UNIX we can create two types of pointers (links) to other directories (very useful)
1. symbolic links