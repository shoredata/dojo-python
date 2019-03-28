-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `dojo_wall`;

CREATE SCHEMA IF NOT EXISTS `dojo_wall` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;

USE `dojo_wall` ;

-- -----------------------------------------------------
-- Table `mydb`.`friends`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojo_wall`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `namefirst` VARCHAR(45) NULL,
  `namelast` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `passwordhash` VARCHAR(128) NULL,
  `user_level` VARCHAR(45) NULL,
  `warning_level` VARCHAR(45) NULL,
  `expires_at` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `dojo_wall`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `from_id` INT NOT NULL,
  `to_id` INT NOT NULL,
  `message` VARCHAR(64) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- COPY users (id, "namefirst", "namelast", isofficial, percentage) FROM stdin;
-- HMD	Heard Island and McDonald Islands	Antarctica	Antarctica	359	\N	0	\N	0.00	\N	Heard and McDonald Islands	Territory of Australia	Elisabeth II	\N	HM
-- ATF	French Southern territories	Antarctica	Antarctica	7780	\N	0	\N	0.00	\N	Terres australes fran�aises	Nonmetropolitan Territory of France	Jacques Chirac	\N	TF
-- UMI	United States Minor Outlying Islands	Oceania	Micronesia/Caribbean	16	\N	0	\N	0.00	\N	United States Minor Outlying Islands	Dependent Territory of the US	George W. Bush	\N	UM
-- \.
-- --
-- -- Data for Name: countrylanguage; Type: TABLE DATA; Schema: public; Owner: chriskl
-- --
-- COPY countrylanguage (countrycode, "language", isofficial, percentage) FROM stdin;
-- AFG	Pashto	t	52.400002


-- INSERT INTO table_name (column1, column2, column3, ...)
-- VALUES (value1, value2, value3, ...);

-- INSERT INTO messages (from_id, to_id, message, created_at) VALUES (1,2,"xxxxxx sample message ...", now());
-- INSERT INTO messages (from_id, to_id, message, created_at) VALUES (1,2,"xxx fadsfads  another message", now());
-- INSERT INTO messages (from_id, to_id, message, created_at) VALUES (2, 1, "a response", now());
-- INSERT INTO messages (from_id, to_id, message, created_at) VALUES (2, 1, "response g356v4", now());
-- INSERT INTO messages (from_id, to_id, message, created_at) VALUES (2, 1, "response 6f45c5cwt ", now());
-- INSERT INTO messages (from_id, to_id, message, created_at) VALUES (2, 1, "response r45334", now());
-- INSERT INTO messages (from_id, to_id, message, created_at) VALUES (2, 1, "fasdf response df af sdf", now());
-- INSERT INTO messages (from_id, to_id, message, created_at) VALUES (2, 1, "a adsf sdf dsa fasdfads", now());




-- SELECT 
--   messages.message,
--   messages.created_at as sent_on,
--   sender.email as senderemail,
--   CONCAT(sender.namefirst, ' ', sender.namelast) as sendername,
--   messages.from_id as senderid 
-- FROM
--   messages
-- LEFT OUTER JOIN 
--   users sender ON messages.from_id = sender.id
-- LEFT OUTER JOIN 
--   users receiver ON messages.to_id = receiver.id
-- WHERE
--   messages.to_id = 1; 

-- SELECT  messages.message, 
--         messages.created_at as sent_on, 
--         receiver.email as to_email, 
--         sender.email as from_email, 
--         CONCAT(receiver.namefirst, ' ', receiver.namelast) as to_name, 
--         CONCAT(sender.namefirst, ' ', sender.namelast) as from_name, 
--         messages.to_id as to_id,  
--         messages.from_id as from_id  
--         FROM messages 
--         LEFT OUTER JOIN 
--         users sender ON messages.from_id = sender.id 
--         LEFT OUTER JOIN 
--         users receiver ON messages.to_id = receiver.id 
--         WHERE 
--         messages.from_id = 1;
