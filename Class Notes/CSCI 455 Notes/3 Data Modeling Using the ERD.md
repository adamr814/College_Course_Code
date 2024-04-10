## Objectives
- Overview of Database Design
- Role of conceptual data modeling notation in database design
- Application of ER and UML to Design DB

## Overview of Database Design Process
1. Requirement collection and analysis
2. Conceptual Database Design
3. Logical Database Design (data model mapping)
4. Schema Refinement
5. Physical Database Design
6. Security Design
![[Pasted image 20240404112640.png]]
## Conceptual Design
- Revolves around discovering and analyzing data requirements (organizational, use, etc.)
- The important activities art to identify
	- Entities
	- Attributes
	- Relationships
	- Constraints
	- Design of ER/UML Diagrams
### Why is it important?
- Formalizing organizational data requirements
	- Helps users and systems developers identify data requirements (abstract model)
	- Helps in understanding how existing systems can be maintained
### Example of Database Application
- The COMPANY database keeps track of a company's employees, departments, projects, etc.
	- The company is organized into departments
	- A department controls several projects
	- Each project has a unique name, ID, and a single location
	- Employees may have dependents, and DB keeps track of dependents
	- An employee works on different projects
	- A project may be worked on by employees from different departments
#### Description of departments
- Specification of Department entity
	- A unique name and number
	- start_date
	- a set of locations
	- a manager
- Business rule:
	- each department controls several projects
	- each department must have a manager
#### Project specification
- Each project has
	- a unique name
	- a number
	- a single location
- Rules:
	- each project can be done by one or more department
	- each project has controlling (owner) department
#### Description of Employee
- Specification of employee includes
	- SSN, address, Manager
	- salary, sex, and birthdates
- Business rules:
	- an employee is assigned to only one department
	- an employee may work on several projects (not necessarily controlled by the same department)
	- an employee works certain hours per week
	- an employee has a direct supervisor
	- an employee may have dependent(s)
#### Description of dependents
- Each dependent has
	- name
	- sex
	- birthdate
	- relationship to the employee
![[Pasted image 20240404114105.png]]

## Entities and Attributes
- Entity?
	- The basic object represented by the ER model
	- could be a "thing" or "object" in the real world
	- e.g.: Entities are car, course, faculty, book, office
- Attributes?
	- Properties used to describe the entity
	- e.g.: name, age, address
- An entity will have a value for each of its attributes
![[Pasted image 20240404114411.png]]
### Types of attributes
- Simple (atomic) vs. composite
	- e.g., first name vs. address
- Single-valued vs. multi-valued
	- e.g., first name vs. degree
- stored vs. derived
	- e.g. birthdate vs. age
- complex attributes
	- combination of composite and multi-valued
	- e.g., employees having multiple addresses and each address is a complex address
- null values
	- N/A, not know, not available
##### More on Composite Attributes
- Attributes that can be divided into smaller subparts or more basic attributes
![[Pasted image 20240404115026.png]]
##### Simple Attributes
- Attributes that cannot be decomposed any further
##### Single valued-attributes
- attributes having a single value for a particular entity
##### Multi-valued attributes
- attributes having a set of values for the same entity
- may have a lower and upper bounds on the numbers of values for an individual entity
##### Derived and stored attributes
- Derived
	- attributes that can be calculated from existing attributes
- Stored
	- The actual values stored in the columns of a relational database
### Entity Types, Value sets, and key attributes
- an entity-type
	- defines a set of entities having the same attributes
	- describe the schema (intention)
	- represent by a box in the ER diagram
- Key attributes
	- A single attribute (or the combination of some attributes) is used to identify each entity uniquely
- Value sets (or domains of attributes)
	- a set of all possible values that can be assigned to an attribute
- Intention (type) vs. extension (state)
![[Pasted image 20240404115800.png]]
![[Pasted image 20240404115813.png]]

## Relationship types and relationship instances
- Relationship type
	- Defines a set of associations among a set of entity types `E1, E2, ..., En`
	- `R = {r1, ..., rn}` is a set of relationship instance `ri` where each `ri` associates n entities
### Degree of a relationship
- The degree of a relationship type is the number of participating entity types
	- Binary relationships
	- Ternary relationships
	- N-nary relationships
### Constraints on Relationship Types
- Constraints represent the restrictions on the possible connections among entities (or objects)
- The constraints come from the requirements
	- e.g., an employee cannot work for more than one department
- Two types of constraints:
	- Cardinality (maximum)
	- Participation (existence dependencies)
		- Partial
		- Total
### Cardinality Ratio?
- Cardinality 
	- The maximum number of records in one file or entity can be linked to a single record in another file or vice versa
	- Driven from requirements
- Cardinality ration
	- 1:1
![[Pasted image 20240404120955.png]]
- 1:N
![[Pasted image 20240404121023.png]]
- N:M
### Roles: Recursive Relationship type
- A relationship type playing distinct with the same participation entity type
- Each relationship instance `ri` relates two distinct EMPLOYEE records:
	- one employee is a supervisor role
	- one employee is a supervisee role
![[Pasted image 20240404121541.png]]
