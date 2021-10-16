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
CREATE DATABASE IF NOT EXISTS `lms` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `lms`;

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `learner` (
  `id` int(11) NOT NULL,
  `CoursesTaking` varchar(50)  DEFAULT NULL,
  `CompletedCourses` varchar(50)  DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `doctor`
--
INSERT INTO `learner` (`id`, `CoursesTaking`, `CompletedCourses`) VALUES
(3, 'IS212', 'IS214');

--
-- Table structure for table `person`
--

CREATE TABLE `employee` (
  `StaffID` int(11) NOT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `Username` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `CurrentDesignation` varchar(50) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  `ContactNo` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `person`
--

INSERT INTO `employee` (`StaffID`, `Name`, `Username`,`Email`,`CurrentDesignation`,`Department`,`ContactNo`) VALUES
(3, 'Constance Wilkinson', 'cons','cons@gmail.com','learner','Learning','92130843');

--
-- Indexes for dumped tables
--


--
-- Indexes for table `doctor`
--
ALTER TABLE `learner`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `person`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`StaffID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- Constraints for dumped tables
--

--
-- Constraints for table `doctor`
--
ALTER TABLE `learner`
  ADD CONSTRAINT `learner_ibfk_1` FOREIGN KEY (`id`) REFERENCES `employee` (`StaffID`);
