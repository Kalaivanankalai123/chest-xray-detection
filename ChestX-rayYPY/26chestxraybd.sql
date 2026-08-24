-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 04, 2025 at 08:34 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1bonefrabd`
--

-- --------------------------------------------------------

--
-- Table structure for table `doctortb`
--

CREATE TABLE `doctortb` (
  `id` bigint(10) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `specialist` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `doctortb`
--

INSERT INTO `doctortb` (`id`, `Name`, `Email`, `Mobile`, `Address`, `specialist`, `UserName`, `Password`) VALUES
(1, 'sangeeth Kumar', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'heart', 'sangeeth', 'sangeeth');

-- --------------------------------------------------------

--
-- Table structure for table `drugtb`
--

CREATE TABLE `drugtb` (
  `id` bigint(250) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `EmailId` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `DoctorName` varchar(250) NOT NULL,
  `Medicine` varchar(250) NOT NULL,
  `OtherInfo` varchar(500) NOT NULL,
  `Report` varchar(500) NOT NULL,
  `Date` date NOT NULL,
  `SImage` varchar(500) NOT NULL,
  `Result` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `drugtb`
--

INSERT INTO `drugtb` (`id`, `UserName`, `EmailId`, `Mobile`, `DoctorName`, `Medicine`, `OtherInfo`, `Report`, `Date`, `SImage`, `Result`) VALUES
(1, 'san', '9486365535', 'sangeeth5535@gmail.com', 'sangeeth', 'nill', 'gfj', '1-rotated1-rotated1-rotated2-rotated1.jpg', '2025-02-05', '5631-rotated1-rotated2.jpg', 'Fractured'),
(2, 'san', '9486365535', 'sangeeth5535@gmail.com', 'sangeeth', 'Nil', 'Nil', 'Nil', '2025-02-05', '2161.jpg', 'Nil');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(10) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `Name`, `Email`, `Mobile`, `Address`, `UserName`, `Password`) VALUES
(1, 'sangeeth Kumar', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san');
