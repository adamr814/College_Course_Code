# OptiChart-MySQL Query - Create Tables
# Version 1.0
# Purpose: This is used to define and create the database structure for OptiChart.
# Creation Date: 4-29-2024
# Modification History:
### 4-29-2024 - First version based on class diagram and class descriptions

use OptiChart;

CREATE TABLE
    Patient (
        MRN INT NOT NULL,
        lastName VARCHAR(20) NOT NULL,
        firstName VARCHAR(20) NOT NULL,
        username VARCHAR(20) NOT NULL UNIQUE, -- Ensures unique usernames
        password VARCHAR(20) NOT NULL,
        DOB DATE NOT NULL,
        gender CHAR(1) NOT NULL CHECK (gender IN ('M', 'F')),
        address VARCHAR(30) NOT NULL,
        phoneNumber VARCHAR(20) NOT NULL,
        contactPreference VARCHAR(8) NOT NULL CHECK (contactPreference IN ('CALL', 'TEXT', 'MAIL')),
        referralNumber VARCHAR(20) DEFAULT NULL -- Allows null values
        PRIMARY KEY (MRN)
    );

CREATE TABLE
    Staff (
        EIN INT NOT NULL,
        lastName VARCHAR(20) NOT NULL,
        firstName VARCHAR(20) NOT NULL,
        username VARCHAR(20) NOT NULL UNIQUE, -- Ensures unique usernames
        password VARCHAR(20) NOT NULL,
        role VARCHAR(10) NOT NULL CHECK (role IN ('Physician', 'Assistant', 'Admin')),
        email VARCHAR(20) NOT NULL UNIQUE, -- Ensures unique email addresses
        PRIMARY KEY (EIN)
    );

CREATE TABLE
    Visit (
        visitID INT AUTO_INCREMENT NOT NULL,
        staffEIN INT NOT NULL,
        apptID INT NOT NULL,
        chiefComplaint TEXT,
        allergies VARCHAR(30),
        medications VARCHAR(30),
        surgeries VARCHAR(30),
        familyHistory TEXT,
        socialHistory TEXT,
        testResults TEXT NOT NULL,
        apptNotes TEXT NOT NULL,
        followup TEXT,
        orders VARCHAR(30) NOT NULL,
        PRIMARY KEY (visitID),
        FOREIGN KEY (staffEIN) REFERENCES Staff (EIN),
        FOREIGN KEY (apptID) REFERENCES Appointment (apptID)
    );

CREATE TABLE
    Appointment (
        apptID INT AUTO_INCREMENT NOT NULL,
        date DATE NOT NULL,
        time TIME NOT NULL,
        reason TEXT,
        room VARCHAR(5),
        patientMRN INT NOT NULL,
        staffEIN INT NOT NULL,
        PRIMARY KEY (apptID),
        FOREIGN KEY (patientMRN) REFERENCES Patient (MRN),
        FOREIGN KEY (staffEIN) REFERENCES Staff (EIN)
    );

CREATE TABLE
    Insurance (
        insuranceID INT PRIMARY KEY,
        patientMRN INT NOT NULL,
        policyNumber INT NOT NULL,
        policyHolder VARCHAR(40) NOT NULL,
        provider VARCHAR(20) NOT NULL,
        FOREIGN KEY (patientMRN) REFERENCES Patient (MRN)
    );

CREATE TABLE
    Prescription (
        prescriptionID INT AUTO_INCREMENT NOT NULL,
        patientMRN INT NOT NULL,
        staffEIN INT NOT NULL,
        medicationID INT NOT NULL,
        dosage VARCHAR(20) NOT NULL,
        pharmacyID INT NOT NULL,
        startDate DATE NOT NULL,
        endDate DATE NOT NULL,
        PRIMARY KEY (prescriptionID),
        FOREIGN KEY (patientMRN) REFERENCES Patient (MRN),
        FOREIGN KEY (staffEIN) REFERENCES Staff (EIN),
        FOREIGN KEY (medicationID) REFERENCES Medication (medicationID),
        FOREIGN KEY (pharmacyID) REFERENCES Pharmacy (pharmacyID)
    );

CREATE TABLE
    Pharmacy (
        pharmacyID INT NOT NULL,
        name VARCHAR(20) NOT NULL,
        address VARCHAR(30) NOT NULL,
        phone VARCHAR(20) NOT NULL,
        PRIMARY KEY pharmacyID
    );

CREATE TABLE
    TestResults (
        resultID INT AUTO_INCREMENT NOT NULL,
        patientMRN INT NOT NULL,
        staffEIN INT NOT NULL,
        testID INT NOT NULL,
        result TEXT NOT NULL,
        PRIMARY KEY (resultID),
        FOREIGN KEY (patientMRN) REFERENCES Patient (MRN),
        FOREIGN KEY (staffEIN) REFERENCES Staff (EIN),
        FOREIGN KEY (testID) REFERENCES Test (testID)
    );

CREATE TABLE
    Test (
        testID INT AUTO_INCREMENT NOT NULL,
        name VARCHAR(20) NOT NULL,
        purpose TEXT,
        PRIMARY KEY testID
    );

CREATE TABLE
    Medication (
        medicationID INT,
        name VARCHAR(20) NOT NULL,
        PRIMARY KEY medicationID
    );
