-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: bookwings
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `accounts_address`
--

DROP TABLE IF EXISTS `accounts_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_address` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `local_address` varchar(255) NOT NULL,
  `commune` varchar(255) NOT NULL,
  `district` varchar(255) NOT NULL,
  `province` varchar(255) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_address_user_id_c8c74ddf_fk_accounts_user_id` (`user_id`),
  CONSTRAINT `accounts_address_user_id_c8c74ddf_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_address`
--

LOCK TABLES `accounts_address` WRITE;
/*!40000 ALTER TABLE `accounts_address` DISABLE KEYS */;
INSERT INTO `accounts_address` VALUES (2,'K58/18 Ngô Sĩ Liên','Hòa Khánh Bắc','Liên Chiểu','Đà Nẵng',2);
/*!40000 ALTER TABLE `accounts_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_user`
--

DROP TABLE IF EXISTS `accounts_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(40) NOT NULL,
  `phone_number` varchar(20) NOT NULL,
  `email` varchar(255) NOT NULL,
  `gender` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone_number` (`phone_number`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user`
--

LOCK TABLES `accounts_user` WRITE;
/*!40000 ALTER TABLE `accounts_user` DISABLE KEYS */;
INSERT INTO `accounts_user` VALUES (2,'pbkdf2_sha256$720000$Hs3NXYnXe1rvmUmgnTeEQq$fQ5HAa0tlommxFcDZL83wIdPluqMny9YcroaIYbvwIc=','2024-05-11 14:09:25.357552','Tora','Law','0123456789','toraolaw6@gmail.com',1,'2024-05-07 15:10:30.837827',0),(3,'pbkdf2_sha256$720000$uIb49bTILoo5Cqz4HpZlmP$h6dNfGzXR00Uu+DepyM0gX/XnAht/BV3rMjDwcTFbpY=','2024-05-11 13:24:01.837549','Quang','Nguyen','0973734250','ncnhatquang26@gmail.com',1,'2024-05-07 15:24:20.157672',1);
/*!40000 ALTER TABLE `accounts_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can view permission',1,'view_permission'),(5,'Can add group',2,'add_group'),(6,'Can change group',2,'change_group'),(7,'Can delete group',2,'delete_group'),(8,'Can view group',2,'view_group'),(9,'Can add content type',3,'add_contenttype'),(10,'Can change content type',3,'change_contenttype'),(11,'Can delete content type',3,'delete_contenttype'),(12,'Can view content type',3,'view_contenttype'),(13,'Can add session',4,'add_session'),(14,'Can change session',4,'change_session'),(15,'Can delete session',4,'delete_session'),(16,'Can view session',4,'view_session'),(17,'Can add user',5,'add_user'),(18,'Can change user',5,'change_user'),(19,'Can delete user',5,'delete_user'),(20,'Can view user',5,'view_user'),(21,'Can add address',6,'add_address'),(22,'Can change address',6,'change_address'),(23,'Can delete address',6,'delete_address'),(24,'Can view address',6,'view_address'),(25,'Can add book',7,'add_book'),(26,'Can change book',7,'change_book'),(27,'Can delete book',7,'delete_book'),(28,'Can view book',7,'view_book'),(29,'Can add category',8,'add_category'),(30,'Can change category',8,'change_category'),(31,'Can delete category',8,'delete_category'),(32,'Can view category',8,'view_category'),(33,'Can add order',9,'add_order'),(34,'Can change order',9,'change_order'),(35,'Can delete order',9,'delete_order'),(36,'Can view order',9,'view_order'),(37,'Can add delivery information',10,'add_deliveryinformation'),(38,'Can change delivery information',10,'change_deliveryinformation'),(39,'Can delete delivery information',10,'delete_deliveryinformation'),(40,'Can view delivery information',10,'view_deliveryinformation'),(41,'Can add book in order',11,'add_bookinorder'),(42,'Can change book in order',11,'change_bookinorder'),(43,'Can delete book in order',11,'delete_bookinorder'),(44,'Can view book in order',11,'view_bookinorder'),(45,'Can add coupon',12,'add_coupon'),(46,'Can change coupon',12,'change_coupon'),(47,'Can delete coupon',12,'delete_coupon'),(48,'Can view coupon',12,'view_coupon'),(49,'Can add cart',13,'add_cart'),(50,'Can change cart',13,'change_cart'),(51,'Can delete cart',13,'delete_cart'),(52,'Can view cart',13,'view_cart'),(53,'Can add book in cart',14,'add_bookincart'),(54,'Can change book in cart',14,'change_bookincart'),(55,'Can delete book in cart',14,'delete_bookincart'),(56,'Can view book in cart',14,'view_bookincart'),(57,'Can add log entry',15,'add_logentry'),(58,'Can change log entry',15,'change_logentry'),(59,'Can delete log entry',15,'delete_logentry'),(60,'Can view log entry',15,'view_logentry'),(61,'Can add shipping',16,'add_shipping'),(62,'Can change shipping',16,'change_shipping'),(63,'Can delete shipping',16,'delete_shipping'),(64,'Can view shipping',16,'view_shipping');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_book`
--

DROP TABLE IF EXISTS `books_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books_book` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `publisher` varchar(100) NOT NULL,
  `edition` int NOT NULL,
  `be_sold` int NOT NULL,
  `status` tinyint(1) NOT NULL,
  `cover` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_book`
--

LOCK TABLES `books_book` WRITE;
/*!40000 ALTER TABLE `books_book` DISABLE KEYS */;
INSERT INTO `books_book` VALUES (1,'Coraline','Neil Gaimai',68000.00,'Hội nhà văn',2,0,1,'books/coraline.jpg'),(2,'Sapiens - Lược sử loài người','Yuval Noah Harari',299000.00,'NXB Tri thức',6,0,1,'books/sapiens.jpg'),(3,'Chiếc lá cuối cùng','O. Henry',98000.00,'NXB Văn học',12,0,1,'books/clcq.jpg'),(4,'Công chúa nhỏ','Frances Hodgson Burnett',60000.00,'NXB Văn học',2,0,1,NULL),(5,'Trăm năm cô đơn','Gabriel Garcia Marquez',169000.00,'NXB Văn học',4,0,1,NULL),(6,'Đồi gió hú','Emily Bronte',72000.00,'NXB Văn học',2,0,1,NULL),(7,'Conan tập 90','Aoyama Gosho',25000.00,'NXB Kim Đồng',1,0,1,NULL),(8,'Cây cam ngọt của tôi','Jose Mauro Yasconcelos',75600.00,'NXB Hội Nhà Văn',20,0,1,'books/2a6154ba08df6ce6161c13f4303fa19e.jpg'),(9,'Nhà giả kim','Paulo Coelho',55300.00,'NXB Văn học',5,0,1,'books/737846efdb9f28f0f51352cacf9225c5.jpg'),(10,'Biến thể của cô đơn','Yang Phan',63000.00,'Nhã Nam',4,0,1,'books/nxbtre_full_11582024_035832.jpg'),(11,'Lũ trẻ đường tàu','Edith Nesbit',70500.00,'NXB Thanh Niên',8,0,1,''),(12,'Người bà tài giỏi vùng Saga','Yoshichi Shimada',85000.00,'NXB Thanh Niên',1,0,1,''),(13,'Nỗi buồn chiến tranh','Andrea Hirata',76300.00,'NXB Văn học',8,0,1,''),(14,'One piece - Tập 102','Eichiro Oda',25000.00,'NXB Kim Đồng',1,0,1,''),(15,'One piece - Tập 101','Eichiro Oda',25000.00,'NXB Kim Đồng',1,0,1,''),(16,'One piece - Tập 100','Eichiro Oda',25000.00,'NXB Kim Đồng',1,0,1,'');
/*!40000 ALTER TABLE `books_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_book_tags`
--

DROP TABLE IF EXISTS `books_book_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books_book_tags` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `book_id` bigint NOT NULL,
  `category_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `books_book_tags_book_id_category_id_83085b7d_uniq` (`book_id`,`category_id`),
  KEY `books_book_tags_category_id_b2ac0ac4_fk_books_category_id` (`category_id`),
  CONSTRAINT `books_book_tags_book_id_45714dc1_fk_books_book_id` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`id`),
  CONSTRAINT `books_book_tags_category_id_b2ac0ac4_fk_books_category_id` FOREIGN KEY (`category_id`) REFERENCES `books_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_book_tags`
--

LOCK TABLES `books_book_tags` WRITE;
/*!40000 ALTER TABLE `books_book_tags` DISABLE KEYS */;
INSERT INTO `books_book_tags` VALUES (1,1,1),(2,1,3),(3,2,4),(4,2,6),(5,3,12),(6,3,13),(7,4,2),(8,4,12),(9,5,11),(10,5,12),(13,6,3),(12,6,10),(11,6,11),(14,6,12),(15,7,1),(16,7,14),(17,8,11),(18,8,13),(19,9,10),(20,9,12),(21,10,8),(22,10,18),(26,11,5),(23,11,10),(24,11,11),(25,11,12),(27,12,14),(28,12,15),(30,13,10),(32,13,12),(29,13,16),(31,13,18),(33,14,10),(34,14,14),(35,15,10),(36,15,14),(37,16,10),(38,16,14);
/*!40000 ALTER TABLE `books_book_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_category`
--

DROP TABLE IF EXISTS `books_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_category`
--

LOCK TABLES `books_category` WRITE;
/*!40000 ALTER TABLE `books_category` DISABLE KEYS */;
INSERT INTO `books_category` VALUES (1,'Trinh thám',''),(2,'Cổ tích',''),(3,'Kinh dị',''),(4,'Lịch sử',''),(5,'Chiến tranh',''),(6,'Khoa học thường thức',''),(7,'Công nghệ',''),(8,'Sức khỏe',''),(9,'Ẩm thực',''),(10,'Phiêu lưu',''),(11,'Tiểu thuyết',''),(12,'Văn học kinh điển',''),(13,'Truyện ngắn',''),(14,'Truyện tranh',''),(15,'Tình yêu',''),(16,'Bi kịch',''),(17,'Hài kịch',''),(18,'Phát triển bản thân','');
/*!40000 ALTER TABLE `books_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart_bookincart`
--

DROP TABLE IF EXISTS `cart_bookincart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart_bookincart` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `book_id` bigint NOT NULL,
  `cart_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cart_bookincart_book_id_94328a5d_fk_books_book_id` (`book_id`),
  KEY `cart_bookincart_cart_id_df61f57d_fk_cart_cart_id` (`cart_id`),
  CONSTRAINT `cart_bookincart_book_id_94328a5d_fk_books_book_id` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`id`),
  CONSTRAINT `cart_bookincart_cart_id_df61f57d_fk_cart_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `cart_cart` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart_bookincart`
--

LOCK TABLES `cart_bookincart` WRITE;
/*!40000 ALTER TABLE `cart_bookincart` DISABLE KEYS */;
INSERT INTO `cart_bookincart` VALUES (1,4,1,1),(2,1,2,1),(3,1,3,1),(4,1,5,1);
/*!40000 ALTER TABLE `cart_bookincart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart_cart`
--

DROP TABLE IF EXISTS `cart_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart_cart` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cart_cart_customer_id_bbe4c408_fk_accounts_user_id` (`customer_id`),
  CONSTRAINT `cart_cart_customer_id_bbe4c408_fk_accounts_user_id` FOREIGN KEY (`customer_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart_cart`
--

LOCK TABLES `cart_cart` WRITE;
/*!40000 ALTER TABLE `cart_cart` DISABLE KEYS */;
INSERT INTO `cart_cart` VALUES (1,2);
/*!40000 ALTER TABLE `cart_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coupons_coupon`
--

DROP TABLE IF EXISTS `coupons_coupon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coupons_coupon` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(20) NOT NULL,
  `discount` decimal(10,2) NOT NULL,
  `type` varchar(20) NOT NULL,
  `usage_limit` int NOT NULL,
  `is_expired` tinyint(1) NOT NULL,
  `min_order_value` decimal(10,2) NOT NULL,
  `usage_type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coupons_coupon`
--

LOCK TABLES `coupons_coupon` WRITE;
/*!40000 ALTER TABLE `coupons_coupon` DISABLE KEYS */;
INSERT INTO `coupons_coupon` VALUES (1,'NY2024',10.00,'PERCENTAGE',100,0,10.00,'ORDER'),(2,'SUMMER2024',15.00,'PERCENTAGE',500,0,20.00,'ORDER');
/*!40000 ALTER TABLE `coupons_coupon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-05-07 15:27:07.481147','1','Trinh thám',1,'[{\"added\": {}}]',8,3),(2,'2024-05-07 15:27:13.370434','1','Trinh thám',2,'[]',8,3),(3,'2024-05-07 15:27:25.500653','2','Cổ tích',1,'[{\"added\": {}}]',8,3),(4,'2024-05-07 15:27:33.704031','3','Kinh dị',1,'[{\"added\": {}}]',8,3),(5,'2024-05-07 15:27:41.071754','4','Lịch sử',1,'[{\"added\": {}}]',8,3),(6,'2024-05-07 15:27:49.653327','5','Chiến tranh',1,'[{\"added\": {}}]',8,3),(7,'2024-05-07 15:28:21.479361','6','Khoa học thường thức',1,'[{\"added\": {}}]',8,3),(8,'2024-05-07 15:28:29.377306','7','Công nghệ',1,'[{\"added\": {}}]',8,3),(9,'2024-05-07 15:28:38.465031','8','Sức khỏe',1,'[{\"added\": {}}]',8,3),(10,'2024-05-07 15:28:49.807834','9','Ẩm thực',1,'[{\"added\": {}}]',8,3),(11,'2024-05-07 15:29:43.617558','10','Phiêu lưu',1,'[{\"added\": {}}]',8,3),(12,'2024-05-07 15:29:50.226378','11','Tiểu thuyết',1,'[{\"added\": {}}]',8,3),(13,'2024-05-07 15:30:01.404846','12','Văn học kinh điển',1,'[{\"added\": {}}]',8,3),(14,'2024-05-07 15:34:24.425470','1','Coraline',1,'[{\"added\": {}}]',7,3),(15,'2024-05-07 15:34:46.324137','1','Coraline',2,'[{\"changed\": {\"fields\": [\"Tags\"]}}]',7,3),(16,'2024-05-07 15:36:13.617752','2','Sapiens - Lược sử loài người',1,'[{\"added\": {}}]',7,3),(17,'2024-05-10 07:32:48.712703','1','Coupon object (1)',1,'[{\"added\": {}}]',12,3),(18,'2024-05-10 07:33:16.830910','2','Coupon object (2)',1,'[{\"added\": {}}]',12,3),(19,'2024-05-10 07:35:27.477836','1','Giao hàng nhanh',1,'[{\"added\": {}}]',16,3),(20,'2024-05-10 07:35:34.334219','2','Giao hàng tiết kiệm',1,'[{\"added\": {}}]',16,3),(21,'2024-05-10 14:58:32.845684','13','Truyện ngắn',1,'[{\"added\": {}}]',8,3),(22,'2024-05-10 14:58:36.446273','14','Truyện tranh',1,'[{\"added\": {}}]',8,3),(23,'2024-05-10 14:59:33.535989','3','O. Henry - Truyện ngắn chọn lọc',1,'[{\"added\": {}}]',7,3),(24,'2024-05-10 15:01:41.077994','4','Công chúa nhỏ',1,'[{\"added\": {}}]',7,3),(25,'2024-05-10 15:02:51.216250','5','Trăm năm cô đơn',1,'[{\"added\": {}}]',7,3),(26,'2024-05-10 15:03:43.094311','6','Đồi gió hú',1,'[{\"added\": {}}]',7,3),(27,'2024-05-11 01:50:35.871953','7','Conan tập 90',1,'[{\"added\": {}}]',7,3),(28,'2024-05-11 05:36:02.871346','1','Coraline',2,'[{\"changed\": {\"fields\": [\"Cover\"]}}]',7,3),(29,'2024-05-11 05:37:03.078015','2','Sapiens - Lược sử loài người',2,'[{\"changed\": {\"fields\": [\"Cover\"]}}]',7,3),(30,'2024-05-11 05:49:14.153270','1','Coraline',2,'[{\"changed\": {\"fields\": [\"Cover\"]}}]',7,3),(31,'2024-05-11 07:27:32.761200','1','Coraline',2,'[{\"changed\": {\"fields\": [\"Cover\"]}}]',7,3),(32,'2024-05-11 07:28:57.907441','1','Coraline',2,'[{\"changed\": {\"fields\": [\"Cover\"]}}]',7,3),(33,'2024-05-11 07:35:22.006033','2','Sapiens - Lược sử loài người',2,'[{\"changed\": {\"fields\": [\"Cover\"]}}]',7,3),(34,'2024-05-11 07:37:16.435664','3','Chiếc lá cuối cùng',2,'[{\"changed\": {\"fields\": [\"Title\"]}}]',7,3),(35,'2024-05-11 07:37:45.880852','3','Chiếc lá cuối cùng',2,'[{\"changed\": {\"fields\": [\"Cover\"]}}]',7,3),(36,'2024-05-11 07:56:56.865929','8','Cây cam ngọt của tôi',1,'[{\"added\": {}}]',7,3),(37,'2024-05-11 07:57:05.722522','15','Tình yêu',1,'[{\"added\": {}}]',8,3),(38,'2024-05-11 07:57:18.772503','16','Bi kịch',1,'[{\"added\": {}}]',8,3),(39,'2024-05-11 07:57:22.924828','17','Hài kịch',1,'[{\"added\": {}}]',8,3),(40,'2024-05-11 07:58:50.092528','9','Nhà giả kim',1,'[{\"added\": {}}]',7,3),(41,'2024-05-11 07:58:59.811480','18','Phát triển bản thân',1,'[{\"added\": {}}]',8,3),(42,'2024-05-11 08:00:18.586788','10','Biến thể của cô đơn',1,'[{\"added\": {}}]',7,3),(43,'2024-05-11 08:01:22.167946','11','Lũ trẻ đường tàu',1,'[{\"added\": {}}]',7,3),(44,'2024-05-11 08:02:29.873733','12','Người bà tài giỏi vùng Saga',1,'[{\"added\": {}}]',7,3),(45,'2024-05-11 08:03:28.071548','13','Nỗi buồn chiến tranh',1,'[{\"added\": {}}]',7,3),(46,'2024-05-11 08:04:37.031703','14','One piece - Tập 102',1,'[{\"added\": {}}]',7,3),(47,'2024-05-11 08:05:01.171433','15','One piece - Tập 101',1,'[{\"added\": {}}]',7,3),(48,'2024-05-11 08:05:15.645274','16','One piece - Tập 100',1,'[{\"added\": {}}]',7,3),(49,'2024-05-11 08:06:04.479631','8','Cây cam ngọt của tôi',2,'[{\"changed\": {\"fields\": [\"Cover\"]}}]',7,3);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (6,'accounts','address'),(5,'accounts','user'),(15,'admin','logentry'),(2,'auth','group'),(1,'auth','permission'),(7,'books','book'),(8,'books','category'),(14,'cart','bookincart'),(13,'cart','cart'),(3,'contenttypes','contenttype'),(12,'coupons','coupon'),(11,'orders','bookinorder'),(10,'orders','deliveryinformation'),(9,'orders','order'),(16,'orders','shipping'),(4,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'accounts','0001_initial','2024-05-07 14:40:50.068866'),(2,'contenttypes','0001_initial','2024-05-07 14:40:50.128387'),(3,'contenttypes','0002_remove_content_type_name','2024-05-07 14:40:50.192414'),(4,'auth','0001_initial','2024-05-07 14:40:50.436245'),(5,'auth','0002_alter_permission_name_max_length','2024-05-07 14:40:50.485442'),(6,'auth','0003_alter_user_email_max_length','2024-05-07 14:40:50.494444'),(7,'auth','0004_alter_user_username_opts','2024-05-07 14:40:50.502956'),(8,'auth','0005_alter_user_last_login_null','2024-05-07 14:40:50.510958'),(9,'auth','0006_require_contenttypes_0002','2024-05-07 14:40:50.512955'),(10,'auth','0007_alter_validators_add_error_messages','2024-05-07 14:40:50.518961'),(11,'auth','0008_alter_user_username_max_length','2024-05-07 14:40:50.527957'),(12,'auth','0009_alter_user_last_name_max_length','2024-05-07 14:40:50.535962'),(13,'auth','0010_alter_group_name_max_length','2024-05-07 14:40:50.567957'),(14,'auth','0011_update_proxy_permissions','2024-05-07 14:40:50.578955'),(15,'auth','0012_alter_user_first_name_max_length','2024-05-07 14:40:50.599475'),(16,'books','0001_initial','2024-05-07 14:40:50.906474'),(17,'coupons','0001_initial','2024-05-07 14:40:50.942219'),(18,'orders','0001_initial','2024-05-07 14:40:51.328296'),(19,'sessions','0001_initial','2024-05-07 14:40:51.367295'),(20,'books','0002_remove_category_books','2024-05-07 14:45:01.299774'),(21,'cart','0001_initial','2024-05-07 14:53:20.308463'),(22,'admin','0001_initial','2024-05-07 15:25:12.319734'),(23,'admin','0002_logentry_remove_auto_add','2024-05-07 15:25:12.327773'),(24,'admin','0003_logentry_add_action_flag_choices','2024-05-07 15:25:12.345769'),(25,'books','0003_alter_category_options_alter_category_description','2024-05-07 15:26:58.534744'),(26,'coupons','0002_alter_coupon_type','2024-05-09 15:48:58.522767'),(27,'orders','0002_alter_deliveryinformation_start_delivery_date_and_more','2024-05-09 15:48:58.942736'),(28,'coupons','0003_coupon_usage_type','2024-05-09 23:37:58.841247'),(29,'orders','0003_shipping_alter_deliveryinformation_shipping_company','2024-05-09 23:37:59.085923'),(30,'accounts','0002_address_commune','2024-05-10 07:59:00.110151'),(31,'orders','0004_alter_shipping_options','2024-05-10 07:59:00.114150'),(32,'coupons','0004_rename_minimum_order_value_coupon_min_order_value','2024-05-10 10:28:33.816794'),(33,'orders','0005_alter_order_coupon','2024-05-10 10:28:33.828798'),(34,'orders','0006_alter_order_coupon','2024-05-10 14:29:50.916304'),(35,'books','0004_book_cover','2024-05-11 05:33:54.194485');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('jcy4a3vc7ws77dm1lzleiyzjiultkod0','.eJxVjEEOwiAQRe_C2hDKlAAu3XsGMsMwUjU0Ke3KeHdt0oVu_3vvv1TCba1p62VJE6uzsur0uxHmR2k74Du226zz3NZlIr0r-qBdX2cuz8vh_h1U7PVbZ4xkLTtvJGTITsQERioeyI_ZYAkiAdBEHBkQkMgJEA5MFGMconp_ABc-OUo:1s5yZf:Jy3jWPbdXcYrtu_xm46GKAkqQcQW41PVlohxkGFZGJI','2024-05-26 02:04:27.124090'),('witc4jffg7lcsxwh4hck9eg1mg01i1gq','.eJxVjDsOwyAQBe9CHaGFXQykTO8zIL7BSYQlY1dR7h5bcpG0b2bemzm_rdVtPS9uSuzKkF1-t-DjM7cDpIdv95nHua3LFPih8JN2Ps4pv26n-3dQfa97nY0HLZQWkoqWVg8gItrgZSoSldIEBixFbWmAsrtkJaChoEAgWSzs8wWifjXG:1s5brn:XaDhb9tMNmKhkbmAp_V-_6kGsUIm4rK7EoOQh2RJdfg','2024-05-25 01:49:39.470250');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_bookinorder`
--

DROP TABLE IF EXISTS `orders_bookinorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_bookinorder` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `book_id` bigint NOT NULL,
  `order_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_bookinorder_book_id_18c40669_fk_books_book_id` (`book_id`),
  KEY `orders_bookinorder_order_id_78597e29_fk_orders_order_id` (`order_id`),
  CONSTRAINT `orders_bookinorder_book_id_18c40669_fk_books_book_id` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`id`),
  CONSTRAINT `orders_bookinorder_order_id_78597e29_fk_orders_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders_order` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_bookinorder`
--

LOCK TABLES `orders_bookinorder` WRITE;
/*!40000 ALTER TABLE `orders_bookinorder` DISABLE KEYS */;
INSERT INTO `orders_bookinorder` VALUES (11,3,1,6),(12,1,2,6),(13,4,1,7),(14,1,2,7),(15,3,1,8),(16,1,2,8),(17,1,5,8);
/*!40000 ALTER TABLE `orders_bookinorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_deliveryinformation`
--

DROP TABLE IF EXISTS `orders_deliveryinformation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_deliveryinformation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `shipping_company_id` bigint NOT NULL,
  `start_delivery_date` datetime(6) NOT NULL,
  `finish_delivery_date` datetime(6) DEFAULT NULL,
  `delivery_fee` decimal(10,2) NOT NULL,
  `address_id` bigint DEFAULT NULL,
  `order_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_id` (`order_id`),
  KEY `orders_deliveryinfor_address_id_3569a3b7_fk_accounts_` (`address_id`),
  KEY `orders_deliveryinformation_shipping_company_id_b8d629d8` (`shipping_company_id`),
  CONSTRAINT `orders_deliveryinfor_address_id_3569a3b7_fk_accounts_` FOREIGN KEY (`address_id`) REFERENCES `accounts_address` (`id`),
  CONSTRAINT `orders_deliveryinfor_shipping_company_id_b8d629d8_fk_orders_sh` FOREIGN KEY (`shipping_company_id`) REFERENCES `orders_shipping` (`id`),
  CONSTRAINT `orders_deliveryinformation_order_id_3f63cf3b_fk_orders_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders_order` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_deliveryinformation`
--

LOCK TABLES `orders_deliveryinformation` WRITE;
/*!40000 ALTER TABLE `orders_deliveryinformation` DISABLE KEYS */;
INSERT INTO `orders_deliveryinformation` VALUES (6,1,'2024-05-10 08:18:26.552144',NULL,30000.00,2,6),(7,1,'2024-05-12 02:01:58.711161',NULL,30000.00,2,7),(8,1,'2024-05-12 02:04:27.109105',NULL,30000.00,2,8);
/*!40000 ALTER TABLE `orders_deliveryinformation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_order`
--

DROP TABLE IF EXISTS `orders_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `total` decimal(10,2) NOT NULL,
  `date_ordered` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `customer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `orders_order_customer_id_0b76f6a4_fk_accounts_user_id` (`customer_id`),
  CONSTRAINT `orders_order_customer_id_0b76f6a4_fk_accounts_user_id` FOREIGN KEY (`customer_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_order`
--

LOCK TABLES `orders_order` WRITE;
/*!40000 ALTER TABLE `orders_order` DISABLE KEYS */;
INSERT INTO `orders_order` VALUES (6,533000.00,'2024-05-10 08:18:26.541119',0,2),(7,571000.00,'2024-05-12 02:01:58.701121',0,2),(8,601200.00,'2024-05-12 02:04:27.097561',0,2);
/*!40000 ALTER TABLE `orders_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_order_coupon`
--

DROP TABLE IF EXISTS `orders_order_coupon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_order_coupon` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `order_id` bigint NOT NULL,
  `coupon_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `orders_order_coupon_order_id_coupon_id_5fab1d57_uniq` (`order_id`,`coupon_id`),
  KEY `orders_order_coupon_coupon_id_521edee3_fk_coupons_coupon_id` (`coupon_id`),
  CONSTRAINT `orders_order_coupon_coupon_id_521edee3_fk_coupons_coupon_id` FOREIGN KEY (`coupon_id`) REFERENCES `coupons_coupon` (`id`),
  CONSTRAINT `orders_order_coupon_order_id_5e37b5bd_fk_orders_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders_order` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_order_coupon`
--

LOCK TABLES `orders_order_coupon` WRITE;
/*!40000 ALTER TABLE `orders_order_coupon` DISABLE KEYS */;
INSERT INTO `orders_order_coupon` VALUES (1,7,1),(2,8,2);
/*!40000 ALTER TABLE `orders_order_coupon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_shipping`
--

DROP TABLE IF EXISTS `orders_shipping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_shipping` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `shipping_company_name` varchar(255) NOT NULL,
  `shipping_fee` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_shipping`
--

LOCK TABLES `orders_shipping` WRITE;
/*!40000 ALTER TABLE `orders_shipping` DISABLE KEYS */;
INSERT INTO `orders_shipping` VALUES (1,'Giao hàng nhanh',30000.00),(2,'Giao hàng tiết kiệm',25000.00);
/*!40000 ALTER TABLE `orders_shipping` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-12  9:19:38
