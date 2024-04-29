## Objectives
- Important concepts and definitions
- Major categories of requirements
	- Functional requirements
	- Non-Functional requirements
	- Domain requirements
- Important features of the requirements
	- Completeness
	- Correctness
	- Consistent
## Requirement Engineering
- Software requirements engineering
	- The systematic process of gathering, analyzing, documenting, and managing the requirements for a software system to meet the needs and expectations of stakeholders.
	- Essential for ensuring the success of software projects by providing a clear understanding of user needs, defining project scope, reducing risks, aligning with business goals, facilitating communication and collaboration, and ultimately, delivering customer satisfaction
### Why are the requirements important?
- The hardest single part of building a software system is deciding precisely what to build. No other part of the conceptual work is as difficult as establishing the detailed technical requirements including all the interfaces to people, to machines, and other software systems. No other part of work so cripple the resulting system is done wrong. No other part is more difficult to rectify.
### What is a requirement?
- A description of what a system should do
	- High-level: an abstract statement of a service or of a system constraint (abstract)
	- Low-level: a detailed mathematical functional specification (concrete)
- Requirements serve dual functions
	- The basis for a bid for a contract (must be open to interpretation)
	- The basis for the contract itself (must be defined in detail)
	- both these statements may be called requirements.
### Requirement definition vs. Requirements specifications
- Requirements definition?
	- a complete listing of what the customer wants to achieve
	- describe the entities in the environment where the system will be installed
	- written for users/customers
- Requirements specification?
	- restates the requirements as a specification of how the proposed system shall behave
	- written for technical people
### Types of requirements
- Functional requirement:
	- describes required behavior in terms of required activities
	- what will the system do?
	- what kinds of transformations must be done?
- Non-Functional requirement:
	- describes some quality characteristics that the software must possess
	- how easy should it be for a user to understand and use the systems
### Constraints
- Design constraint:
	- limitations of restrictions that influence the design of a system, product, or solution such as a choice of platform or interface components, configuration, size of the system, and the language used to implement the systems?
- Process constraint:
	- a restriction on the techniques that can be used to build the system
	- what methods, personnel, or resources are needed to build the system?
	- what skills must the developers have?
## Functional Requirements
- statements of services the system should provide
- how the system should react to particular inputs
- how the system should behave in particular situations
### Functional requirements for the EMR
1. A user shall be able to search the appointments lists for clinics
2. The system shall generate a report for each clinic, and a list of patients who are expected to attend appointments on that day
3. Each staff member using the system shall be uniquely identified by their 8-digit employee number
#### Examples for a real-time system (insulin pump software)
1. the system shall measure the blood sugar and deliver insulin, if it is required every 10 minutes
2. The system shall run a self-test routine every minute
### Domain Requirements (application domain)
- A significant portion of the RE process is about developing domain description
- Works with the model of the domain, which provides an abstract description of the world in which a proposed system will operate
- Domain requirements
	- Constraints on the system from the application domains
### Problems with Requirements: impression
- Precision, exactness problem
	- ambiguous requirements may be interpreted in different ways by developers and users.
- Example: A user shall be able to "search the appointment" lists for clinics
- What is meant by "search the appointment"
	- User intention? search for a patient name across all appointments in all clinics
	- developer interpretation? search for a patient name in an individual clinic
### Completeness problem
- Completeness? The description should include descriptions of ALL facilities required
- Let's say a team is developing a web application for an e-commerce platform. In the initial requirements document, there's a section outlining the functionality for user authentication & authorization. However, the requirements only specify the basic authentication process, such as login and password recovery.
	- The documentation fails to address more advanced scenarios, such as account lockout mechanisms after multiple failed login attempts, password complexity requirements, session management, or roles and permissions for different user types within the system
### Requirements consistency issues
- Consistency? There should be no conflicts in the descriptions of the system facilities
	- The same input should always result in the same output (no conflict)
	- The same input results in multiple outputs (inconsistencies)
#### How to make requirements more precise
- make requirements more precise (more verifiable)
	- use quantitive description instead of each adverb and adjective
	- replace pronouns with specific names of entities
	- make sure that every noun is defined in exactly one place in the requirements document
		- Airbag should be deployed very fast (BAD)
		- Airbag should be deployed in less than 20 milliseconds (GOOD)
### Formal Methods
- Formal Methods (FM)
	- play a significant role to make specification more precise and more accurate
- Examples include
	- Logic Based
		- First order predicate logic (symbolized reasoning)
		- Temporal logic (timing information)
		- Linear logic (resources and their usages)
	- Automata Based (Finite States, Petri Nets, State Charts)
	- Model-Based (e.g. Z)
	- Process-Based (e.g. CSP)
## Non-Functional Requirements
- Non-functional requirements
	- Constraints on the services or functions offered by the system such as timing constraints
	- Apply to the system as a whole rather than individual features or services
	- Difficult to express them in a measurable or testable form
- These requirements define system properties and constraints
	- Reliability
- non-functional requirements may be more critical than functional requirements
	- Usability
- the system can be useless if it does not meet these requirements
![[Pasted image 20240416133250.png]]
### Non-functional classifications
- Product requirements
	- Requirements which specify that the delivered product must behave in a particular way
		- performance, reliability etc.
- Organizational requirements
	- requirements which are a consequence of organizational policies and procedures
		- process standards used, implementation requirements, etc.
- External requirements
	- Come from factors which are external to the system and its development process
		- Interoperability requirements, legislative requirements, etc.
		  ![[Pasted image 20240416133851.png]]
### Non-Functional requirements implementation
- Non-functional requirements may affect the overall architecture of a system
- For example, to ensure real-time computational performance is met, you may have to organize the system to minimize communications between components as much as possible
- NRF can also be negatively/positively correlated with other requirements (trade-off analysis)
- Some examples:
	- Availability vs. Security (negative correlation)
	- Maintainability vs. Reusability (positive correlation)
### Domain Requirements
- The system's operational domain imposes requirements on the system
#### Problems dealing with domain requirements
- Implicitness
	- Domain specialists understand the area so well that they do not think of making the domain requirements explicit
- Understandability
	- Requirements are expressed in the language of the application domain
	- Hard to understand by software engineers developing the system
### Key points review
- requirements for a software system set out what the system should do, and define constraints on its operation and implementation
- functional requirements (FRS)
	- Statements of the services (or behaviors) that the system must provide
- non-functional requirements (NFR)
	- criteria that can be used to judge the quality of operation of a system provide, rather than specific behaviors
	- apply to the system as a whole
# Requirements Definition, Requirements Specification
## Objectives
- Requirements Definition
- Requirements Specification
- Organization of requirements documents
- Requirements engineering process
	- Elicitation
	- Analysis & Specifications (Modeling and specification)
	- Validation (agreement)
- Requirement change management
## The Software requirements specification (SRS)
- The software requirements specification document is the official statement of what is required of the system developers.