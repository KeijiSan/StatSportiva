-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-11-2024 a las 02:09:51
-- Versión del servidor: 11.5.2-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `basquetbol_torneo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `account_emailaddress`
--

CREATE TABLE `account_emailaddress` (
  `id` int(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `account_emailconfirmation`
--

CREATE TABLE `account_emailconfirmation` (
  `id` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `sent` datetime(6) DEFAULT NULL,
  `key` varchar(64) NOT NULL,
  `email_address_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(2, 'Administrador'),
(1, 'Planillero');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 49),
(2, 1, 50),
(3, 1, 52);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add campeonato', 7, 'add_campeonato'),
(26, 'Can change campeonato', 7, 'change_campeonato'),
(27, 'Can delete campeonato', 7, 'delete_campeonato'),
(28, 'Can view campeonato', 7, 'view_campeonato'),
(29, 'Can add entrenador', 8, 'add_entrenador'),
(30, 'Can change entrenador', 8, 'change_entrenador'),
(31, 'Can delete entrenador', 8, 'delete_entrenador'),
(32, 'Can view entrenador', 8, 'view_entrenador'),
(33, 'Can add estadio', 9, 'add_estadio'),
(34, 'Can change estadio', 9, 'change_estadio'),
(35, 'Can delete estadio', 9, 'delete_estadio'),
(36, 'Can view estadio', 9, 'view_estadio'),
(37, 'Can add equipo', 10, 'add_equipo'),
(38, 'Can change equipo', 10, 'change_equipo'),
(39, 'Can delete equipo', 10, 'delete_equipo'),
(40, 'Can view equipo', 10, 'view_equipo'),
(41, 'Can add fase', 11, 'add_fase'),
(42, 'Can change fase', 11, 'change_fase'),
(43, 'Can delete fase', 11, 'delete_fase'),
(44, 'Can view fase', 11, 'view_fase'),
(45, 'Can add jugador', 12, 'add_jugador'),
(46, 'Can change jugador', 12, 'change_jugador'),
(47, 'Can delete jugador', 12, 'delete_jugador'),
(48, 'Can view jugador', 12, 'view_jugador'),
(49, 'Can add partido', 13, 'add_partido'),
(50, 'Can change partido', 13, 'change_partido'),
(51, 'Can delete partido', 13, 'delete_partido'),
(52, 'Can view partido', 13, 'view_partido'),
(53, 'Can add partido estadistica', 14, 'add_partidoestadistica'),
(54, 'Can change partido estadistica', 14, 'change_partidoestadistica'),
(55, 'Can delete partido estadistica', 14, 'delete_partidoestadistica'),
(56, 'Can view partido estadistica', 14, 'view_partidoestadistica'),
(57, 'Can add posicion', 15, 'add_posicion'),
(58, 'Can change posicion', 15, 'change_posicion'),
(59, 'Can delete posicion', 15, 'delete_posicion'),
(60, 'Can view posicion', 15, 'view_posicion'),
(61, 'Can add cuartos', 16, 'add_cuartos'),
(62, 'Can change cuartos', 16, 'change_cuartos'),
(63, 'Can delete cuartos', 16, 'delete_cuartos'),
(64, 'Can view cuartos', 16, 'view_cuartos'),
(65, 'Can add campeon', 17, 'add_campeon'),
(66, 'Can change campeon', 17, 'change_campeon'),
(67, 'Can delete campeon', 17, 'delete_campeon'),
(68, 'Can view campeon', 17, 'view_campeon'),
(69, 'Can add site', 19, 'add_site'),
(70, 'Can change site', 19, 'change_site'),
(71, 'Can delete site', 19, 'delete_site'),
(72, 'Can view site', 19, 'view_site'),
(73, 'Can add email address', 20, 'add_emailaddress'),
(74, 'Can change email address', 20, 'change_emailaddress'),
(75, 'Can delete email address', 20, 'delete_emailaddress'),
(76, 'Can view email address', 20, 'view_emailaddress'),
(77, 'Can add email confirmation', 21, 'add_emailconfirmation'),
(78, 'Can change email confirmation', 21, 'change_emailconfirmation'),
(79, 'Can delete email confirmation', 21, 'delete_emailconfirmation'),
(80, 'Can view email confirmation', 21, 'view_emailconfirmation'),
(81, 'Can add social account', 22, 'add_socialaccount'),
(82, 'Can change social account', 22, 'change_socialaccount'),
(83, 'Can delete social account', 22, 'delete_socialaccount'),
(84, 'Can view social account', 22, 'view_socialaccount'),
(85, 'Can add social application', 23, 'add_socialapp'),
(86, 'Can change social application', 23, 'change_socialapp'),
(87, 'Can delete social application', 23, 'delete_socialapp'),
(88, 'Can view social application', 23, 'view_socialapp'),
(89, 'Can add social application token', 24, 'add_socialtoken'),
(90, 'Can change social application token', 24, 'change_socialtoken'),
(91, 'Can delete social application token', 24, 'delete_socialtoken'),
(92, 'Can view social application token', 24, 'view_socialtoken'),
(93, 'Can add video', 18, 'add_video'),
(94, 'Can change video', 18, 'change_video'),
(95, 'Can delete video', 18, 'delete_video'),
(96, 'Can view video', 18, 'view_video');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(6, 'pbkdf2_sha256$870000$ZcKuf1bRfKT9drEg19QXci$YT0W0t07xP1zCnTYJyadlW6eF6Lc49DhNmURSQptJ6w=', '2024-11-25 00:05:30.116503', 0, 'Stevencolocolino', '', '', 'Stevencolocololover@gmail.com', 0, 1, '2024-11-15 17:15:00.038003'),
(7, 'pbkdf2_sha256$870000$yLX3neTB12pahNHQ1zLZgr$wrBYzodXTbeiXFVkYKTp3uiP0k14hPVlsJqPdE1wZVg=', '2024-11-20 14:23:50.474820', 0, 'thomasdsasda', '', '', 'fabian.cardinaletp@gmail.com', 0, 1, '2024-11-16 16:59:00.656908'),
(8, 'pbkdf2_sha256$870000$wCAdbU3UDSqU7yPefHO72J$sGM+kxutJZhv1C1O+Y95SqfwyiLzz3pxF0auIJ5luJA=', '2024-11-20 14:26:17.882541', 0, 'keijinagano', '', '', 'keiji@gmail.com', 0, 1, '2024-11-16 17:01:15.480735'),
(9, 'pbkdf2_sha256$870000$iCblJF33QdAY60nHi4iu2A$dXJ4TfnAJWUETLtRpyJp6huRRPfByR82uxFVMa4wzVo=', '2024-11-20 14:28:41.130761', 0, 'fabiangodsanchez', '', '', 'fabian.cardinaletp@gmail.com', 0, 1, '2024-11-16 17:03:27.498549'),
(10, 'pbkdf2_sha256$870000$8qEmv3wMmPhHpkdRaFgZGC$myMwktXUE0a3l6qmCY1CbInFEXfSzlHi3615Ol25tvc=', '2024-11-20 14:28:57.801508', 0, 'wally', '', '', 'wally@gmail.com', 0, 1, '2024-11-16 17:05:43.144312'),
(11, 'pbkdf2_sha256$870000$gXKK2MlPfQIvLg0Pk0udcE$Yx4Hace2+dc2iw1jFYgbSXbxWXa6xfWhKpxjZEDFgBI=', '2024-11-21 19:15:09.607353', 0, 'juan', '', '', 'juan@gmail.com', 0, 1, '2024-11-16 17:07:30.132702'),
(12, 'pbkdf2_sha256$870000$CoFq4kEkDKUTUkR3mTPjXC$jOJ1nG1EqEYND097xgFSfX4NbbzkNMBrCIT7t+ro1TM=', '2024-11-20 14:33:45.636398', 0, 'mario', '', '', 'mario@gmail.com', 0, 1, '2024-11-16 17:09:09.103222'),
(13, 'pbkdf2_sha256$870000$me4q71CgdMymiig8Yz9Mqi$MvDDMLm++CIB76hNsy2NhmjCulsYrQGB6HdrYFeSWcU=', '2024-11-20 14:36:10.243587', 0, 'raul', '', '', 'rcardinale017@gmail.com', 0, 1, '2024-11-16 17:10:46.155701'),
(14, 'pbkdf2_sha256$870000$paikgHHJD3JYlVlyYa5fbB$cgDGBZAGgF5JPBvWBSUIFtZskIfUnMrFM3ULXcKn21I=', '2024-11-20 14:38:30.558238', 0, 'llorons', '', '', 'lloron@gmail.com', 0, 1, '2024-11-16 17:12:48.592894'),
(15, 'pbkdf2_sha256$870000$SyUjykobdvvV8XoE24B7kI$SxDrdQTP3GjtE7SyQEp9tW+qsc+ibZrRt7TdyvZLSBE=', '2024-11-20 14:40:48.607250', 0, 'michael', '', '', 'maicol@gmail.com', 0, 1, '2024-11-16 17:14:36.337564'),
(16, 'pbkdf2_sha256$870000$RwH1BOVaXxIZARHmczL4lu$RnoVyNWWMiDn1RdoJaQ04yfJ6Tt+LMLnPM/gcr45bdw=', '2024-11-22 00:05:06.069564', 1, 'administrador', '', '', 'fabian.cardinaletp@gmail.com', 1, 1, '2024-11-16 17:41:32.000000'),
(17, 'pbkdf2_sha256$870000$T94TSx2ICu8L25sF7m5hhv$ro/u9hM+asmnAEkl+mJ33RqLN0rgIXFu+BuNsTjmCPM=', '2024-11-18 22:57:43.000000', 0, 'planillero1', '', '', '', 0, 1, '2024-11-16 19:22:03.000000'),
(20, 'pbkdf2_sha256$870000$WHNIz8bbwNavEsLPDe6mgt$fBN1+r4j2a0aReMMPhKRXJCDLzqlno4poHK+mQ164J8=', '2024-11-24 20:29:02.769209', 0, 'planillero', 'fabian', 'sanchez', 'fabian@example.com', 0, 1, '2024-11-18 23:06:50.491662'),
(21, 'pbkdf2_sha256$870000$rthH77pLil1SIQM1qecolH$eYYONI3TDRWaHd0pr89tLOPDmw1qa7uguv4hT6c/I6I=', '2024-11-25 00:06:45.767476', 1, 'fabian', '', '', 'fabianaramis21@gmail.com', 1, 1, '2024-11-18 23:51:15.000000'),
(22, 'pbkdf2_sha256$870000$lQzINmbWRPlJA32vVUNK5M$U9rkhrdHeZ9JxXDvZxeOrpPFa8npXVoutN/u3qaPkzM=', '2024-11-19 00:32:17.360393', 0, 'estiben', '', '', 'steven@gmail.com', 0, 1, '2024-11-19 00:30:54.099027'),
(23, 'pbkdf2_sha256$870000$6f1wa0gV1whfnWaPkWgGdA$UaJXldpaiYraelA16lhd5TyAYQpTRhmhjyKq7RF+/v8=', NULL, 0, 'keijisan', '', '', 'fabianaramis21@gmail.com', 0, 1, '2024-11-19 03:11:15.999979'),
(26, 'pbkdf2_sha256$870000$RKaO3UujMYnl7T1pBNfdL5$GbF6C/NqhYbV1Ev524j1FNvr2RQ1r1mYdMmwEihjoUo=', '2024-11-22 01:33:12.095349', 0, 'thomasellocoooo', '', '', 'fa.sanchez@duocuc.cl', 0, 1, '2024-11-22 01:33:11.450956'),
(27, 'pbkdf2_sha256$870000$OK0Y8ihD28BC11oPfTO60e$dSS28rimcV8IEh+ztj3RsMAY6YZEsdQ1cz14c6+zbVo=', '2024-11-22 22:15:34.640374', 0, 'fabiansanchez', '', '', 'fa.sanchez@duocuc.cl', 0, 1, '2024-11-22 16:08:00.177211');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 9, 1),
(5, 16, 2),
(3, 17, 1),
(4, 20, 1),
(6, 21, 2),
(7, 22, 1),
(8, 23, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `basquetbol_campeon`
--

CREATE TABLE `basquetbol_campeon` (
  `id` bigint(20) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `campeonato_id` bigint(20) NOT NULL,
  `equipo_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `basquetbol_campeon`
--

INSERT INTO `basquetbol_campeon` (`id`, `fecha`, `campeonato_id`, `equipo_id`) VALUES
(7, '2024-11-21 02:41:28.024324', 1, 37);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `basquetbol_campeonato`
--

CREATE TABLE `basquetbol_campeonato` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL,
  `descripcion` longtext NOT NULL,
  `max_equipos` int(10) UNSIGNED NOT NULL CHECK (`max_equipos` >= 0),
  `premios` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `basquetbol_campeonato`
--

INSERT INTO `basquetbol_campeonato` (`id`, `nombre`, `fecha_inicio`, `fecha_fin`, `descripcion`, `max_equipos`, `premios`) VALUES
(1, 'Campeonato statsportiva', '2024-12-12', '2024-12-12', 'dfsdfsdfs', 10, 'sdsdfsdfsdf'),
(7, 'campeonato municipal', '2024-11-18', '2025-01-18', 'campeonato municipal', 10, 'copa municipal');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `basquetbol_cuartos`
--

CREATE TABLE `basquetbol_cuartos` (
  `id` bigint(20) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `goles_local` int(10) UNSIGNED DEFAULT NULL CHECK (`goles_local` >= 0),
  `goles_visitante` int(10) UNSIGNED DEFAULT NULL CHECK (`goles_visitante` >= 0),
  `campeonato_id` bigint(20) NOT NULL,
  `equipo_local_id` bigint(20) NOT NULL,
  `equipo_visitante_id` bigint(20) NOT NULL,
  `estadio_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `basquetbol_entrenador`
--

CREATE TABLE `basquetbol_entrenador` (
  `id` bigint(20) NOT NULL,
  `nombre_entrenador` varchar(100) NOT NULL,
  `nacionalidad` varchar(50) NOT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `basquetbol_entrenador`
--

INSERT INTO `basquetbol_entrenador` (`id`, `nombre_entrenador`, `nacionalidad`, `fecha_nacimiento`, `user_id`) VALUES
(41, 'steven', 'chileno', '2024-11-08', 6),
(42, 'Thomas', 'Peruano', '2024-11-03', 7),
(43, 'Keiji', 'Japones', '2024-10-30', 8),
(44, 'Wally', 'senegal', '2024-11-07', 10),
(45, 'Juan', 'Chile', '2024-11-13', 11),
(46, 'Mario', 'Italia', '2024-11-14', 12),
(47, 'Raul', 'Chile', '2024-11-07', 13),
(48, 'Lloron', 'Chile', '2024-11-14', 14),
(49, 'Michel', 'EEUU', '2024-11-14', 15),
(50, 'Fabian sanchez Cardinale', 'Argentina', '2001-01-03', 21),
(51, 'clavito godoy', 'chileno', '2024-11-08', 26);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `basquetbol_equipo`
--

CREATE TABLE `basquetbol_equipo` (
  `id` bigint(20) NOT NULL,
  `nombre_equipo` varchar(100) NOT NULL,
  `historia` longtext DEFAULT NULL,
  `color_principal` varchar(7) NOT NULL,
  `color_secundario` varchar(7) NOT NULL,
  `logo` varchar(100) DEFAULT NULL,
  `sitio_web` varchar(200) DEFAULT NULL,
  `campeonato_id` bigint(20) DEFAULT NULL,
  `entrenador_id` bigint(20) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `campeon_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `basquetbol_equipo`
--

INSERT INTO `basquetbol_equipo` (`id`, `nombre_equipo`, `historia`, `color_principal`, `color_secundario`, `logo`, `sitio_web`, `campeonato_id`, `entrenador_id`, `activo`, `campeon_id`) VALUES
(32, 'U.de Chile', 'U. de chile', '#0e15cd', '#e60000', 'logos_equipos/Emblema_del_Club_Universidad_de_Chile_B5v1lRB.png', NULL, 1, 41, 0, NULL),
(33, 'Wanders', 'Wanders', '#11ff00', '#ffffff', 'logos_equipos/wanders.png', NULL, 1, 42, 1, NULL),
(34, 'U.Catolica', 'Universidad Catolica amateur', '#94cbff', '#ffffff', 'logos_equipos/descarga_5.png', NULL, 1, 43, 1, NULL),
(35, 'Coquimbo Unido', 'Los piratas', '#000000', '#f2f542', 'logos_equipos/descarga_9.jpg', NULL, 1, 44, 1, NULL),
(36, 'Curico unido', 'Piitu Curicano basquet club', '#ffffff', '#ff0000', 'logos_equipos/descarga_6.png', NULL, 1, 45, 1, NULL),
(37, 'Audax Italiano', 'Club deportivo Audax Italiano', '#006b02', '#ffffff', 'logos_equipos/descarga_7.png', NULL, 1, 46, 1, NULL),
(38, 'Ñublense', 'Ñublenchestes amateur', '#ff0000', '#000000', 'logos_equipos/descarga_8.png', NULL, 1, 47, 0, NULL),
(39, 'Magallanes', 'El viejo Magallanes', '#6188ff', '#ffffff', 'logos_equipos/descarga_9.png', NULL, 1, 48, 1, NULL),
(40, 'O´higgins', 'Equipo Amateur', '#00bfff', '#33eb00', 'logos_equipos/descarga_10.png', NULL, 1, 49, 1, NULL),
(41, 'Colo Colo', 'Colo Colo basquetbol club amateur', '#ffffff', '#000000', 'logos_equipos/descarga_11.png', NULL, 1, 50, 1, NULL),
(42, 'ranger', 'dasdasdsad', '#ff0000', '#000000', 'logos_equipos/descarga_9_N5wLcRk.jpg', NULL, NULL, 51, 1, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `basquetbol_estadio`
--

CREATE TABLE `basquetbol_estadio` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `capacidad` int(10) UNSIGNED NOT NULL CHECK (`capacidad` >= 0),
  `ciudad` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `basquetbol_estadio`
--

INSERT INTO `basquetbol_estadio` (`id`, `nombre`, `capacidad`, `ciudad`) VALUES
(1, 'Gimnasio municipal', 20000, 'Santiago');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `basquetbol_fase`
--

CREATE TABLE `basquetbol_fase` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `orden` int(10) UNSIGNED NOT NULL CHECK (`orden` >= 0),
  `campeonato_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `basquetbol_jugador`
--

CREATE TABLE `basquetbol_jugador` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `posicion` varchar(20) NOT NULL,
  `numero` int(10) UNSIGNED NOT NULL CHECK (`numero` >= 0),
  `equipo_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `basquetbol_jugador`
--

INSERT INTO `basquetbol_jugador` (`id`, `nombre`, `posicion`, `numero`, `equipo_id`) VALUES
(137, 'steven', 'BASE', 5, 32),
(138, 'fabian', 'ESCOLTA', 10, 32),
(139, 'thomas', 'ALERO', 4, 32),
(140, 'keiji', 'ALA-PIVOT', 1, 32),
(141, 'mario', 'PIVOT', 2, 32),
(142, 'Roger', 'BASE', 4, 33),
(143, 'lucas', 'ESCOLTA', 1, 33),
(144, 'pedro', 'ALERO', 12, 33),
(145, 'felipe', 'ALA-PIVOT', 3, 33),
(146, 'juan', 'PIVOT', 8, 33),
(147, 'Kubo', 'BASE', 1, 34),
(148, 'Jin sun park', 'ESCOLTA', 4, 34),
(149, 'hiroshima', 'ALERO', 3, 34),
(150, 'nakamura', 'ALA-PIVOT', 6, 34),
(151, 'hanamichi', 'PIVOT', 10, 34),
(152, 'Hakuna', 'BASE', 5, 35),
(153, 'Timon', 'ESCOLTA', 7, 35),
(154, 'Pumba', 'ALERO', 8, 35),
(155, 'samir', 'ALA-PIVOT', 2, 35),
(156, 'mamberroi', 'PIVOT', 12, 35),
(157, 'Juan', 'BASE', 5, 36),
(158, 'rodrigo', 'ESCOLTA', 2, 36),
(159, 'mateo', 'ALERO', 7, 36),
(160, 'matias', 'ALA-PIVOT', 14, 36),
(161, 'kevin', 'PIVOT', 23, 36),
(162, 'giusseppe', 'BASE', 3, 37),
(163, 'alexandri', 'ESCOLTA', 8, 37),
(164, 'figaro', 'ALERO', 4, 37),
(165, 'bonucci', 'ALA-PIVOT', 2, 37),
(166, 'faustino', 'PIVOT', 16, 37),
(167, 'michael', 'BASE', 6, 38),
(168, 'harry', 'ESCOLTA', 1, 38),
(169, 'kane', 'ALERO', 8, 38),
(170, 'louis', 'ALA-PIVOT', 2, 38),
(171, 'niall', 'PIVOT', 3, 38),
(172, 'LLorel', 'BASE', 5, 39),
(173, 'mario', 'ESCOLTA', 1, 39),
(174, 'catrina', 'ALERO', 8, 39),
(175, 'nahuel', 'ALA-PIVOT', 4, 39),
(176, 'bruno', 'PIVOT', 9, 39),
(177, 'Bobby', 'BASE', 5, 40),
(178, 'Richard', 'ESCOLTA', 3, 40),
(179, 'mattew', 'ALERO', 4, 40),
(180, 'robber', 'ALA-PIVOT', 12, 40),
(181, 'martin', 'PIVOT', 78, 40),
(182, 'Fabian', 'BASE', 10, 41),
(183, 'Rukawa', 'ESCOLTA', 5, 41),
(184, 'ryota', 'ALERO', 3, 41),
(185, 'Amaury', 'ALA-PIVOT', 11, 41),
(186, 'Ivan', 'PIVOT', 7, 41),
(188, 'indart', 'BASE', 232, 41),
(189, 'thomas', 'BASE', 5, 42),
(190, 'a', 'BASE', 42, 42),
(191, 'cx', 'BASE', 6, 42),
(192, 'v', 'BASE', 663, 42),
(193, 'nbnnm', 'BASE', 436, 42);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `basquetbol_partido`
--

CREATE TABLE `basquetbol_partido` (
  `id` bigint(20) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `fase` varchar(50) NOT NULL,
  `goles_local` int(10) UNSIGNED DEFAULT NULL CHECK (`goles_local` >= 0),
  `goles_visitante` int(10) UNSIGNED DEFAULT NULL CHECK (`goles_visitante` >= 0),
  `equipo_local_id` bigint(20) NOT NULL,
  `equipo_visitante_id` bigint(20) NOT NULL,
  `estadio_id` bigint(20) DEFAULT NULL,
  `campeonato_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `basquetbol_partido`
--

INSERT INTO `basquetbol_partido` (`id`, `fecha`, `fase`, `goles_local`, `goles_visitante`, `equipo_local_id`, `equipo_visitante_id`, `estadio_id`, `campeonato_id`) VALUES
(183, '2024-12-11 23:00:00.000000', 'Clasificatorias', NULL, NULL, 39, 40, NULL, 1),
(184, '2024-12-12 23:00:00.000000', 'Clasificatorias', NULL, NULL, 33, 40, NULL, 1),
(185, '2024-12-13 23:00:00.000000', 'Clasificatorias', NULL, NULL, 35, 37, NULL, 1),
(186, '2024-12-14 23:00:00.000000', 'Clasificatorias', NULL, NULL, 40, 41, NULL, 1),
(187, '2024-12-15 23:00:00.000000', 'Clasificatorias', NULL, NULL, 34, 36, NULL, 1),
(188, '2024-12-16 23:00:00.000000', 'Clasificatorias', NULL, NULL, 33, 38, NULL, 1),
(189, '2024-12-17 23:00:00.000000', 'Clasificatorias', NULL, NULL, 36, 38, NULL, 1),
(190, '2024-12-18 23:00:00.000000', 'Clasificatorias', NULL, NULL, 32, 33, NULL, 1),
(191, '2024-12-19 23:00:00.000000', 'Clasificatorias', NULL, NULL, 32, 36, NULL, 1),
(192, '2024-12-20 23:00:00.000000', 'Clasificatorias', NULL, NULL, 35, 38, NULL, 1),
(193, '2024-12-21 23:00:00.000000', 'Clasificatorias', NULL, NULL, 32, 37, NULL, 1),
(194, '2024-12-22 23:00:00.000000', 'Clasificatorias', NULL, NULL, 34, 35, NULL, 1),
(195, '2024-12-23 23:00:00.000000', 'Clasificatorias', NULL, NULL, 37, 39, NULL, 1),
(196, '2024-12-24 23:00:00.000000', 'Clasificatorias', NULL, NULL, 39, 41, NULL, 1),
(197, '2024-12-25 23:00:00.000000', 'Clasificatorias', NULL, NULL, 34, 41, NULL, 1),
(267, '2024-11-21 02:00:56.652295', 'Cuartos', NULL, NULL, 35, 37, NULL, 1),
(268, '2024-11-22 02:00:56.652295', 'Cuartos', NULL, NULL, 38, 41, NULL, 1),
(269, '2024-11-23 02:00:56.652295', 'Cuartos', NULL, NULL, 33, 40, NULL, 1),
(270, '2024-11-24 02:00:56.652295', 'Cuartos', NULL, NULL, 36, 34, NULL, 1),
(283, '2024-12-01 02:00:56.652295', 'Semifinal', NULL, NULL, 37, 38, NULL, 1),
(284, '2024-12-01 02:00:56.652295', 'Semifinal', NULL, NULL, 33, 36, NULL, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `basquetbol_partidoestadistica`
--

CREATE TABLE `basquetbol_partidoestadistica` (
  `id` bigint(20) NOT NULL,
  `pases_equipo_local` int(10) UNSIGNED NOT NULL CHECK (`pases_equipo_local` >= 0),
  `pases_equipo_visitante` int(10) UNSIGNED NOT NULL CHECK (`pases_equipo_visitante` >= 0),
  `faltas_equipo_local` int(10) UNSIGNED NOT NULL CHECK (`faltas_equipo_local` >= 0),
  `faltas_equipo_visitante` int(10) UNSIGNED NOT NULL CHECK (`faltas_equipo_visitante` >= 0),
  `triples_equipo_local` int(10) UNSIGNED NOT NULL CHECK (`triples_equipo_local` >= 0),
  `triples_equipo_visitante` int(10) UNSIGNED NOT NULL CHECK (`triples_equipo_visitante` >= 0),
  `rebotes_equipo_local` int(10) UNSIGNED NOT NULL CHECK (`rebotes_equipo_local` >= 0),
  `rebotes_equipo_visitante` int(10) UNSIGNED NOT NULL CHECK (`rebotes_equipo_visitante` >= 0),
  `partido_id` bigint(20) NOT NULL,
  `puntos_equipo_local` int(10) UNSIGNED NOT NULL CHECK (`puntos_equipo_local` >= 0),
  `puntos_equipo_visitante` int(10) UNSIGNED NOT NULL CHECK (`puntos_equipo_visitante` >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `basquetbol_partidoestadistica`
--

INSERT INTO `basquetbol_partidoestadistica` (`id`, `pases_equipo_local`, `pases_equipo_visitante`, `faltas_equipo_local`, `faltas_equipo_visitante`, `triples_equipo_local`, `triples_equipo_visitante`, `rebotes_equipo_local`, `rebotes_equipo_visitante`, `partido_id`, `puntos_equipo_local`, `puntos_equipo_visitante`) VALUES
(92, 7, 11, 18, 16, 16, 13, 48, 32, 183, 102, 127),
(93, 5, 4, 16, 21, 13, 14, 48, 49, 184, 104, 94),
(94, 8, 5, 19, 26, 12, 8, 43, 53, 185, 98, 104),
(95, 3, 6, 22, 21, 18, 19, 51, 48, 186, 125, 119),
(96, 4, 5, 14, 18, 19, 19, 35, 49, 187, 131, 142),
(97, 54, 35, 4, 0, 3, 12, 54, 44, 188, 123, 122),
(98, 34, 23, 1, 3, 12, 5, 45, 56, 189, 80, 112),
(99, 12, 33, 1, 5, 23, 12, 43, 54, 190, 122, 154),
(100, 23, 43, 1, 0, 12, 11, 23, 33, 191, 112, 122),
(101, 23, 43, 1, 2, 34, 12, 43, 54, 192, 124, 123),
(102, 43, 54, 3, 0, 2, 4, 54, 65, 193, 124, 165),
(103, 32, 43, 1, 4, 1, 3, 54, 54, 194, 143, 134),
(104, 32, 34, 1, 0, 32, 3, 123, 34, 195, 154, 156),
(105, 1, 21, 4, 5, 3, 4, 34, 54, 196, 123, 167),
(106, 23, 43, 1, 3, 34, 2, 123, 23, 197, 144, 146),
(123, 12, 23, 1, 3, 23, 4, 12, 34, 267, 143, 154),
(124, 32, 43, 1, 0, 34, 4, 43, 45, 268, 143, 134),
(125, 43, 54, 1, 0, 34, 54, 133, 34, 269, 154, 145),
(126, 134, 23, 1, 0, 43, 54, 65, 23, 270, 134, 125);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `basquetbol_posicion`
--

CREATE TABLE `basquetbol_posicion` (
  `id` bigint(20) NOT NULL,
  `puntos` int(11) NOT NULL,
  `partidos_jugados` int(11) NOT NULL,
  `partidos_ganados` int(11) NOT NULL,
  `partidos_perdidos` int(11) NOT NULL,
  `equipo_id` bigint(20) NOT NULL,
  `campeonato_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `basquetbol_posicion`
--

INSERT INTO `basquetbol_posicion` (`id`, `puntos`, `partidos_jugados`, `partidos_ganados`, `partidos_perdidos`, `equipo_id`, `campeonato_id`) VALUES
(17, 18, 16, 6, 10, 40, 1),
(18, 3, 5, 1, 4, 39, 1),
(19, 42, 37, 14, 23, 33, 1),
(20, 84, 32, 28, 4, 35, 1),
(21, 48, 28, 16, 12, 37, 1),
(22, 12, 17, 4, 13, 41, 1),
(23, 15, 17, 5, 12, 34, 1),
(24, 57, 38, 19, 19, 36, 1),
(25, 54, 29, 18, 11, 38, 1),
(26, 0, 3, 0, 3, 32, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `basquetbol_video`
--

CREATE TABLE `basquetbol_video` (
  `id` bigint(20) NOT NULL,
  `title` varchar(100) NOT NULL,
  `url` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `basquetbol_video`
--

INSERT INTO `basquetbol_video` (`id`, `title`, `url`) VALUES
(1, 'LO IMPOSIBLE', 'https://www.youtube.com/shorts/dfoCBTMe8sI'),
(2, 'VOLANDO', 'https://www.youtube.com/shorts/-524ku1zdkc'),
(3, 'CLAVADA', 'https://www.youtube.com/shorts/Z5O4ooDy4qw'),
(4, 'prueba', 'https://www.youtube.com/shorts/PqK9mRt5xrE'),
(5, 'tiro raro', 'https://www.youtube.com/shorts/yxFkegil1FA'),
(6, 'GOAT', 'https://www.youtube.com/shorts/kgkC1h2gpxY'),
(7, 'TAPON', 'https://www.youtube.com/shorts/iDCQ40-q760'),
(8, 'JUGADOR DEL AÑO', 'https://www.youtube.com/shorts/RYILPoju2bw');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-11-18 22:56:02.076018', '17', 'planillero1', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 16),
(2, '2024-11-18 22:57:11.123126', '17', 'planillero1', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 4, 16),
(3, '2024-11-18 22:59:31.516049', '17', 'planillero1', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 16),
(4, '2024-11-19 00:10:40.081362', '2', 'Administrador', 1, '[{\"added\": {}}]', 3, 21),
(5, '2024-11-19 00:11:02.842128', '16', 'administrador', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 21),
(6, '2024-11-19 00:11:12.017572', '21', 'fabian', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 21),
(7, '2024-11-22 01:02:43.515027', '1', 'GoogleLogin', 1, '[{\"added\": {}}]', 23, 16),
(8, '2024-11-22 01:27:59.198768', '1', 'LO IMPOSIBLE', 1, '[{\"added\": {}}]', 18, 16),
(9, '2024-11-22 01:28:30.636696', '2', 'VOLANDO', 1, '[{\"added\": {}}]', 18, 16),
(10, '2024-11-22 01:28:47.186166', '3', 'CLAVADA', 1, '[{\"added\": {}}]', 18, 16),
(11, '2024-11-22 22:50:35.705049', '4', 'prueba', 1, '[{\"added\": {}}]', 18, 21),
(12, '2024-11-22 22:51:48.280995', '5', 'tiro raro', 1, '[{\"added\": {}}]', 18, 21),
(13, '2024-11-22 23:18:30.204211', '1', 'LO IMPOSIBLE', 2, '[]', 18, 21),
(14, '2024-11-23 17:22:02.164076', '6', 'GOAT', 1, '[{\"added\": {}}]', 18, 21),
(15, '2024-11-23 17:22:28.998856', '7', 'TAPON', 1, '[{\"added\": {}}]', 18, 21),
(16, '2024-11-23 17:22:54.545388', '8', 'JUGADOR DEL AÑO', 1, '[{\"added\": {}}]', 18, 21);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(20, 'account', 'emailaddress'),
(21, 'account', 'emailconfirmation'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(17, 'basquetbol', 'campeon'),
(7, 'basquetbol', 'campeonato'),
(16, 'basquetbol', 'cuartos'),
(8, 'basquetbol', 'entrenador'),
(10, 'basquetbol', 'equipo'),
(9, 'basquetbol', 'estadio'),
(11, 'basquetbol', 'fase'),
(12, 'basquetbol', 'jugador'),
(13, 'basquetbol', 'partido'),
(14, 'basquetbol', 'partidoestadistica'),
(15, 'basquetbol', 'posicion'),
(18, 'basquetbol', 'video'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(19, 'sites', 'site'),
(22, 'socialaccount', 'socialaccount'),
(23, 'socialaccount', 'socialapp'),
(24, 'socialaccount', 'socialtoken');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-10-02 16:28:16.105530'),
(2, 'auth', '0001_initial', '2024-10-02 16:28:16.342750'),
(3, 'admin', '0001_initial', '2024-10-02 16:28:16.409257'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-10-02 16:28:16.414509'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-10-02 16:28:16.420613'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-10-02 16:28:16.459244'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-10-02 16:28:16.484051'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-10-02 16:28:16.500123'),
(9, 'auth', '0004_alter_user_username_opts', '2024-10-02 16:28:16.505168'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-10-02 16:28:16.529594'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-10-02 16:28:16.530606'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-10-02 16:28:16.536601'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-10-02 16:28:16.570118'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-10-02 16:28:16.585331'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-10-02 16:28:16.600283'),
(16, 'auth', '0011_update_proxy_permissions', '2024-10-02 16:28:16.606580'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-10-02 16:28:16.622539'),
(18, 'basquetbol', '0001_initial', '2024-10-02 16:28:16.786772'),
(19, 'sessions', '0001_initial', '2024-10-02 16:28:16.806431'),
(20, 'basquetbol', '0002_remove_equipo_estadio', '2024-10-04 15:05:28.639432'),
(21, 'basquetbol', '0003_entrenador_user', '2024-10-04 15:50:57.993492'),
(22, 'basquetbol', '0004_remove_equipo_redes_sociales_alter_entrenador_user_and_more', '2024-11-16 17:22:45.991842'),
(23, 'basquetbol', '0005_partido', '2024-11-16 17:22:46.071043'),
(24, 'basquetbol', '0006_partido_campeonato', '2024-11-16 17:33:25.902631'),
(25, 'basquetbol', '0007_remove_partido_campeonato', '2024-11-16 17:53:04.571498'),
(26, 'basquetbol', '0008_partido_campeonato', '2024-11-16 17:59:29.486151'),
(27, 'basquetbol', '0009_alter_equipo_campeonato_alter_equipo_color_principal_and_more', '2024-11-16 18:32:02.899022'),
(28, 'basquetbol', '0010_campeonato_equipos_alter_partido_campeonato', '2024-11-16 18:49:17.004359'),
(29, 'basquetbol', '0011_remove_campeonato_equipos', '2024-11-16 19:04:30.119050'),
(30, 'basquetbol', '0012_partidoestadistica', '2024-11-16 19:30:14.324415'),
(31, 'basquetbol', '0013_partidoestadistica_puntos_equipo_local_and_more', '2024-11-16 19:34:59.346848'),
(32, 'basquetbol', '0014_alter_campeonato_nombre_alter_partido_fecha', '2024-11-16 19:52:29.944427'),
(33, 'basquetbol', '0015_alter_partido_campeonato', '2024-11-16 20:14:20.130702'),
(34, 'basquetbol', '0016_posicion', '2024-11-16 20:31:55.209788'),
(35, 'basquetbol', '0017_posicion_campeonato_alter_posicion_equipo', '2024-11-16 20:44:52.270110'),
(36, 'basquetbol', '0018_alter_equipo_campeonato', '2024-11-18 16:41:20.181008'),
(37, 'basquetbol', '0019_rename_nombre_entrenador_nombre_entrenador_and_more', '2024-11-18 17:32:39.988540'),
(38, 'basquetbol', '0020_alter_posicion_campeonato_alter_posicion_equipo', '2024-11-18 22:10:44.669941'),
(39, 'basquetbol', '0021_equipo_activo', '2024-11-20 03:49:23.973113'),
(40, 'basquetbol', '0022_equipo_usuario', '2024-11-20 03:56:19.887078'),
(41, 'basquetbol', '0023_alter_entrenador_fecha_nacimiento', '2024-11-20 04:22:39.656679'),
(42, 'basquetbol', '0024_alter_jugador_posicion', '2024-11-20 13:43:18.809184'),
(43, 'basquetbol', '0025_remove_equipo_fundacion_remove_equipo_usuario', '2024-11-20 14:17:40.785279'),
(44, 'basquetbol', '0026_alter_posicion_unique_together', '2024-11-20 16:53:18.153925'),
(45, 'basquetbol', '0027_alter_posicion_unique_together', '2024-11-20 18:44:19.951522'),
(46, 'basquetbol', '0028_alter_posicion_unique_together', '2024-11-20 18:45:20.115237'),
(47, 'basquetbol', '0029_cuartos', '2024-11-20 21:24:06.554153'),
(48, 'basquetbol', '0030_equipo_campeon', '2024-11-21 02:14:58.404884'),
(49, 'basquetbol', '0031_alter_equipo_campeonato_campeon', '2024-11-21 02:32:30.728596'),
(50, 'account', '0001_initial', '2024-11-22 00:34:59.212674'),
(51, 'account', '0002_email_max_length', '2024-11-22 00:34:59.233739'),
(52, 'account', '0003_alter_emailaddress_create_unique_verified_email', '2024-11-22 00:34:59.262639'),
(53, 'account', '0004_alter_emailaddress_drop_unique_email', '2024-11-22 00:35:00.352116'),
(54, 'account', '0005_emailaddress_idx_upper_email', '2024-11-22 00:35:00.359821'),
(55, 'account', '0006_emailaddress_lower', '2024-11-22 00:35:00.379403'),
(56, 'account', '0007_emailaddress_idx_email', '2024-11-22 00:35:00.403880'),
(57, 'account', '0008_emailaddress_unique_primary_email_fixup', '2024-11-22 00:35:00.422580'),
(58, 'account', '0009_emailaddress_unique_primary_email', '2024-11-22 00:35:00.433683'),
(59, 'basquetbol', '0032_video', '2024-11-22 00:55:45.158435'),
(60, 'sites', '0001_initial', '2024-11-22 00:55:45.168506'),
(61, 'sites', '0002_alter_domain_unique', '2024-11-22 00:55:45.189692'),
(62, 'socialaccount', '0001_initial', '2024-11-22 00:55:45.399162'),
(63, 'socialaccount', '0002_token_max_lengths', '2024-11-22 00:55:45.447002'),
(64, 'socialaccount', '0003_extra_data_default_dict', '2024-11-22 00:55:45.454039'),
(65, 'socialaccount', '0004_app_provider_id_settings', '2024-11-22 00:55:45.520216'),
(66, 'socialaccount', '0005_socialtoken_nullable_app', '2024-11-22 00:55:45.875176'),
(67, 'socialaccount', '0006_alter_socialaccount_extra_data', '2024-11-22 00:55:45.912684');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1w8kwa8bq3cyyxw6uwjozmdxbznbche7', 'e30:1tDB3H:EqZDImG8w7HmE2Tu4-G8nI34IcNdEFcRXHzWmS4BUrc', '2024-12-02 23:21:03.127891'),
('5v9jgarw14xpwfj6znhwv7h11buu0gww', '.eJxVjDsOwyAQBe9CHSEw_5TpfQa0sEtwEmHJ2FWUu0dILpL2zcx7swjHXuPRaYsLsiubBLv8jgnyk9og-IB2X3le274tiQ-Fn7TzeUV63U7376BCr6O2FosFR7pkBYBCkaCSg5MBhQjBo5KBKGVvDEiptDW6aOchZVMmRezzBSnJOJ4:1tFJE6:fJJQHvqb7K1p7athSFfjTa2ETC1aiRJOrSfk-f6C1bg', '2024-12-08 20:29:02.778899'),
('cp8my5h3e0a56qthcsq3sbad9z1elg3n', '.eJxVjDsOwyAQBe9CHSEw_5TpfQa0sEtwEmHJ2FWUu0dILpL2zcx7swjHXuPRaYsLsiubBLv8jgnyk9og-IB2X3le274tiQ-Fn7TzeUV63U7376BCr6O2FosFR7pkBYBCkaCSg5MBhQjBo5KBKGVvDEiptDW6aOchZVMmRezzBSnJOJ4:1t6tMz:N8gY1-jS_qbOp9JpDMHBq7T-t0QQJ4IokdYQEkmkJLs', '2024-11-15 15:15:25.016840'),
('f5as8fh3r1p81x2tgr6ix17hbkvnnpxk', '.eJxVjDsOwjAQBe_iGlmOv1lKes5g7XodHEC2FCcV4u4QKQW0b2beS0Tc1hK3npc4szgLPYjT70iYHrnuhO9Yb02mVtdlJrkr8qBdXhvn5-Vw_w4K9vKtlVfO0oTkMAysNIALYTRgBj0mApcT6syBLACg0d7YnLx2ZppYETKI9wfu0jfe:1tFMcn:sCvm6cZA_MlrBNJH6ZjF0ObJFhdj3YvO2Dux3e98DGk', '2024-12-09 00:06:45.770128'),
('frwhe3vevgg49huy1f5tsuyl6nh8l655', '.eJxVjMEOwiAQRP-FsyFAKawevfsNZNkFqRpISnsy_rtt0oPeJvPezFsEXJcS1p7mMLG4iLM4_XYR6ZnqDviB9d4ktbrMU5S7Ig_a5a1xel0P9--gYC_b2rg8gjeafYyOyPgxI6YBPEJEjUDZRtgicXJWDy5rryxrMEol9laJzxf9Pzgv:1tCPhs:LzHtn1qHVTJ4Cbhj8xT_hgjLmX134px_qskDBuxVcow', '2024-11-30 20:47:48.510725'),
('ft9math7f37wu40msar54deguy6mfliz', '.eJxVjDsOwjAQBe_iGlmOv1lKes5g7XodHEC2FCcV4u4QKQW0b2beS0Tc1hK3npc4szgLPYjT70iYHrnuhO9Yb02mVtdlJrkr8qBdXhvn5-Vw_w4K9vKtlVfO0oTkMAysNIALYTRgBj0mApcT6syBLACg0d7YnLx2ZppYETKI9wfu0jfe:1t6tL7:4qc-2tOhrup_WOQmw5Qu9hzBS3f--0L9-uWiFP9m8ic', '2024-11-15 15:13:29.418982'),
('ijwh2uwxfahnmrzld1e8xue2zgu2rnwq', '.eJxVjDsOwjAQBe_iGlmOv1lKes5g7XodHEC2FCcV4u4QKQW0b2beS0Tc1hK3npc4szgLPYjT70iYHrnuhO9Yb02mVtdlJrkr8qBdXhvn5-Vw_w4K9vKtlVfO0oTkMAysNIALYTRgBj0mApcT6syBLACg0d7YnLx2ZppYETKI9wfu0jfe:1tDpt2:THlqAQvVySnfsVRR7-ytgI42PNWNyOagSKF0Qf5_yWc', '2024-12-04 18:57:12.611012'),
('k39e90cympk7za9j2g56rwrc6m9fzxdg', '.eJxVjMEOwiAQRP-FsyFAKawevfsNZNkFqRpISnsy_rtt0oPeJvPezFsEXJcS1p7mMLG4iLM4_XYR6ZnqDviB9d4ktbrMU5S7Ig_a5a1xel0P9--gYC_b2rg8gjeafYyOyPgxI6YBPEJEjUDZRtgicXJWDy5rryxrMEol9laJzxf9Pzgv:1tCPTN:9LCZPsS7Guh7rOP2jeDkImJ3CEnkNk8TkEsp1fnJK2o', '2024-11-30 20:32:49.932381'),
('p21sahxmi4lj0abzpug572nbmu02ml1j', 'e30:1tEIMj:Tdd_R8nfWUu3t8A1Gk8LV0CVukelN48iXK-8dFffwco', '2024-12-06 01:21:45.478134');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_site`
--

CREATE TABLE `django_site` (
  `id` int(11) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'http://127.0.0.1:8000/', 'localhost');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `socialaccount_socialaccount`
--

CREATE TABLE `socialaccount_socialaccount` (
  `id` int(11) NOT NULL,
  `provider` varchar(200) NOT NULL,
  `uid` varchar(191) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `extra_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`extra_data`)),
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `socialaccount_socialapp`
--

CREATE TABLE `socialaccount_socialapp` (
  `id` int(11) NOT NULL,
  `provider` varchar(30) NOT NULL,
  `name` varchar(40) NOT NULL,
  `client_id` varchar(191) NOT NULL,
  `secret` varchar(191) NOT NULL,
  `key` varchar(191) NOT NULL,
  `provider_id` varchar(200) NOT NULL,
  `settings` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL CHECK (json_valid(`settings`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `socialaccount_socialapp`
--

INSERT INTO `socialaccount_socialapp` (`id`, `provider`, `name`, `client_id`, `secret`, `key`, `provider_id`, `settings`) VALUES
(1, 'google', 'GoogleLogin', '687645987641-eq7o3ic502uf3likoa4fg4qalf2snvli.apps.googleusercontent.com', '687645987641-eq7o3ic502uf3likoa4fg4qalf2snvli.apps.googleusercontent.com', '', '', '{}');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `socialaccount_socialapp_sites`
--

CREATE TABLE `socialaccount_socialapp_sites` (
  `id` bigint(20) NOT NULL,
  `socialapp_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `socialaccount_socialapp_sites`
--

INSERT INTO `socialaccount_socialapp_sites` (`id`, `socialapp_id`, `site_id`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `socialaccount_socialtoken`
--

CREATE TABLE `socialaccount_socialtoken` (
  `id` int(11) NOT NULL,
  `token` longtext NOT NULL,
  `token_secret` longtext NOT NULL,
  `expires_at` datetime(6) DEFAULT NULL,
  `account_id` int(11) NOT NULL,
  `app_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account_emailaddress_user_id_email_987c8728_uniq` (`user_id`,`email`),
  ADD KEY `account_emailaddress_email_03be32b2` (`email`);

--
-- Indices de la tabla `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `key` (`key`),
  ADD KEY `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` (`email_address_id`);

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `basquetbol_campeon`
--
ALTER TABLE `basquetbol_campeon`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `campeonato_id` (`campeonato_id`),
  ADD KEY `basquetbol_campeon_equipo_id_4016c316_fk_basquetbol_equipo_id` (`equipo_id`);

--
-- Indices de la tabla `basquetbol_campeonato`
--
ALTER TABLE `basquetbol_campeonato`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `basquetbol_cuartos`
--
ALTER TABLE `basquetbol_cuartos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `basquetbol_cuartos_campeonato_id_189e66dd_fk_basquetbo` (`campeonato_id`),
  ADD KEY `basquetbol_cuartos_equipo_local_id_dbfecb3d_fk_basquetbo` (`equipo_local_id`),
  ADD KEY `basquetbol_cuartos_equipo_visitante_id_3c67480c_fk_basquetbo` (`equipo_visitante_id`),
  ADD KEY `basquetbol_cuartos_estadio_id_1b2f1373_fk_basquetbol_estadio_id` (`estadio_id`);

--
-- Indices de la tabla `basquetbol_entrenador`
--
ALTER TABLE `basquetbol_entrenador`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indices de la tabla `basquetbol_equipo`
--
ALTER TABLE `basquetbol_equipo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `entrenador_id` (`entrenador_id`),
  ADD KEY `basquetbol_equipo_campeonato_id_7b1c17be_fk_basquetbo` (`campeonato_id`),
  ADD KEY `basquetbol_equipo_campeon_id_d6775b76_fk_basquetbol_equipo_id` (`campeon_id`);

--
-- Indices de la tabla `basquetbol_estadio`
--
ALTER TABLE `basquetbol_estadio`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `basquetbol_fase`
--
ALTER TABLE `basquetbol_fase`
  ADD PRIMARY KEY (`id`),
  ADD KEY `basquetbol_fase_campeonato_id_52f4a462_fk_basquetbo` (`campeonato_id`);

--
-- Indices de la tabla `basquetbol_jugador`
--
ALTER TABLE `basquetbol_jugador`
  ADD PRIMARY KEY (`id`),
  ADD KEY `basquetbol_jugador_equipo_id_a3094891_fk_basquetbol_equipo_id` (`equipo_id`);

--
-- Indices de la tabla `basquetbol_partido`
--
ALTER TABLE `basquetbol_partido`
  ADD PRIMARY KEY (`id`),
  ADD KEY `basquetbol_partido_equipo_local_id_b3dbe6ec_fk_basquetbo` (`equipo_local_id`),
  ADD KEY `basquetbol_partido_equipo_visitante_id_4336744c_fk_basquetbo` (`equipo_visitante_id`),
  ADD KEY `basquetbol_partido_estadio_id_17709fcf_fk_basquetbol_estadio_id` (`estadio_id`),
  ADD KEY `basquetbol_partido_campeonato_id_f3b0847b_fk_basquetbo` (`campeonato_id`);

--
-- Indices de la tabla `basquetbol_partidoestadistica`
--
ALTER TABLE `basquetbol_partidoestadistica`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `partido_id` (`partido_id`);

--
-- Indices de la tabla `basquetbol_posicion`
--
ALTER TABLE `basquetbol_posicion`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `basquetbol_posicion_equipo_id_campeonato_id_6447d3fe_uniq` (`equipo_id`,`campeonato_id`),
  ADD KEY `basquetbol_posicion_equipo_id_37926ca8` (`equipo_id`),
  ADD KEY `basquetbol_posicion_campeonato_id_ada1b0ee_fk_basquetbo` (`campeonato_id`);

--
-- Indices de la tabla `basquetbol_video`
--
ALTER TABLE `basquetbol_video`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `django_site`
--
ALTER TABLE `django_site`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`);

--
-- Indices de la tabla `socialaccount_socialaccount`
--
ALTER TABLE `socialaccount_socialaccount`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `socialaccount_socialaccount_provider_uid_fc810c6e_uniq` (`provider`,`uid`),
  ADD KEY `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `socialaccount_socialapp`
--
ALTER TABLE `socialaccount_socialapp`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `socialaccount_socialapp_sites`
--
ALTER TABLE `socialaccount_socialapp_sites`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `socialaccount_socialapp_sites_socialapp_id_site_id_71a9a768_uniq` (`socialapp_id`,`site_id`),
  ADD KEY `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` (`site_id`);

--
-- Indices de la tabla `socialaccount_socialtoken`
--
ALTER TABLE `socialaccount_socialtoken`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq` (`app_id`,`account_id`),
  ADD KEY `socialaccount_social_account_id_951f210e_fk_socialacc` (`account_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `basquetbol_campeon`
--
ALTER TABLE `basquetbol_campeon`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `basquetbol_campeonato`
--
ALTER TABLE `basquetbol_campeonato`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `basquetbol_cuartos`
--
ALTER TABLE `basquetbol_cuartos`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `basquetbol_entrenador`
--
ALTER TABLE `basquetbol_entrenador`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT de la tabla `basquetbol_equipo`
--
ALTER TABLE `basquetbol_equipo`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT de la tabla `basquetbol_estadio`
--
ALTER TABLE `basquetbol_estadio`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `basquetbol_fase`
--
ALTER TABLE `basquetbol_fase`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `basquetbol_jugador`
--
ALTER TABLE `basquetbol_jugador`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=194;

--
-- AUTO_INCREMENT de la tabla `basquetbol_partido`
--
ALTER TABLE `basquetbol_partido`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=285;

--
-- AUTO_INCREMENT de la tabla `basquetbol_partidoestadistica`
--
ALTER TABLE `basquetbol_partidoestadistica`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=141;

--
-- AUTO_INCREMENT de la tabla `basquetbol_posicion`
--
ALTER TABLE `basquetbol_posicion`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de la tabla `basquetbol_video`
--
ALTER TABLE `basquetbol_video`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=68;

--
-- AUTO_INCREMENT de la tabla `django_site`
--
ALTER TABLE `django_site`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `socialaccount_socialaccount`
--
ALTER TABLE `socialaccount_socialaccount`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `socialaccount_socialapp`
--
ALTER TABLE `socialaccount_socialapp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `socialaccount_socialapp_sites`
--
ALTER TABLE `socialaccount_socialapp_sites`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `socialaccount_socialtoken`
--
ALTER TABLE `socialaccount_socialtoken`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `account_emailaddress`
--
ALTER TABLE `account_emailaddress`
  ADD CONSTRAINT `account_emailaddress_user_id_2c513194_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `account_emailconfirmation`
--
ALTER TABLE `account_emailconfirmation`
  ADD CONSTRAINT `account_emailconfirm_email_address_id_5b7f8c58_fk_account_e` FOREIGN KEY (`email_address_id`) REFERENCES `account_emailaddress` (`id`);

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `basquetbol_campeon`
--
ALTER TABLE `basquetbol_campeon`
  ADD CONSTRAINT `basquetbol_campeon_campeonato_id_4e4e955b_fk_basquetbo` FOREIGN KEY (`campeonato_id`) REFERENCES `basquetbol_campeonato` (`id`),
  ADD CONSTRAINT `basquetbol_campeon_equipo_id_4016c316_fk_basquetbol_equipo_id` FOREIGN KEY (`equipo_id`) REFERENCES `basquetbol_equipo` (`id`);

--
-- Filtros para la tabla `basquetbol_cuartos`
--
ALTER TABLE `basquetbol_cuartos`
  ADD CONSTRAINT `basquetbol_cuartos_campeonato_id_189e66dd_fk_basquetbo` FOREIGN KEY (`campeonato_id`) REFERENCES `basquetbol_campeonato` (`id`),
  ADD CONSTRAINT `basquetbol_cuartos_equipo_local_id_dbfecb3d_fk_basquetbo` FOREIGN KEY (`equipo_local_id`) REFERENCES `basquetbol_equipo` (`id`),
  ADD CONSTRAINT `basquetbol_cuartos_equipo_visitante_id_3c67480c_fk_basquetbo` FOREIGN KEY (`equipo_visitante_id`) REFERENCES `basquetbol_equipo` (`id`),
  ADD CONSTRAINT `basquetbol_cuartos_estadio_id_1b2f1373_fk_basquetbol_estadio_id` FOREIGN KEY (`estadio_id`) REFERENCES `basquetbol_estadio` (`id`);

--
-- Filtros para la tabla `basquetbol_entrenador`
--
ALTER TABLE `basquetbol_entrenador`
  ADD CONSTRAINT `basquetbol_entrenador_user_id_5608015e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `basquetbol_equipo`
--
ALTER TABLE `basquetbol_equipo`
  ADD CONSTRAINT `basquetbol_equipo_campeon_id_d6775b76_fk_basquetbol_equipo_id` FOREIGN KEY (`campeon_id`) REFERENCES `basquetbol_equipo` (`id`),
  ADD CONSTRAINT `basquetbol_equipo_campeonato_id_7b1c17be_fk_basquetbo` FOREIGN KEY (`campeonato_id`) REFERENCES `basquetbol_campeonato` (`id`),
  ADD CONSTRAINT `basquetbol_equipo_entrenador_id_1b4eb147_fk_basquetbo` FOREIGN KEY (`entrenador_id`) REFERENCES `basquetbol_entrenador` (`id`);

--
-- Filtros para la tabla `basquetbol_fase`
--
ALTER TABLE `basquetbol_fase`
  ADD CONSTRAINT `basquetbol_fase_campeonato_id_52f4a462_fk_basquetbo` FOREIGN KEY (`campeonato_id`) REFERENCES `basquetbol_campeonato` (`id`);

--
-- Filtros para la tabla `basquetbol_jugador`
--
ALTER TABLE `basquetbol_jugador`
  ADD CONSTRAINT `basquetbol_jugador_equipo_id_a3094891_fk_basquetbol_equipo_id` FOREIGN KEY (`equipo_id`) REFERENCES `basquetbol_equipo` (`id`);

--
-- Filtros para la tabla `basquetbol_partido`
--
ALTER TABLE `basquetbol_partido`
  ADD CONSTRAINT `basquetbol_partido_campeonato_id_f3b0847b_fk_basquetbo` FOREIGN KEY (`campeonato_id`) REFERENCES `basquetbol_campeonato` (`id`),
  ADD CONSTRAINT `basquetbol_partido_equipo_local_id_b3dbe6ec_fk_basquetbo` FOREIGN KEY (`equipo_local_id`) REFERENCES `basquetbol_equipo` (`id`),
  ADD CONSTRAINT `basquetbol_partido_equipo_visitante_id_4336744c_fk_basquetbo` FOREIGN KEY (`equipo_visitante_id`) REFERENCES `basquetbol_equipo` (`id`),
  ADD CONSTRAINT `basquetbol_partido_estadio_id_17709fcf_fk_basquetbol_estadio_id` FOREIGN KEY (`estadio_id`) REFERENCES `basquetbol_estadio` (`id`);

--
-- Filtros para la tabla `basquetbol_partidoestadistica`
--
ALTER TABLE `basquetbol_partidoestadistica`
  ADD CONSTRAINT `basquetbol_partidoes_partido_id_ac6920e4_fk_basquetbo` FOREIGN KEY (`partido_id`) REFERENCES `basquetbol_partido` (`id`);

--
-- Filtros para la tabla `basquetbol_posicion`
--
ALTER TABLE `basquetbol_posicion`
  ADD CONSTRAINT `basquetbol_posicion_campeonato_id_ada1b0ee_fk_basquetbo` FOREIGN KEY (`campeonato_id`) REFERENCES `basquetbol_campeonato` (`id`),
  ADD CONSTRAINT `basquetbol_posicion_equipo_id_37926ca8_fk_basquetbol_equipo_id` FOREIGN KEY (`equipo_id`) REFERENCES `basquetbol_equipo` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `socialaccount_socialaccount`
--
ALTER TABLE `socialaccount_socialaccount`
  ADD CONSTRAINT `socialaccount_socialaccount_user_id_8146e70c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `socialaccount_socialapp_sites`
--
ALTER TABLE `socialaccount_socialapp_sites`
  ADD CONSTRAINT `socialaccount_social_socialapp_id_97fb6e7d_fk_socialacc` FOREIGN KEY (`socialapp_id`) REFERENCES `socialaccount_socialapp` (`id`),
  ADD CONSTRAINT `socialaccount_socialapp_sites_site_id_2579dee5_fk_django_site_id` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`);

--
-- Filtros para la tabla `socialaccount_socialtoken`
--
ALTER TABLE `socialaccount_socialtoken`
  ADD CONSTRAINT `socialaccount_social_account_id_951f210e_fk_socialacc` FOREIGN KEY (`account_id`) REFERENCES `socialaccount_socialaccount` (`id`),
  ADD CONSTRAINT `socialaccount_social_app_id_636a42d7_fk_socialacc` FOREIGN KEY (`app_id`) REFERENCES `socialaccount_socialapp` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
