## Objectives
-  Relational Models
	- Concepts
	- Notations
	- Constraints
	- Database Schemas
- Update Operations
- Constraints Violations

## Relational Models Concepts
- Relational Data Models
	- Introduced by E.F. Codd at IBM in 1970
		- Provides formal mathematical foundations (relations)
		- Simplicity
	- The top commercial DBMS Systems include
		- Oracle (commercial)
		- MySQL (open-source)
		- Microsoft SQL Server and ACCESS (commercial)
		- PostgreSQL (open-source)
		- IBM DB2 (commercial)
		- SQLite (open-source)
- Relation?
	- A table consists of a collection of tuples (or rows)
	- Each tuple represents a relationship among attributes (columns)
	- A relationship among n-values is mathematically represented by an n-tuple (i.e., a row in the table)
	- A relation can be visualized as a table of values
	- A relation is an entity in ERD
## Domains: Logical Definitions
- A domain means a set of permissible atomic values
- a domain can be specified as a datatype
- examples of domains
	- SSN: a set of 9-digits
	- Phone Numbers: a set of 10-digits
## Relational Schema
- A relation schema R represented by `R (A1, A2, ..., An)` where
	- Each `Ai` belongs to some domain `Di`
	- `Dom(A1)` means domain of `A1` (i.e., all possible values related to attribute `A1`)
- Degree of relation?
	- Number of attributes in the relation schema R
	- E.g., Student (Name, SSN, Home_phone, address, Age, GPA)
		- The degree of student = 6
## Relation state
- Relation state r of Schema R
	- Denoted by r(R)
	- A set of n-tuples `r = {t1, t2, ..., tn}` where each `ti` is ordered list of values
		- `ti = V1, V2, ..., Vn>`
		- `Vi ∈ {dom(Ai) ∪ NULL}`
	- `t[Ai] = t.Ai = t[i]` used to refer to `i`th value in tuple t
- Relation intention (R) vs. relation extension r(R)
![[Pasted image 20240409123040.png]]
### Formal definition of a relation
- Formal relation of r(R)
	- `r(R)⊆(dom(A1)´dom(A2)´...´dom(An))`
		- i.e., r is a subset of all possible n-tuple
		- X is Cartesian product operation
		- used to specify all possible combinations of values from the underlying domains
	- The total number of all possible instances of tuples can be represented as products of cardinalities of all domain
		- `|dom(A1)|´|dom(A2)|´...´|dom(An)|`
	- Several attributes may have the same domains
	- Attribute names can present different roles
		- E.g. Phone numbers can play different roles
		- Home Phone
		- Office Phone
### Example of tuples
- E.g. Suppose
	- `A = {1,2} with cardinality |A|=2`
	- `B ={3,4}, with cardinality |B|=2`
	- `A × B = {1,2} × {3,4} = {(1,3), (1,4), (2,3), (2,4)}`
	- `B × A = {3,4} × {1,2} = {(3,1), (3,2), (4,1), (4,2)}`
	- `A = B = {1,2} then A × B = {1,2} × {1,2} = {(1,1), (1,2), (2,1), (2,2)}`
- In general
	- `AxB != BxA`
### Characteristics of Relations
- ordering of tuples in a relation not important
- ordering of values within a tuple
	- important (for simplicity) if
		- `r(R) ⊆ (dom(A1) x dom(A2) x ... x dom(An))`
	- unimportant if
		- `r(R) ⊆ (dom(A1) ∪ dom(A2) ∪ ... ∪ dom(An))` (i.e., a set of attributes) Tuple values
	- Atomic
	- Null
- Interpretation of a relation and tuples
	- Tuples interpreted as facts
	- Relation schema interpreted as a type declaration
![[Pasted image 20240409124350.png]]
![[Pasted image 20240409124403.png]]
## Relational Databases and Relational Database Schemas
- Relational database schema
	- a set of relation schemas
	- a set of integrity constraints
- Relational database state DB of S:
	- a set of relation states DB={r1, r2, ... ,rm}
	- some tuples in a relation (aka cardinality)
- DB State
	- Valid state vs. invalid state