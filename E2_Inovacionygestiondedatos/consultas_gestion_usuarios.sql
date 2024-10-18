-- crear la base de datos 
create database gestion_usuarios;
use gestion_usuarios;

-- crear la tabla usuario
create table usuario (
	id int auto_increment primary key ,
    username varchar(50) not null,
    password varchar(255) not null,
    email varchar(100) not null
);

-- Crear la tabla Acceso
create table Acceso (
	id int auto_increment primary key,
    fechaIngreso datetime not null,
    fechaSalida datetime,
    usuarioLogueado int,
    foreign key (usuarioLogueado) references Usuario(id) on delete cascade
);

-- Insertar datos de prueba
-- Insertar datos en la tabla usuario 
insert into usuario (username, password, email)
values
('user1', 'passwoed1', 'user1@example.com'),
('user2', 'password2', 'user2@example.com');

-- Insertar datos en la tabla acceso 
insert into Acceso (fechaIngreso, fechaSalida, usuarioLogueado)
values
('2024-10-10 08:00:00', '2024-10-10 17:00:00', 1),
('2024-10-11 09:00:00', '2024-10-11 18:00:00', 1),
('2024-10-12 08:30:00', '2024-10-12 16:30:00', 2);

-- Consultas SQL (CRUD)

-- SELECT
-- Seleccionar todos los ususrios con sus accesesos 
select u.id, u.username, a.fechaIngreso, a.fechaSalida
from usuario u
left join Acceso a on u.id = a.usuarioLogueado;

-- INSERT
insert into usuario (username, password, email)
values ('user3', 'password3', 'user3@example.com');

-- UPDATE
-- Actualizar la contraseña de un usuario 
update usuario
set password = "newpassword"
where id = 1;


-- DELETE 
-- Eliminar un acceso especifico 
delete from Acceso
where id = 2;

-- Consultas JOIN
-- Obtener los accesos y sus usuarios asociados
select u.username, a.fechaIngreso, a.fechaSalida
from Acceso a
join usuario u on a.usuarioLogueado = u.id;

-- Obtener los usuarios que tienen mas de un acceso
select u.username, count(a.id) as num_accesos
from usuario u
join Acceso a on u.id = a.usuariologueado
group by u.username
having count(a.id) > 1;


