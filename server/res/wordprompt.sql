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
    (1,'salmon','noun','animal',1),
    (2,'squirrel','noun','animal',1),
    (3,'dog','noun','animal',1),
    (4,'kitten','noun','animal',1),
    (5,'rabbit','noun','animal',1),
    (6,'goldfish','noun','animal',1),
    (7,'hamster','noun','animal',1),
    (8,'pigeon','noun','animal',1),
    (9,'cow','noun','animal',1),
    (10,'bear','noun','animal',1),
    (11,'jumping','verb','activity',1),
    (12,'running','verb','activity',1),
    (13,'dancing','verb','activity',1),
    (14,'skating','verb','activity',1),
    (15,'hiking','verb','activity',1),
    (16,'sitting','verb','activity',1),
    (17,'eating','verb','activity',1),
    (18,'drawing','verb','activity',1),
    (19,'writing','verb','activity',1),
    (20,'candy','noun','food',1),
    (21,'coffee','noun','drink',1),
    (22,'apple','noun','food',1),
    (23,'orange','noun','food',1),
    (24,'rice','noun','food',1),
    (25,'kale','noun','food',1),
    (26,'mushroom','noun','food',1),
    (27,'corn','noun','food',1),
    (28,'steak','noun','food',1),
    (29,'sushi','noun','food',1),
    (30,'cake','noun','food',1),
    (31,'books','noun','object',1),
    (32,'chair','noun','furniture',1),
    (33,'umbrella','noun','object',1),
    (34,'diary','noun','object',1),
    (35,'phone','noun','electronic',1),
    (36,'paint','noun','object',1),
    (37,'backpack','noun','object',1),
    (38,'balloon','noun','toy',1),
    (39,'lego','noun','toy',1),
    (40,'sky','noun','nature',1),
    (41,'forest','noun','nature',1),
    (42,'lake','noun','nature',1),
    (43,'mountain','noun','nature',1),
    (44,'river','noun','nature',1),
    (45,'sunset','noun','nature',1),
    (46,'meadow','noun','nature',1),
    (47,'rain','noun','nature',1),
    (48,'winter','noun','nature',1),
    (49,'summer','noun','nature',1),
    (50,'autumn','noun','nature',1),
    (51,'spring','noun','nature',1),
    (52,'library','noun','place',1),
    (53,'kitchen','noun','place',1),
    (54,'gym','noun','place',1),
    (55,'Canada','noun','place',1),
    (56,'mall','noun','place',1),
    (57,'hallway','noun','place',1),
    (58,'school','noun','place',1),
    (59,'store','noun','place',1),
    (60,'jeans','noun','fashion',1),
    (61,'belt','noun','fashion',1),
    (62,'beret','noun','fashion',1),
    (63,'scarf','noun','fashion',1),
    (64,'dress','noun','fashion',1),
    (65,'boots','noun','fashion',1),
    (66,'heels','noun','fashion',1),
    (67,'cardigan','noun','fashion',1),
    (68,'romper','noun','fashion',1),
    (69,'mittens','noun','fashion',1),
    (70,'tennis','noun','sport',1),
    (71,'baseball','noun','sport',1),
    (72,'hockey','noun','sport',1),
    (73,'soccer','noun','sport',1),
    (74,'football','noun','sport',1),
    (75,'golf','noun','sport',1),
    (76,'Olympics','noun','event',1),
    (77,'party','noun','event',1),
    (78,'rodeo','noun','event',1),
    (79,'parade','noun','event',1),
    (80,'concert','noun','event',1),
	(81, 'pear', 'noun', 'food', 1),
	(82, 'dinosaur', 'noun', 'animal', 1),
	(83, 'totem', 'noun', 'sculpture', 1),
	(84, 'fossil', 'noun', 'object', 1),
	(85, 'tomato', 'noun', 'food', 1),
	(86, 'zucchini', 'noun', 'food', 1),
	(87, 'chicken', 'noun', 'animal', 1),
	(88, 'turkey', 'noun', 'animal', 1),
	(89, 'swing', 'noun', 'toy', 1),
	(90, 'tea', 'noun', 'drink', 1),
	(91, 'cider', 'noun', 'drink', 1),
	(92, 'juice', 'noun', 'drink', 1),
	(93, 'soda', 'noun', 'drink', 1),
	(94, 'crane', 'noun', 'animal', 1),
	(95, 'crow', 'noun', 'animal', 1),
	(96, 'noodles', 'noun', 'food', 1),
	(97, 'pickles', 'noun', 'food', 1),
	(98, 'fries', 'noun', 'food', 1),
	(99, 'USA', 'noun', 'place', 1),
	(100, 'bed', 'noun', 'furniture', 1)
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
