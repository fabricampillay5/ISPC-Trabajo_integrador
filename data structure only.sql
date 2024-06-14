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
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `DNI` int NOT NULL,
  `NOMBRE` varchar(45) DEFAULT NULL,
  `DIRECCION` varchar(45) DEFAULT NULL,
  `TELEFONO` int DEFAULT NULL,
  `ACTIVO` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`DNI`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `orden de compra`
--

DROP TABLE IF EXISTS `orden de compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orden de compra` (
  `NRO_ORDEN` int NOT NULL,
  `NOMBRE_PRODUCTO` varchar(45) DEFAULT NULL,
  `CANT_ORDEN` int DEFAULT NULL,
  `TIPO_PRODUCTO` varchar(45) DEFAULT NULL,
  `PROVEEDOR_ID` int NOT NULL,
  PRIMARY KEY (`NRO_ORDEN`),
  KEY `fk_ORDEN DE COMPRA_PROVEEDOR1_idx` (`PROVEEDOR_ID`),
  CONSTRAINT `fk_ORDEN DE COMPRA_PROVEEDOR1` FOREIGN KEY (`PROVEEDOR_ID`) REFERENCES `proveedor` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `orden de despacho`
--

DROP TABLE IF EXISTS `orden de despacho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orden de despacho` (
  `NUM_DESPACHO` int NOT NULL,
  `NOMBRE_PRODUCTO` varchar(45) DEFAULT NULL,
  `CANT_DESPACHO` int DEFAULT NULL,
  `DNI` int NOT NULL,
  `TIPO _PRODUCTO` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`NUM_DESPACHO`),
  KEY `DNI_idx` (`DNI`),
  CONSTRAINT `DNI` FOREIGN KEY (`DNI`) REFERENCES `clientes` (`DNI`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `orden de despacho_has_producto`
--

DROP TABLE IF EXISTS `orden de despacho_has_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orden de despacho_has_producto` (
  `ORDEN DE DESPACHO_ID` int NOT NULL,
  `PRODUCTO_ID` int NOT NULL,
  PRIMARY KEY (`ORDEN DE DESPACHO_ID`,`PRODUCTO_ID`),
  KEY `fk_ORDEN DE DESPACHO_has_PRODUCTO_PRODUCTO1_idx` (`PRODUCTO_ID`),
  KEY `fk_ORDEN DE DESPACHO_has_PRODUCTO_ORDEN DE DESPACHO1_idx` (`ORDEN DE DESPACHO_ID`),
  CONSTRAINT `fk_ORDEN DE DESPACHO_has_PRODUCTO_ORDEN DE DESPACHO1` FOREIGN KEY (`ORDEN DE DESPACHO_ID`) REFERENCES `orden de despacho` (`NUM_DESPACHO`),
  CONSTRAINT `fk_ORDEN DE DESPACHO_has_PRODUCTO_PRODUCTO1` FOREIGN KEY (`PRODUCTO_ID`) REFERENCES `producto` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `ID` int NOT NULL,
  `CANTIDAD` int DEFAULT NULL,
  `NOMBRE_PRODUCTO` varchar(45) DEFAULT NULL,
  `FECHA_VENCIMIENTO` date DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `producto_has_orden de compra`
--

DROP TABLE IF EXISTS `producto_has_orden de compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto_has_orden de compra` (
  `PRODUCTO_ID` int NOT NULL,
  `ORDEN DE COMPRA_ID` int NOT NULL,
  PRIMARY KEY (`PRODUCTO_ID`,`ORDEN DE COMPRA_ID`),
  KEY `fk_PRODUCTO_has_ORDEN DE COMPRA_ORDEN DE COMPRA1_idx` (`ORDEN DE COMPRA_ID`),
  KEY `fk_PRODUCTO_has_ORDEN DE COMPRA_PRODUCTO1_idx` (`PRODUCTO_ID`),
  CONSTRAINT `fk_PRODUCTO_has_ORDEN DE COMPRA_ORDEN DE COMPRA1` FOREIGN KEY (`ORDEN DE COMPRA_ID`) REFERENCES `orden de compra` (`NRO_ORDEN`),
  CONSTRAINT `fk_PRODUCTO_has_ORDEN DE COMPRA_PRODUCTO1` FOREIGN KEY (`PRODUCTO_ID`) REFERENCES `producto` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `ID` int NOT NULL,
  `RAZON SOCIAL` varchar(45) DEFAULT NULL,
  `TIPO PRODUCTO` varchar(45) DEFAULT NULL,
  `TELEFONO` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-14  8:55:37
