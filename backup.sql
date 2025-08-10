-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         11.3.2-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando estructura para tabla control_escolar.administradores
CREATE TABLE IF NOT EXISTS `administradores` (
  `id_admin` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(128) NOT NULL,
  `paterno` varchar(128) NOT NULL,
  `materno` varchar(128) NOT NULL,
  `username` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `status` int(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id_admin`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla control_escolar.administradores: ~4 rows (aproximadamente)
DELETE FROM `administradores`;
INSERT INTO `administradores` (`id_admin`, `nombre`, `paterno`, `materno`, `username`, `password`, `status`) VALUES
	(1, 'Gael Emiliano', 'Anaya', 'Garcia', 'ZGrupo115@admin.com', 'bas019efE%', 1),
	(2, 'Jair Antonio', 'Anaya', 'Garcia', 'Jairsupremo90@admin.com', 'hsBW6erDY@', 1),
	(3, 'Jorge', 'Anaya', 'Garcia', 'Billyork69@admin.com', 'LosAngeles87!', 1),
	(4, 'Oscar Julio', 'Alferez', 'Orozco', 'ZGrupo935@admin.com', 'qw123df4wQ$', 1);

-- Volcando estructura para tabla control_escolar.alumnos
CREATE TABLE IF NOT EXISTS `alumnos` (
  `id_alumno` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(128) NOT NULL,
  `paterno` varchar(128) NOT NULL,
  `materno` varchar(128) NOT NULL,
  `nacimiento` date NOT NULL,
  `username` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `id_carrera` int(11) NOT NULL,
  `id_grupo` int(11) NOT NULL,
  `status` int(1) NOT NULL DEFAULT 1,
  `prerregistro` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id_alumno`),
  KEY `id_carrera` (`id_carrera`),
  CONSTRAINT `id_carrera` FOREIGN KEY (`id_carrera`) REFERENCES `carreras` (`id_carrera`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla control_escolar.alumnos: ~22 rows (aproximadamente)
DELETE FROM `alumnos`;
INSERT INTO `alumnos` (`id_alumno`, `nombre`, `paterno`, `materno`, `nacimiento`, `username`, `password`, `id_carrera`, `id_grupo`, `status`, `prerregistro`) VALUES
	(1, 'Santino', 'Barocio', 'Orozco', '2001-11-15', 'santino.alexandro@alumnos.com', 'GF$%fg3d4fd$F#', 2, 0, 1, 0),
	(2, 'Gael Emiliano', 'Anaya', 'Garcia', '2003-05-19', 'gael.anaya@alumnos.com', 'bas019efE7$', 1, 0, 1, 1),
	(3, 'Juan', 'García', 'López', '2005-05-10', 'juang@alumnos.com', 'password123', 1, 0, 1, 1),
	(4, 'María', 'Martínez', 'Rodríguez', '2006-02-15', 'mariam@alumnos.com', 'password456', 1, 2, 1, 1),
	(5, 'Carlos', 'Hernández', 'Pérez', '2004-08-20', 'carlosh@alumnos.com', 'password789', 1, 2, 1, 1),
	(6, 'Laura', 'González', 'Sánchez', '2007-11-25', 'laurag@alumnos.com', 'passwordabc', 1, 1, 1, 1),
	(7, 'Pedro', 'Díaz', 'Martínez', '2003-04-30', 'pedrod@alumnos.com', 'passworddef', 1, 2, 1, 1),
	(8, 'Ana', 'Pérez', 'Gómez', '2006-07-18', 'anap@alumnos.com', 'passwordghi', 1, 1, 1, 1),
	(9, 'David', 'Rodríguez', 'López', '2004-10-05', 'davidd@alumnos.com', 'passwordjkl', 1, 0, 1, 1),
	(10, 'Marta', 'Sánchez', 'Martínez', '2005-12-12', 'martas@alumnos.com', 'passwordmno', 1, 2, 1, 1),
	(11, 'Sergio', 'Gómez', 'Ruiz', '2003-09-08', 'sergiog@alumnos.com', 'passwordpqr', 1, 2, 1, 1),
	(12, 'Elena', 'López', 'Hernández', '2007-01-20', 'elenal@alumnos.com', 'passwordstu', 1, 0, 1, 1),
	(13, 'Pablo', 'Martínez', 'García', '2006-08-07', 'pablom@alumnos.com', 'passwordvwx', 1, 0, 1, 1),
	(14, 'Julia', 'Fernández', 'Pérez', '2004-03-15', 'juliaf@alumnos.com', 'passwordyz', 1, 0, 1, 1),
	(15, 'Andrés', 'Ruiz', 'García', '2005-06-22', 'andresr@alumnos.com', 'password1234', 1, 1, 1, 1),
	(16, 'Beatriz', 'López', 'Pérez', '2003-11-28', 'beatrizl@alumnos.com', 'password5678', 1, 1, 1, 1),
	(17, 'Francisco', 'García', 'Martínez', '2006-04-03', 'franciscog@alumnos.com', 'password9012', 1, 1, 1, 1),
	(18, 'Cristina', 'Martínez', 'Sánchez', '2004-09-17', 'cristinam@alumnos.com', 'password3456', 1, 1, 1, 1),
	(19, 'Diego', 'Pérez', 'Gómez', '2007-02-24', 'diegop@alumnos.com', 'password7890', 1, 1, 1, 1),
	(20, 'Ana María', 'Rodríguez', 'Pérez', '2005-10-11', 'anamariar@alumnos.com', 'password12345', 1, 2, 1, 1),
	(21, 'José Luis', 'Gómez', 'Martínez', '2003-05-19', 'joseluisg@alumnos.com', 'password67890', 1, 1, 1, 1),
	(22, 'Laura', 'Pérez', 'Martínez', '2006-08-30', 'laurap@alumnos.com', 'passwordabcd', 1, 1, 1, 1);

-- Volcando estructura para tabla control_escolar.alumnos_grupo
CREATE TABLE IF NOT EXISTS `alumnos_grupo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_grupo` int(11) NOT NULL,
  `id_alumno` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_alumno` (`id_alumno`),
  KEY `id_grupo` (`id_grupo`),
  CONSTRAINT `alumnos_grupo_ibfk_1` FOREIGN KEY (`id_alumno`) REFERENCES `alumnos` (`id_alumno`),
  CONSTRAINT `alumnos_grupo_ibfk_2` FOREIGN KEY (`id_grupo`) REFERENCES `grupos` (`id_grupo`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla control_escolar.alumnos_grupo: ~15 rows (aproximadamente)
DELETE FROM `alumnos_grupo`;
INSERT INTO `alumnos_grupo` (`id`, `id_grupo`, `id_alumno`) VALUES
	(1, 1, 22),
	(2, 1, 6),
	(3, 1, 19),
	(4, 1, 8),
	(5, 1, 18),
	(6, 1, 16),
	(7, 1, 21),
	(8, 1, 17),
	(9, 1, 15),
	(10, 2, 10),
	(11, 2, 5),
	(12, 2, 7),
	(13, 2, 11),
	(14, 2, 4),
	(15, 2, 20);

-- Volcando estructura para tabla control_escolar.carreras
CREATE TABLE IF NOT EXISTS `carreras` (
  `id_carrera` int(11) NOT NULL AUTO_INCREMENT,
  `clave` varchar(128) NOT NULL,
  `carrera` varchar(128) NOT NULL,
  `semestres` varchar(128) NOT NULL,
  PRIMARY KEY (`id_carrera`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla control_escolar.carreras: ~7 rows (aproximadamente)
DELETE FROM `carreras`;
INSERT INTO `carreras` (`id_carrera`, `clave`, `carrera`, `semestres`) VALUES
	(1, 'ICOM', 'Ingeniería en Computación', '9'),
	(2, 'INNI', 'Ingeniería en Informática', '7'),
	(3, 'LIME', 'Licenciatura en Mercadotecnia', '8'),
	(4, 'INFI', 'Licenciatura en Fisica', '6'),
	(6, 'LICI', 'Ingeniería Civil', '6'),
	(7, 'QFB', 'Licenciatura en Químico Farmacéutico Biólogo', '9'),
	(8, 'LKC', 'Licenciatura en Química', '6');

-- Volcando estructura para tabla control_escolar.edificio
CREATE TABLE IF NOT EXISTS `edificio` (
  `id_edificio` int(11) NOT NULL AUTO_INCREMENT,
  `edificio` varchar(128) NOT NULL,
  PRIMARY KEY (`id_edificio`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla control_escolar.edificio: ~7 rows (aproximadamente)
DELETE FROM `edificio`;
INSERT INTO `edificio` (`id_edificio`, `edificio`) VALUES
	(1, 'A'),
	(2, 'B'),
	(3, 'C'),
	(4, 'D'),
	(5, 'E'),
	(6, 'F'),
	(7, 'G');

-- Volcando estructura para tabla control_escolar.grupos
CREATE TABLE IF NOT EXISTS `grupos` (
  `id_grupo` int(11) NOT NULL AUTO_INCREMENT,
  `id_carrera` int(11) NOT NULL,
  `grupo` varchar(128) NOT NULL,
  `semestre` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `cupo` int(11) NOT NULL,
  `cupos_disponibles` int(11) NOT NULL,
  PRIMARY KEY (`id_grupo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla control_escolar.grupos: ~2 rows (aproximadamente)
DELETE FROM `grupos`;
INSERT INTO `grupos` (`id_grupo`, `id_carrera`, `grupo`, `semestre`, `fecha`, `cupo`, `cupos_disponibles`) VALUES
	(1, 1, 'A01', 1, '2024-04-22', 10, 1),
	(2, 1, 'A02', 1, '2024-04-23', 10, 4);

-- Volcando estructura para tabla control_escolar.horarios
CREATE TABLE IF NOT EXISTS `horarios` (
  `id_horario` int(11) NOT NULL AUTO_INCREMENT,
  `id_carrera` int(11) NOT NULL,
  `id_materia` int(11) NOT NULL,
  `id_maestro` int(11) NOT NULL,
  `id_salon` int(11) NOT NULL,
  `L` int(1) NOT NULL DEFAULT 0,
  `M` int(1) NOT NULL DEFAULT 0,
  `I` int(1) NOT NULL DEFAULT 0,
  `J` int(1) NOT NULL DEFAULT 0,
  `V` int(1) NOT NULL DEFAULT 0,
  `S` int(1) NOT NULL DEFAULT 0,
  `horas` varchar(128) NOT NULL,
  `disponibilidad` int(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id_horario`),
  KEY `id_carrera` (`id_carrera`),
  KEY `id_maestro` (`id_maestro`),
  KEY `id_salon` (`id_salon`),
  KEY `horarios_ibfk_2` (`id_materia`),
  CONSTRAINT `horarios_ibfk_1` FOREIGN KEY (`id_carrera`) REFERENCES `carreras` (`id_carrera`),
  CONSTRAINT `horarios_ibfk_2` FOREIGN KEY (`id_materia`) REFERENCES `materias` (`id_materia`),
  CONSTRAINT `horarios_ibfk_3` FOREIGN KEY (`id_maestro`) REFERENCES `maestros` (`id_maestro`),
  CONSTRAINT `horarios_ibfk_4` FOREIGN KEY (`id_salon`) REFERENCES `salones` (`id_salon`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla control_escolar.horarios: ~18 rows (aproximadamente)
DELETE FROM `horarios`;
INSERT INTO `horarios` (`id_horario`, `id_carrera`, `id_materia`, `id_maestro`, `id_salon`, `L`, `M`, `I`, `J`, `V`, `S`, `horas`, `disponibilidad`) VALUES
	(1, 1, 5, 2, 6, 0, 1, 0, 1, 0, 1, '9:00 - 10:55', 0),
	(2, 1, 5, 3, 2, 0, 1, 0, 1, 0, 0, '7:00 - 8:55', 0),
	(3, 1, 4, 3, 4, 0, 1, 0, 1, 0, 0, '11:00 - 12:55', 0),
	(4, 6, 3, 1, 4, 1, 0, 1, 0, 1, 0, '7:00 - 8:55', 1),
	(5, 4, 7, 1, 6, 0, 1, 0, 1, 0, 0, '7:00 - 8:55', 1),
	(6, 1, 12, 4, 5, 1, 0, 1, 0, 0, 0, '7:00 - 8:55', 0),
	(7, 1, 7, 5, 3, 1, 0, 1, 0, 0, 0, '11:00 - 12:55', 0),
	(8, 1, 7, 6, 1, 0, 1, 0, 1, 0, 0, '9:00 - 10:55', 0),
	(9, 1, 12, 4, 4, 1, 0, 0, 0, 0, 0, '11:00 - 12:55', 1),
	(10, 1, 6, 3, 5, 1, 0, 1, 0, 0, 0, '11:00 - 12:55', 0),
	(11, 1, 9, 7, 4, 0, 0, 0, 0, 1, 0, '11:00 - 12:55', 0),
	(12, 1, 7, 8, 5, 0, 0, 0, 0, 0, 1, '9:00 - 10:55', 1),
	(13, 1, 6, 8, 5, 0, 0, 0, 0, 1, 0, '9:00 - 10:55', 0),
	(14, 1, 8, 6, 3, 0, 0, 1, 0, 1, 0, '7:00 - 8:55', 0),
	(15, 1, 8, 6, 3, 0, 0, 1, 0, 1, 0, '9:00 - 10:55', 0),
	(16, 1, 10, 7, 4, 0, 0, 0, 0, 0, 1, '9:00 - 10:55', 0),
	(17, 1, 3, 5, 4, 0, 0, 0, 0, 0, 1, '11:00 - 12:55', 0),
	(18, 1, 7, 5, 5, 0, 1, 0, 1, 0, 0, '11:00 - 12:55', 1);

-- Volcando estructura para tabla control_escolar.horarios_grupo
CREATE TABLE IF NOT EXISTS `horarios_grupo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_grupo` int(11) NOT NULL,
  `id_horario` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_grupo` (`id_grupo`),
  KEY `id_horario` (`id_horario`),
  CONSTRAINT `horarios_grupo_ibfk_1` FOREIGN KEY (`id_grupo`) REFERENCES `grupos` (`id_grupo`),
  CONSTRAINT `horarios_grupo_ibfk_2` FOREIGN KEY (`id_horario`) REFERENCES `horarios` (`id_horario`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla control_escolar.horarios_grupo: ~13 rows (aproximadamente)
DELETE FROM `horarios_grupo`;
INSERT INTO `horarios_grupo` (`id`, `id_grupo`, `id_horario`) VALUES
	(1, 1, 1),
	(2, 1, 14),
	(3, 1, 7),
	(4, 1, 11),
	(5, 1, 13),
	(6, 1, 3),
	(7, 1, 17),
	(8, 2, 2),
	(9, 2, 10),
	(10, 2, 6),
	(11, 2, 16),
	(12, 2, 8),
	(13, 2, 15);

-- Volcando estructura para tabla control_escolar.maestros
CREATE TABLE IF NOT EXISTS `maestros` (
  `id_maestro` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(128) NOT NULL,
  `paterno` varchar(128) NOT NULL,
  `materno` varchar(128) NOT NULL,
  `username` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `status` int(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id_maestro`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla control_escolar.maestros: ~23 rows (aproximadamente)
DELETE FROM `maestros`;
INSERT INTO `maestros` (`id_maestro`, `nombre`, `paterno`, `materno`, `username`, `password`, `status`) VALUES
	(1, 'Ramiro', 'Lupercio', 'Coronel', 'lupercio.coronel@academico.com', '$F%#Y56u876', 1),
	(2, 'Gael Emiliano', 'Anaya', 'Garcia', 'gael.anaya@academico.com', 'hsBW6erDY5%', 1),
	(3, 'Levy', 'Navarro', 'Absalon', 'levy.absalon@academico.com', '#$TFD&%yu674uf53y', 1),
	(4, 'Juan', 'López', 'García', 'juanl@academico.com', 'password123', 1),
	(5, 'María', 'Martínez', 'Rodríguez', 'mariamr@academico.com', 'password456', 1),
	(6, 'Carlos', 'Hernández', 'Pérez', 'carloshp@academico.com', 'password789', 1),
	(7, 'Laura', 'González', 'Sánchez', 'laurags@academico.com', 'passwordabc', 1),
	(8, 'Pedro', 'Díaz', 'Martínez', 'pedrod@academico.com', 'passworddef', 1),
	(9, 'Ana', 'Pérez', 'Gómez', 'anap@academico.com', 'passwordghi', 1),
	(10, 'David', 'Rodríguez', 'López', 'davidrl@academico.com', 'passwordjkl', 1),
	(11, 'Marta', 'Sánchez', 'Martínez', 'martasm@academico.com', 'passwordmno', 1),
	(12, 'Sergio', 'Gómez', 'Ruiz', 'sergiogr@academico.com', 'passwordpqr', 1),
	(13, 'Elena', 'López', 'Hernández', 'elenalh@academico.com', 'passwordstu', 1),
	(14, 'Pablo', 'Martínez', 'García', 'pablomg@academico.com', 'passwordvwx', 1),
	(15, 'Julia', 'Fernández', 'Pérez', 'juliafp@academico.com', 'passwordyz', 1),
	(16, 'Andrés', 'Ruiz', 'García', 'andresrg@academico.com', 'password1234', 1),
	(17, 'Beatriz', 'López', 'Pérez', 'beatrizlp@academico.com', 'password5678', 1),
	(18, 'Francisco', 'García', 'Martínez', 'franciscogm@academico.com', 'password9012', 1),
	(19, 'Cristina', 'Martínez', 'Sánchez', 'cristinams@academico.com', 'password3456', 1),
	(20, 'Diego', 'Pérez', 'Gómez', 'diegopg@academico.com', 'password7890', 1),
	(21, 'Ana María', 'Rodríguez', 'Pérez', 'anamariarp@academico.com', 'password12345', 1),
	(22, 'José Luis', 'Gómez', 'Martínez', 'joseluisgm@academico.com', 'password67890', 1),
	(23, 'Laura', 'Pérez', 'Martínez', 'laurapm@academico.com', 'passwordabcd', 1);

-- Volcando estructura para tabla control_escolar.maestro_carreras
CREATE TABLE IF NOT EXISTS `maestro_carreras` (
  `id_maestro_carreras` int(11) NOT NULL AUTO_INCREMENT,
  `id_maestro` int(11) NOT NULL,
  `id_carrera` int(11) NOT NULL,
  PRIMARY KEY (`id_maestro_carreras`),
  KEY `id_maestro` (`id_maestro`),
  KEY `id_carreras` (`id_carrera`),
  CONSTRAINT `maestro_carreras_ibfk_1` FOREIGN KEY (`id_maestro`) REFERENCES `maestros` (`id_maestro`),
  CONSTRAINT `maestro_carreras_ibfk_2` FOREIGN KEY (`id_carrera`) REFERENCES `carreras` (`id_carrera`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla control_escolar.maestro_carreras: ~16 rows (aproximadamente)
DELETE FROM `maestro_carreras`;
INSERT INTO `maestro_carreras` (`id_maestro_carreras`, `id_maestro`, `id_carrera`) VALUES
	(1, 2, 1),
	(2, 2, 2),
	(10, 3, 3),
	(11, 3, 7),
	(12, 3, 1),
	(13, 2, 4),
	(14, 1, 1),
	(15, 1, 2),
	(16, 1, 4),
	(17, 1, 6),
	(18, 4, 1),
	(19, 5, 1),
	(20, 6, 1),
	(21, 6, 4),
	(24, 7, 1),
	(25, 8, 1);

-- Volcando estructura para tabla control_escolar.maestro_materias
CREATE TABLE IF NOT EXISTS `maestro_materias` (
  `id_maestro_materias` int(11) NOT NULL AUTO_INCREMENT,
  `id_maestro` int(11) NOT NULL,
  `id_materia` int(11) NOT NULL,
  PRIMARY KEY (`id_maestro_materias`),
  KEY `id_maestro` (`id_maestro`),
  KEY `id_materia` (`id_materia`),
  CONSTRAINT `maestro_materias_ibfk_1` FOREIGN KEY (`id_maestro`) REFERENCES `maestros` (`id_maestro`),
  CONSTRAINT `maestro_materias_ibfk_2` FOREIGN KEY (`id_materia`) REFERENCES `materias` (`id_materia`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla control_escolar.maestro_materias: ~26 rows (aproximadamente)
DELETE FROM `maestro_materias`;
INSERT INTO `maestro_materias` (`id_maestro_materias`, `id_maestro`, `id_materia`) VALUES
	(1, 2, 2),
	(2, 2, 5),
	(10, 3, 6),
	(11, 3, 7),
	(12, 3, 5),
	(13, 2, 4),
	(14, 2, 7),
	(17, 2, 3),
	(18, 1, 2),
	(19, 1, 3),
	(20, 1, 5),
	(21, 1, 7),
	(22, 4, 9),
	(23, 4, 12),
	(24, 4, 5),
	(25, 5, 2),
	(26, 5, 3),
	(27, 5, 7),
	(28, 6, 8),
	(29, 6, 3),
	(30, 6, 7),
	(31, 7, 9),
	(32, 7, 10),
	(33, 8, 7),
	(34, 8, 6),
	(35, 3, 4);

-- Volcando estructura para tabla control_escolar.materias
CREATE TABLE IF NOT EXISTS `materias` (
  `id_materia` int(11) NOT NULL AUTO_INCREMENT,
  `asignatura` varchar(128) NOT NULL,
  `créditos` int(11) NOT NULL,
  PRIMARY KEY (`id_materia`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla control_escolar.materias: ~21 rows (aproximadamente)
DELETE FROM `materias`;
INSERT INTO `materias` (`id_materia`, `asignatura`, `créditos`) VALUES
	(2, 'Ingeniería de Software', 10),
	(3, 'Física 1', 8),
	(4, 'Precalculo', 8),
	(5, 'Estructura de Datos', 8),
	(6, 'Calculo Diferencial e Integral', 8),
	(7, 'Matemáticas Discretas', 7),
	(8, 'Matemáticas', 5),
	(9, 'Lengua y Literatura', 4),
	(10, 'Ciencias Naturales', 3),
	(11, 'Historia', 4),
	(12, 'Geografía', 3),
	(13, 'Educación Física', 2),
	(14, 'Arte', 2),
	(15, 'Música', 2),
	(16, 'Inglés', 3),
	(17, 'Tecnología', 3),
	(18, 'Informática', 3),
	(19, 'Ética', 2),
	(20, 'Religión', 2),
	(21, 'Ciudadanía', 2),
	(22, 'Educación Cívica', 2);

-- Volcando estructura para tabla control_escolar.materias_carreras
CREATE TABLE IF NOT EXISTS `materias_carreras` (
  `id_materias_carreras` int(11) NOT NULL AUTO_INCREMENT,
  `id_carrera` int(11) NOT NULL,
  `id_materia` int(11) NOT NULL,
  PRIMARY KEY (`id_materias_carreras`),
  KEY `id_carrera` (`id_carrera`),
  KEY `id_materia` (`id_materia`),
  CONSTRAINT `materias_carreras_ibfk_1` FOREIGN KEY (`id_carrera`) REFERENCES `carreras` (`id_carrera`),
  CONSTRAINT `materias_carreras_ibfk_2` FOREIGN KEY (`id_materia`) REFERENCES `materias` (`id_materia`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla control_escolar.materias_carreras: ~35 rows (aproximadamente)
DELETE FROM `materias_carreras`;
INSERT INTO `materias_carreras` (`id_materias_carreras`, `id_carrera`, `id_materia`) VALUES
	(1, 1, 3),
	(2, 3, 3),
	(3, 6, 3),
	(4, 2, 4),
	(5, 3, 4),
	(6, 4, 4),
	(8, 3, 2),
	(10, 2, 2),
	(11, 1, 2),
	(12, 4, 2),
	(13, 1, 5),
	(14, 2, 5),
	(15, 1, 6),
	(16, 7, 6),
	(17, 3, 6),
	(18, 1, 7),
	(19, 3, 7),
	(20, 4, 7),
	(21, 7, 7),
	(23, 1, 8),
	(24, 1, 9),
	(25, 1, 10),
	(26, 1, 11),
	(27, 1, 12),
	(28, 1, 13),
	(29, 1, 14),
	(30, 1, 15),
	(31, 1, 16),
	(32, 1, 17),
	(33, 1, 18),
	(34, 1, 19),
	(35, 1, 20),
	(36, 1, 21),
	(37, 1, 22),
	(38, 1, 4);

-- Volcando estructura para tabla control_escolar.prerregistro
CREATE TABLE IF NOT EXISTS `prerregistro` (
  `id_prerregistro` int(11) NOT NULL AUTO_INCREMENT,
  `id_alumno` int(11) NOT NULL,
  `materias` text NOT NULL,
  PRIMARY KEY (`id_prerregistro`),
  KEY `id_alumno` (`id_alumno`),
  CONSTRAINT `prerregistro_ibfk_1` FOREIGN KEY (`id_alumno`) REFERENCES `alumnos` (`id_alumno`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla control_escolar.prerregistro: ~21 rows (aproximadamente)
DELETE FROM `prerregistro`;
INSERT INTO `prerregistro` (`id_prerregistro`, `id_alumno`, `materias`) VALUES
	(1, 2, '[1,2,3,4,5,6]'),
	(2, 3, '[2, 3, 4, 5, 6, 5]'),
	(3, 4, '[3, 4, 5, 6, 7, 5]'),
	(4, 5, '[4, 5, 6, 7, 8, 5]'),
	(5, 6, '[5, 6, 7, 8, 9, 5]'),
	(6, 7, '[6, 7, 8, 9, 10, 5]'),
	(7, 8, '[7, 8, 9, 10, 11, 5]'),
	(8, 9, '[8, 9, 10, 11, 12, 5]'),
	(9, 10, '[9, 10, 11, 12, 13, 5]'),
	(10, 11, '[10, 11, 12, 13, 14, 5]'),
	(11, 12, '[11, 12, 13, 14, 2, 5]'),
	(12, 13, '[12, 13, 14, 2, 3, 5]'),
	(13, 14, '[13, 14, 2, 3, 4, 5]'),
	(14, 15, '[14, 2, 3, 4, 5, 5]'),
	(15, 16, '[2, 3, 4, 5, 6, 5]'),
	(16, 17, '[3, 4, 5, 6, 7, 5]'),
	(17, 18, '[4, 5, 6, 7, 8, 5]'),
	(18, 19, '[5, 6, 7, 8, 9, 5]'),
	(19, 20, '[6, 7, 8, 9, 10, 5]'),
	(20, 21, '[7, 8, 9, 10, 11, 5]'),
	(21, 22, '[8, 9, 10, 11, 12, 5]');

-- Volcando estructura para tabla control_escolar.salones
CREATE TABLE IF NOT EXISTS `salones` (
  `id_salon` int(11) NOT NULL AUTO_INCREMENT,
  `id_edificio` int(11) NOT NULL,
  `nombre` varchar(128) NOT NULL,
  PRIMARY KEY (`id_salon`),
  KEY `id_edificio` (`id_edificio`),
  CONSTRAINT `id_edificio` FOREIGN KEY (`id_edificio`) REFERENCES `edificio` (`id_edificio`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla control_escolar.salones: ~7 rows (aproximadamente)
DELETE FROM `salones`;
INSERT INTO `salones` (`id_salon`, `id_edificio`, `nombre`) VALUES
	(1, 3, 'C1'),
	(2, 3, 'C2'),
	(3, 3, 'C3'),
	(4, 1, 'A1'),
	(5, 1, 'A2'),
	(6, 3, 'C4'),
	(7, 5, 'E1');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
