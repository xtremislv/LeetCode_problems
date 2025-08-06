# Write your MySQL query statement below
Select patient_id, patient_name, conditions From Patients
Where conditions like 'DIAB1%' Or conditions like '% DIAB1%'