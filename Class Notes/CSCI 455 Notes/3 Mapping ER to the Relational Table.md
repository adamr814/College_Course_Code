Chapter 3 and Chapter 9
## Converting ER Diagrams to Relational Tables
- Key Concepts
	- Primary Key (PK)
	- Optional-Max Conversion
	- Foreign Key (FK)
	- Intersection Table
## Basic Conversion Rules
- Three basic rules to convert ER into tables:
	- For a 1:1 cardinality relationship, either
		- merge all the attributes into a single table (bad)
		- or use the foreign key/primary key approach (good)
	- For a 1:N cardinality relationship
		- Post the PK from the "one" side as an attribute into the "many" side
	- For N:M cardinality relationships
		- Create a brand-new table (intersection)
		- Post the PKs from each participating entity as attributes in the new table

## The optional-max conversion process
- The upper bound is used to determine what relational tables will be created
- The lower bound is used to determine if the upper bound should be treated as a "many"
	- e.g.,
		- Treat (0,1) as many (N)
		- the lower cardinality bounds are optional (0)
		- upper cardinality bounds are one (1)
## Conversion guidelines
- construct an ER diagram, and label the upper bounds
	- all multi-valued attributes should be represented as an entity
	- if the lower bound = 0 and the upper bound = 1, then label the upper bound as N
	- use the entity name for each entity as the table name
	- select a PK for each table
	- take all the attributes that describe an entity and post them as column names in the relational table
- For 1:1, merge all the attributes into a single table or use PK/FK approach
- For 1:N, take the ID of the "one" side of the 1:N and post it as an attribute to the "many" side
- For N:M, create a new table (intersection) and use the relationship name as the name for the table
	- Take any additional attributes that describe entities or relationships and post these as column names in the appropriate relational table.
- Decompose composite attributes into simple or atomic attribute

Example: Tables and attributes
- Suppose the base tables have the following attributes
```
FACULTY: FID (PK), FNAME, LNANME
COURSE: CID (PK), CNAME, CREDIT
STUDENT: SID (PK), FNAME, LNAME
MAJOR: MID (PK), DESCRIPTION
LOCKER: LID (PK), BUILDING
HOME-ADDRESS: HSTREET, HCITY, HSTATE
```
## Create Tables (some examples)
- Identify One-To-One RELATIONSHIP (1 relationship)
	- Tables:
		- Student
		- HomeAddress
	- Merge two tables or use One-Side-To-Many-Side
		- Student (**SID**, FNAME, LNAME, HSTREET, HCITY)
- Identify One-To-Many RELATIONSHIP (1 relationship)
	- Tables:
		- Student
		- Major
	- Post PK of One Side (i.e., MID) to Many Side
		- Student (SID, FNAME, LNAME, MID)
- Identify Many-To-Many RELATIONSHIPS (3 relationships)
	- Create three new tables (intersection)
		- ENROLL (CID, SID, GRADE)
		- TEACH (FID, CID)
		- ASSIGNED (SID, LID)
### Overall Tables
- Final tables
```
1. FACULTY: FID (PK), FNAME, LNAME
2. COURSE: CID (PK), CNAME, CREDIT
3. STUDENT: SID (PK), FNAME, LNAME
4. MAJOR: MID (PK), DESCRIPTION
5. LOCKER: LID (PK), BUILDING
6. HOME-ADDRESS: HSTREET, HCITYM HSTATE
7. ENROLL (NEW): CID, SID, GRADE
8. TEACH (NEW): FID, CID, ...
9. ASSIGNED (NEW): SID, LID, ...
```

## Summary of ER diagrams using Chen Notations
![[Pasted image 20240408124622.png]]
## Summary of ER diagrams using "crow's foot"
![[Pasted image 20240408124706.png]]
## Unified Modeling Language (UML)
- The unified language model (UML) is a general-purpose OO modeling notation that can be used for:
	- specification
	- visualization
	- construction
	- documentation of software system artifacts
- Accepted as a standard by object Mgt group (OMG) 1997
- the most recent version is UML 2.5
- offers various diagrams modeling both static and dynamic aspects of a system
### UML Class Diagram
- UML class diagram
	- centerpiece diagram in UML used by both application and database engineers
	- shows the static structure of the systems
	- used as an alternative to ERD for data modeling
		- conceptual design
		- more details (code)
	- incorporate OO concepts such as objects, inheritance (subclass/superclass), encapsulation, information hiding
- represent classes (or entity types) as large rounded boxes with three sections:
	- The top section includes the entity type (class) name
	- The second section includes attributes
	- The third section includes class operation (operations are not in the basic ER model)
- Relationships (associations) are represented as lines connecting the classes
	- other UML terminology also differs from ER terminology
- Used in database design and object-oriented software design
- UML has many other types of diagrams for software design
![[Pasted image 20240408125524.png]]
Note: Qualified associations are useful when the association between classes needs additional context or when the relationship itself needs to be qualified by certain conditions or attributes. They provide a way to model more complex relationships and associations in UML diagrams. For example, a Qualified association using a dependent name for navigating from Employee to Dependent add additional information to the relationship. Manages and WORKS-ON are examples of association classes; they have their own attributes and/or models
### UML: sequence diagram
- Sequence diagram
	- represents the dynamic aspect of a system
	- a diagram of interacting objects and the messages they send to each other
	- arranged in time ordered
	- shows how use cases are implemented
![[Pasted image 20240408140110.png]]
### UML: Activity diagram
- shows the flow of business process
- Depicts who is involved with performing the various parts of the process
- Complements on use-case model by elaborating the business flow in each of the use cases
![[Pasted image 20240408140231.png]]


## Use Case Diagrams
A use case diagram captures the functional aspects of a system. More specifically, it captures the business processes carried out in the system. As you discuss the functionality and processes of the system, you discover significant characteristics of the system that you model in the use case diagram. Use case diagrams define the system's requirements and are used to write test scripts for the modeled system.
### Requirements Engineering: Use Case Diagrams
- Use Case
	- Captures the functional aspects of a system
	- Used to model the system's intended functions (or services) and its environments
	- can be used as a contract between the customer and the development
	Note: A use case diagram  captures the functional aspects of a system. More specifically, it captures the business process carried out in the system. As you discuss the functionality of the system, you discover significant characteristics of the system that you model in the use case diagram. Use case diagrams define the system's requirements and are used to write test scripts for the modeled system
### Use Case Diagrams: 1
- The diagram contains
	- Actors
		- Anyone or any system that may use the system
	- Use case
		- Actions (function/services), initiated by an actor, that the system performs
![[Pasted image 20240408130748.png]]
## Popular examples of conceptual modeling tools
- the tools include:
	- astah
	- architect (sparx systems)
	- ER/Studio
	- Erwin data modeler (erwin)
- These tools support facilities
	- Build a model
	- Map the model to logistical or internal data model working with varieties of DBMS platforms
	- Reverse engineering support to go from internal to conceptual models
## Chapter summary
- ER model concepts
	- Entities
	- Attributes
	- Relationships
- Constraints in the ER model
- Using ER in step-by-step conceptual schema design for the COMPANY database
- ER Diagrams Notation
- Mapping ERD to Relational Tables
- Discussed UML diagrams
	- Sequence diagrams
	- Activity diagrams
	- Class diagram
