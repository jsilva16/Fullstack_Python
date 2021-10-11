-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: friends
-- ------------------------------------------------------
-- Server version	5.7.19

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
-- Table structure for table `friendships`
--

DROP TABLE IF EXISTS `friendships`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `friendships` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `friend_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id_idx` (`user_id`),
  KEY `friend_id_idx` (`friend_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `friendships`
--

LOCK TABLES `friendships` WRITE;
/*!40000 ALTER TABLE `friendships` DISABLE KEYS */;
INSERT INTO `friendships` VALUES (1,1,2,'2019-02-08 11:13:27',NULL),(2,1,3,'2019-02-08 11:14:03',NULL),(3,1,4,'2019-02-08 11:14:38',NULL),(4,2,4,'2019-02-08 11:15:11',NULL),(5,2,5,'2019-02-08 11:15:23',NULL),(6,5,3,'2019-02-08 11:16:02',NULL);
/*!40000 ALTER TABLE `friendships` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Amy','Giver','2019-02-08 11:12:11',NULL),(2,'Eli','Byers','2019-02-08 11:12:11',NULL),(3,'Big','Bird','2019-02-08 11:12:11',NULL),(4,'Kermit','The Frog','2019-02-08 11:12:11',NULL),(5,'Marky','Mark','2019-02-08 11:12:11',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-08 11:20:17


SELECT a.id, a.first_name, a.last_name, b.id, b.first_name, b.last_name
FROM users a
LEFT JOIN friendships ON a.id=friendships.user_id 
LEFT JOIN users b ON b.id = friendships.friend_id
WHERE b.id IS NOT NULL;

-- Devuelva a todos los usuarios que son amigos de Kermit, asegúrese de que sus nombres se muestren en los resultados.--
SELECT a.id, a.first_name, a.last_name, b.id, b.first_name, b.last_name
FROM users a
LEFT JOIN friendships ON a.id=friendships.user_id 
LEFT JOIN users b ON b.id = friendships.friend_id
WHERE b.id = 4 ;

-- Devuelve el recuento de todas las amistades.
SELECT a.id, CONCAT(a.first_name, ' ', a.last_name) as friend, count(a.id)
FROM users a
LEFT JOIN friendships ON a.id=friendships.user_id 
LEFT JOIN users b ON b.id = friendships.friend_id
WHERE b.id IS NOT NULL
GROUP BY a.id;

-- Descubre quién tiene más amigos y devuelve el recuento de sus amigos.
SELECT a.id, CONCAT(a.first_name, ' ', a.last_name) , count(a.id) as friendcount
FROM users a
LEFT JOIN friendships c ON a.id=c.user_id 
LEFT JOIN users b ON b.id = c.friend_id
WHERE b.id IS NOT NULL AND count(a.id)= max(count(a.id))
GROUP BY a.id;

-- Crea un nuevo usuario y hazlos amigos de Eli Byers, Kermit The Frog y Marky Mark.
INSERT INTO users(first_name, last_name)
VALUES ('NAME1', 'LASTNAME1');

INSERT INTO friendships(user_id, friend_id)
VALUES ('6', '2'), ('6', '4'), ('6', '5');

-- Devuelve a los amigos de Eli en orden alfabético.
SELECT CONCAT(b.first_name, ' ', b.last_name) as friend
FROM users a
LEFT JOIN friendships ON a.id=friendships.user_id 
LEFT JOIN users b ON b.id = friendships.friend_id
WHERE a.id=2
ORDER BY (b.first_name);

-- Eliminar a Marky Mark de los amigos de Eli.
DELETE FROM friendships 
WHERE id= 5;

-- Devuelve todas las amistades, mostrando solo el nombre y apellido de ambos amigos
SELECT CONCAT(a.first_name, ' ', a.last_name) as user, CONCAT(b.first_name, ' ', b.last_name) as friend
FROM users a
LEFT JOIN friendships ON a.id=friendships.user_id 
LEFT JOIN users b ON b.id = friendships.friend_id
WHERE b.id IS NOT NULL
ORDER BY (a.first_name);



SELECT * FROM friendships;
SELECT * FROM users
