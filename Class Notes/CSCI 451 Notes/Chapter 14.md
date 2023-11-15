Computer Security

**Goals:**
- Prevent mischievous, intentional violations of access restrictions.
- to ensure that each program use system resources only in ways consistent with stated policies

**Policy vs Mechanism:**
- policies determine what will be allowed or what will be done
- Mechanisms determine how it will be done

Confidentiality - generally covers privacy issues

Integrity - Generally covers data integrity (data is correct) and system integrity (system does what it is supposed to).

Availability - System is available to authorized users

Protection is a problem internal to the system. Security is a problem external to the system.

Security is primarily concerned with the loss of data or the dissemination of data.
Data loss/ dissemination can occur because of:
- acts of god (fires, floods, rats, wars , riots, etc).
- Hardware failures
- Software errors/
- Human errors (data entry errors, lost tapes, accidental erasures).
- Casual snooping by non-technical users (loss of secrets).
- Snooping by technical users who find it a challenge to break the security barriers (loss of secrets)
- Malicious snooping by technical users who need to break the security barriers (in order to rob money or secrets).
- Commercial and military espionage.

**Levels:**
Physical or External - The site or sites must be secure against intrusion. The site or sites must be secure against acts of god
- offsite backups along with UPS/surge suppressors
- hot site/cold site to provide backup computing capability
- in some cases. physically secure systems cannot be on the net

Human or operational - users must be screened before accounts are given which would give them access to secure data.
- system administrators are given different responsibilities to insure that no one administrator has complete access to the system.
- important documents must be shredded
- magnetic materials must be degaussed
- tempest

**Guidelines:**
Formulation of security requirements has been of primary concern to the U.S. Government. 3 documents specifically deal with computer security issues:
- DOD Directive 5200.28 - specifies how classified material is to be handled in data processing systems
- Computer security technology reference manual - specifies how to evaluate the security of U.S Air force computer systems
- the privacy act of 1974 - requires federal agencies to ensure the integrity and security of information about individuals
- NIST (Preliminary) Cybersecurity Framework.

**Classifications:**
The U.S. DOD trusted computer system evaluation criteria specifies 7 levels of computer security. These are:
1. D - Lowest level of security. Examples include DOS and Windows9x
2. C1 - Incorporates some form of controls to protect private information and to prevent other users from accidentally reading or destroying that private data Examples include most unix systems and windows XP
3. C2 - adds to the requirement of a C1 system an individual level access control. Examples include some special certified versions of UNIX
4. B1 - Adds to the requirements of a C2 system that security labels be attached to files. This prevents anyone without the proper security level from reading a file
5. B2 - Adds to the requirements of a B1 system that the security labels are also attached to system resources (disks, etc)
6. B3 - adds to the requirements of a B2 system the creation of access control lists. The system is also capable of monitoring events and notifying the system admin of security violations
7. A - same as B3, except the security methodology is proven using formal methods

- another computer security criteria is TEMPEST; which guards against electronic eavesdropping by requiring EM shielding of the system

**Threats:**
Unauthorized disclosure - threat to confidentially:
- exposure of information - usually by and insider of system failure.
- Interception of information - usually via a network
- Inference of information - usually via traffic analysis

**Viruses:**
- file - a file virus attaches itself to an executable file, causing it to run the virus code first and then jump to the start of the original program. These viruses are termed parasitic, because they do not leave any new files on the system, and the original program is still fully functional.
- Boot - A boot virus occupies the boot sector, and runs before the OS is loaded. These are also known as memory viruses, because in operation they reside in memory, and do not appear in the file system.
- Macro - these viruses exist as a micro (script) that are run automatically by certain macro-capable programs such as MS Word or Excel. These viruses can exist in word processing documents or spreadsheet files
- Source code viruses look for source code and infect it in order to spread
- Polymorphic viruses change every time they spread - Not their underlying functionality but just their *signature*, by which virus checkers reorganize them.
- Encrypted viruses travel in encrypted form to escape detection. In practice they are self-decrypting, which then allows them to infect other files.
- Stealth viruses try to avoid detection by modifying parts of the system that could be used to detect it.
- Tunneling viruses attempt to avoid detection by inserting themselves into the interrupt handler chain, or into device drivers
- Multipartite viruses attack multiple parts of the system, such as files, boot sector, and memory
- armored viruses are coded to make them hard for anti-virus researchers to decode and understand. In additions many files associated with viruses are hidden, protected, or given innocuous looking names such as "..."

**Human Threats:**
- Request memory pages - Request memory pages, disk pages, or tapes and just read them. They may be full of interesting info
- Browsing - When a user snoops into another's directories or files.
- Masquerade - Using another's account name and password. Or, as is common on campus, using another's account when they've left it active and walked away from the machine.