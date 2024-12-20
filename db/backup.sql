-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: localhost    Database: schoolControll
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Assistance`
--

DROP TABLE IF EXISTS `Assistance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Assistance` (
  `id` int NOT NULL AUTO_INCREMENT,
  `studentID` int NOT NULL,
  `subjectID` int NOT NULL,
  `assistance_status` enum('present','absent','justified') NOT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `studentID` (`studentID`,`subjectID`,`date`),
  KEY `subjectID` (`subjectID`),
  CONSTRAINT `Assistance_ibfk_1` FOREIGN KEY (`studentID`) REFERENCES `User` (`id`),
  CONSTRAINT `Assistance_ibfk_2` FOREIGN KEY (`subjectID`) REFERENCES `Subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Assistance`
--

LOCK TABLES `Assistance` WRITE;
/*!40000 ALTER TABLE `Assistance` DISABLE KEYS */;
INSERT INTO `Assistance` VALUES (2,3,1,'present','2024-12-17 17:51:16'),(3,3,2,'absent','2024-12-17 17:51:26'),(4,3,3,'present','2024-12-17 17:51:33'),(5,3,4,'justified','2024-12-17 17:51:44'),(6,3,5,'present','2024-12-17 17:51:53'),(7,3,8,'present','2024-12-17 17:51:57'),(8,3,6,'present','2024-12-17 17:52:05'),(9,3,7,'justified','2024-12-17 17:52:16'),(10,3,9,'present','2024-12-17 17:52:26'),(11,3,10,'justified','2024-12-17 17:52:34'),(12,3,11,'present','2024-12-17 17:52:44'),(13,3,12,'present','2024-12-17 17:52:49');
/*!40000 ALTER TABLE `Assistance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Subject`
--

DROP TABLE IF EXISTS `Subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Subject` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `room` varchar(255) NOT NULL,
  `teacherID` int NOT NULL,
  `weekday` int NOT NULL,
  `startTime` time NOT NULL,
  `endTime` time NOT NULL,
  PRIMARY KEY (`id`),
  KEY `teacherID` (`teacherID`),
  CONSTRAINT `Subject_ibfk_1` FOREIGN KEY (`teacherID`) REFERENCES `User` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Subject`
--

LOCK TABLES `Subject` WRITE;
/*!40000 ALTER TABLE `Subject` DISABLE KEYS */;
INSERT INTO `Subject` VALUES (1,'Matemticas','A101',15,0,'08:00:00','09:00:00'),(2,'Historia','B102',15,0,'09:15:00','10:15:00'),(3,'Ciencias Naturales','C103',15,0,'10:30:00','11:30:00'),(4,'Ingls','D104',15,0,'11:45:00','12:45:00'),(5,'Arte','E105',15,0,'13:00:00','14:00:00'),(6,'Geografa','B202',15,1,'08:00:00','09:00:00'),(7,'Educacin Fsica','Gimnasio',15,1,'09:15:00','10:15:00'),(8,'Qumica','C203',15,1,'10:30:00','11:30:00'),(9,'Literatura','D204',15,1,'11:45:00','12:45:00'),(10,'Msica','E205',15,1,'13:00:00','14:00:00'),(11,'Fsica','A301',15,2,'08:00:00','09:00:00'),(12,'Historia del Arte','B302',15,2,'09:15:00','10:15:00'),(13,'Matemticas Avanzadas','C303',15,2,'10:30:00','11:30:00'),(14,'Biologa','D304',15,2,'11:45:00','12:45:00'),(15,'Informtica','E305',15,2,'13:00:00','14:00:00'),(16,'Lengua','A401',15,3,'08:00:00','09:00:00'),(17,'Qumica Orgnica','B402',15,3,'09:15:00','10:15:00'),(18,'Filosofa','C403',15,3,'10:30:00','11:30:00'),(19,'Educacin Fsica','Gimnasio',15,3,'11:45:00','12:45:00'),(20,'Teatro','D404',15,3,'13:00:00','14:00:00'),(21,'Economa','A501',15,4,'08:00:00','09:00:00'),(22,'Clculo','B502',15,4,'09:15:00','10:15:00'),(23,'Historia Contempornea','C503',15,4,'10:30:00','11:30:00'),(24,'Ingls Conversacional','D504',15,4,'11:45:00','12:45:00'),(25,'Robtica','E505',15,4,'13:00:00','14:00:00');
/*!40000 ALTER TABLE `Subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `lastName` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `hashedPassword` varchar(255) DEFAULT NULL,
  `token` varchar(255) DEFAULT NULL,
  `groupID` int NOT NULL,
  `roleID` int NOT NULL,
  `cardID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `groupID` (`groupID`),
  KEY `roleID` (`roleID`),
  CONSTRAINT `User_ibfk_1` FOREIGN KEY (`groupID`) REFERENCES `UserGroup` (`id`),
  CONSTRAINT `User_ibfk_2` FOREIGN KEY (`roleID`) REFERENCES `UserRole` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (2,'admin','','admin@admin.com','$2b$12$.o0K10HVis8U1RdLrPbnQ.ptWAJLV3co.FPmJ6S8Hux0iOxmaFPum','7f9ebbda-39a7-43ed-be9b-127b332c5ca4',3,3,NULL),(3,'victor','merino','vmerino@gmail.com','$2b$12$u46y.yXqE5cBEpSWfXkZeuBoaMnYdQuYFMa1fo62/OAR.sbCmDfpO','d5feaa43-c884-4474-a188-7eddc1d8bff3',4,1,NULL),(4,'juan','perez','jperez@gmail.com','$2b$12$Um33YOpQMC5gnOGO7lm5Puo4CKjOYxT0oHXIoQRy62UN98/xEPuLi','35309027-23d4-4bed-88cb-ffedacd86ae4',4,1,NULL),(5,'ana','gomez','agomez@gmail.com','$2b$12$0IbyIYKM88Hq50nESs1BduzJ/xVgVrzK4ukCZ.3auiWE2PY//HrbC','fe2cfa6c-8684-42d9-8539-0d6a67ce2047',4,1,NULL),(6,'luis','rodriguez','lrodriguez@gmail.com','$2b$12$9Di2DB22klVQ1shr835OqOKUPsyL4e89FpIBpab7aOAH7hMEqiv.6','8db6e2a6-f333-4b45-8fea-89693f023ecd',4,1,NULL),(7,'carlos','sanchez','csanchez@gmail.com','$2b$12$VhHBCJD489hI2huFCjsJ0.vm40BnZ2WrUAcHhN.Y0PyNjjReVSJEW','6859c1ca-8713-47a4-b729-a7d099840b7a',4,1,NULL),(8,'maria','lopez','mlopez@gmail.com','$2b$12$aGH.WnUsZv.cYWI1omHSheXqLuNd1XxCep092fsNvMXNwWuSgPCWe','4088d520-368e-49ca-8194-72440e186bac',4,1,NULL),(9,'fernando','torres','ftorres@gmail.com','$2b$12$RtwbC7UHBCfN6gdNnus9s.kZLRQdMJccqEfKzin1tMCDFjr5iu9Mu','5eae10f5-3d80-43a7-95b4-9813b843cf04',4,1,NULL),(10,'paula','ramirez','pramirez@gmail.com','$2b$12$H00P.wQ8hhjTiYeiacPgl.AqtHDMqg/45tuCI.w.IusyklBAgJcrm','aae39e09-be27-4e6e-a288-145c77ccf1f3',4,1,NULL),(11,'diego','fernandez','dfernandez@gmail.com','$2b$12$ZxDLH3Vn33YDWs8iRAqfE.tXqXLGe9NmSY5P2wIdxnNxc5D0TchKi','7191be2c-6dfc-40c9-b29d-09a1075491bc',4,1,NULL),(12,'camila','martinez','cmartinez@gmail.com','$2b$12$uQcjq1zOigFuoUiWlb0rquxp78kt63/Jr0PQJs.bH7id4AAfyTj0m','ec9e4969-aeae-4bb8-933b-c236aa3a2905',4,1,NULL),(13,'jorge','hidalgo','jhidalgo@gmail.com','$2b$12$.mnqLG1zJMHiUmUetCILOecdLKK/qrV0oqzAkR/TsupVohmY1XG1K','20953330-9b20-4b23-be6f-b284f8f037e6',4,1,NULL),(14,'valeria','ortega','vortega@gmail.com','$2b$12$ugwvkpZy3sdzW4piczz8Ku5VXpw5k0hJDlzqpxteBRWrcsZWhmV7S','a6f5366a-b93f-4e69-a194-ac773a6208af',4,1,NULL),(15,'roger','sobrino','roger@gmail.com','$2b$12$S6nSkIZ96cV4A2X6b7iPI.L6ryWLUmXI3s7zb4H6PRd8fMW.bXxEu','ef44efdb-f05e-40a9-9f66-145fd358976b',4,2,NULL);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserGroup`
--

DROP TABLE IF EXISTS `UserGroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `UserGroup` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserGroup`
--

LOCK TABLES `UserGroup` WRITE;
/*!40000 ALTER TABLE `UserGroup` DISABLE KEYS */;
INSERT INTO `UserGroup` VALUES (2,'teacher'),(3,'admin'),(4,'DAW2');
/*!40000 ALTER TABLE `UserGroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserRole`
--

DROP TABLE IF EXISTS `UserRole`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `UserRole` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserRole`
--

LOCK TABLES `UserRole` WRITE;
/*!40000 ALTER TABLE `UserRole` DISABLE KEYS */;
INSERT INTO `UserRole` VALUES (1,'student'),(2,'teacher'),(3,'admin');
/*!40000 ALTER TABLE `UserRole` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserSubject`
--

DROP TABLE IF EXISTS `UserSubject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `UserSubject` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userID` int NOT NULL,
  `subjectID` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userID` (`userID`),
  KEY `subjectID` (`subjectID`),
  CONSTRAINT `UserSubject_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `User` (`id`),
  CONSTRAINT `UserSubject_ibfk_2` FOREIGN KEY (`subjectID`) REFERENCES `Subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=305 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserSubject`
--

LOCK TABLES `UserSubject` WRITE;
/*!40000 ALTER TABLE `UserSubject` DISABLE KEYS */;
INSERT INTO `UserSubject` VALUES (2,3,2),(3,3,3),(4,3,4),(5,3,5),(6,3,6),(7,3,7),(8,3,8),(9,3,9),(10,3,10),(11,3,11),(12,3,12),(13,3,13),(14,3,14),(15,3,15),(16,3,16),(17,3,17),(18,3,18),(19,3,19),(20,3,20),(21,3,21),(22,3,22),(23,3,23),(24,3,24),(25,3,25),(26,4,1),(27,4,2),(28,4,3),(29,4,4),(30,4,5),(31,4,6),(32,4,7),(33,4,8),(34,4,9),(35,4,10),(36,4,11),(37,4,12),(38,4,13),(39,4,14),(40,4,15),(41,4,16),(42,4,17),(43,4,18),(44,4,19),(45,4,20),(46,4,21),(47,4,22),(48,4,23),(49,4,24),(50,4,25),(51,5,1),(52,5,2),(53,5,3),(54,5,4),(55,5,5),(56,5,6),(57,5,7),(58,5,8),(59,5,9),(60,5,10),(61,5,11),(62,5,12),(63,5,13),(64,5,14),(65,5,15),(66,5,16),(67,5,17),(68,5,18),(69,5,19),(70,5,20),(71,5,21),(72,5,22),(73,5,23),(74,5,24),(75,5,25),(76,6,1),(77,6,2),(78,6,3),(79,6,4),(80,6,5),(81,6,6),(82,6,7),(83,6,8),(84,6,9),(85,6,10),(86,6,11),(87,6,12),(88,6,13),(89,6,14),(90,6,15),(91,6,16),(92,6,17),(93,6,18),(94,6,19),(95,6,20),(96,6,21),(97,6,22),(98,6,23),(99,6,24),(100,6,25),(101,7,1),(102,7,2),(103,7,3),(104,7,4),(105,7,5),(106,7,6),(107,7,7),(108,7,8),(109,7,9),(110,7,10),(111,7,11),(112,7,12),(113,7,13),(114,7,14),(115,7,15),(116,7,16),(117,7,17),(118,7,18),(119,7,19),(120,7,20),(121,7,21),(122,7,22),(123,7,23),(124,7,24),(125,7,25),(126,8,1),(127,8,2),(128,8,3),(129,8,4),(130,8,5),(131,8,6),(132,8,7),(133,8,8),(134,8,9),(135,8,10),(136,8,11),(137,8,12),(138,8,13),(139,8,14),(140,8,15),(141,8,16),(142,8,17),(143,8,18),(144,8,19),(145,8,20),(146,8,21),(147,8,22),(148,8,23),(149,8,24),(150,8,25),(151,9,1),(152,9,2),(153,9,3),(154,9,4),(155,9,5),(156,9,6),(157,9,7),(158,9,8),(159,9,9),(160,9,10),(161,9,11),(162,9,12),(163,9,13),(164,9,14),(165,9,15),(166,9,16),(167,9,17),(168,9,18),(169,9,19),(170,9,20),(171,9,21),(172,9,22),(173,9,23),(174,9,24),(175,9,25),(176,10,1),(177,10,2),(178,10,3),(179,10,4),(180,10,5),(181,10,6),(182,10,7),(183,10,8),(184,10,9),(185,10,10),(186,10,11),(187,10,12),(188,10,13),(189,10,14),(190,10,15),(191,10,16),(192,10,17),(193,10,18),(194,10,19),(195,10,20),(196,10,21),(197,10,22),(198,10,23),(199,10,24),(200,10,25),(201,11,1),(202,11,2),(203,11,3),(204,11,4),(205,11,5),(206,11,6),(207,11,7),(208,11,8),(209,11,9),(210,11,10),(211,11,11),(212,11,12),(213,11,13),(214,11,14),(215,11,15),(216,11,16),(217,11,17),(218,11,18),(219,11,19),(220,11,20),(221,11,21),(222,11,22),(223,11,23),(224,11,24),(225,11,25),(226,12,1),(227,12,2),(228,12,3),(229,12,4),(230,12,5),(231,12,6),(232,12,7),(233,12,8),(234,12,9),(235,12,10),(236,12,11),(237,12,12),(238,12,13),(239,12,14),(240,12,15),(241,12,16),(242,12,17),(243,12,18),(244,12,19),(245,12,20),(246,12,21),(247,12,22),(248,12,23),(249,12,24),(250,12,25),(251,13,1),(252,13,2),(253,13,3),(254,13,4),(255,13,5),(256,13,6),(257,13,7),(258,13,8),(259,13,9),(260,13,10),(261,13,11),(262,13,12),(263,13,13),(264,13,14),(265,13,15),(266,13,16),(267,13,17),(268,13,18),(269,13,19),(270,13,20),(271,13,21),(272,13,22),(273,13,23),(274,13,24),(275,13,25),(276,14,1),(277,14,2),(278,14,3),(279,14,4),(280,14,5),(281,14,6),(282,14,7),(283,14,8),(284,14,9),(285,14,10),(286,14,11),(287,14,12),(288,14,13),(289,14,14),(290,14,15),(291,14,16),(292,14,17),(293,14,18),(294,14,19),(295,14,20),(296,14,21),(297,14,22),(298,14,23),(299,14,24),(300,14,25),(304,3,1);
/*!40000 ALTER TABLE `UserSubject` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-18 18:57:23
