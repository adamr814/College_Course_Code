### Objectives
- Discuss the Software Engineering Principles
	- Rigor, etc.
- Cover different types of processes and modeling
	- Waterfall and its variations
	- V-Model
	- Spiral
	- Prototyping
	- Agile
- Discuss Tools and Techniques for process modeling

### Software Engineering Principles
- Principles?
	- Some important design guidelines that are focal points to any successful development of software (e.g., Separation of concerns)
	- These principles deal with both the process and the product
#### Rigor And Formality
- Rigor
	- Means precise (detailed) and accurate (correct)
	- Used to increase repeatability and reliability
	- Every person involved in the project has to observe the rules
- Formality
	- The highest degree of rigor
	- Used to formally reason about the system
	- Automated testing and/or error removals are possible

### Separation of concerns
- Separation of concerns
	- Dealing with different aspects of a problem, so that we can concentrate on each sub-problem individually
- Some examples
	- Functionality
	- Quality (e.g., Security)
	- Development process
	- Design strategies
	- Error recovery
	- Views (e.g., dataflow vs. control flow)
- We may miss global optimizations if we only look at pieces

### Modularity
- A complex system may be divided into simpler pieces called modules
	- A system that is composed of modules is called a modular system
- Helps to realize the principle of separation of concerns:
	- Dealing with each component
	- Dealing with the overall organization of a set of components
	- Composability (bottom-up)
	- Decomposability (top-down)

### Abstraction
- Abstraction
	- fundamental technique for understanding and analyzing complex problems
	- Need to identify the essentials of a phenomenon and ignore its details
- Some examples
	- Software architecture (used as a representation of systems of systems)
	- Data abstraction (hiding the details of the internal data representation (attributes) and exposing only the essential information through methods (functions))
	- Memory (used as an abstraction of circuits)

### Anticipation of change
- Change is inevitable
- Good Software changes constantly
	- Fixing errors
	- New requirements
	- Effect of personnel turnover
- Change affecting process
	- Employee turnover
- Requiring new tool and proper design decisions
	- New Compiler for new platform

### Generality
- Trying to solve a new problem by identifying a more general problem that can be hidden behind the new problem
	- reuse the old solutions to solve new problems
	- E.g., Object oriented design patterns
- Requires tradeoffs
	- Textbooks say to be as general as possible
		- The more general, the harder, slower, more complex to use
	- Practice demands more specific

### Incrementally
- Refers to a process that proceeds in a stepwise fashion, in increments
- Applied to many engineering activities
	- In software engineering, the desired product is produced as a result of an evolutionary process
	- Starting from core features, we may progressively add additional features

### Design of a compiler
- let's see how the principles are applied during the construction of a compiler
	- rigor and formality
		- use BNF to formally define the syntax of PL
	- separation of concerns
		- correctness (object code consistent with source code)
		- Maintainability (introduce new language without changing the backend)
		- Efficiency (compile-time and optimization)
		- Usability (the diagnostics messages)
		- Portability (retargeting the compiler for different machine)
	- Modularity
		- lexical analysis
		- syntax analysis
		- code generation
	- Abstraction
		- Intermediate code (abstract)
		- Final code (concerete)
	- Generality (reuse)
		- Software architectural styles (Pipe/Filter)
		- Object-oriented design 
	- Incrementally
		- Design core features and extend it with additional features
		- e.g., implement core programming construct such as IF/THEN, etc. then add optional features (pointers, list, class, etc)

### The Meaning of Process and Product
- Process?
	- used to produce the software product
	- a series of steps involving activities, constraints, and resources that produce an intended output of some kind
	- involves a set of tools and techniques
- Product?
	- The things/objects delivered to the customer
	- customer-visible product (e.g., executable code and the user manual)
	- Developer-visible product (e.g., requirement specifications and design documentation)

### The importance of Processes
- Impose consistency and order on a set of activities
- Guide us to understand, control, exam, and improve the activities
- Enable us to document our experiences and pass them along

### Process Qualities
 - Process quality refers to the overall excellence, efficiency, and effectiveness of a process within an organization.
	 - It encompasses various attributes that contribute to the reliability, consistency, and success of the process.
- Example: Careful planning of test data before any design development begins should increase product reliability

### Typical process qualities
- productivity
	- denotes its efficiency and performance (faster delivery)
	- proper usage of tools and improve productivity
- Timeliness
	- ability to deliver a product on time
	- requires careful scheduling, accurate estimation of work, and specified and verifiable milestones
- Visibility
	- a software is visible if all of its steps and current status are documented

### Software Development Process Models
- Waterfall model
- V-Model
- Prototyping model
- Operational specification
- Transformational model
- Increments and iteration models
- Spiral model
- Agile Methods

#### Waterfall Model with no iteration
![[Pasted image 20240402135407.png]]
#### Waterfall Model: 2
- Many software development processes involve numerous iterations, often conducted in an unstructured manner
![[Pasted image 20240402135634.png]]
#### Drawbacks of the waterfall model
- No guidance on how to handle changes to products and activities during development
	- assumes requirements can be frozen!
- Views software development as a manufacturing process rather than as a creative process
- No iterative activities that lead to creating a final product
- Long wait before a final product

#### Prototyping Model
- Allows repeated investigations of the requirements or good design
- Reduces risk and uncertainty in the development (good)
![[Pasted image 20240402135943.png]]
#### Waterfall Model with Prototype
- A prototype is a partially developed product
- Prototyping helps
	- developers access alternative design strategies (design prototype)
	- users understand what the system will look like (user interface prototype)
- Used for verification and validation
![[Pasted image 20240402140135.png]]
#### V-Model (revisited)
- A variation of the waterfall model
- Shows how the testing related to front-end activities
- Uses unit testing to verify procedural design
- Uses integration testing to verify architectural (system design)
- Uses acceptance to validate the requirements
![[Pasted image 20240403000458.png]]
##### The role of requirements and error interaction during Late discovery of problems
![[Screenshot 2024-04-03 at 12.19.42 AM.png]]
- using "v" so common in systems engineering circles, we add notes from a National Institute of Standards, and Technology (NIST) document that points out that requirements generation and interaction errors (software only, software-software, and software hardware, ... all the combinations and permutations) is where most defects originate - on the left side of "v". Unfortunately, when the team follows the typical "as-is" development trail, around "80% of these errors/defects are not found until physical/logical interaction takes place during the right upper three layers of verification (the "test" blocks)". The truly unfortunate aspect of this late discovery is that costs at these stages of synthesis of the system are very high. The red text shows what the authors of this original paper estimated were the multipliers for correcting faults (with the baseline reference being finding the fault. of the requirement state - 1x). Note that even if faults are corrected at this earliest integration stage of synthesis (unit test), the cost to fix this set of faults is 5x the cost to fix them at the requirements generation stage (during the decomposition stage or design stages) of development. Moreover, later data suggests that these original estimates of the cost to fix at a given stage of synthesis are low by more than an order of magnitude for the latter stages (system test or integration test).
#### Operational Specification Model (executable form)
- Exam requirements and their implications early in the development process
- Shows the behavior of a system
![[Pasted image 20240403004648.png]]
#### Transformational Model
- Applies a series of transformations to change a specification intro a deliverable system
	- Change data representation
	- Select algorithms
	- Optimize
	- Compile
- Requires formal specification (to allow transformations)!!!
![[Pasted image 20240403010005.png]]
#### Increments and Iterations
- Long waiting is not acceptable
- The system delivered in pieces
	- Enables customers to have some functionality while the rest is being developed
- Two systems functioning in parallel
	- The development system (release n+1): the next version
	- The operational system (product or release n): currently being used
![[Pasted image 20240403010741.png]]
- Incremental development:
	- starts with a small functional subsystem and adds functionality with each new release
- Iterative development:
	- starts with the full system, then changes the functionality of each subsystem with each new release
##### GOOD
- The Model is desirable for several reasons:
	- A very common approach to building a software product
	- Training can begin early, even though some functions are missing
	- Markets can be created early for functionality that has never before been offered
	- Frequent releases allow developers to fix unanticipated problems globally and quickly
	- The development team can focus on different areas of expertise with different releases
##### BAD
- Can be difficult when a replacement system is being developed
	- Users want ALL of the functionalities of the old systems, not an incomplete system
	- No specification until the final increment is specified
- The modern method combines both approaches
	- Deliver new releases with additional features and enhanced functionalities

#### Spiral Model (revisited)
- Suggested by Boehm (1988)
- Combines development activities with risk management to minimize and control risks
	- Continuous risk analysis and mitigation throughout the development process, helping to address a variety of potential challenges and uncertainties
- The model is presented as a spiral in which each iteration is represented by a circuit around four major activities (i.e., requirements analysis, design, etc.)

##### Main steps
- Each loop in the process consists of
	- Define a set of goals identity project risks, access alternatives and constraints on process and product
	- Evaluate alternatives and perform risk reductions
		- for example, if requirements are not well understood, then use a prototyping system to reduce the risk
	- Develop and validate the system
		- For example, if safety is important, use formal methods
	- Plan for the next round
![[Pasted image 20240403012111.png]]
##### Spiral model usage
- Very influential in helping people think about iteration in software process
- introducing the risk-driven approach to development
- the model is rarely used as published for practical software development\
##### GOOD
- A lot of risk analysis and risk mitigations
- Suitable for large and mission-critical projects
- Requires strong approval and documentation control
- Additional functionality can be added at a later date
- Software is produced early during SDLC
##### BAD
- Can be a costly and complex model to use
- Demand effective risk assessment skills and expertise
	- The project's success is highly dependent on the risk analysis phase
- Doesn't work well for smaller projects
- Customer involvement
- Requires significant documentation (overhead)

Complexity: The spiral model can become overly complex, especially in large projects. With multiple iterations and phases, managing the complexity of the model itself can be challenging.

Costly: The iterative nature of the spiral model may lead to an increase in development costs. Conducting through risk analysis, prototyping, and testing in each iteration can demand additional resources and time

Time-Consuming: The model can be time-consuming, particularly if the project requires extensive risk analysis and frequent iterations. The time spent on planning and risk assessment in each cycle may delay the overall project timeline.

Not suitable for small projects: The spiral model may be excessive for small projects with well defined and stable requirements. It's emphasis on risk analysis and iteration my be unnecessary in situations where the project scope is limited

Dependency on Risk Assessment Skills: Effective risk assessment is crucial in the spiral model. The success of the model heavily depends on the team's ability to accurately identify and analyze potential risks inexperienced teams may struggle with this aspect.

Inflexibility in Phases: The structured phases of the spiral model may not be easily adaptable to all types of projects. Some projects may require a more fluid and dynamic development process.

Customer Involvement: Continuous customer involvement is essential for success in the Spiral Model. If customers are not actively engaged or are unable to provide regular feedback, it can hinder the iterative and adaptive nature of the model.

Not ideal for fixed budgets: Projects with fixed budgets may find it challenging to accommodate to the uncertainties associated with the spiral model. The model's iterative nature might lead to increased costs, making it less suitable for fixed-budget scenarios.

Documentation Overhead: The need for documentation at each phase can result in a significant overhead. Managing documentation for multiple iterations may lead to an extensive and potentially cumbersome set of project documents.

Potential for scope creep: The iterative nature of the model, coupled with the potential for evolving requirements, may increase the risk of scope creep if not managed carefully. This can lead to expanding project scope beyond the original plan.

#### Agile Methods
- Emphasis on flexibility in producing software quickly
- Agile manifesto
	- Value individuals and communications over process and tools
	- Main focus includes:
		- producing working software vs. producing comprehensive documentations
		- customer collaboration vs. contract negotiation
	- Concentrate on responding to change rather than on creating a plan and then following it
##### Examples of Agile methods
- Extreme Programming (XP)
	- Advocates frequent "releases" in short development cycle
	- Encourages starting with the simplest solution, and adding extra capabilities later
	- Works on small teams (e.g., twelve or fewer people)
- Scrum:
	- 30-day iterations (sprints)
	- multiple self-organizing teams
	- Daily (24h) "scrum" coordination

##### Problems with agile
- Lack of documentations
- lack of software design
- requires too much cultural change to adopt
- can lead to more difficult contractual negotiations
- realistic estimates of work effort is difficult
- non-functional quality attributes are hard to be placed
- scaling issues to development of large scale project
- scope creep (continuous additions of new requirements impact the delivery time)
##### Benefits of agile
- Flexibility and Adaptability, and continuous improvement
- customer satisfaction
- Faster time to market
- Improved collaboration and communication
- Handling risk and uncertainty
- Increased productivity

#### Reuse-Oriented software engineering
- based on systematic reuse where systems are integrated from existing components or COTS (Commercial-off-the-shelf) systems
- standard approach for building many types of business system
- Process stages
	- Component analysis;
		- search to find reusable components
	- Requirements modification;
		- modify requirements to fit existing components
	- System design with reuse
		- Design new components with reusability in mind;
	- Development and integration
		- Integrate the adapted components into the new system
	- Validation
		- Validate the functionality and correctness of the newly integrated components
#### Types of software components
- Web services
	- Developed according to service standards
	- should be available for remote invocation
- Collections of objects
	- developed as a package to be integrated with a component framework such as .NET
- Stand-alone software systems (COTS)
	- Configured for use in a particular environment
- Open-source software (OSS)

##### Obvious disadvantages of reuse
- Disadvantages
	- Access to source code
	- Binds user to market trends (critical components may become unavailable and impossible to reuse)
	- Certification may not meet the reliability requirements of mission-critical systems (e.g., Medical equipment)
	- Managing a repository of reusable components involves significant effort

#### The rational unified process (RUP)
- a modern generic process derived from the work the UML
	- Results-oriented vs. activities-oriented
- Combines aspects of the generic processes model discussed previously
	- Phases (software development cycles) and key activities (aka disciplines)
- New product can be created using evolution cycle
##### Phases of the rational unified process (RUP)
- Main phases:
	- Inception (exercise mangagement skill)
	- Elaboration (exercise architectural skill)
	- Construction (exercise development skills)
	- Transition (exercise deployment skills)
![[Pasted image 20240403111651.png]]
##### Inception phase
- inception (exercise management skill)
	- establish the business case for the system (people and systems interact with the system and their interactions)
	- Justification for building a new product and enhancing the existing one
	- Must pass Objective Milestone
##### Elaboration Phase
- Elaboration (exercise architectural skill)
	- To analyze the solution of the application domain, develop a comprehensive project plan that factors in the elements of risks
	- Deliverables may include design artifacts such as'
		- UML class diagram'
		- ADL, and development plan
	- Must pass architectural model milestone
##### Construction Phases
- Construction (exercise development skills)
	- Involves system design, coding, and testing
	- On completion, a working software system and related documentations should be produced
	- Must pass Operational Capability Milestone
##### Transition Phase
- Transition (exercise development/release skills)
	- Deploy the system in its operating environment
	- Must pass the Product Release Milestone
##### Iteration Phase
- Two types of iterations:
	- In-phase iteration: Each phase is iterative and contains all weighted activities and artifacts correspond to the development phases
	- Cross-phase iteration: The whole set of phases may be executed incrementally
![[Pasted image 20240403112430.png]]
![[Pasted image 20240403112451.png]]
##### Advantages of Rational Unified Process
- Develop software iteratively
	- plan increments based on customer priorities
	- deliver highest priority increments first
- Manage requirements
	- explicitly document customer requirements
	- keep track of changes to these requirements
##### RUP Good Practice
- Visually model software
	- Use graphical UML models (discussed later)
	- Verify software quality
	- Ensure that the software meets organizational quality standards
- Control changes to software (configuration and change management)
	- Manage software changes using a change management system and configuration management tools
##### Disadvantages
- Complexity and Overhead
	- The unified process can be perceived as complex and bureaucratic
- Learning curve
	- Team members may face a steep learning curve when adopting the Unified
- Communication Challenges
	- Effective communication and collaboration are essential in UP
	- Miscommunication or lack of collaboration among team members can be a serious issue

#### Compare and Contrast Waterfall vs. Agile
- Waterfall Model
	- Disciplined, detailed plan
	- Emphasis on long-term planning
	- Focus on process
	- Rigid
	- Heavily document driven
- Agile Model: Middle ground between two extremes (too much vs too little)
	- Short-term focus
	- Focus on Flexibility and humans and agility
	- Light document driven

### What are the engineering process for developing AI-Driven systems? & Issues
- AI driven are used to create software
	- The AI based approach in operational commercial software is the least covered approach
	- The development process of AI-enabled applications that employ ML techniques, include deep learning, involves creation of ML models based on data
	- When creating ML models, requires several experiments before selecting the final ML model
	- learning algorithms are applied to a dataset to train and evaluate the accuracy and performance of created ML models
		- Verification and Validation