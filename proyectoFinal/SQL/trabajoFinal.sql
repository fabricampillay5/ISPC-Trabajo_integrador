-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: nutricion_animal
-- ------------------------------------------------------
-- Server version	8.0.37

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
  `nombre` varchar(45) NOT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `activo` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`DNI`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (12345678,'Juan Pérez','Calle Falsa 123','5551234',1),(23456789,'María García','Avenida Siempre Viva 456','5555678',1),(34567890,'Carlos Rodríguez','Boulevard de los Sueños 789','5558765',1),(45678901,'Ana López','Camino de la Esperanza 101','5554321',1);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orden_compra`
--

DROP TABLE IF EXISTS `orden_compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orden_compra` (
  `nro_orden` int NOT NULL,
  `fecha` date NOT NULL,
  `proveedor_id` int DEFAULT NULL,
  PRIMARY KEY (`nro_orden`),
  KEY `proveedor_id` (`proveedor_id`),
  CONSTRAINT `orden_compra_ibfk_1` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orden_compra`
--

LOCK TABLES `orden_compra` WRITE;
/*!40000 ALTER TABLE `orden_compra` DISABLE KEYS */;
INSERT INTO `orden_compra` VALUES (1,'2024-01-15',1),(2,'2024-02-10',2),(3,'2024-03-05',3),(4,'2024-04-20',4),(5,'2024-05-25',5);
/*!40000 ALTER TABLE `orden_compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orden_despacho`
--

DROP TABLE IF EXISTS `orden_despacho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orden_despacho` (
  `num_despacho` int NOT NULL,
  `fecha` date NOT NULL,
  `cliente_dni` int DEFAULT NULL,
  PRIMARY KEY (`num_despacho`),
  KEY `cliente_dni` (`cliente_dni`),
  CONSTRAINT `orden_despacho_ibfk_1` FOREIGN KEY (`cliente_dni`) REFERENCES `clientes` (`DNI`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orden_despacho`
--

LOCK TABLES `orden_despacho` WRITE;
/*!40000 ALTER TABLE `orden_despacho` DISABLE KEYS */;
INSERT INTO `orden_despacho` VALUES (1,'2024-06-10',12345678),(2,'2024-07-15',23456789),(3,'2024-08-20',34567890),(4,'2024-09-25',45678901);
/*!40000 ALTER TABLE `orden_despacho` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `id` int NOT NULL,
  `nombre_producto` varchar(45) NOT NULL,
  `cantidad` int DEFAULT '0',
  `fecha_vencimiento` date DEFAULT NULL,
  `proveedor_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `proveedor_id` (`proveedor_id`),
  CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,'Alimento para terneros',100,'2025-06-13',1),(2,'Alimento para cerdos',200,'2025-06-14',2),(3,'Alimento para ñandúes',150,'2025-06-15',3),(4,'Alimento para gallinas',250,'2025-06-16',4),(5,'Alimento para toros',180,'2025-06-17',5);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto_orden_compra`
--

DROP TABLE IF EXISTS `producto_orden_compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto_orden_compra` (
  `orden_compra_id` int NOT NULL,
  `producto_id` int NOT NULL,
  `cantidad` int NOT NULL,
  PRIMARY KEY (`orden_compra_id`,`producto_id`),
  KEY `producto_id` (`producto_id`),
  CONSTRAINT `producto_orden_compra_ibfk_1` FOREIGN KEY (`orden_compra_id`) REFERENCES `orden_compra` (`nro_orden`) ON DELETE CASCADE,
  CONSTRAINT `producto_orden_compra_ibfk_2` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto_orden_compra`
--

LOCK TABLES `producto_orden_compra` WRITE;
/*!40000 ALTER TABLE `producto_orden_compra` DISABLE KEYS */;
INSERT INTO `producto_orden_compra` VALUES (1,1,50),(2,2,100),(3,3,80),(4,4,120),(5,5,60);
/*!40000 ALTER TABLE `producto_orden_compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto_orden_despacho`
--

DROP TABLE IF EXISTS `producto_orden_despacho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto_orden_despacho` (
  `orden_despacho_id` int NOT NULL,
  `producto_id` int NOT NULL,
  `cantidad` int NOT NULL,
  PRIMARY KEY (`orden_despacho_id`,`producto_id`),
  KEY `producto_id` (`producto_id`),
  CONSTRAINT `producto_orden_despacho_ibfk_1` FOREIGN KEY (`orden_despacho_id`) REFERENCES `orden_despacho` (`num_despacho`) ON DELETE CASCADE,
  CONSTRAINT `producto_orden_despacho_ibfk_2` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto_orden_despacho`
--

LOCK TABLES `producto_orden_despacho` WRITE;
/*!40000 ALTER TABLE `producto_orden_despacho` DISABLE KEYS */;
INSERT INTO `producto_orden_despacho` VALUES (1,1,20),(2,2,50),(3,3,30),(4,4,60);
/*!40000 ALTER TABLE `producto_orden_despacho` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `id` int NOT NULL,
  `razon_social` varchar(100) NOT NULL,
  `tipo_producto` varchar(45) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
INSERT INTO `proveedor` VALUES (1,'NutriTerneros S.A.','Alimentos para terneros','5551111'),(2,'PorcinoNutri Ltda.','Alimentos para cerdos','5552222'),(3,'ÑandúCare','Alimentos para ñandúes','5553333'),(4,'GallinasVital','Alimentos para gallinas','5554444'),(5,'ToroFeed Co.','Alimentos para toros','5555555');
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'nutricion_animal'
--

--
-- Dumping routines for database 'nutricion_animal'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-29 12:31:42
