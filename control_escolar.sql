-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 29-04-2024 a las 07:59:19
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `control_escolar`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `administradores`
--

CREATE TABLE `administradores` (
  `id_admin` int(11) NOT NULL,
  `nombre` varchar(128) NOT NULL,
  `paterno` varchar(128) NOT NULL,
  `materno` varchar(128) NOT NULL,
  `username` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `status` int(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `administradores`
--

INSERT INTO `administradores` (`id_admin`, `nombre`, `paterno`, `materno`, `username`, `password`, `status`) VALUES
(1, 'Gael Emiliano', 'Anaya', 'Garcia', 'ZGrupo115@admin.com', 'bas019efE%', 1),
(2, 'Jair Antonio', 'Anaya', 'Garcia', 'Jairsupremo90@admin.com', 'hsBW6erDY@', 1),
(3, 'Jorge', 'Anaya', 'Garcia', 'Billyork69@admin.com', 'LosAngeles87!', 1),
(4, 'Oscar Julio', 'Alferez', 'Orozco', 'ZGrupo935@admin.com', 'qw123df4wQ$', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos`
--

CREATE TABLE `alumnos` (
  `id_alumno` int(11) NOT NULL,
  `nombre` varchar(128) NOT NULL,
  `paterno` varchar(128) NOT NULL,
  `materno` varchar(128) NOT NULL,
  `nacimiento` date NOT NULL,
  `username` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `id_carrera` int(11) NOT NULL,
  `id_grupo` int(11) NOT NULL,
  `status` int(1) NOT NULL DEFAULT 1,
  `prerregistro` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `alumnos`
--

INSERT INTO `alumnos` (`id_alumno`, `nombre`, `paterno`, `materno`, `nacimiento`, `username`, `password`, `id_carrera`, `id_grupo`, `status`, `prerregistro`) VALUES
(1, 'Santino', 'Barocio', 'Orozco', '2001-11-15', 'santino.alexandro@alumnos.com', 'GF$%fg3d4fd$F#', 2, 0, 1, 0),
(2, 'Gael Emiliano', 'Anaya', 'Garcia', '2003-05-19', 'gael.anaya@alumnos.com', 'bas019efE7$', 1, 0, 1, 1),
(3, 'Juan', 'García', 'López', '2005-05-10', 'juang@alumnos.com', 'password123', 1, 0, 1, 1),
(4, 'María', 'Martínez', 'Rodríguez', '2006-02-15', 'mariam@alumnos.com', 'password456', 1, 0, 1, 1),
(5, 'Carlos', 'Hernández', 'Pérez', '2004-08-20', 'carlosh@alumnos.com', 'password789', 1, 0, 1, 1),
(6, 'Laura', 'González', 'Sánchez', '2007-11-25', 'laurag@alumnos.com', 'passwordabc', 1, 0, 1, 1),
(7, 'Pedro', 'Díaz', 'Martínez', '2003-04-30', 'pedrod@alumnos.com', 'passworddef', 1, 0, 1, 1),
(8, 'Ana', 'Pérez', 'Gómez', '2006-07-18', 'anap@alumnos.com', 'passwordghi', 1, 0, 1, 1),
(9, 'David', 'Rodríguez', 'López', '2004-10-05', 'davidd@alumnos.com', 'passwordjkl', 1, 0, 1, 1),
(10, 'Marta', 'Sánchez', 'Martínez', '2005-12-12', 'martas@alumnos.com', 'passwordmno', 1, 0, 1, 1),
(11, 'Sergio', 'Gómez', 'Ruiz', '2003-09-08', 'sergiog@alumnos.com', 'passwordpqr', 1, 0, 1, 1),
(12, 'Elena', 'López', 'Hernández', '2007-01-20', 'elenal@alumnos.com', 'passwordstu', 1, 0, 1, 1),
(13, 'Pablo', 'Martínez', 'García', '2006-08-07', 'pablom@alumnos.com', 'passwordvwx', 1, 0, 1, 1),
(14, 'Julia', 'Fernández', 'Pérez', '2004-03-15', 'juliaf@alumnos.com', 'passwordyz', 1, 0, 1, 1),
(15, 'Andrés', 'Ruiz', 'García', '2005-06-22', 'andresr@alumnos.com', 'password1234', 1, 0, 1, 1),
(16, 'Beatriz', 'López', 'Pérez', '2003-11-28', 'beatrizl@alumnos.com', 'password5678', 1, 0, 1, 1),
(17, 'Francisco', 'García', 'Martínez', '2006-04-03', 'franciscog@alumnos.com', 'password9012', 1, 0, 1, 1),
(18, 'Cristina', 'Martínez', 'Sánchez', '2004-09-17', 'cristinam@alumnos.com', 'password3456', 1, 0, 1, 1),
(19, 'Diego', 'Pérez', 'Gómez', '2007-02-24', 'diegop@alumnos.com', 'password7890', 1, 0, 1, 1),
(20, 'Ana María', 'Rodríguez', 'Pérez', '2005-10-11', 'anamariar@alumnos.com', 'password12345', 1, 0, 1, 1),
(21, 'José Luis', 'Gómez', 'Martínez', '2003-05-19', 'joseluisg@alumnos.com', 'password67890', 1, 0, 1, 1),
(22, 'Laura', 'Pérez', 'Martínez', '2006-08-30', 'laurap@alumnos.com', 'passwordabcd', 1, 0, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos_grupo`
--

CREATE TABLE `alumnos_grupo` (
  `id` int(11) NOT NULL,
  `id_grupo` int(11) NOT NULL,
  `id_alumno` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `alumnos_grupo`
--

INSERT INTO `alumnos_grupo` (`id`, `id_grupo`, `id_alumno`) VALUES
(1, 1, 22),
(2, 1, 6),
(3, 1, 19),
(4, 1, 8),
(5, 1, 18),
(6, 1, 16),
(7, 1, 21),
(8, 1, 17),
(9, 1, 15);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carreras`
--

CREATE TABLE `carreras` (
  `id_carrera` int(11) NOT NULL,
  `clave` varchar(128) NOT NULL,
  `carrera` varchar(128) NOT NULL,
  `semestres` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carreras`
--

INSERT INTO `carreras` (`id_carrera`, `clave`, `carrera`, `semestres`) VALUES
(1, 'ICOM', 'Ingeniería en Computación', '9'),
(2, 'INNI', 'Ingeniería en Informática', '7'),
(3, 'LIME', 'Licenciatura en Mercadotecnia', '8'),
(4, 'INFI', 'Licenciatura en Fisica', '6'),
(6, 'LICI', 'Ingeniería Civil', '6'),
(7, 'QFB', 'Licenciatura en Químico Farmacéutico Biólogo', '9');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `edificio`
--

CREATE TABLE `edificio` (
  `id_edificio` int(11) NOT NULL,
  `edificio` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `edificio`
--

INSERT INTO `edificio` (`id_edificio`, `edificio`) VALUES
(1, 'A'),
(2, 'B'),
(3, 'C'),
(4, 'D'),
(5, 'E'),
(6, 'F'),
(7, 'G');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupos`
--

CREATE TABLE `grupos` (
  `id_grupo` int(11) NOT NULL,
  `id_carrera` int(11) NOT NULL,
  `grupo` varchar(128) NOT NULL,
  `semestre` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `cupo` int(11) NOT NULL,
  `cupos_disponibles` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `grupos`
--

INSERT INTO `grupos` (`id_grupo`, `id_carrera`, `grupo`, `semestre`, `fecha`, `cupo`, `cupos_disponibles`) VALUES
(1, 1, 'A01', 1, '2024-04-22', 10, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horarios`
--

CREATE TABLE `horarios` (
  `id_horario` int(11) NOT NULL,
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
  `disponibilidad` int(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `horarios`
--

INSERT INTO `horarios` (`id_horario`, `id_carrera`, `id_materia`, `id_maestro`, `id_salon`, `L`, `M`, `I`, `J`, `V`, `S`, `horas`, `disponibilidad`) VALUES
(1, 1, 5, 2, 6, 0, 1, 0, 1, 0, 1, '9:00 - 10:55', 0),
(2, 1, 5, 3, 2, 0, 1, 0, 1, 0, 0, '7:00 - 8:55', 1),
(3, 1, 4, 3, 4, 0, 1, 0, 1, 0, 0, '11:00 - 12:55', 0),
(4, 6, 3, 1, 4, 1, 0, 1, 0, 1, 0, '7:00 - 8:55', 1),
(5, 4, 7, 1, 6, 0, 1, 0, 1, 0, 0, '7:00 - 8:55', 1),
(6, 1, 12, 4, 5, 1, 0, 1, 0, 0, 0, '7:00 - 8:55', 1),
(7, 1, 7, 5, 3, 1, 0, 1, 0, 0, 0, '11:00 - 12:55', 0),
(8, 1, 7, 6, 1, 0, 1, 0, 1, 0, 0, '9:00 - 10:55', 1),
(9, 1, 12, 4, 4, 1, 0, 0, 0, 0, 0, '11:00 - 12:55', 1),
(10, 1, 6, 3, 5, 1, 0, 1, 0, 0, 0, '11:00 - 12:55', 1),
(11, 1, 9, 7, 4, 0, 0, 0, 0, 1, 0, '11:00 - 12:55', 0),
(12, 1, 7, 8, 5, 0, 0, 0, 0, 0, 1, '9:00 - 10:55', 1),
(13, 1, 6, 8, 5, 0, 0, 0, 0, 1, 0, '9:00 - 10:55', 0),
(14, 1, 8, 6, 3, 0, 0, 1, 0, 1, 0, '7:00 - 8:55', 0),
(15, 1, 8, 6, 3, 0, 0, 1, 0, 1, 0, '9:00 - 10:55', 1),
(16, 1, 10, 7, 4, 0, 0, 0, 0, 0, 1, '9:00 - 10:55', 1),
(17, 1, 3, 5, 4, 0, 0, 0, 0, 0, 1, '11:00 - 12:55', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `horarios_grupo`
--

CREATE TABLE `horarios_grupo` (
  `id` int(11) NOT NULL,
  `id_grupo` int(11) NOT NULL,
  `id_horario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `horarios_grupo`
--

INSERT INTO `horarios_grupo` (`id`, `id_grupo`, `id_horario`) VALUES
(1, 1, 1),
(2, 1, 14),
(3, 1, 7),
(4, 1, 11),
(5, 1, 13),
(6, 1, 3),
(7, 1, 17);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `maestros`
--

CREATE TABLE `maestros` (
  `id_maestro` int(11) NOT NULL,
  `nombre` varchar(128) NOT NULL,
  `paterno` varchar(128) NOT NULL,
  `materno` varchar(128) NOT NULL,
  `username` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `status` int(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `maestros`
--

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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `maestro_carreras`
--

CREATE TABLE `maestro_carreras` (
  `id_maestro_carreras` int(11) NOT NULL,
  `id_maestro` int(11) NOT NULL,
  `id_carrera` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `maestro_carreras`
--

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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `maestro_materias`
--

CREATE TABLE `maestro_materias` (
  `id_maestro_materias` int(11) NOT NULL,
  `id_maestro` int(11) NOT NULL,
  `id_materia` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `maestro_materias`
--

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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materias`
--

CREATE TABLE `materias` (
  `id_materia` int(11) NOT NULL,
  `asignatura` varchar(128) NOT NULL,
  `créditos` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `materias`
--

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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materias_carreras`
--

CREATE TABLE `materias_carreras` (
  `id_materias_carreras` int(11) NOT NULL,
  `id_carrera` int(11) NOT NULL,
  `id_materia` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `materias_carreras`
--

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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prerregistro`
--

CREATE TABLE `prerregistro` (
  `id_prerregistro` int(11) NOT NULL,
  `id_alumno` int(11) NOT NULL,
  `materias` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `prerregistro`
--

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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `salones`
--

CREATE TABLE `salones` (
  `id_salon` int(11) NOT NULL,
  `id_edificio` int(11) NOT NULL,
  `nombre` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `salones`
--

INSERT INTO `salones` (`id_salon`, `id_edificio`, `nombre`) VALUES
(1, 3, 'C1'),
(2, 3, 'C2'),
(3, 3, 'C3'),
(4, 1, 'A1'),
(5, 1, 'A2'),
(6, 3, 'C4');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `administradores`
--
ALTER TABLE `administradores`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indices de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`id_alumno`),
  ADD KEY `id_carrera` (`id_carrera`);

--
-- Indices de la tabla `alumnos_grupo`
--
ALTER TABLE `alumnos_grupo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_alumno` (`id_alumno`),
  ADD KEY `id_grupo` (`id_grupo`);

--
-- Indices de la tabla `carreras`
--
ALTER TABLE `carreras`
  ADD PRIMARY KEY (`id_carrera`);

--
-- Indices de la tabla `edificio`
--
ALTER TABLE `edificio`
  ADD PRIMARY KEY (`id_edificio`);

--
-- Indices de la tabla `grupos`
--
ALTER TABLE `grupos`
  ADD PRIMARY KEY (`id_grupo`);

--
-- Indices de la tabla `horarios`
--
ALTER TABLE `horarios`
  ADD PRIMARY KEY (`id_horario`),
  ADD KEY `id_carrera` (`id_carrera`),
  ADD KEY `id_maestro` (`id_maestro`),
  ADD KEY `id_salon` (`id_salon`),
  ADD KEY `horarios_ibfk_2` (`id_materia`);

--
-- Indices de la tabla `horarios_grupo`
--
ALTER TABLE `horarios_grupo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_grupo` (`id_grupo`),
  ADD KEY `id_horario` (`id_horario`);

--
-- Indices de la tabla `maestros`
--
ALTER TABLE `maestros`
  ADD PRIMARY KEY (`id_maestro`);

--
-- Indices de la tabla `maestro_carreras`
--
ALTER TABLE `maestro_carreras`
  ADD PRIMARY KEY (`id_maestro_carreras`),
  ADD KEY `id_maestro` (`id_maestro`),
  ADD KEY `id_carreras` (`id_carrera`);

--
-- Indices de la tabla `maestro_materias`
--
ALTER TABLE `maestro_materias`
  ADD PRIMARY KEY (`id_maestro_materias`),
  ADD KEY `id_maestro` (`id_maestro`),
  ADD KEY `id_materia` (`id_materia`);

--
-- Indices de la tabla `materias`
--
ALTER TABLE `materias`
  ADD PRIMARY KEY (`id_materia`);

--
-- Indices de la tabla `materias_carreras`
--
ALTER TABLE `materias_carreras`
  ADD PRIMARY KEY (`id_materias_carreras`),
  ADD KEY `id_carrera` (`id_carrera`),
  ADD KEY `id_materia` (`id_materia`);

--
-- Indices de la tabla `prerregistro`
--
ALTER TABLE `prerregistro`
  ADD PRIMARY KEY (`id_prerregistro`),
  ADD KEY `id_alumno` (`id_alumno`);

--
-- Indices de la tabla `salones`
--
ALTER TABLE `salones`
  ADD PRIMARY KEY (`id_salon`),
  ADD KEY `id_edificio` (`id_edificio`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `administradores`
--
ALTER TABLE `administradores`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  MODIFY `id_alumno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT de la tabla `alumnos_grupo`
--
ALTER TABLE `alumnos_grupo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `carreras`
--
ALTER TABLE `carreras`
  MODIFY `id_carrera` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `edificio`
--
ALTER TABLE `edificio`
  MODIFY `id_edificio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `grupos`
--
ALTER TABLE `grupos`
  MODIFY `id_grupo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `horarios`
--
ALTER TABLE `horarios`
  MODIFY `id_horario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `horarios_grupo`
--
ALTER TABLE `horarios_grupo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `maestros`
--
ALTER TABLE `maestros`
  MODIFY `id_maestro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `maestro_carreras`
--
ALTER TABLE `maestro_carreras`
  MODIFY `id_maestro_carreras` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `maestro_materias`
--
ALTER TABLE `maestro_materias`
  MODIFY `id_maestro_materias` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT de la tabla `materias`
--
ALTER TABLE `materias`
  MODIFY `id_materia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT de la tabla `materias_carreras`
--
ALTER TABLE `materias_carreras`
  MODIFY `id_materias_carreras` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT de la tabla `prerregistro`
--
ALTER TABLE `prerregistro`
  MODIFY `id_prerregistro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `salones`
--
ALTER TABLE `salones`
  MODIFY `id_salon` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD CONSTRAINT `id_carrera` FOREIGN KEY (`id_carrera`) REFERENCES `carreras` (`id_carrera`);

--
-- Filtros para la tabla `alumnos_grupo`
--
ALTER TABLE `alumnos_grupo`
  ADD CONSTRAINT `alumnos_grupo_ibfk_1` FOREIGN KEY (`id_alumno`) REFERENCES `alumnos` (`id_alumno`),
  ADD CONSTRAINT `alumnos_grupo_ibfk_2` FOREIGN KEY (`id_grupo`) REFERENCES `grupos` (`id_grupo`);

--
-- Filtros para la tabla `horarios`
--
ALTER TABLE `horarios`
  ADD CONSTRAINT `horarios_ibfk_1` FOREIGN KEY (`id_carrera`) REFERENCES `carreras` (`id_carrera`),
  ADD CONSTRAINT `horarios_ibfk_2` FOREIGN KEY (`id_materia`) REFERENCES `materias` (`id_materia`),
  ADD CONSTRAINT `horarios_ibfk_3` FOREIGN KEY (`id_maestro`) REFERENCES `maestros` (`id_maestro`),
  ADD CONSTRAINT `horarios_ibfk_4` FOREIGN KEY (`id_salon`) REFERENCES `salones` (`id_salon`);

--
-- Filtros para la tabla `horarios_grupo`
--
ALTER TABLE `horarios_grupo`
  ADD CONSTRAINT `horarios_grupo_ibfk_1` FOREIGN KEY (`id_grupo`) REFERENCES `grupos` (`id_grupo`),
  ADD CONSTRAINT `horarios_grupo_ibfk_2` FOREIGN KEY (`id_horario`) REFERENCES `horarios` (`id_horario`);

--
-- Filtros para la tabla `maestro_carreras`
--
ALTER TABLE `maestro_carreras`
  ADD CONSTRAINT `maestro_carreras_ibfk_1` FOREIGN KEY (`id_maestro`) REFERENCES `maestros` (`id_maestro`),
  ADD CONSTRAINT `maestro_carreras_ibfk_2` FOREIGN KEY (`id_carrera`) REFERENCES `carreras` (`id_carrera`);

--
-- Filtros para la tabla `maestro_materias`
--
ALTER TABLE `maestro_materias`
  ADD CONSTRAINT `maestro_materias_ibfk_1` FOREIGN KEY (`id_maestro`) REFERENCES `maestros` (`id_maestro`),
  ADD CONSTRAINT `maestro_materias_ibfk_2` FOREIGN KEY (`id_materia`) REFERENCES `materias` (`id_materia`);

--
-- Filtros para la tabla `materias_carreras`
--
ALTER TABLE `materias_carreras`
  ADD CONSTRAINT `materias_carreras_ibfk_1` FOREIGN KEY (`id_carrera`) REFERENCES `carreras` (`id_carrera`),
  ADD CONSTRAINT `materias_carreras_ibfk_2` FOREIGN KEY (`id_materia`) REFERENCES `materias` (`id_materia`);

--
-- Filtros para la tabla `prerregistro`
--
ALTER TABLE `prerregistro`
  ADD CONSTRAINT `prerregistro_ibfk_1` FOREIGN KEY (`id_alumno`) REFERENCES `alumnos` (`id_alumno`);

--
-- Filtros para la tabla `salones`
--
ALTER TABLE `salones`
  ADD CONSTRAINT `id_edificio` FOREIGN KEY (`id_edificio`) REFERENCES `edificio` (`id_edificio`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
