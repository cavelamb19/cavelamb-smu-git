-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Sep 27, 2021 at 08:33 AM
-- Server version: 5.7.26
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `is212_example`
--
CREATE DATABASE IF NOT EXISTS `lms_IS212` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `lms_IS212`;

-- --------------------------------------------------------

--
-- Table structure for table `Course`
--

CREATE TABLE `Course` (
  `courseID` int(11) NOT NULL,
  `courseName` varchar(50) DEFAULT NULL,
  `courseDesc` varchar(50) DEFAULT NULL,
  `preRequisites` varchar(50) DEFAULT NULL,
  `classesID` int(11)  NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Course` (`courseID`, `courseName`, `courseDesc`, `preRequisites`, `classesID`) VALUES
(1, 'IS212 Software Project Management G2', 'agile methods', 'NULL', 1),
(2, 'IS115 Computational Thinking G1', 'Math and coding', 'IS112 Business applications', 2),
(3, 'IS113 Web application G3', 'Designing frontend web', 'NULL', 3),
(4, 'IS112 Business applications G1', 'Business processes', 'NULL', 4),
(5, 'IS212 Software Project Management G3', 'agile methods', 'NULL', 5);


-- --------------------------------------------------------
-- Table structure for table `Classes`
--

CREATE TABLE `Classes` (
  `classesID` int(11)  NOT NULL,
  `startDate` varchar(50) DEFAULT NULL,
  `startTime` varchar(50)  DEFAULT NULL,
  `endDate` varchar(50) DEFAULT NULL,
  `endTime` varchar(50) DEFAULT NULL,
  `classesSize` int(11) DEFAULT NULL,
  `trainerAssigned` varchar(50)  DEFAULT NULL,
  `currentEnrolled` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Classes` (`classesID`, `startDate`, `startTime`, `endDate`, `endTime`, `classesSize`, `trainerAssigned`, `currentEnrolled`) VALUES
(1, 'August 18 2021', '8am', 'November 5 2021', '12pm', 50, 'James Sim', 0),
(2, 'August 30 2021', '12pm', 'November 2 2021', '3pm', 50, 'John Tan', 0),
(3, 'August 5 2021', '3.15pm', 'November 8 2021', '6.45pm', 50, 'Alan Lim', 0),
(4, 'August 27 2021', '3.15pm', 'November 13 2021', '6.45pm', 50, 'Brandon Lum', 0),
(5, 'August 22 2021', '12pm', 'November 16 2021', '3pm', 50, 'Mary low', 0);


-- --------------------------------------------------------
-- --------------------------------------------------------
-- Table structure for table `Lesson`
--

CREATE TABLE `Lesson` (
  `lessonID` int(11)  NOT NULL,
  `courseMaterial` varchar(50) DEFAULT NULL,
  `classesID` int(11)  NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Lesson` (`lessonID`, `courseMaterial`,`classesID`) VALUES
(1, 'Week1a-Introduction', 1),
(2, 'Week2-SWDevProcess', 1);
-- --------------------------------------------------------
-- --------------------------------------------------------
-- Table structure for table `Quiz`
--
CREATE TABLE `Quiz` (
  `quizID` int(11)  NOT NULL,
  `StartTime` varchar(50) DEFAULT NULL,
  `EndTime` varchar(50) DEFAULT NULL,
  `quizDuration` varchar(50) DEFAULT NULL,
  `attemptNo` varchar(50) DEFAULT NULL,
  `quizTitle`  varchar(50) DEFAULT NULL,
  `quizDesc`  varchar(50) DEFAULT NULL,
  `lessonID` int(11)  DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Table structure for table `Quiz`
--
CREATE TABLE `Quizscore` (
  `qsID` int(11)  NOT NULL,
  `quizscore` float(50) DEFAULT NULL,
  `quizID` int(11) DEFAULT NULL,
  `learnerID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Table structure for table `Question`
--

CREATE TABLE `Question` (
  `qnID` int(11)  NOT NULL,
  `qn` varchar(10000) DEFAULT NULL,
  `ans` varchar(10000) DEFAULT NULL,
  `ansID` int(11) DEFAULT NULL,
  `qnType` varchar(50) DEFAULT NULL,
  `quizID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `QuizAttempt` (
  `AttemptID` int(11)  NOT NULL,
  `qn` varchar(10000) DEFAULT NULL,
  `qnID` int(11)  DEFAULT NULL,
  `ans` varchar(10000) DEFAULT NULL,
  `ansID` int(11) DEFAULT NULL,
  `qnType` varchar(50) DEFAULT NULL,
  `quizID` int(11) DEFAULT NULL,
  `learnerID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- --------------------------------------------------------
--
-- Table structure for table `Administrator`
--

CREATE TABLE `Administrator` (
  `id` int(11) NOT NULL  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Administrator`
--

INSERT INTO `Administrator` (`id`) VALUES
(1);

-- --------------------------------------------------------
-- Table structure for table `Trainer`
--

CREATE TABLE `Trainer` (
  `id` int(11) NOT NULL,
  `coursesTeaching` varchar(50) DEFAULT NULL
  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Trainer`
--

INSERT INTO `Trainer` (`id`, `coursesTeaching`) VALUES
(2, 'IS212 Software Project Management G2');

-- --------------------------------------------------------

--
-- Table structure for table `learner`
--

CREATE TABLE `Learner` (
  `id` int(11) NOT NULL,
  `CoursesAssigned` varchar(50)  DEFAULT NULL,
  `CompletedCourses` varchar(50)  DEFAULT NULL,
  `CoursesEnrolled` varchar(50) DEFAULT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Learner`
--

INSERT INTO `Learner` (`id`, `CoursesAssigned`, `CompletedCourses`,`CoursesEnrolled`) VALUES
(3, '', 'IS214 System Design', ''),
(4, '', 'IS115 Computational Thinking', ''),
(5, '', 'IS113 Web application', ''),
(6, '', 'IS112 Business applications', '');

-- --------------------------------------------------------

--
-- Table structure for table `Employee`
--

CREATE TABLE `Employee` (
  `StaffID` int(11) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Username` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `CurrentDesignation` varchar(50) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  `ContactNo` varchar(50) DEFAULT NULL,
  `Role` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Employee`
--

INSERT INTO `Employee` (`staffID`, `Name`, `Username`,`Email`,`CurrentDesignation`,`Department`,`ContactNo`,`Role`) VALUES
(1, 'Phris Coskitt', 'csok','coski@gmail.com','Hr','hr','90227823','administrator'),
(2, 'Arnold de Mari', 'Ard','Dr@gmail.com','Senior Engineer','Training','82329832','trainer'),
(3, 'Constance Wilkinson', 'cons','cons@gmail.com','Engineer','Learning','92130843','learner'),
(4, 'Johnson sim', 'john','johnson@gmail.com','Engineer','Learning','90247788','learner'),
(5, 'Mary lamb', 'Mar','Mar@gmail.com','Engineer','Learning','83425667','learner'),
(6, 'David bee', 'bee','bee@gmail.com','Engineer','Learning','92358877','learner');



ALTER TABLE `Course`
  ADD PRIMARY KEY (`courseID`),
  ADD KEY `classesID` (`classesID`);

ALTER TABLE `Classes`
  ADD PRIMARY KEY (`classesID`);

ALTER TABLE `Lesson`
  ADD PRIMARY KEY (`lessonID`),
  ADD KEY `classesID` (`classesID`);

ALTER TABLE `Quiz`
  ADD PRIMARY KEY (`quizID`),
  ADD KEY `lessonID` (`lessonID`);

ALTER TABLE `Quizscore`
  ADD PRIMARY KEY (`qsID`),
  ADD KEY `quizID` (`quizID`),
  ADD KEY `learnerID` (`learnerID`);

ALTER TABLE `Question`
  ADD PRIMARY KEY (`qnID`),
  ADD KEY `quizID` (`quizID`);

ALTER TABLE `QuizAttempt`
  ADD PRIMARY KEY (`AttemptID`),
  ADD KEY `quizID` (`quizID`);

  
ALTER TABLE `Course`
  ADD CONSTRAINT `Course_ibfk_1` FOREIGN KEY (`classesID`) REFERENCES `Classes`(`classesID`);  

ALTER TABLE `Lesson`
  ADD CONSTRAINT `Lesson_ibfk_1` FOREIGN KEY (`classesID`) REFERENCES `Classes`(`classesID`);

ALTER TABLE `Quiz`
  ADD CONSTRAINT `Quiz_ibfk_1` FOREIGN KEY (`lessonID`) REFERENCES `Lesson`(`lessonID`);

ALTER TABLE `Quizscore`
  ADD CONSTRAINT `Quizscore_ibfk_1` FOREIGN KEY (`quizID`) REFERENCES `Quiz`(`quizID`);

ALTER TABLE `Question`
  ADD CONSTRAINT `Question_ibfk_1` FOREIGN KEY (`quizID`) REFERENCES `Quiz`(`quizID`);

ALTER TABLE `QuizAttempt`
  ADD CONSTRAINT `QuizAttempt_ibfk_1` FOREIGN KEY (`quizID`) REFERENCES `Quiz`(`quizID`);
  

--
-- AUTO_INCREMENT for table QuizAttempt
--
ALTER TABLE  `QuizAttempt`
  MODIFY `AttemptID` int(11) NOT NULL AUTO_INCREMENT;              

ALTER TABLE `Employee`
  ADD PRIMARY KEY (`StaffID`);

ALTER TABLE `Learner`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `Trainer`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `Administrator`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `Learner`
  ADD CONSTRAINT `learner_ibfk_1` FOREIGN KEY (`id`) REFERENCES `Employee` (`StaffID`);

ALTER TABLE `Trainer`
  ADD CONSTRAINT `trainer_ibfk_1` FOREIGN KEY (`id`) REFERENCES `Employee` (`StaffID`);

ALTER TABLE `Administrator`
  ADD CONSTRAINT `administrator_ibfk_1` FOREIGN KEY (`id`) REFERENCES `Employee` (`StaffID`);






