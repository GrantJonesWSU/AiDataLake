-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 27, 2021 at 09:30 PM
-- Server version: 10.3.16-MariaDB
-- PHP Version: 7.3.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `id14800504_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `clients`
--

CREATE TABLE `clients` (
  `person_id` int(11) NOT NULL,
  `age` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `clients`
--

INSERT INTO `clients` (`person_id`, `age`) VALUES
(1, 23),
(2, 35),
(5, 30),
(6, 35),
(8, 19),
(9, 33),
(10, 27);

-- --------------------------------------------------------

--
-- Table structure for table `counselors`
--

CREATE TABLE `counselors` (
  `person_id` int(11) NOT NULL,
  `experience` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `counselors`
--

INSERT INTO `counselors` (`person_id`, `experience`) VALUES
(3, 5),
(4, 3),
(7, 7);

-- --------------------------------------------------------

--
-- Table structure for table `persons`
--

CREATE TABLE `persons` (
  `id` int(11) NOT NULL,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `type` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `persons`
--

INSERT INTO `persons` (`id`, `name`, `type`) VALUES
(1, 'Lula', 1),
(2, 'Bronwyn', 1),
(3, 'Hershel', 2),
(4, 'Marcelina', 2),
(5, 'Lynda', 1),
(6, 'Von', 1),
(7, 'Camila', 2),
(8, 'Lance', 1),
(9, 'Marshall', 1),
(10, 'Joey', 1);

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE `sessions` (
  `id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  `counselor_id` int(11) NOT NULL,
  `start_datetime` timestamp NOT NULL DEFAULT current_timestamp(),
  `end_datetime` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `sessions`
--

INSERT INTO `sessions` (`id`, `client_id`, `counselor_id`, `start_datetime`, `end_datetime`) VALUES
(1, 1, 3, '2020-04-18 08:10:00', '2020-04-18 08:35:00'),
(2, 2, 3, '2020-04-07 11:05:00', '2020-04-07 11:30:00'),
(3, 5, 4, '2020-04-15 20:08:00', '2020-04-15 20:27:00'),
(4, 5, 4, '2020-04-22 14:22:00', '2020-04-22 14:50:00'),
(5, 8, 4, '2020-04-03 16:45:00', '2020-04-03 17:03:00'),
(6, 9, 7, '2020-04-19 09:36:00', '2020-04-19 09:58:00'),
(7, 10, 7, '2020-04-06 15:41:00', '2020-04-06 16:04:00');

-- --------------------------------------------------------

--
-- Table structure for table `utterances`
--

CREATE TABLE `utterances` (
  `id` int(11) NOT NULL,
  `session_id` int(11) NOT NULL,
  `speaker` int(11) NOT NULL,
  `u_sequence` int(11) NOT NULL,
  `u_content` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `time_stamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `utterances`
--

INSERT INTO `utterances` (`id`, `session_id`, `speaker`, `u_sequence`, `u_content`, `time_stamp`) VALUES
(1, 1, 1, 1, 'Lorem ipsum dolor sit amet', '2020-04-18 08:15:00'),
(2, 1, 2, 2, 'consectetur adipiscing elit', '2020-04-18 08:17:00'),
(3, 1, 1, 3, 'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', '2020-04-18 08:21:00'),
(4, 2, 2, 1, 'Ut enim ad minim veniam', '2020-04-07 11:08:00'),
(5, 2, 1, 2, 'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', '2020-04-07 11:11:00'),
(6, 2, 2, 3, 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', '2020-04-07 11:12:00'),
(7, 2, 1, 4, 'Excepteur sint occaecat cupidatat non proident', '2020-04-07 11:18:00'),
(8, 2, 2, 5, 'sunt in culpa qui officia deserunt mollit anim id est laborum.', '2020-04-07 11:20:00'),
(9, 3, 1, 1, 'Lorem ipsum dolor sit amet', '2020-04-15 20:13:00'),
(10, 3, 2, 2, 'consectetur adipiscing elit', '2020-04-15 20:20:00'),
(11, 3, 1, 3, 'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', '2020-04-15 20:22:00'),
(12, 4, 1, 1, 'Ut enim ad minim veniam', '2020-04-22 14:24:00'),
(13, 4, 2, 2, 'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', '2020-04-22 14:26:00'),
(14, 4, 1, 3, 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', '2020-04-22 14:29:00'),
(15, 4, 2, 4, 'Excepteur sint occaecat cupidatat non proident', '2020-04-22 14:35:00'),
(16, 4, 1, 5, 'sunt in culpa qui officia deserunt mollit anim id est laborum.', '2020-04-22 14:37:00'),
(17, 4, 2, 6, 'Lorem ipsum dolor sit amet', '2020-04-22 14:41:00'),
(18, 4, 1, 7, 'consectetur adipiscing elit', '2020-04-22 14:46:00'),
(19, 5, 2, 1, 'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', '2020-04-03 16:46:00'),
(20, 5, 1, 2, 'Ut enim ad minim veniam', '2020-04-03 16:49:00'),
(21, 5, 2, 3, 'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', '2020-04-03 16:52:00'),
(22, 5, 1, 4, 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', '2020-04-03 16:54:00'),
(23, 5, 2, 5, 'Lorem ipsum dolor sit amet', '2020-04-03 16:58:00'),
(24, 5, 1, 6, 'consectetur adipiscing elit', '2020-04-03 17:00:00'),
(25, 5, 2, 7, 'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', '2020-04-03 17:01:00'),
(26, 6, 2, 1, 'Ut enim ad minim veniam', '2020-04-19 09:41:00'),
(27, 6, 1, 2, 'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', '2020-04-19 09:44:00'),
(28, 6, 2, 3, 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', '2020-04-19 09:50:00'),
(29, 7, 2, 1, 'Excepteur sint occaecat cupidatat non proident', '2020-04-06 15:45:00'),
(30, 7, 1, 2, 'sunt in culpa qui officia deserunt mollit anim id est laborum.', '2020-04-06 15:47:00'),
(31, 7, 2, 3, 'Lorem ipsum dolor sit amet', '2020-04-06 15:49:00'),
(32, 7, 1, 4, 'consectetur adipiscing elit', '2020-04-06 15:53:00'),
(33, 7, 2, 5, 'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', '2020-04-06 15:59:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clients`
--
ALTER TABLE `clients`
  ADD PRIMARY KEY (`person_id`);

--
-- Indexes for table `counselors`
--
ALTER TABLE `counselors`
  ADD PRIMARY KEY (`person_id`);

--
-- Indexes for table `persons`
--
ALTER TABLE `persons`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `client_id` (`client_id`),
  ADD KEY `counselor_id` (`counselor_id`);

--
-- Indexes for table `utterances`
--
ALTER TABLE `utterances`
  ADD PRIMARY KEY (`id`),
  ADD KEY `session_id` (`session_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `persons`
--
ALTER TABLE `persons`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `sessions`
--
ALTER TABLE `sessions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `utterances`
--
ALTER TABLE `utterances`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `clients`
--
ALTER TABLE `clients`
  ADD CONSTRAINT `clients_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `persons` (`id`);

--
-- Constraints for table `counselors`
--
ALTER TABLE `counselors`
  ADD CONSTRAINT `counselors_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `persons` (`id`);

--
-- Constraints for table `sessions`
--
ALTER TABLE `sessions`
  ADD CONSTRAINT `sessions_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `clients` (`person_id`),
  ADD CONSTRAINT `sessions_ibfk_2` FOREIGN KEY (`counselor_id`) REFERENCES `counselors` (`person_id`);

--
-- Constraints for table `utterances`
--
ALTER TABLE `utterances`
  ADD CONSTRAINT `utterances_ibfk_1` FOREIGN KEY (`session_id`) REFERENCES `sessions` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
