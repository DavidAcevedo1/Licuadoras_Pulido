-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: db_licuadoraspulido
-- ------------------------------------------------------
-- Server version	5.7.33

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
-- Table structure for table `administrador_copiaseguridad`
--

DROP TABLE IF EXISTS `administrador_copiaseguridad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrador_copiaseguridad` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `archivo` varchar(100) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador_copiaseguridad`
--

LOCK TABLES `administrador_copiaseguridad` WRITE;
/*!40000 ALTER TABLE `administrador_copiaseguridad` DISABLE KEYS */;
/*!40000 ALTER TABLE `administrador_copiaseguridad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `administrador_electrodomestico`
--

DROP TABLE IF EXISTS `administrador_electrodomestico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrador_electrodomestico` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(25) NOT NULL,
  `referencia` varchar(25) NOT NULL,
  `estado` varchar(20) NOT NULL,
  `marca_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `administrador_electr_marca_id_20d39cc7_fk_administr` (`marca_id`),
  CONSTRAINT `administrador_electr_marca_id_20d39cc7_fk_administr` FOREIGN KEY (`marca_id`) REFERENCES `administrador_marca` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador_electrodomestico`
--

LOCK TABLES `administrador_electrodomestico` WRITE;
/*!40000 ALTER TABLE `administrador_electrodomestico` DISABLE KEYS */;
INSERT INTO `administrador_electrodomestico` VALUES (1,'batidora','5677222','Activo',2),(2,'tosta','56772','Activo',1);
/*!40000 ALTER TABLE `administrador_electrodomestico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `administrador_elemento`
--

DROP TABLE IF EXISTS `administrador_elemento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrador_elemento` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(25) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `precio` int(11) NOT NULL,
  `stock_elemento` int(11) NOT NULL,
  `favorito` tinyint(1) NOT NULL,
  `foto` varchar(100) DEFAULT NULL,
  `estado` varchar(10) NOT NULL,
  `marca_id` bigint(20) DEFAULT NULL,
  `tipo_elemento_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `administrador_elemen_marca_id_c1dfdcd4_fk_administr` (`marca_id`),
  KEY `administrador_elemen_tipo_elemento_id_9f66d34b_fk_administr` (`tipo_elemento_id`),
  CONSTRAINT `administrador_elemen_marca_id_c1dfdcd4_fk_administr` FOREIGN KEY (`marca_id`) REFERENCES `administrador_marca` (`id`),
  CONSTRAINT `administrador_elemen_tipo_elemento_id_9f66d34b_fk_administr` FOREIGN KEY (`tipo_elemento_id`) REFERENCES `administrador_tipos_elemento` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador_elemento`
--

LOCK TABLES `administrador_elemento` WRITE;
/*!40000 ALTER TABLE `administrador_elemento` DISABLE KEYS */;
INSERT INTO `administrador_elemento` VALUES (1,'Tornillo 3Cm','la mejor papu',50,1,1,'carrito/img5.jpg','Activo',3,1),(2,'Licuadora V4','la mejor papu',400000,29,1,'carrito/licuadoraOster.jpg','Activo',1,2);
/*!40000 ALTER TABLE `administrador_elemento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `administrador_favorito`
--

DROP TABLE IF EXISTS `administrador_favorito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrador_favorito` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `favorito` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador_favorito`
--

LOCK TABLES `administrador_favorito` WRITE;
/*!40000 ALTER TABLE `administrador_favorito` DISABLE KEYS */;
/*!40000 ALTER TABLE `administrador_favorito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `administrador_marca`
--

DROP TABLE IF EXISTS `administrador_marca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrador_marca` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(10) NOT NULL,
  `estado` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador_marca`
--

LOCK TABLES `administrador_marca` WRITE;
/*!40000 ALTER TABLE `administrador_marca` DISABLE KEYS */;
INSERT INTO `administrador_marca` VALUES (1,'Oster','Activo'),(2,'Imusa','Activo'),(3,'Generico','Activo');
/*!40000 ALTER TABLE `administrador_marca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `administrador_servicio`
--

DROP TABLE IF EXISTS `administrador_servicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrador_servicio` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `tiposervicio` varchar(20) NOT NULL,
  `fallas_basicas` varchar(255) NOT NULL,
  `diagnostico` varchar(250) NOT NULL,
  `observacion` varchar(100) NOT NULL,
  `fecha_entrada` date NOT NULL,
  `estado` varchar(20) NOT NULL,
  `electrodomestico_id` bigint(20) DEFAULT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `administrador_servic_electrodomestico_id_c999c5b8_fk_administr` (`electrodomestico_id`),
  KEY `administrador_servic_usuario_id_de390085_fk_usuarios_` (`usuario_id`),
  CONSTRAINT `administrador_servic_electrodomestico_id_c999c5b8_fk_administr` FOREIGN KEY (`electrodomestico_id`) REFERENCES `administrador_electrodomestico` (`id`),
  CONSTRAINT `administrador_servic_usuario_id_de390085_fk_usuarios_` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios_usuario` (`Uid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador_servicio`
--

LOCK TABLES `administrador_servicio` WRITE;
/*!40000 ALTER TABLE `administrador_servicio` DISABLE KEYS */;
INSERT INTO `administrador_servicio` VALUES (1,'Reparación','kikjhkj','iiuouoiuoiu','sflvjslkjgslkj','2022-09-14','Activo',2,2);
/*!40000 ALTER TABLE `administrador_servicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `administrador_tipos_elemento`
--

DROP TABLE IF EXISTS `administrador_tipos_elemento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrador_tipos_elemento` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `categoria` varchar(20) NOT NULL,
  `subcategoria` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `subcategoria` (`subcategoria`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador_tipos_elemento`
--

LOCK TABLES `administrador_tipos_elemento` WRITE;
/*!40000 ALTER TABLE `administrador_tipos_elemento` DISABLE KEYS */;
INSERT INTO `administrador_tipos_elemento` VALUES (1,'Accesorios','Tornillo'),(2,'Productos','Licuadora');
/*!40000 ALTER TABLE `administrador_tipos_elemento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add copiaseguridad',7,'add_copiaseguridad'),(26,'Can change copiaseguridad',7,'change_copiaseguridad'),(27,'Can delete copiaseguridad',7,'delete_copiaseguridad'),(28,'Can view copiaseguridad',7,'view_copiaseguridad'),(29,'Can add favorito',8,'add_favorito'),(30,'Can change favorito',8,'change_favorito'),(31,'Can delete favorito',8,'delete_favorito'),(32,'Can view favorito',8,'view_favorito'),(33,'Can add elemento',9,'add_elemento'),(34,'Can change elemento',9,'change_elemento'),(35,'Can delete elemento',9,'delete_elemento'),(36,'Can view elemento',9,'view_elemento'),(37,'Can add servicio',10,'add_servicio'),(38,'Can change servicio',10,'change_servicio'),(39,'Can delete servicio',10,'delete_servicio'),(40,'Can view servicio',10,'view_servicio'),(41,'Can add marca',11,'add_marca'),(42,'Can change marca',11,'change_marca'),(43,'Can delete marca',11,'delete_marca'),(44,'Can view marca',11,'view_marca'),(45,'Can add electrodomestico',12,'add_electrodomestico'),(46,'Can change electrodomestico',12,'change_electrodomestico'),(47,'Can delete electrodomestico',12,'delete_electrodomestico'),(48,'Can view electrodomestico',12,'view_electrodomestico'),(49,'Can add tipos_ elemento',13,'add_tipos_elemento'),(50,'Can change tipos_ elemento',13,'change_tipos_elemento'),(51,'Can delete tipos_ elemento',13,'delete_tipos_elemento'),(52,'Can view tipos_ elemento',13,'view_tipos_elemento'),(53,'Can add rol',14,'add_rol'),(54,'Can change rol',14,'change_rol'),(55,'Can delete rol',14,'delete_rol'),(56,'Can view rol',14,'view_rol'),(57,'Can add usuario',15,'add_usuario'),(58,'Can change usuario',15,'change_usuario'),(59,'Can delete usuario',15,'delete_usuario'),(60,'Can view usuario',15,'view_usuario'),(61,'Can add factura',16,'add_factura'),(62,'Can change factura',16,'change_factura'),(63,'Can delete factura',16,'delete_factura'),(64,'Can view factura',16,'view_factura'),(65,'Can add detalle servicio',17,'add_detalleservicio'),(66,'Can change detalle servicio',17,'change_detalleservicio'),(67,'Can delete detalle servicio',17,'delete_detalleservicio'),(68,'Can view detalle servicio',17,'view_detalleservicio'),(69,'Can add detalle',18,'add_detalle'),(70,'Can change detalle',18,'change_detalle'),(71,'Can delete detalle',18,'delete_detalle'),(72,'Can view detalle',18,'view_detalle');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$390000$7hZAktxIBBhyJrv6sli7oN$Ja1MHQFd84zGZSw4134Hilv3hc0SRQ/R7gWitXI0QKY=','2022-09-14 18:20:36.478120',1,'admin','','','',1,1,'2022-09-14 18:20:21.895480');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'administrador','copiaseguridad'),(12,'administrador','electrodomestico'),(9,'administrador','elemento'),(8,'administrador','favorito'),(11,'administrador','marca'),(10,'administrador','servicio'),(13,'administrador','tipos_elemento'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(18,'facturas','detalle'),(17,'facturas','detalleservicio'),(16,'facturas','factura'),(6,'sessions','session'),(14,'usuarios','rol'),(15,'usuarios','usuario');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-09-14 18:19:39.863838'),(2,'auth','0001_initial','2022-09-14 18:19:40.262203'),(3,'admin','0001_initial','2022-09-14 18:19:40.341831'),(4,'admin','0002_logentry_remove_auto_add','2022-09-14 18:19:40.348261'),(5,'admin','0003_logentry_add_action_flag_choices','2022-09-14 18:19:40.348261'),(6,'contenttypes','0002_remove_content_type_name','2022-09-14 18:19:40.414393'),(7,'auth','0002_alter_permission_name_max_length','2022-09-14 18:19:40.427856'),(8,'auth','0003_alter_user_email_max_length','2022-09-14 18:19:40.441854'),(9,'auth','0004_alter_user_username_opts','2022-09-14 18:19:40.448886'),(10,'auth','0005_alter_user_last_login_null','2022-09-14 18:19:40.477013'),(11,'auth','0006_require_contenttypes_0002','2022-09-14 18:19:40.478984'),(12,'auth','0007_alter_validators_add_error_messages','2022-09-14 18:19:40.485014'),(13,'auth','0008_alter_user_username_max_length','2022-09-14 18:19:40.499995'),(14,'auth','0009_alter_user_last_name_max_length','2022-09-14 18:19:40.513030'),(15,'auth','0010_alter_group_name_max_length','2022-09-14 18:19:40.526365'),(16,'auth','0011_update_proxy_permissions','2022-09-14 18:19:40.534372'),(17,'auth','0012_alter_user_first_name_max_length','2022-09-14 18:19:40.547365'),(18,'sessions','0001_initial','2022-09-14 18:19:40.592668'),(19,'usuarios','0001_initial','2022-09-14 18:19:47.090750'),(20,'administrador','0001_initial','2022-09-14 18:19:47.372587'),(21,'facturas','0001_initial','2022-09-14 18:19:47.686472');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('36rn5gz68r2p6dbzbt2im8muldnfodfp','.eJxVjDsOgzAQRO-ydWT5sxhDmT5nQLv-BJIISzZUiLsHJBo03bw3s4GnUqYlQ7_tDxhoXcZhrbEMU4AeFNw6Jv-N8wnCh-Z3Fj7PS5lYnIq4aBWvHOLvebm3g5HqeKyNa0ixdsGgxQ4TW0TXeq1ck9BHMtKxJEssQ6Nj6vSRhK3EqAwr28L-B_h6O6g:1oYXcT:zU7nCNROz8764nCoeZadlN9jNz6PtRsz7HkAssHOP5Q','2022-09-28 19:00:21.032053');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facturas_detalle`
--

DROP TABLE IF EXISTS `facturas_detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `facturas_detalle` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `estado` varchar(10) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `elemento_id` bigint(20) DEFAULT NULL,
  `factura_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `facturas_detalle_elemento_id_c1285739_fk_administr` (`elemento_id`),
  KEY `facturas_detalle_factura_id_2b4976b9_fk_facturas_factura_id` (`factura_id`),
  CONSTRAINT `facturas_detalle_elemento_id_c1285739_fk_administr` FOREIGN KEY (`elemento_id`) REFERENCES `administrador_elemento` (`id`),
  CONSTRAINT `facturas_detalle_factura_id_2b4976b9_fk_facturas_factura_id` FOREIGN KEY (`factura_id`) REFERENCES `facturas_factura` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facturas_detalle`
--

LOCK TABLES `facturas_detalle` WRITE;
/*!40000 ALTER TABLE `facturas_detalle` DISABLE KEYS */;
INSERT INTO `facturas_detalle` VALUES (1,'Abierta',40,1,1),(2,'Abierta',30,2,1),(3,'Abierta',12,1,2),(4,'Abierta',5,2,2),(5,'Abierta',23,1,3),(6,'Abierta',45,2,3),(8,'Abierta',34,1,4),(9,'Abierta',30,2,4),(10,'Abierta',11,2,5),(11,'Abierta',-9,1,5),(12,'Abierta',21,1,6),(13,'Abierta',18,1,7);
/*!40000 ALTER TABLE `facturas_detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facturas_detalleservicio`
--

DROP TABLE IF EXISTS `facturas_detalleservicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `facturas_detalleservicio` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `estado` varchar(10) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `factura_id` bigint(20) DEFAULT NULL,
  `servicio_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `facturas_detalleserv_factura_id_08df39dc_fk_facturas_` (`factura_id`),
  KEY `facturas_detalleserv_servicio_id_18598f77_fk_administr` (`servicio_id`),
  CONSTRAINT `facturas_detalleserv_factura_id_08df39dc_fk_facturas_` FOREIGN KEY (`factura_id`) REFERENCES `facturas_factura` (`id`),
  CONSTRAINT `facturas_detalleserv_servicio_id_18598f77_fk_administr` FOREIGN KEY (`servicio_id`) REFERENCES `administrador_servicio` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facturas_detalleservicio`
--

LOCK TABLES `facturas_detalleservicio` WRITE;
/*!40000 ALTER TABLE `facturas_detalleservicio` DISABLE KEYS */;
/*!40000 ALTER TABLE `facturas_detalleservicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facturas_factura`
--

DROP TABLE IF EXISTS `facturas_factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `facturas_factura` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `tipofactura` varchar(10) NOT NULL,
  `estado` varchar(10) NOT NULL,
  `decision` varchar(10) NOT NULL,
  `rol_id` int(11) DEFAULT NULL,
  `servicio_id` bigint(20) DEFAULT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `facturas_factura_rol_id_6180f164_fk_usuarios_rol_Rid` (`rol_id`),
  KEY `facturas_factura_servicio_id_d8e98c98_fk_administr` (`servicio_id`),
  KEY `facturas_factura_usuario_id_2269c3b8_fk_usuarios_usuario_Uid` (`usuario_id`),
  CONSTRAINT `facturas_factura_rol_id_6180f164_fk_usuarios_rol_Rid` FOREIGN KEY (`rol_id`) REFERENCES `usuarios_rol` (`Rid`),
  CONSTRAINT `facturas_factura_servicio_id_d8e98c98_fk_administr` FOREIGN KEY (`servicio_id`) REFERENCES `administrador_servicio` (`id`),
  CONSTRAINT `facturas_factura_usuario_id_2269c3b8_fk_usuarios_usuario_Uid` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios_usuario` (`Uid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facturas_factura`
--

LOCK TABLES `facturas_factura` WRITE;
/*!40000 ALTER TABLE `facturas_factura` DISABLE KEYS */;
INSERT INTO `facturas_factura` VALUES (1,'2022-09-14','Compra','Cerrada','Inactivo',NULL,NULL,1),(2,'2022-09-14','Venta','Cerrada','Inactivo',NULL,NULL,2),(3,'2022-09-14','Compra','Cerrada','Inactivo',NULL,NULL,1),(4,'2022-09-14','Venta','Cerrada','Activo',NULL,NULL,2),(5,'2022-09-14','Venta','Cerrada','Activo',NULL,NULL,2),(6,'2022-09-14','Venta','Abierta','Activo',NULL,NULL,2),(7,'2022-09-14','Venta','Abierta','Activo',NULL,NULL,2);
/*!40000 ALTER TABLE `facturas_factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_rol`
--

DROP TABLE IF EXISTS `usuarios_rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios_rol` (
  `Rid` int(11) NOT NULL AUTO_INCREMENT,
  `Rnombre` varchar(20) NOT NULL,
  PRIMARY KEY (`Rid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_rol`
--

LOCK TABLES `usuarios_rol` WRITE;
/*!40000 ALTER TABLE `usuarios_rol` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios_rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_usuario`
--

DROP TABLE IF EXISTS `usuarios_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios_usuario` (
  `Uid` int(11) NOT NULL AUTO_INCREMENT,
  `documento` varchar(10) NOT NULL,
  `tipo_documento` varchar(3) NOT NULL,
  `rol` varchar(13) NOT NULL,
  `Unombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `celular` varchar(10) NOT NULL,
  `estado` varchar(10) NOT NULL,
  PRIMARY KEY (`Uid`),
  UNIQUE KEY `documento` (`documento`),
  UNIQUE KEY `celular` (`celular`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_usuario`
--

LOCK TABLES `usuarios_usuario` WRITE;
/*!40000 ALTER TABLE `usuarios_usuario` DISABLE KEYS */;
INSERT INTO `usuarios_usuario` VALUES (1,'10045665','C.C','Proveedor','ANDRES','Diaz','32457765','Activo'),(2,'10045662','C.C','Cliente','Jorge','Hernandez','7868768768','Activo');
/*!40000 ALTER TABLE `usuarios_usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-14 14:00:28
