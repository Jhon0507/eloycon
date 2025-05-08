DROP DATABASE IF EXISTS EloyCon;
CREATE DATABASE EloyCon;

USE EloyCon;

CREATE TABLE clientes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellidos VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    direccion VARCHAR(255) NOT NULL,
    telefono VARCHAR(255),
    ciudad VARCHAR(255),
    usuario VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(510) NOT NULL,
    fecha_registro DATETIME DEFAULT NOW()
);

CREATE TABLE proyectos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    nombre VARCHAR(255),
    ciudad VARCHAR(255),
    fecha_inicio DATETIME NOT NULL,
    fecha_final_estimada DATETIME NOT NULL,
    fecha_final_real DATETIME,
    estado ENUM('En revisión', 'En desarrollo', 'Terminado'),
    presupuesto DECIMAL(13, 2),

    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE imagenes_proyectos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(510) NOT NULL UNIQUE,
    tipo VARCHAR(255),
    id_proyecto INT,

    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE traducciones(
    id INT AUTO_INCREMENT PRIMARY KEY,
    clave VARCHAR(50) NOT NULL UNIQUE,
    es VARCHAR(1500) NOT NULL,
    en VARCHAR(1500) NOT NULL,
    id_proyecto INT,

    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE Table empleados(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellidos VARCHAR(255) NOT NULL,
    fecha_nacimiento DATETIME,
    email VARCHAR(255) NOT NULL UNIQUE,
    dni VARCHAR(25) NOT NULL UNIQUE,
    telefono VARCHAR(255),
    antiguedad INT, -- sera en meses
    nacionalidad VARCHAR(50),
    profesion VARCHAR(255),
    departamento VARCHAR(255),
    url_foto VARCHAR(510),
    direccion VARCHAR(255),
    usuario VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(510) NOT NULL UNIQUE 
);

CREATE TABLE proyecto_empleados(
    id_proyecto INT NOT NULL,
    id_empleados INT NOT NULL,
    tipo_servicio ENUM('construccion', 'reforma'),

    PRIMARY KEY (id_proyecto, id_empleados),
    FOREIGN KEY (id_proyecto) REFERENCES proyectos(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (id_empleados) REFERENCES empleados(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE peticiones_contacto(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    apellidos VARCHAR(255),
    email VARCHAR(255),
    localidad VARCHAR(255),
    servicio VARCHAR(255),
    idea VARCHAR(1500),
    estado ENUM('pendiente', 'en proceso', 'aceptado', 'en espera', 'rechazada') DEFAULT 'pendiente'
);