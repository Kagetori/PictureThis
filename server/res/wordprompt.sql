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
    (1,'salmon','noun','animal'),
    (2,'squirrel','noun','animal'),
    (3,'pug','noun','animal'),
    (4,'kitten','noun','animal'),
    (5,'rabbit','noun','animal'),
    (6,'goldfish','noun','animal'),
    (7,'hamster','noun','animal'),
    (8,'pigeon','noun','animal'),
    (9,'cow','noun','animal'),
    (10,'bear','noun','animal'),
    (11,'jumping','verb','activity'),
    (12,'running','verb','activity'),
    (13,'dancing','verb','activity'),
    (14,'skating','verb','activity'),
    (15,'hiking','verb','activity'),
    (16,'sitting','verb','activity'),
    (17,'eating','verb','activity'),
    (18,'drawing','verb','activity'),
    (19,'writing','verb','activity'),
    (20,'candy','noun','food'),
    (21,'coffee','noun','food'),
    (22,'apple','noun','food'),
    (23,'orange','noun','food'),
    (24,'rice','noun','food'),
    (25,'kale','noun','food'),
    (26,'mushroom','noun','food'),
    (27,'corn','noun','food'),
    (28,'steak','noun','food'),
    (29,'sushi','noun','food'),
    (30,'cake','noun','food'),
    (31,'books','noun','object'),
    (32,'chair','noun','object'),
    (33,'umbrella','noun','object'),
    (34,'diary','noun','object'),
    (35,'phone','noun','object'),
    (36,'paint','noun','object'),
    (37,'backpack','noun','object'),
    (38,'balloon','noun','object'),
    (39,'lego','noun','object'),
    (40,'sky','noun','nature'),
    (41,'forest','noun','nature'),
    (42,'lake','noun','nature'),
    (43,'mountain','noun','nature'),
    (44,'river','noun','nature'),
    (45,'sunset','noun','nature'),
    (46,'meadow','noun','nature'),
    (47,'rain','noun','nature'),
    (48,'winter','noun','nature'),
    (49,'summer','noun','nature'),
    (50,'autumn','noun','nature'),
    (51,'spring','noun','nature'),
    (52,'library','noun','place'),
    (53,'kitchen','noun','place'),
    (54,'gym','noun','place'),
    (55,'Canada','noun','place'),
    (56,'mall','noun','place'),
    (57,'hallway','noun','place'),
    (58,'school','noun','place'),
    (59,'store','noun','place'),
    (60,'jeans','noun','fashion'),
    (61,'belt','noun','fashion'),
    (62,'beret','noun','fashion'),
    (63,'scarf','noun','fashion'),
    (64,'dress','noun','fashion'),
    (65,'boots','noun','fashion'),
    (66,'heels','noun','fashion'),
    (67,'cardigan','noun','fashion'),
    (68,'romper','noun','fashion'),
    (69,'mittens','noun','fashion'),
    (70,'tennis','noun','sport'),
    (71,'baseball','noun','sport'),
    (72,'hockey','noun','sport'),
    (73,'soccer','noun','sport'),
    (74,'football','noun','sport'),
    (75,'golf','noun','sport'),
    (76,'Olympics','noun','event'),
    (77,'party','noun','event'),
    (78,'rodeo','noun','event'),
    (79,'parade','noun','event'),
    (80,'concert','noun','event');
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

-- Dump completed on 2015-11-17 13:28:00
