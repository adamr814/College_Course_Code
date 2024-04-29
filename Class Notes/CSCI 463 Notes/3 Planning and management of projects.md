## Objectives
- Discuss a range of technical management issues
- Project scheduling techniques
	- WBS, PERT, Gantt Charts
- Cost/effort Estimation techniques
	- Expert-based techniques
	- Algorithmic (or formal)
## Software project management
- Software project management?
	- An umbrella of activity within software engineering
	- Begins before any technical activity is initiated
	- Continues throughout the modeling, construction, and deployment of computer software
- Key factors (aka 4Ps) affecting the project software management
	- People (highly skilled and talented people)
	- Product (goals, objectives, scope)
	- Process (a set of activities)
	- Project (develop common sense approach for planning monitoring, and controlling the project)
- The main objectives of Project Management are
	- Ensure products meet the customer's specifications and expectations
	- Ensure all desired project attributes, such as (e.g., security are met)
	- Meet project deliverables and milestones according to the schedule
	- Foster effective collaboration and productivity among team members
	- Ensure the availability and optimization of necessary resources
## Confusion between software project management and software engineering process
- Software Project mgt?
	- Enforce a management framework to ensure effective implementation of software engineering processes
	- Focuses on overseeing project activities rather than directly engaging in software engineering processes
## Why Project Management?
- Before expanding any resources, customer may have lots of questions
- Typical questions customer may ask:
	- Do you understand my needs?
	- Can you design a system that will solve my problem
	- How long will it take to develop such a system?
	- How much will it cost to develop such a system?
## Project Planning
- Project planning?
	- Essential phase of any project
	- Could be a maker or breaker
	- Helps facilitate the changes
	- used to communicate how the work will be done to the project team and customers
## Essential elements of project management
- The core elements include:
	- Schedule and planning techniques (defining SE tasks, milestones, schedules, task, assignments, etc.)
	- Estimation techniques (resources, workload, time)
	- Risk accessments
	- people management
## Project Scheduling
- Project scheduling?
	- Describes how the work in a project will be organized as phase
	- how each phase breakdown into a set of sub-phases (activities)
	- Shows the interactions among these activities together with estimates of the time that each activity will take
## Work Breakdown structure
- Work breakdown structure (WBS)
	- it involves breaking down a project into smaller, deliverable components
	- Components can include data, services, products, or combinations thereof
	- Used for project control, monitoring, and cost estimation
	- Specifies precursor conditions
	- Includes due dates for deliverables
	- Defines endpoints such as milestones or final deliverables
![[Pasted image 20240412130509.png]]
## Activity Graph or Program Eval and Review technique (PERT)
- An activity graph is used to show the dependencies regarding project milestones
	- Circles and boxes represent milestones
	- Lines represent dependencies or activities between milestones
	- Activities at the end of a line cannot commence until the activity at the beginning of the line is completed
![[Pasted image 20240412130807.png]]
## Some concepts: Milestones and deliverables
- Milestones?
	- Points in the schedule against which we can access progress
	- e.g. completion of unit testing
- Deliverables?
	- Refer to work products that are delivered to the customer
	- e.g. A requirements document for the system, source code, etc
- Slack Time (float)?
	- Slack time = available time (or latest start time) - real time (earliest start time)
- Critical path method (CPM)
	- A path that can be used to measure the minimum amount of time needed to complete the project
![[Pasted image 20240412131210.png]]
## Program Evaluation Review Tech
- PERT
	- A critical path analysis technique
	- Used to determine the probability of the earliest start time for activity is close the schedule time for that activity
	- Used by project manager to monitor the project the project having concurrent activities
## Tools to track progress
- Examples of tools to track the projects progress are
	- Work Breakdown Structure
	- Gantt Chart
## Gantt Charts
- A project control/progress technique
- Designed by Henry L. Gantt
- Used for several purposes such as
	- Scheduling
	- Budgeting
	- Resource Planning
![[Pasted image 20240412131745.png]]
Example PERT chart
![[Pasted image 20240412133748.png]]
### Analysis of PERT charts
- Critical path for the project
	- any delay in any activity on the path causes a delay in the entire project
	- activities on the critical path must be monitored more closely than other activities
## Gantt & PERT charts
- Force the manager to plan
- show interrelationships among tasks
	- PERT clearly identifies the critical path
	- PERT exposes parallelism in the activities
		- helps in allocating resources
- Allow scheduling and simulation of alternative schedules
- Enable the manager to monitor and control project process and detect derivations
# Part 2  Cost Estimation Techniques
## Objectives
- Cost estimation techniques to estimate effort, durations, time, etc.
	- Algorithmic-base
	- Experienced based
	- AI-based
## Cost estimation
- Cost estimation is part of the planning stage of any engineering activity
- Cost and schedule overruns have been a common risk in software projects
- According to the Oxford University study on 5,400 large scale IT projects
	- On average, large software projects run 66% over budget and 33% overtime
## Effort estimations
- The dominating cost is the number of people or effort needed to implement the system
- Effort estimation?
	- The process of estimating the number of engineers needed to complete a project
	- an integral part of software project management (during planning and monitoring)
### Estimate uncertainty
![[Pasted image 20240412134557.png]]
### Effort estimation: 1
- Once requirements are defined, estimates can be made
- Estimates are made to identify the cost to the developer of a software system.
- Estimates inlclude:
	- Hardware cost
	- Software cost
	- Travel expenses
	- Training and effort costs
	- Staff
	- ...
### Effort Estimation Methods
- Main techniques:
	1. Experience-based techniques
	2. Algorithmic cost modeling
	3. AI-based techniques
#### Experience-based techniques
- Experience-based techniques
	- The estimate of future effort is based on the manager's experience of past projects and the application domain. (i.e. the manager makes an informed judgement of what efforts are needed)
- Experts may be over-optimistic or past experience may be incorrect/incomplete
- a projection from past experiences to the future which may be adjusted to account for differences between past and future
	- requires to have past experience to make some judgements
	- need to know something about the future
	- we may need to make some adjustments to account for the differences between past and future
	- documented in a spreadsheet, estimate them individually and compute the total effort required
#### Algorithmic cost and AI-based techniques
- Algorithmic cost modeling
	- Formulaic approaches to compute the project effort based on estimates of project attributes (e.g., size, functions, etc.)
- Examples
	- COCOMA models 1, 2, and 3
- AI-based
	- ML (neural-net works (e.g., deep learning model for estimating story points))
	- Care-based Reasoning (CBR)
### Estimation using Size: 1
- Most estimation models, tools, and methods use some measure of size as the main product attribute
- Suppose we have estimated that the future product size in line of code (LOC) will be 50,000 LOC
	- Assuming no further adjustments are needed if the future project is similar to the past project
	- Using past experiences, the software productivity for the same type of project is 500 LOC per person-month (i.e., 500 LOC/PM)
### Using size to compute effort/duration: 2
- using size the effort and duration can be calculated as follows
	- `Effort = 50,000-LOC / 500-LOC/PM = 100 PM`
- Suppose we have 10 full time equivalent (FTE) persons, then 
	- `Duration = 100PM / 10P = 10M`
## Project Size (revisited)
- project size metrics used to estimate cost
	- Algorithmic
	- Experts-based
- size cab be computed using
	- code size (i.e. SLOC)
	- Functionalities (i.e. Function Points)
	- Applicability (i.e., Application Points)
### How to estimate size?
- size estimation can be obtained
	- by analogy/comparing with other projects
	- by converting function (or application points) to LOC
	- by engineering judgement
### Size Estimating Pros
- when size is used as the primary factor for estimation
	- can be used as an indicator of complexity
	- can have a direct relationship to the project attributes such as effort and schedule
	- can be measured very accurately
	- easy to collect data about the size of the project
### Size Estimating Cons
- Problems using size
	- difficult to estimate LOC early in a project
	- difficult to relate changes to the requirements to changes in estimated LOC
	- poor quality LOC can be created
### Factors influencing the final size
- several factors influence the final size
	- use of COTS and components
	- Type of programming languages (Low vs. High level)
	- Modern development methods
	- The complexity of the design which requires more coding/testing
### Factors affecting productivity
- study based on LOC identifies two key attributes:
	- Capability of the personnel
	- Complexity of the product (i.e., reliability, performance, security)
- the least important factors include
	- Schedule
	- Previous experience with languages used in project
# Function Points, COCOMA models, ML-based
## Function Points

^6ea0e6

- Function Points?
	- used during the requirements analysis phase to help stakeholders understand the scope and complexity of the software being developed
	- identifying and quantifying the functionalities required by the users
	- provide a basis for estimating the size (LOC), effort, time, needed to develop the software
	- they can be used as input to various software estimation models, such as COCOMO II (COnstructive COst MOdel)
	- COCOMO II (discussed later) use FP's [[#^6ea0e6]] and other factors such a project complexity, productivity, etc. to estimate the effort, time, and resources required to develop the system
### Function Point Metric: 1
- Using historical data (e.g. Productivity), the FP metric can be used to estimate
	- Cost, or effort to design, code, and test the software
	- Predict the number of errors (defects) that will be encountered during testing
	- Forecast the number or Source Line of Codes (SLOC) in the delivered system
#### FP Information Domain
- Function Points (FP) can be calculated by counting and weighing
	- Number of external inputs (EIs)
		- Customer buys a book
	- Number of external outputs (EOs)
		- System displays the contents of the shopping cart
	- Number of internal logical files or Data Entries (ILFs)
		- Customer database storming customer information
	- Number of external Queries (EQs)
		- user checks the status of an order
	- Number of external interface files (EIFs)
		- payment gateway interface
### How to compute FP's
- Function Points can be computed using the following
	- `FP = count_total X [0.65 + 0.01 X SUM(Fi)] where`
		- count_total = sum of all FP entries
		- SUM(Fi) = Fi (for i = 1 to 14) (aka relative complexity adjustment factor (RCAF))
		- .065 is constant
		- .01 is weight
![[Pasted image 20240415123053.png]]
### Calculation to create Composite Function Points (CFP) of total FP
- Main assumptions:
	- Productivity = 6.5 FP/PM
	- RCAF = 0
	- Cost per FP = $1230
	- Each FP = 66 LOC of C++
	- Number of Staff = 6 Full Time Staff
	- `Effort = Total FP (CFP)/Productivity = 242FP / 6.5(FP/PM) = 37 PM`
	- Total Cost = 37 X $1230 = $45,510
	- Converting FP to LOC to get size
		- `Size(FP) = 37 X 66 = 2442 (LOC in C++)`
	- Duration can be computed:
		- `Duration = Effort/#staff = 37/6 = 6 month`
![[Pasted image 20240415123612.png]]
CFP (Composite Function Point). It provides a standardized measure of the functional size of a software system, allowing organizations to estimate effort, time and resources required for software development, maintenance, and enhancement projects.
TCF (Technical Complexity Factor). It is a multiplier used to adjust the function point count based on various technical and environmental factors that can influence the complexity of software development projects.
![[Pasted image 20240415123927.png]]
![[Pasted image 20240415124148.png]]
## COCOMA Models I, II, III
## Algorithmic Cost Modeling (revisited)
- Uses a mathematical formula to predict project cost using size and following attributes
	- Product
	- Project
	- Process
- `Effort = A x Size^B x M (standard formula)`
	- A = a constant factor depending on the type of software
	- B = it depends on the complexity (ranges from 1-1.5)
	- M = a multiplier reflecting product, process, and people attributes
- The estimations of the factors related to B and M are subjective!
## Algorithmic models: Main Issues
- Models are complex and difficult to use because
	- Too many attributes an uncertainty can be used when estimating the values of attributes
	- Requires calibration (the modelers need to adjust their model and attribute values using their data)
	- Requires a range of estimates
		- Worst
		- Expected
		- Best
- The model can be an accurate estimate if
	- we understand the type of software to be produced
	- Know how properly to calibrate the cost modeling using local and/or past data
## The COnstructive COst MOdel (COCOMO) cost modeling
- An empirical model based on project experiences
- Developed by Barry Boehm at USC
- Not tied to a specific software vendor
- A long history from the initial version published in 1981 (COCOMO-81) through various versions to COCOMO II
- COCOMO II
	- Takes into account different modern approaches to software development (e.g. reuse)
### CCOCOMO-81
- Three COCOMO modes of software engineering
	1. Organic Model
		- Small software teams develop software in a highly familiar, in-house environment.
	2. Semidetached Model
		- Intermediate between the organic and embedded modes
	3. Embedded Model
		- need to operate within tight constraints. (e.g., air traffic control system)
![[Pasted image 20240415130013.png]]
Where a, b, c, d are constants
§Effort (PM)  = ab(KLOC)bb {person-month ]

§Development Time (DT) = cb(Effort )db [months]

§People (P) = Effort / Development Time [count]

§Example: Suppose KLOC = 500 using Organic model

§PM = 2.4 (500) 1.05 = 2.4 (682.2) = 1637.3

§DT =  2.5 (1637.3) 0.38 = 41.6

§P = PM/DT= 1637.3/41.6= 39.36 40 SE is needed

### COCOMO II Models
- Incorporates a range of sub-models to generate more detailed and hence accurate software estimates
- The sub-models in COCOMO II include:
	- Application composition model (reusable components, application points, etc.)
	- Early design model (FP)
	- Reuse model (integrate reusable and generate code)
	- Post-architect model (SA and 15 cost drivers)
![[Pasted image 20240415235821.png]]
## Application composition model (or objects)
- Supports prototyping projects and projects where there exists extensive reuse
- Based on standard estimates of developer productivity in application points/month
- Formula
	- `Effort = (NAP x (1 - %reuse/100))/PROD`
		- Effort = the effort in person months (PM)
		- NAP = the total number of application points
		- PROD = NAP/Month (i.e., number of application points per month)
		- %reuse = an estimate of the amount of reused code
![[Pasted image 20240416000258.png]]
### Early design model
- Estimates are made after the requirements have been finalized and agreed
- Based on a standard formula for algorithmic models
	- `Effort = A x Size^B x M` where
		- `M = PERS x RCPX x RUSE x PDIF x PREX x FCIL x SCED`
			1. PERS: Personal Capability
			2. RCPX: Reliability and Complexity
			3. RUSE: Reuse required
			4. PDIF: Platform difficulty
			5. PREX: Personnel experience
			6. SCED: Schedule
			7. FCIL: The team support facilities
		- `A = 2.94 in initial calibration`
		- Size = KLOC
		- B = complexity (1.1 - 1.24)
- Effort = 2.94 x Size^(1.1-1.24) x M
- Effort = 2.94 x 128000^1.17 x 1 = 847 PM
### Multipliers (M)
- Multipliers reflect in capability of
	- the developers experiences
	- the NFR (non-functional requirements)
	- the familiarity with the development platform, etc.
- Seven Multipliers:
	- RCPX - product reliability and complexity
	- RUSE - the reuse required
	- PDIF - platform difficulty
	- PREX - personnel experience (familiarly and proficiency with specific tech)
	- PRES - personnel capability (competency or qualifications)
	- SCED - required schedule
	- FCIL - the team support facilities
![[Pasted image 20240416001441.png]]
## The Reuse model
- Used to estimate effort needed to integrate reusable components, codes, etc.
- Takes into account black-box code and white-box reused code
- There are two versions:
	- Black-box reuse (code is not modified)
		- no need to understand the code
	- White-box reuse (code is modified)
		- Need development effort to understand and reuse the code
## Compute the source code equivalent
- The formula used to compute the source code equivalent is complex and consists of
	- `ESLOC = (ASLOC x 1 - AT / 100) x AAM` where
		- ESLOC = the equivalent number of lines of new source code
		- ASLOC = an estimate of LOCs in the reused components that have to be changed
		- AT = The percentage of reused code that can be modified automatically
		- AAM = an adaption adjustment multiplier refracting the additional effort needed to access, understand, and modify the reuse component
	- `Effort = A x ESLOC^B x M` where
		- A, B, and M have the same values as used in the early design model
## Post-architecture level
- The most detailed of Models in the COCOMO II
- Applied when the software architecture becomes available
- Uses a standard formula with 15 multipliers
	- `Effort = A x Size^B x M`
- The code SIZE is computed by adding the following estimates:
	1. Number of new SLOCs to be developed
	2. Estimate of reused costs using ESLOC
	3. An estimate of the number of lines of modified code
		- i.e., the code that may be modified because of changing requirements
## About Exponent term 'B'
- B exponent in formula
	- reflects project complexity
	- depends on 5 factors
- Calculated:
	- `B = (SUM Fi / 100) + 1.01` where I (factor) is from 1-5
- Factors are rated on a six-point scale from 0 (very high) - 5 (very low)
![[Pasted image 20240416113356.png]]
## Example 1: A company working on a new project
- Suppose a company takes on a project
	- The project is in a new domain with new hiring
	- The client has not demanded a process to be used
	- Not enough time is spent on risk analysis
	- Team members are new
	- The company has a CMM level is 2 rating
### Solution
- Rank the B based on five factors on a scale of 0 to 5
	- Precedent: new project means low (4)
	- Development flexibility: no client involvement means very high (1)
	- Architecture/risk resolution: no risk analysis means very low (5)
	- Team cohesion: a new team which means nominal (3)
	- Process maturity: some control which means nominal (3)
## Partial list of multipliers and their descriptions
- Product attributes
	- Describes quality of the software product being developed
		- Reliability (RELY)
		- Complexity (CPLX)
- Platform attributes (computer)
	- Time and space constraints imposed on the software by the hardware platform
		- Execution Time (TIME), Memory etc.
- Personnel attributes
	- Has to do with expertise and skills of the people working on the project into account
		- Language skill and experience (LEXP)
- Project attributes (process)
	- Concerned with the particular characteristics of the software development project
		- CASE tool (TOOL)
![[Pasted image 20240416114418.png]]
## Project duration and staffing
- The calendar time required to complete a project and what staff will be required
- Calendar time can be estimated using a COCOMO II formula
	- TDEV = 3 x (effort) ^(0.33+0.2 x (B-1.01))
		- Effort = PM
		- B = the exponent computed as discussed above (B is 1 for the early prototyping model)
## Staffing requirements
- Staff needed to perform the job can't be computed by dividing the total effort by the required schedule
- The number of people working on a project varies depending on the phase of the project
	- Number of staff is small at the beginning (initial design)
	- Number of staff is large during development and testing
	- Number of staff is small during deployment
- In general, the more people work on the project, the more effort is required because people spend more time on communicating with each other
## Pros and Cons of COCOMO II
- COCOMO II
- Strengths
	- Relatively objective, repeatable
	- Analyzable formula
	- Efficient, good for sensitivity analysis
- Weaknesses
	- Subjective inputs because of M, B
	- Assessment of exceptional circumstances
	- Calibrated to past, not future
## Expert Judgement (revisited)
- A typical method for estimating the cost size by experts involve three possible code sizes
- Estimated size S is computed as
	- `S = (SI + SH + 4SM) / 6`
- Strengths (GOOD)
	- Assessment of representativeness, interactions, exceptional circumstances
	- Fast estimate
- Weaknesses (BAD)
	- No better than the participants
	- Suffers from biases, incomplete
	- The complexity of the new project might be different from previous ones
## Performance of estimation models
- Many studies have attempted to evaluate the cost estimation models
	- Results are NOT encouraging
- No model can estimate the cost of software with a high degree of accuracy because of
	- So man y interrelated factors exist (user screens, volatility of system requirements, etc.)
	- Using COTS
	- Lack of Complexity measurements
	- Development environments
	- Type of applications
	- Lack of established data repository of the projects by industries
## ML approaches to cost estimation
- Cost estimation using machine learning involves using algorithms to predict the costs associated with various projects, tasks, or activities based on historical data, features, and other relevant factors.
- The key steps involve:
	- Data collection
	- Data Preprocessing
	- Feature selection/engineering
	- Model selection
	- Training the model
	- Model evaluation
	- Hyperparameter Tuning
	- Deployment
	- Monitoring and Maintenance
## The content of project plan documentation
- Project scope
- Project schedule
- Project team organization
- Technical description of system
- Project standards and procedures
- Quality assurance plan
- Configuration management plan
- Documentation plan
- Data management plan
- Resource management plan
- Test plan
- Training plan
- Security plan
- Risk management plan
- Maintenance plan