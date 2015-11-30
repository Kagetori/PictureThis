-- MySQL dump 10.13  Distrib 5.5.44, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: picturethis_db
-- ------------------------------------------------------
-- Server version	5.5.44-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `api_wordprompt`
--

DROP TABLE IF EXISTS `api_wordprompt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `api_wordprompt` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `word` varchar(31) NOT NULL,
  `word_class` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `word` (`word`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_wordprompt`
--

LOCK TABLES `api_wordprompt` WRITE;
/*!40000 ALTER TABLE `api_wordprompt` DISABLE KEYS */;
INSERT INTO `api_wordprompt` VALUES
    (1,'salmon','noun','animal',0),
    (2,'squirrel','noun','animal',0),
    (3,'dog','noun','animal',0),
    (4,'kitten','noun','animal',0),
    (5,'rabbit','noun','animal',0),
    (6,'goldfish','noun','animal',0),
    (7,'hamster','noun','animal',0),
    (8,'pigeon','noun','animal',0),
    (9,'cow','noun','animal',0),
    (10,'bear','noun','animal',0),
    (11,'jumping','verb','activity',0),
    (12,'running','verb','activity',0),
    (13,'dancing','verb','activity',0),
    (14,'skating','verb','activity',0),
    (15,'hiking','verb','activity',0),
    (16,'sitting','verb','activity',0),
    (17,'eating','verb','activity',0),
    (18,'drawing','verb','activity',0),
    (19,'writing','verb','activity',0),
    (20,'candy','noun','food',0),
    (21,'coffee','noun','drink',0),
    (22,'apple','noun','food',0),
    (23,'orange','noun','food',0),
    (24,'rice','noun','food',0),
    (25,'kale','noun','food',0),
    (26,'mushroom','noun','food',0),
    (27,'corn','noun','food',0),
    (28,'steak','noun','food',0),
    (29,'sushi','noun','food',0),
    (30,'cake','noun','food',0),
    (31,'books','noun','object',0),
    (32,'chair','noun','furniture',1),
    (33,'umbrella','noun','object',0),
    (34,'diary','noun','object',0),
    (35,'phone','noun','electronic',0),
    (36,'paint','noun','object',0),
    (37,'backpack','noun','object',0),
    (38,'balloon','noun','toy',0),
    (39,'lego','noun','toy',0),
    (40,'sky','noun','nature',0),
    (41,'forest','noun','nature',0),
    (42,'lake','noun','nature',0),
    (43,'mountain','noun','nature',0),
    (44,'river','noun','nature',0),
    (45,'sunset','noun','nature',0),
    (46,'meadow','noun','nature',0),
    (47,'rain','noun','nature',0),
    (48,'winter','noun','nature',0),
    (49,'summer','noun','nature',0),
    (50,'autumn','noun','nature',0),
    (51,'spring','noun','nature',0),
    (52,'library','noun','place',0),
    (53,'kitchen','noun','place',0),
    (54,'gym','noun','place',0),
    (55,'Canada','noun','place',0),
    (56,'mall','noun','place',0),
    (57,'hallway','noun','place',0),
    (58,'school','noun','place',0),
    (59,'store','noun','place',0),
    (60,'jeans','noun','fashion',0),
    (61,'belt','noun','fashion',0),
    (62,'beret','noun','fashion',0),
    (63,'scarf','noun','fashion',0),
    (64,'dress','noun','fashion',0),
    (65,'boots','noun','fashion',0),
    (66,'heels','noun','fashion',0),
    (67,'cardigan','noun','fashion',0),
    (68,'romper','noun','fashion',0),
    (69,'mittens','noun','fashion',0),
    (70,'tennis','noun','sport',0),
    (71,'baseball','noun','sport',0),
    (72,'hockey','noun','sport',0),
    (73,'soccer','noun','sport',0),
    (74,'football','noun','sport',0),
    (75,'golf','noun','sport',0),
    (76,'Olympics','noun','event',0),
    (77,'party','noun','event',0),
    (78,'rodeo','noun','event',0),
    (79,'parade','noun','event',0),
    (80,'concert','noun','event',0),
	(81, 'pear', 'noun', 'food', 0),
	(82, 'dinosaur', 'noun', 'animal', 0),
	(83, 'totem', 'noun', 'sculpture', 0),
	(84, 'fossil', 'noun', 'object', 0),
	(85, 'tomato', 'noun', 'food', 0),
	(86, 'zucchini', 'noun', 'food', 0),
	(87, 'chicken', 'noun', 'animal', 0),
	(88, 'turkey', 'noun', 'animal', 0),
	(89, 'swing', 'noun', 'toy', 0),
	(90, 'tea', 'noun', 'drink', 0),
	(91, 'cider', 'noun', 'drink', 0),
	(92, 'juice', 'noun', 'drink', 0),
	(93, 'soda', 'noun', 'drink', 0),
	(94, 'crane', 'noun', 'animal', 0),
	(95, 'crow', 'noun', 'animal', 0),
	(96, 'noodles', 'noun', 'food', 0),
	(97, 'pickles', 'noun', 'food', 0),
	(98, 'fries', 'noun', 'food', 0),
	(99, 'USA', 'noun', 'place', 0),
	(100, 'bed', 'noun', 'furniture', 0),
    (101, 'bicycle', 'noun', 'transport', 1),
    (102, 'mouse', 'noun', 'animal', 1),
    (103, 'student', 'noun', 'people', 1);
/*!40000 ALTER TABLE `api_wordprompt` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-29  1:09:39
