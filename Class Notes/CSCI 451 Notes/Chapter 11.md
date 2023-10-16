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

Teh I-list follows the superblock. The size (# of blocks allocated / number of I-nodes) of the I-list may vary from drive to drive

The storage space (for file contents) follows the I-list and makes up the remainder of the drive

**Partitions**
partitions are low level structures on which directories and files reside. A single drive can be broken into several partitions or several drives can be combined into a single partition (even across networked machines)
