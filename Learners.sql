drop database if exists learners;
create database learners;
use learners;

DROP TABLE IF EXISTS `course_table`;
CREATE TABLE IF NOT EXISTS `course_table` (
  `Course_ID` text NOT NULL,
  `Course_Name` text NOT NULL,
  `Section` text NOT NULL,
  `Course_Description` text NOT NULL,
  `Course_Vacancy` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `employee_table`;
CREATE TABLE IF NOT EXISTS `employee_table` (
  `Employee_ID` text NOT NULL,
  `Username` text NOT NULL,
  `Employee_Name` text NOT NULL,
  `Designation` text NOT NULL,
  `Department` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `quiz_table`;
CREATE TABLE IF NOT EXISTS `quiz_table` (
  `Course_ID` text NOT NULL,
  `Quiz_Number` text NOT NULL,
  `Quiz_Name` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO employee_table (Employee_ID, Username, Employee_Name, Designation, Department) VALUES
('1', 'Johnhhh', 'john doe', 'Senior Engineer', 'Engineers');
INSERT INTO employee_table (Employee_ID, Username, Employee_Name, Designation, Department) VALUES
('2', 'Maryyyy', 'Mary Tan', 'Engineer', 'Learner');
INSERT INTO employee_table (Employee_ID, Username, Employee_Name, Designation, Department) VALUES
('3', 'Johnhhh', 'john doe', 'Engineer', 'Learner');
INSERT INTO employee_table (Employee_ID, Username, Employee_Name, Designation, Department) VALUES
('4', 'Johnhhh', 'john doe', 'HR', 'HR');


INSERT INTO course_table (Course_ID, Course_Name, Section, Course_Description, Course_Vacancy) VALUES
('1111', 'Engineering Business','G1', 'Learn to be good at engineering', '40');
INSERT INTO course_table (Course_ID, Course_Name, Section, Course_Description, Course_Vacancy) VALUES
('1111', 'Engineering Business','G2', 'Learn to be good at engineering', '40');
INSERT INTO course_table (Course_ID, Course_Name, Section, Course_Description, Course_Vacancy) VALUES
('1112', 'Engineering Mechanics','G1', 'Learn to be good at engineering', '40');
INSERT INTO course_table (Course_ID, Course_Name, Section, Course_Description, Course_Vacancy) VALUES
('1113', 'Engineering Science','G1', 'Learn to be good at engineering', '40');
INSERT INTO course_table (Course_ID, Course_Name, Section, Course_Description, Course_Vacancy) VALUES
('1114', 'Engineering Math','G1', 'Learn to be good at engineering', '40');

INSERT INTO quiz_table (Course_ID, Quiz_Number, Quiz_Name) VALUES
('1111', '1', 'Math level 1');
INSERT INTO quiz_table (Course_ID, Quiz_Number, Quiz_Name) VALUES
('1111', '2', 'Math level 2');
INSERT INTO quiz_table (Course_ID, Quiz_Number, Quiz_Name) VALUES
('1111', '3', 'Math level 3');
INSERT INTO quiz_table (Course_ID, Quiz_Number, Quiz_Name) VALUES
('1112', '4', 'Math level 4');
INSERT INTO quiz_table (Course_ID, Quiz_Number, Quiz_Name) VALUES
('1112', '1', 'Dropout rate level 1');
INSERT INTO quiz_table (Course_ID, Quiz_Number, Quiz_Name) VALUES
('1113', '1', 'Revision 1');
INSERT INTO quiz_table (Course_ID, Quiz_Number, Quiz_Name) VALUES
('1113', '2', 'Revision 2');
INSERT INTO quiz_table (Course_ID, Quiz_Number, Quiz_Name) VALUES
('1114', '1', 'Mechanics 1');

COMMIT;

