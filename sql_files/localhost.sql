-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 22, 2021 at 02:38 AM
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
-- Database: `id16988493_amazondatalake`
--
CREATE DATABASE IF NOT EXISTS `id16988493_amazondatalake` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `id16988493_amazondatalake`;

-- --------------------------------------------------------

--
-- Table structure for table `requestTable`
--

CREATE TABLE `requestTable` (
  `requestTimeStamp` datetime NOT NULL,
  `requestText` text COLLATE utf8_unicode_ci NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `requestTable`
--

INSERT INTO `requestTable` (`requestTimeStamp`, `requestText`, `id`) VALUES
('2021-06-09 03:35:42', 'hello class', 2);

-- --------------------------------------------------------

--
-- Table structure for table `userLogin`
--

CREATE TABLE `userLogin` (
  `id` int(11) NOT NULL,
  `username` text COLLATE utf8_unicode_ci NOT NULL,
  `password` text COLLATE utf8_unicode_ci NOT NULL,
  `dateAccountCreated` date NOT NULL DEFAULT current_timestamp(),
  `loginStatus` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `userLogin`
--

INSERT INTO `userLogin` (`id`, `username`, `password`, `dateAccountCreated`, `loginStatus`) VALUES
(1, 'usernameTest1', 'passwordTest1', '2021-07-06', 0),
(2, 'usernameTest2', 'passwordTest2', '2021-08-06', 1),
(3, 'usernameTest3', 'passwordTest3', '2021-08-06', 0),
(4, 'helllooo', 'password', '2021-06-07', 0),
(5, 'hellllooooo', '$2y$10$0.6/IDfFogtkztL4FckkoeCKRQpsQgbKFf.GaVdovqWzhvIahyz2m', '2021-06-07', 0),
(6, 'testytesty', '$2y$10$oND6kkqAUa5nZvfwrx4sVe1WWFWCtW2CRry33W1lrblGj1Kq8iYoi', '2021-06-07', 0),
(7, 'testUser', '$2y$10$x393n5Cx6E7iioTqB//HFO8dmqkiZZ6Wp8Z2ZOBA7S1h.lHuh9yC6', '2021-06-08', NULL),
(9, 'inClassTest', '$2y$10$muyjBee4LyJfssiiP.DHEujFiAHOCw30gTMnEYLkHC/GD6ezCQb7C', '2021-06-08', NULL),
(10, 'testUserPrisci', '$2y$10$3NPAWfvtDAE5L..FutyyVO9hRkedLOYZ7SwnAc6rkiE8/05KC/kI2', '2021-06-09', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `userTable`
--

CREATE TABLE `userTable` (
  `requestText` text COLLATE utf8_unicode_ci NOT NULL,
  `metaGeneration` text COLLATE utf8_unicode_ci NOT NULL,
  `sqlOutput` text COLLATE utf8_unicode_ci NOT NULL,
  `id` int(11) NOT NULL,
  `requestDateTime` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `userTable`
--

INSERT INTO `userTable` (`requestText`, `metaGeneration`, `sqlOutput`, `id`, `requestDateTime`) VALUES
('request Text sample 1', 'meta sample 1, meta sample 1, meta sample 1', 'SQL output 1', 1, '2021-07-06 02:40:00'),
('request Text sample 2', 'meta sample 2, meta sample 2, meta sample 2', 'SQL output 2', 2, '2021-07-06 02:41:00'),
('request Text sample 3', 'meta sample 3, meta sample 3, meta sample 3', 'SQL output 3', 3, '2021-07-06 02:42:00'),
('request Text sample 4', 'meta sample 4, meta sample 4, meta sample 4', 'SQL output 4', 2, '2021-07-06 02:43:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `userLogin`
--
ALTER TABLE `userLogin`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `userLogin`
--
ALTER TABLE `userLogin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
