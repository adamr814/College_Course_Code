
CREATE DATABASE COMPANY;
USE COMPANY;

CREATE TABLE EMPLOYEE
		(Fname				VARCHAR(15)				NOT NULL,
         Minit				CHAR,
         Lname				VARCHAR(15)				NOT NULL,
         Ssn				CHAR(9)					NOT NULL,
         Bdate				DATE,
         Address			VARCHAR(30),
         Sex				CHAR,
         Salary				DECIMAL(10,2),
         Super_ssn			CHAR(9),
         Dno				INT						NOT NULL,
		PRIMARY KEY (Ssn));
CREATE TABLE DEPARTMENT
		(Dname				VARCHAR(15)				NOT NULL,
         Dnumber			INT						NOT NULL,
         Mgr_ssn			CHAR(9)					NOT NULL,
         Mgr_start_date		DATE,
		PRIMARY KEY (Dnumber),
        UNIQUE (Dname),
        FOREIGN KEY (Mgr_ssn) REFERENCES EMPLOYEE(Ssn));
CREATE TABLE DEPT_LOCATIONS
		(Dnumber			INT						NOT NULL,
		 Dlocation			VARCHAR(15) 			NOT NULL,
		PRIMARY KEY (Dnumber, Dlocation),
        FOREIGN KEY (Dnumber) REFERENCES DEPARTMENT(Dnumber));
CREATE TABLE PROJECT
		(Pname				VARCHAR(15) 			NOT NULL,
         Pnumber 			INT 					NOT NULL,
         Plocation			VARCHAR(15),
         Dnum 				INT 					NOT NULL,
		PRIMARY KEY (Pnumber),
        UNIQUE (Pname),
        FOREIGN KEY (Dnum) REFERENCES DEPARTMENT (Dnumber));
CREATE TABLE DEPENDENT
		(Essn 				CHAR(9) 				NOT NULL,
         Dependent_name 	VARCHAR(15) 			NOT NULL,
         Sex 				CHAR,
         Bdate 				DATE,
         Relationship 		VARCHAR(8),
         PRIMARY KEY (Essn, Dependent_name),
         FOREIGN KEY (Essn) REFERENCES EMPLOYEE (Ssn));
CREATE TABLE WORKS_ON
		(Essn 				CHAR(9) 				NOT NULL,
         Pno 				INT 					NOT NULL,
         Hours 				DECIMAL(3,1)			NOT NULL,
		PRIMARY KEY (Essn, Pno),
        FOREIGN KEY (Essn) REFERENCES EMPLOYEE(Ssn),
        FOREIGN KEY (Pno) REFERENCES PROJECT (Pnumber));

INSERT INTO COMPANY.EMPLOYEE (Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) VALUES ('John', 'B', 'Smith', '123456789', '1965-01-09', '731 Fondren, Houston, TX', 'M', '30000', '333445555', '5');
INSERT INTO COMPANY.EMPLOYEE (Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) VALUES ('Franklin', 'T', 'Wong', '333445555', '1955-12-08', '638 Voss, Houston, TX', 'M', '40000', '888665555', '5');
INSERT INTO COMPANY.EMPLOYEE (Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) VALUES ('Alicia', 'J', 'Zelaya', '999887777', '1968-01-19', '3321 Castle, Spring, TX', 'F', '25000', '987654321', '4');
INSERT INTO COMPANY.EMPLOYEE (Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) VALUES ('Jennifer', 'S', 'Wallace', '987654321', '1941-06-20', '291 Berry, Bellaire, TX', 'F', '43000', '888665555', '4');
INSERT INTO COMPANY.EMPLOYEE (Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) VALUES ('Ramesh', 'K', 'Narayan', '666884444', '1962-09-15', '975 Fire Oak, Humble, TX', 'M', '38000', '333445555', '5');
INSERT INTO COMPANY.EMPLOYEE (Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) VALUES ('Joyce', 'A', 'English', '453453453', '1972-07-31', '5631 Rice, Houston, TX', 'F', '25000', '333445555', '5');
INSERT INTO COMPANY.EMPLOYEE (Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) VALUES ('Ahmad', 'V', 'Jabbar', '987987987', '1969-03-29', '980 Dallas, Houston, TX', 'M', '25000', '987654321', '4');
INSERT INTO COMPANY.EMPLOYEE (Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) VALUES ('James', 'E', 'Borg', '888665555', '1937-11-10', '450 Stone, Houston, TX', 'M', '55000', 'NULL', '1');

INSERT INTO COMPANY.DEPARTMENT (Dname, Dnumber, Mgr_ssn, Mgr_start_date) VALUES ('Research', '5', '333445555', '1988-05-22');
INSERT INTO COMPANY.DEPARTMENT (Dname, Dnumber, Mgr_ssn, Mgr_start_date) VALUES ('Administration', '4', '987654321', '1995-01-01');
INSERT INTO COMPANY.DEPARTMENT (Dname, Dnumber, Mgr_ssn, Mgr_start_date) VALUES ('Headquarters', '1', '888665555', '1981-06-19');

INSERT INTO COMPANY.DEPT_LOCATIONS (Dnumber, Dlocation) VALUES ('1', 'Houston');
INSERT INTO COMPANY.DEPT_LOCATIONS (Dnumber, Dlocation) VALUES ('4', 'Stafford');
INSERT INTO COMPANY.DEPT_LOCATIONS (Dnumber, Dlocation) VALUES ('5', 'Bellaire');
INSERT INTO COMPANY.DEPT_LOCATIONS (Dnumber, Dlocation) VALUES ('5', 'Sugarland');
INSERT INTO COMPANY.DEPT_LOCATIONS (Dnumber, Dlocation) VALUES ('5', 'Houston');

INSERT INTO COMPANY.PROJECT (Pname, Pnumber, Plocation, Dnum) VALUES ('ProductX', '1', 'Bellaire', '5');
INSERT INTO COMPANY.PROJECT (Pname, Pnumber, Plocation, Dnum) VALUES ('ProductY', '2', 'Sugarland', '5');
INSERT INTO COMPANY.PROJECT (Pname, Pnumber, Plocation, Dnum) VALUES ('ProductZ', '3', 'Houston', '5');
INSERT INTO COMPANY.PROJECT (Pname, Pnumber, Plocation, Dnum) VALUES ('Computerization', '10', 'Stafford', '4');
INSERT INTO COMPANY.PROJECT (Pname, Pnumber, Plocation, Dnum) VALUES ('Reorganization', '20', 'Houston', '1');
INSERT INTO COMPANY.PROJECT (Pname, Pnumber, Plocation, Dnum) VALUES ('Newbenefits', '30', 'Stafford', '4');

INSERT INTO COMPANY.DEPENDENT (Essn, Dependent_name, Sex, Bdate, Relationship) VALUES ('333445555', 'Alice', 'F', '1986-04-05', 'Daughter');
INSERT INTO COMPANY.DEPENDENT (Essn, Dependent_name, Sex, Bdate, Relationship) VALUES ('333445555', 'Theodore', 'M', '1983-10-25', 'Son');
INSERT INTO COMPANY.DEPENDENT (Essn, Dependent_name, Sex, Bdate, Relationship) VALUES ('333445555', 'Joy', 'F', '1958-05-03', 'Spouse');
INSERT INTO COMPANY.DEPENDENT (Essn, Dependent_name, Sex, Bdate, Relationship) VALUES ('987654321', 'Abner', 'M', '1942-02-28', 'Spouse');
INSERT INTO COMPANY.DEPENDENT (Essn, Dependent_name, Sex, Bdate, Relationship) VALUES ('123456789', 'Michael', 'M', '1988-01-04', 'Son');
INSERT INTO COMPANY.DEPENDENT (Essn, Dependent_name, Sex, Bdate, Relationship) VALUES ('123456789', 'Alice', 'F', '1988-12-30', 'Daughter');
INSERT INTO COMPANY.DEPENDENT (Essn, Dependent_name, Sex, Bdate, Relationship) VALUES ('123456789', 'Elizabeth', 'F', '1967-05-05', 'Spouse');

INSERT INTO COMPANY.WORKS_ON (Essn, Pno, Hours) VALUES ('123456789', '1', '32.5');
INSERT INTO COMPANY.WORKS_ON (Essn, Pno, Hours) VALUES ('123456789', '2', '7.5');
INSERT INTO COMPANY.WORKS_ON (Essn, Pno, Hours) VALUES ('666884444', '3', '40.0');
INSERT INTO COMPANY.WORKS_ON (Essn, Pno, Hours) VALUES ('453453453', '1', '20.0');
INSERT INTO COMPANY.WORKS_ON (Essn, Pno, Hours) VALUES ('453453453', '2', '20.0');
INSERT INTO COMPANY.WORKS_ON (Essn, Pno, Hours) VALUES ('333445555', '2', '10.0');
INSERT INTO COMPANY.WORKS_ON (Essn, Pno, Hours) VALUES ('333445555', '3', '10.0');
INSERT INTO COMPANY.WORKS_ON (Essn, Pno, Hours) VALUES ('333445555', '10', '10.0');
INSERT INTO COMPANY.WORKS_ON (Essn, Pno, Hours) VALUES ('333445555', '20', '10.0');
INSERT INTO COMPANY.WORKS_ON (Essn, Pno, Hours) VALUES ('999887777', '30', '30.0');
INSERT INTO COMPANY.WORKS_ON (Essn, Pno, Hours) VALUES ('999887777', '10', '10.0');
INSERT INTO COMPANY.WORKS_ON (Essn, Pno, Hours) VALUES ('987987987', '10', '35.0');
INSERT INTO COMPANY.WORKS_ON (Essn, Pno, Hours) VALUES ('987987987', '30', '5.0');
INSERT INTO COMPANY.WORKS_ON (Essn, Pno, Hours) VALUES ('987654321', '30', '20.0');
INSERT INTO COMPANY.WORKS_ON (Essn, Pno, Hours) VALUES ('987654321', '20', '15.0');
INSERT INTO COMPANY.WORKS_ON (Essn, Pno, Hours) VALUES ('888665555', '20', '0.0');