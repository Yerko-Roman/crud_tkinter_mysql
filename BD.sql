#Crear la BD

create database USUARIO;

#Seleccionar la BD creada

use USUARIO;

#Crear las tablas

create table REGIONES(
	ID_REGION int  not null,
    NOMBRE varchar(80) not null,
    primary key(ID_REGION));
    
create table COMUNAS(
	ID_COMUNA int not null,
    NOMBRE varchar(100) not null,
    ID_REGION int not null,
    primary key(ID_COMUNA),
    foreign key(ID_REGION) references REGIONES(ID_REGION));

create table SEXO(
	ID_SEXO int not null,
    SEXO varchar(20) not null,
    primary key(ID_SEXO));
    
create table ESTADO(
	ID_ESTADO int not null,
    ESTADO varchar(20) not null,
    primary key(ID_ESTADO));
    
create table USUARIOS(
	ID_USUARIO int not null auto_increment,
    RUT varchar(14) not null unique,
    NOMBRE varchar(50) not null,
    APELLIDO varchar(50) not null,
    CORREO varchar(80) unique,
    TELEFONO varchar(14) not null unique,
    FECHA_INGRESO date,
    ID_SEXO int not null,
    ID_ESTADO int not null,
    ID_REGION int not null,
    ID_COMUNA int not null,
    DIRECCION_CIUDAD varchar(70) not null,
    primary key(ID_USUARIO),
    foreign key (ID_REGION) references REGIONES(ID_REGION),
    foreign key (ID_COMUNA) references COMUNAS(ID_COMUNA),
    foreign key (ID_SEXO) references SEXO(ID_SEXO),
    foreign key (ID_ESTADO) references ESTADO(ID_ESTADO));

#Rellenar la tabla sexo y estado con sus datos.
    
insert into SEXO value ("1" , "Hombre");
insert into SEXO value ("2" , "Mujer");

insert into Estado value ("1", "Activo");
insert into Estado value ("2", "Desactivo");