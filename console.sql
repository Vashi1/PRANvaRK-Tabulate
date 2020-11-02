-- MySQL dump 10.13  Distrib 8.0.22, for Linux (x86_64)
--
-- Host: localhost    Database: medical_store
-- ------------------------------------------------------
-- Server version	8.0.22-0ubuntu0.20.10.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bill_detail`
--

DROP TABLE IF EXISTS `bill_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill_detail` (
  `Bill_id` int DEFAULT NULL,
  `Cust_name` char(100) DEFAULT NULL,
  `bill_date` date DEFAULT NULL,
  `mid` int DEFAULT NULL,
  `GST_val` int DEFAULT NULL,
  `Dis` int DEFAULT NULL,
  `tp` int DEFAULT NULL,
  `Quantity` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill_detail`
--

LOCK TABLES `bill_detail` WRITE;
/*!40000 ALTER TABLE `bill_detail` DISABLE KEYS */;
INSERT INTO `bill_detail` VALUES (2,'Appu','2020-10-28',5,18,0,590,5),(2,'Appu','2020-10-28',12,18,0,590,5),(2,'Appu','2020-10-28',14,18,0,354,3),(2,'Appu','2020-10-28',7,0,0,200,2),(2,'Appu','2020-10-28',6,18,0,118,1),(3,'aryan','2020-10-28',5,18,0,118,1),(4,'Ram','2020-10-28',6,18,0,118,1),(4,'raksa','2020-10-28',5,18,0,118,1),(4,'Rakshith','2020-10-28',5,18,0,118,1),(4,'rakshith','2020-10-28',5,18,0,118,1),(4,'toshita','2020-10-28',5,18,0,118,1),(4,'vani','2020-10-28',5,18,0,118,1),(5,'Rakshith1','2020-10-29',5,18,0,472,4),(6,'Raksha','2020-10-29',5,18,0,0,0),(6,'Raksha','2020-10-29',12,18,0,354,3),(6,'Raksha','2020-10-29',7,0,0,500,5),(6,'Raksha','2020-10-29',14,18,0,472,4),(7,'Tim','2020-10-29',7,0,0,100,1),(8,'tom','2020-10-29',5,18,0,0,0),(8,'tom','2020-10-29',14,18,0,118,1),(9,'lalita','2020-10-29',14,18,0,118,1),(9,'lalita','2020-10-29',13,18,0,1180,10),(10,'tom','2020-11-02',14,18,0,118,1),(10,'123','2020-11-02',13,18,0,118,1),(10,'rom','2020-11-02',13,18,0,118,1),(10,'Rit','2020-11-02',13,18,0,118,1),(10,'Tim','2020-11-02',11,18,0,236,2),(10,'Tim','2020-11-02',12,18,0,236,2),(10,'Tim','2020-11-02',13,18,0,236,2),(11,'Pop','2020-11-02',13,18,0,118,1),(11,'Tommy','2020-11-02',13,18,0,236,2),(11,'hex','2020-11-02',13,18,0,118,1),(11,'uid','2020-11-02',13,18,0,118,1),(12,'hex','2020-11-02',13,18,0,118,1),(13,'Ramu','2020-11-02',6,18,0,236,2),(13,'Ramu','2020-11-02',7,0,0,200,2),(13,'Ramu','2020-11-02',11,18,0,236,2),(14,'Rakshith','2020-11-02',6,18,0,236,2),(14,'Rakshith','2020-11-02',7,0,0,200,2),(14,'Rakshith','2020-11-02',11,18,0,354,3);
/*!40000 ALTER TABLE `bill_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payroll`
--

DROP TABLE IF EXISTS `payroll`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payroll` (
  `Uid` int DEFAULT NULL,
  `Name` char(30) DEFAULT NULL,
  `D_O_J` date DEFAULT NULL,
  `Salary` int DEFAULT NULL,
  `Address` char(40) DEFAULT NULL,
  `Mobile_number` int DEFAULT NULL,
  `E_mail` char(40) DEFAULT NULL,
  `ADMIN` char(5) DEFAULT NULL,
  `Password` char(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payroll`
--

LOCK TABLES `payroll` WRITE;
/*!40000 ALTER TABLE `payroll` DISABLE KEYS */;
INSERT INTO `payroll` VALUES (5,'Rakshith','2020-09-01',10000,'Jammu',123,'rakshith','yes','123'),(6,'noadmin','2020-09-01',123,'jam',123,'rak','no','123');
/*!40000 ALTER TABLE `payroll` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales` (
  `sale_id` int DEFAULT NULL,
  `C_name` char(10) DEFAULT NULL,
  `tp` int DEFAULT NULL,
  `d_o_s` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales`
--

LOCK TABLES `sales` WRITE;
/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
INSERT INTO `sales` VALUES (4,'vani',708,'2020-10-28'),(6,'Raksha',1326,'2020-10-29'),(10,'Rit',472,'2020-11-02'),(10,'Tim',1180,'2020-11-02'),(11,'Pop',118,'2020-11-02'),(11,'Tommy',354,'2020-11-02'),(11,'hex',472,'2020-11-02'),(11,'uid',590,'2020-11-02'),(12,'hex',118,'2020-11-02'),(13,'Ramu',672,'2020-11-02'),(14,'Rakshith',790,'2020-11-02');
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stocks`
--

DROP TABLE IF EXISTS `stocks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stocks` (
  `Mid` int DEFAULT NULL,
  `Mname` char(30) DEFAULT NULL,
  `Saltname` char(40) DEFAULT NULL,
  `Brandname` char(40) DEFAULT NULL,
  `Quantity` int DEFAULT NULL,
  `price` int DEFAULT NULL,
  `Location` char(20) DEFAULT NULL,
  `Exp_date` date DEFAULT NULL,
  `D_O_M` date DEFAULT NULL,
  `GST` int DEFAULT NULL,
  `discount` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stocks`
--

LOCK TABLES `stocks` WRITE;
/*!40000 ALTER TABLE `stocks` DISABLE KEYS */;
INSERT INTO `stocks` VALUES (5,'git','git','git',0,100,'Not specified','2021-09-01','2020-10-24',18,0),(6,'Refresh','benzene','cipla',6,100,'Not specified','2020-01-09','2020-10-24',18,0),(7,'PCM','paracitamole','cipla',3,100,'Not specified','2021-01-26','2020-10-24',0,0),(11,'item1','item1','item1',3,100,'Not specified','2021-09-01','2020-10-26',18,0),(12,'Calciumsandos','calcium','cipla',0,100,'Not specified','2021-09-01','2020-10-26',18,0),(13,'randanx','randax','cipla',79,100,'Not specified','2021-09-01','2020-10-26',18,0),(14,'abc','abc','cipla',0,100,'Not specified','2021-09-01','2020-10-26',18,0);
/*!40000 ALTER TABLE `stocks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `supplier_id` int DEFAULT NULL,
  `supplier_name` char(30) DEFAULT NULL,
  `phone_number` int DEFAULT NULL,
  `address` char(40) DEFAULT NULL,
  `supplier_gst` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (2,'sup2',123341,'Jammu',123),(3,'sup1',123,'jam',123);
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier_data`
--

DROP TABLE IF EXISTS `supplier_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier_data` (
  `orderid` int DEFAULT NULL,
  `order_date` date DEFAULT NULL,
  `supplier_id` int DEFAULT NULL,
  `Mid` int DEFAULT NULL,
  `Quantity` int DEFAULT NULL,
  `Price` int DEFAULT NULL,
  `Delievery_date` date DEFAULT NULL,
  `Mname` char(30) DEFAULT NULL,
  `Saltname` char(40) DEFAULT NULL,
  `Brandname` char(40) DEFAULT NULL,
  `Location` char(20) DEFAULT NULL,
  `Exp_date` date DEFAULT NULL,
  `GST` int DEFAULT NULL,
  `discount` int DEFAULT NULL,
  `status` int DEFAULT NULL,
  `order_sp` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier_data`
--

LOCK TABLES `supplier_data` WRITE;
/*!40000 ALTER TABLE `supplier_data` DISABLE KEYS */;
INSERT INTO `supplier_data` VALUES (6,'2020-10-26',2,0,10,100,'2020-10-26','Calciumsandos','calcium','cipla','Not specified',NULL,0,0,2,1),(7,'2020-10-26',3,0,100,100,'2020-10-26','randanx','randax','cipla','Not specified',NULL,0,0,2,1),(8,'2020-10-26',3,0,10,100,'2020-10-26','abc','abc','cipla','Not specified',NULL,0,0,2,1),(9,'2020-10-26',2,0,10,100,'2020-10-26','item1','item1','item1','Not specified',NULL,0,0,2,2),(10,'2020-10-26',2,0,10,100,'2020-10-26','item2','item2','item2','Not specified',NULL,0,0,2,2),(11,'2020-10-28',2,5,15,100,'2020-10-28','git','git','git','Not specified',NULL,18,0,2,3),(12,'2020-10-28',2,6,10,100,'2020-10-28','Refresh','benzene','cipla','Not specified',NULL,18,0,2,3),(13,'2020-10-28',2,7,10,100,'2020-10-28','PCM','paracitamole','cipla','Not specified',NULL,0,0,2,3);
/*!40000 ALTER TABLE `supplier_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-02 18:19:41
