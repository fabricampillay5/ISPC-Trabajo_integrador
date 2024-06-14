-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: allbreads
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (12345678,'Juan Pérez','Calle Falsa 123',5551234,1),(23456789,'María García','Avenida Siempre Viva 456',5555678,1),(34567890,'Carlos Rodríguez','Boulevard de los Sueños 789',5558765,1),(45678901,'Ana López','Camino de la Esperanza 101',5554321,1);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `orden de compra`
--

LOCK TABLES `orden de compra` WRITE;
/*!40000 ALTER TABLE `orden de compra` DISABLE KEYS */;
INSERT INTO `orden de compra` VALUES (1,'Alimentos Balanceados',10,'Balanceados',1),(2,'Suplementos Vitaminicos',5,'Vitaminicos',2),(3,'Forrajes y Henos',8,'Varios',3),(4,'Cerdos',15,'Cerdos',4);
/*!40000 ALTER TABLE `orden de compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `orden de despacho`
--

LOCK TABLES `orden de despacho` WRITE;
/*!40000 ALTER TABLE `orden de despacho` DISABLE KEYS */;
INSERT INTO `orden de despacho` VALUES (1,'Alimentos Balanceados',5,12345678,'Balanceados'),(2,'Suplementos Vitaminicos',3,23456789,'Vitaminicos'),(3,'Forrajes y Henos',7,34567890,'Varios'),(4,'Cerdos',10,45678901,'Cerdos');
/*!40000 ALTER TABLE `orden de despacho` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `orden de despacho_has_producto`
--

LOCK TABLES `orden de despacho_has_producto` WRITE;
/*!40000 ALTER TABLE `orden de despacho_has_producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `orden de despacho_has_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,100,'Alimentos Balanceados','2025-06-13'),(2,200,'Suplementos Vitaminicos','2025-06-14'),(3,150,'Forrajes y Henos','2025-06-15'),(4,250,'Cerdos','2025-06-16');
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `producto_has_orden de compra`
--

LOCK TABLES `producto_has_orden de compra` WRITE;
/*!40000 ALTER TABLE `producto_has_orden de compra` DISABLE KEYS */;
/*!40000 ALTER TABLE `producto_has_orden de compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
INSERT INTO `proveedor` VALUES (1,'NutriAlimentos S.A.','Alimentos Balanceados',5551111),(2,'ProveeNutri Ltda.','Suplementos Vitaminicos',5552222),(3,'AgroNutricion','Forrajes y Henos',5553333),(4,'AnimalFeed Co.','Cerdos',5554444);
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-14  8:54:28
