-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-11-2024 a las 00:53:10
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
-- Base de datos: `basquetbol_torneo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
(48, 'Can view jugador', 12, 'view_jugador');

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
(1, 'pbkdf2_sha256$870000$SL4gihqa6JDkNTjdE2D9nJ$VuCFkYy0W4eh+4WTAqFmfpOcUKw1cMwQUA5H1H81Ll8=', '2024-10-14 01:25:39.093324', 0, 'fabian', '', '', 'fabian.cardinaletp@gmail.com', 0, 1, '2024-10-03 13:05:51.820784'),
(2, 'pbkdf2_sha256$320000$mmfglOQKlgFfDF6kR90xHo$gO4WVPW+sRQHyqX58T84kegaB58pmFQ6UsLJ7xo/ylg=', '2024-11-17 23:30:53.923412', 1, 'thomassalazar', '', '', 'fabian.cardinaletp@gmail.com', 1, 1, '2024-10-04 16:28:28.277475'),
(3, 'pbkdf2_sha256$870000$iRwtOF8GmD2Rceuh2jQh3a$lCMokDAb/IdiDGsg7HMu3t1UTPPq5cJEy5wlSDsgShA=', '2024-10-04 19:35:17.229319', 0, 'thomas', '', '', 'thomas@gmail.com', 0, 1, '2024-10-04 19:35:16.615441'),
(4, 'pbkdf2_sha256$870000$SMUgWRvQFt88EJWjApqiOp$3PPz1X4VE3lGbObJDBDCi03WMuWfJfovi6x+9+1NHLU=', '2024-10-09 14:36:22.224180', 0, 'Keiji', '', '', 'keiji@gmail.com', 0, 1, '2024-10-09 14:36:21.615443'),
(5, 'pbkdf2_sha256$870000$1tYIRVUU2IZHT5JLR0Fn8D$rdUdXraLkmk1fUmUlLXYOO7WR1YTVqgJh2NSKWUns/c=', '2024-10-09 15:01:09.507106', 0, 'wally', '', '', 'wally@gmail.com', 0, 1, '2024-10-09 15:01:08.923380');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
-- Estructura de tabla para la tabla `basquetbol_campeonato`
--

CREATE TABLE `basquetbol_campeonato` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
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
(1, 'Campeonato statsportiva', '2024-12-12', '2024-12-12', 'dfsdfsdfs', 10, 'sdsdfsdfsdf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `basquetbol_entrenador`
--

CREATE TABLE `basquetbol_entrenador` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `nacionalidad` varchar(50) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `basquetbol_entrenador`
--

INSERT INTO `basquetbol_entrenador` (`id`, `nombre`, `nacionalidad`, `fecha_nacimiento`, `user_id`) VALUES
(6, 'keii', 'boliviano', '2005-05-05', 2),
(7, 'El tirgre gareca', 'argentino', '2005-05-05', 3),
(21, 'Keiji', 'Japones', '2005-05-05', 4),
(22, 'wally', 'gorda', '1900-05-05', 5),
(23, 'wally', 'gorda', '1900-05-05', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `basquetbol_equipo`
--

CREATE TABLE `basquetbol_equipo` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `fundacion` date NOT NULL,
  `historia` longtext DEFAULT NULL,
  `color_principal` varchar(7) NOT NULL,
  `color_secundario` varchar(7) NOT NULL,
  `logo` varchar(100) DEFAULT NULL,
  `sitio_web` varchar(200) DEFAULT NULL,
  `campeonato_id` bigint(20) NOT NULL,
  `entrenador_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `basquetbol_equipo`
--

INSERT INTO `basquetbol_equipo` (`id`, `nombre`, `fundacion`, `historia`, `color_principal`, `color_secundario`, `logo`, `sitio_web`, `campeonato_id`, `entrenador_id`) VALUES
(7, 'Chile', '2024-10-01', 'dklasdkasm', '#ff0000', '#ffffff', 'logos_equipos/logo_transparent_background_9YACqs2.png', 'http://127.0.0.1:8000/inscribir_eq', 1, 7),
(13, 'japon', '2024-10-01', 'sda', '#0033ff', '#ffffff', 'logos_equipos/logo_transparent_background_cezGz3j.png', 'http://127.0.0.1:8000/inscribir_eq', 1, 21),
(14, 'gorditos fc', '0000-00-00', 'evaaa', '#f4d2d2', '#6f0daf', 'logos_equipos/logo_transparent_background_oBTlyYD.png', NULL, 1, 22),
(15, 'wally', '2024-10-01', 'lmkmk', '#000000', '#000000', '', NULL, 1, 23);

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
  `posicion` varchar(50) NOT NULL,
  `numero` int(10) UNSIGNED NOT NULL CHECK (`numero` >= 0),
  `equipo_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `basquetbol_jugador`
--

INSERT INTO `basquetbol_jugador` (`id`, `nombre`, `posicion`, `numero`, `equipo_id`) VALUES
(26, 'juan', 'alero', 1, 7),
(27, 'Thomato', 'defensa', 12, 7),
(40, 'keii', 'a', 1, 13),
(41, 'pepe', 'pepe', 45, 13),
(42, 'thomas', 'golpeador', 7, 13),
(43, 'wally', 'comelona', 0, 14),
(44, 'Thomato', 'esposo', 1, 14),
(46, 'wally', 'comelona', 0, 15);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `basquetbol_video`
--

CREATE TABLE `basquetbol_video` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `url` varchar(2083) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `basquetbol_video`
--

INSERT INTO `basquetbol_video` (`id`, `title`, `url`) VALUES
(1, 'michael', 'https://www.youtube.com/shorts/dfoCBTMe8sI'),
(3, 'tiro exotico', 'https://www.youtube.com/shorts/-524ku1zdkc'),
(5, 'tiro pete', 'https://www.youtube.com/shorts/Z5O4ooDy4qw');

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
(1, '2024-11-17 00:16:42.649671', '1', 'michael', 1, '[{\"added\": {}}]', 13, 2),
(2, '2024-11-17 00:18:10.486078', '2', 'lebron', 1, '[{\"added\": {}}]', 13, 2),
(3, '2024-11-17 00:18:53.397670', '3', 'tiro exotico', 1, '[{\"added\": {}}]', 13, 2),
(4, '2024-11-17 23:38:46.509519', '4', 'https://www.youtube.com/watch?v=C3-riALJTvo', 1, '[{\"added\": {}}]', 13, 2),
(5, '2024-11-17 23:47:36.035072', '2', 'lebron', 3, '', 13, 2),
(6, '2024-11-17 23:47:50.533333', '5', 'tiro pete', 1, '[{\"added\": {}}]', 13, 2);

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
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(7, 'basquetbol', 'campeonato'),
(8, 'basquetbol', 'entrenador'),
(10, 'basquetbol', 'equipo'),
(9, 'basquetbol', 'estadio'),
(11, 'basquetbol', 'fase'),
(12, 'basquetbol', 'jugador'),
(13, 'basquetbol', 'video'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

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
(22, 'basquetbol', '0004_auto_20241115_1156', '2024-11-17 01:41:55.339427');

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
('6nnx5h0790lv6cx6bbpvif1y5ildz2ay', '.eJxVjDkOwjAUBe_iGlle4uVT0ucM1veGA8iW4qRC3B1HSgHtzLz3Jg73rbi9p9UtkVyJIJdf5jE8Uz1EfGC9Nxpa3dbF0yOhp-10bjG9bmf7d1Cwl7E2XKCXKjPJhbQGdFZoQ9QBsoQJhE08Q54ApOTKMjNAVp4prQzHUZHPF7qvNqk:1tCojF:2cS8i1w4pH7XQrJ85ik4VwZ2D_dMdDn5-mWZUthIp0Q', '2024-12-01 23:30:53.926572');

--
-- Índices para tablas volcadas
--

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
-- Indices de la tabla `basquetbol_campeonato`
--
ALTER TABLE `basquetbol_campeonato`
  ADD PRIMARY KEY (`id`);

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
  ADD KEY `basquetbol_equipo_campeonato_id_7b1c17be_fk_basquetbo` (`campeonato_id`);

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
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `basquetbol_campeonato`
--
ALTER TABLE `basquetbol_campeonato`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `basquetbol_entrenador`
--
ALTER TABLE `basquetbol_entrenador`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `basquetbol_equipo`
--
ALTER TABLE `basquetbol_equipo`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `basquetbol_estadio`
--
ALTER TABLE `basquetbol_estadio`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `basquetbol_fase`
--
ALTER TABLE `basquetbol_fase`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `basquetbol_jugador`
--
ALTER TABLE `basquetbol_jugador`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT de la tabla `basquetbol_video`
--
ALTER TABLE `basquetbol_video`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Restricciones para tablas volcadas
--

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
-- Filtros para la tabla `basquetbol_entrenador`
--
ALTER TABLE `basquetbol_entrenador`
  ADD CONSTRAINT `basquetbol_entrenador_user_id_5608015e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `basquetbol_equipo`
--
ALTER TABLE `basquetbol_equipo`
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
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
