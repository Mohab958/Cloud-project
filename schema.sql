CREATE DATABASE student;
USE student;

CREATE TABLE students (
    Student_Id INT NOT NULL,
    Student_Name VARCHAR(100) NOT NULL,
    Student_Age  INT NOT NULL,
    Student_CGPA FLOAT NOT NULL,
    PRIMARY KEY (Student_Id)
);

INSERT INTO students (Student_Id, Student_Name, Student_Age, Student_CGPA) VALUES
(22011559, 'Mohamed Sameh Salah', 20, 3.4),
(22011650, 'Mohab Ahmed Elsaied', 20, 3.5),
(22011555, 'Mohamed Ahmed Khalaf', 20, 3.3),
(22010042, 'Adham Ehab Mokhtar', 20, 3.2),
(22010117, 'Seif Ayman Abo Elyazid', 20, 3.1);