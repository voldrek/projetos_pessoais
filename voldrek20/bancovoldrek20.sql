create database voldrek20 default charset = utf8;
set sql_safe_updates = 0;

create table login
(
	id int unsigned not null auto_increment,
    nome varchar (45) not null,
    senha varchar (10) not null,
    email varchar (25) not null,
    primary key (id)
);

