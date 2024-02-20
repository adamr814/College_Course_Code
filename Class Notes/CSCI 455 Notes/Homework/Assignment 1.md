### Patient
Entity: Patient (Has unique prescription with data and quantity)
Attributes: SSN, Name {First Name, Middle Name, Last Name}, Address, Age
Relationships: Primary Care Provider (Doctor), Prescription (Can be from multiple Doctors)

### Doctor
Entity: Doctor
Attributes: SSN, Name {First Name, Middle Name, Last Name}, Specialty, Years of Experience
Relationships: Patients

### Pharmaceutical Company
Entity: Pharmaceutical Company
Attributes: Name, Phone Number

### Drug
Entity: Drug
Attributes: Trade Name (unique to company), Formula, Price of Drug
Relationship: Pharmaceutical Company, Pharmacy, Prescription

### Pharmacy
Entity: Pharmacy
Attributes: Name, Address, Phone Number
Relationship: Drug

### Prescription
Entity: Prescription
Attributes: Unique Identifier, Date Prescribed, Quantity of Drug
Relationship: Doctor, Patient, Drug, Pharmacy
