-- MySQL dump 10.13  Distrib 8.0.32, for macos13 (x86_64)
--
-- Host: localhost    Database: lego_store
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `Address`
--

DROP TABLE IF EXISTS `Address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Address` (
  `AddressID` int NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(50) DEFAULT NULL,
  `LastName` varchar(50) DEFAULT NULL,
  `Country` varchar(50) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `StreetName` varchar(50) DEFAULT NULL,
  `StreetNo` int DEFAULT NULL,
  `AppartmentNo` varchar(10) DEFAULT NULL,
  `PostCode` int DEFAULT NULL,
  PRIMARY KEY (`AddressID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Address`
--

LOCK TABLES `Address` WRITE;
/*!40000 ALTER TABLE `Address` DISABLE KEYS */;
INSERT INTO `Address` VALUES (1,'John','Doe','USA','New York','Broadway',123,'Apt 1A',10001);
/*!40000 ALTER TABLE `Address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BuyingHistory`
--

DROP TABLE IF EXISTS `BuyingHistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BuyingHistory` (
  `BuyingHistoryID` int NOT NULL AUTO_INCREMENT,
  `UserID` int DEFAULT NULL,
  `ShoppingCartID` int DEFAULT NULL,
  `DateOfPurchase` date DEFAULT NULL,
  PRIMARY KEY (`BuyingHistoryID`),
  KEY `UserID` (`UserID`),
  CONSTRAINT `buyinghistory_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `User` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BuyingHistory`
--

LOCK TABLES `BuyingHistory` WRITE;
/*!40000 ALTER TABLE `BuyingHistory` DISABLE KEYS */;
INSERT INTO `BuyingHistory` VALUES (1,1,1,'2022-03-18');
/*!40000 ALTER TABLE `BuyingHistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Product`
--

DROP TABLE IF EXISTS `Product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Product` (
  `ProductID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  `SetNo` varchar(50) DEFAULT NULL,
  `Price` varchar(50) DEFAULT NULL,
  `Description` varchar(250) DEFAULT NULL,
  `Image` blob,
  `Availability` int DEFAULT NULL,
  `ReleaseDate` date DEFAULT NULL,
  `PieceCount` int DEFAULT NULL,
  `ProductTypeID` int DEFAULT NULL,
  PRIMARY KEY (`ProductID`),
  KEY `ProductTypeID` (`ProductTypeID`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`ProductTypeID`) REFERENCES `ProductType` (`ProductTypeID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Product`
--

LOCK TABLES `Product` WRITE;
/*!40000 ALTER TABLE `Product` DISABLE KEYS */;
INSERT INTO `Product` VALUES (1,'Police Station','60141','99.99','Build a bustling police station with LEGO City!',NULL,1,'2020-01-01',1000,1),(2,'Temple of the Ultimate Ultimate Weapon','70617','79.99','Join the ninja heroes at the Temple of the Ultimate Ultimate Weapon!',NULL,1,'2017-01-01',1400,2);
/*!40000 ALTER TABLE `Product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ProductType`
--

DROP TABLE IF EXISTS `ProductType`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ProductType` (
  `ProductTypeID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ProductTypeID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ProductType`
--

LOCK TABLES `ProductType` WRITE;
/*!40000 ALTER TABLE `ProductType` DISABLE KEYS */;
INSERT INTO `ProductType` VALUES (1,'City'),(2,'Ninjago');
/*!40000 ALTER TABLE `ProductType` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Set`
--

DROP TABLE IF EXISTS `Set`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Set` (
  `SetID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  `SetNo` varchar(50) DEFAULT NULL,
  `Price` decimal(10,2) DEFAULT NULL,
  `Description` varchar(250) DEFAULT NULL,
  `Image` blob,
  `Availibility` int DEFAULT NULL,
  `UnitsSold` int DEFAULT NULL,
  `ReleaseDate` date DEFAULT NULL,
  `PieceCount` int DEFAULT NULL,
  `Instruction` text,
  PRIMARY KEY (`SetID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Set`
--

LOCK TABLES `Set` WRITE;
/*!40000 ALTER TABLE `Set` DISABLE KEYS */;
/*!40000 ALTER TABLE `Set` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Set_Product`
--

DROP TABLE IF EXISTS `Set_Product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Set_Product` (
  `SetProductID` int NOT NULL AUTO_INCREMENT,
  `SetID` int DEFAULT NULL,
  `ProductID` int DEFAULT NULL,
  PRIMARY KEY (`SetProductID`),
  KEY `ProductID` (`ProductID`),
  KEY `SetID` (`SetID`),
  CONSTRAINT `set_product_ibfk_1` FOREIGN KEY (`ProductID`) REFERENCES `Product` (`ProductID`),
  CONSTRAINT `set_product_ibfk_2` FOREIGN KEY (`SetID`) REFERENCES `Set` (`SetID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Set_Product`
--

LOCK TABLES `Set_Product` WRITE;
/*!40000 ALTER TABLE `Set_Product` DISABLE KEYS */;
/*!40000 ALTER TABLE `Set_Product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ShoppingCart`
--

DROP TABLE IF EXISTS `ShoppingCart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ShoppingCart` (
  `ShoppingCartID` int NOT NULL AUTO_INCREMENT,
  `ShoppingCart_Item` varchar(50) DEFAULT NULL,
  `ShippingCost` int DEFAULT NULL,
  `NumberOfItems` int DEFAULT NULL,
  `TotalPrice` int DEFAULT NULL,
  PRIMARY KEY (`ShoppingCartID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ShoppingCart`
--

LOCK TABLES `ShoppingCart` WRITE;
/*!40000 ALTER TABLE `ShoppingCart` DISABLE KEYS */;
INSERT INTO `ShoppingCart` VALUES (1,'Police Station',10,1,100);
/*!40000 ALTER TABLE `ShoppingCart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ShoppingCart_Product`
--

DROP TABLE IF EXISTS `ShoppingCart_Product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ShoppingCart_Product` (
  `ShoppingCartProductID` int NOT NULL AUTO_INCREMENT,
  `ShoppingCartID` int DEFAULT NULL,
  `ProductID` int DEFAULT NULL,
  `SetID` int DEFAULT NULL,
  PRIMARY KEY (`ShoppingCartProductID`),
  KEY `ShoppingCartID` (`ShoppingCartID`),
  KEY `ProductID` (`ProductID`),
  KEY `SetID` (`SetID`),
  CONSTRAINT `shoppingcart_product_ibfk_1` FOREIGN KEY (`ShoppingCartID`) REFERENCES `ShoppingCart` (`ShoppingCartID`),
  CONSTRAINT `shoppingcart_product_ibfk_2` FOREIGN KEY (`ProductID`) REFERENCES `Product` (`ProductID`),
  CONSTRAINT `shoppingcart_product_ibfk_3` FOREIGN KEY (`SetID`) REFERENCES `Set` (`SetID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ShoppingCart_Product`
--

LOCK TABLES `ShoppingCart_Product` WRITE;
/*!40000 ALTER TABLE `ShoppingCart_Product` DISABLE KEYS */;
/*!40000 ALTER TABLE `ShoppingCart_Product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `UserID` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(50) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL,
  `ShoppingCartID` int DEFAULT NULL,
  `Address` int DEFAULT NULL,
  PRIMARY KEY (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'johndoe','johndoe@gmail.com','password123',1,1);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-18 12:45:23
