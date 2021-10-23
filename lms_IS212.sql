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

INSERT INTO `course` (`courseID`, `courseName`, `courseDesc`, `preRequisites`, `classesID`) VALUES
(1, 'IS212 Software Project Management G2', 'agile methods', 'NULL', 1);


-- --------------------------------------------------------
-- Table structure for table `Classes`
--

CREATE TABLE `Classes` (
  `classesID` int(11)  NOT NULL,
  `startDate` date DEFAULT NULL,
  `startTime` timestamp  DEFAULT NULL,
  `endDate` date  DEFAULT NULL,
  `endTime` timestamp  DEFAULT NULL,
  `classesSize` int(11) DEFAULT NULL,
  `trainerAssigned` varchar(50)  DEFAULT NULL,
  `currentEnrolled` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `classes` (`classesID`, `startDate`, `startTime`, `endDate`, `endTime`, `classesSize`, `trainerAssigned`, `currentEnrolled`) VALUES
(1, '2021-10-18', '2021-10-18 06:30:00', '2021-11-18', '2021-11-18 06:30:00', 50, 'Arnold de Mari', 0);

-- --------------------------------------------------------
-- --------------------------------------------------------
-- Table structure for table `Lesson`
--

CREATE TABLE `Lesson` (
  `lessonID` int(11)  NOT NULL,
  `courseMaterial` varchar(50) DEFAULT NULL,
  `quizID` int(11) DEFAULT NULL,
  `classesID` int(11)  NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `lesson` (`lessonID`, `courseMaterial`, `quizID`, `classesID`) VALUES
(1, 'Week1a-Introduction', 1, 1);
-- --------------------------------------------------------
-- --------------------------------------------------------
-- Table structure for table `Quiz`
--

CREATE TABLE `Quiz` (
  `quizID` int(11)  NOT NULL,
  `qn` varchar(50) DEFAULT NULL,
  `qnID` int(11) DEFAULT NULL,
  `ans` varchar(50) DEFAULT NULL,
  `ansID` int(11) DEFAULT NULL,
  `qnType` varchar(50) DEFAULT NULL,
  `StartTime` timestamp DEFAULT NULL,
  `EndTime` timestamp DEFAULT NULL,
  `qnDuration` timestamp DEFAULT NULL,
  `attemptNo` int(11) DEFAULT NULL,
  `quizScore` float(50) DEFAULT NULL
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
(2, 'IS212 Software Project Management');

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
(3, '', 'IS214 System Design', 'IS216 Software Design');

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
  `ContactNo` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Employee`
--

INSERT INTO `Employee` (`staffID`, `Name`, `Username`,`Email`,`CurrentDesignation`,`Department`,`ContactNo`) VALUES
(1, 'Phris Coskitt', 'csok','coski@gmail.com','administrator','hr','90227823'),
(2, 'Arnold de Mari', 'Dr','Dr@gmail.com','trainer','Training','82329832'),
(3, 'Constance Wilkinson', 'cons','cons@gmail.com','learner','Learning','92130843');


ALTER TABLE `Course`
  ADD PRIMARY KEY (`courseID`),
  ADD KEY `classesID` (`classesID`);

ALTER TABLE `Classes`
  ADD PRIMARY KEY (`classesID`);

ALTER TABLE `Lesson`
  ADD PRIMARY KEY (`lessonID`);

ALTER TABLE `Quiz`
  ADD PRIMARY KEY (`quizID`);


  
ALTER TABLE `Lesson`
  ADD CONSTRAINT `Lesson_ibfk_1` FOREIGN KEY (`classesID`) REFERENCES `Classes`(`classesID`);



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
