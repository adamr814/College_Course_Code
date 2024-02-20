**Objectives**
- discuss more advanced features of SQL
	- Complex queries (nested and correlated)
	- join operations
	- aggregate functions
	- grouping, order, and having clauses
	- create triggers
	- views
**complex sql retreval queries**
- some queries need the existing values in the database to be retrieved and compared
- nested queries?
	- a query consists of "select from where" blocks nested withing another sql query (outer query)

**using nested queries**
- get a list of project numbers for projects that involve
	- an employee whose last name is "smith"
- the comparison operator in compares a value v with a set of values V and evaluates to true if v is one of the elements in V

**a query involving set comparison operators and a tuple**
- the in operator can be used to compare a tuple of values in parentheses with a set or multiset of union compatible tuples
- e.g. get ssn of all employees who work on the same combination (project, hours) on some project that employees work with

Correlated nested queries
- the query contrains a reference to one or more columns in the outer query
	- when a conditoion in the where clause of a nested query references attributes of a relation defined in the outer query
	- the queyr is evaluated from bottom to top
		- i.e.
- example
	- get the name of each empoloyee who has a dependenrt with the same first name and the same sex as the employee
	`*select`

**The keyword ALL
- cp,comparison operators
	- all, any, some
- can be used with any other comparison operators (E.g., >, =, <, etc)
- s > ALL V returns true if s is greater than ALL values in the set V
- Example: suppose
- Get the names of ALL employees whose salary is greater than the salary of ALL the employees in the department 5
`*SELECT lname fname`

**The exists and not exist functions in SQL
- EXISTS function
	- boolean functions returning true or false
	- used to check the result of a correlated nested query

**Example of EXISTS**
- find the name of each employee who has a dependent with the same first name and the same sex as the employee
`*SELECT`

**NOT EXISTS and example**
- not EXISTS
	- Returns T

**Explicit sets in SQL**
- we have seen several queries with a nested query in the WHERE-clause
- it is also possible to use an explicit set of values in the WHERE-clause, rather than a nested query
- E.g. Get SSNs of all employees who work on project number 11,22,33
```
*SELECT DISTINCT ESSN

```

**Joined tables in SQL and outer joins
- join operations can be specified in FROM clause
	- understandability
- AS construct can be used to rename join attributes (Natural Join)

```
*SELECT FNAME, LNAME,
```

**Renaming and Natural Join**
- the default type of join is INNER join
	- a tuple is included in the result only if a matching tuple exists in the outher relation
- 