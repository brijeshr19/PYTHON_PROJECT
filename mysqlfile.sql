show databases;

create database telusko;
#location of this SQL script is C:\Users\Administrator\PycharmProjects\PYTHON_SANDBOX_FINISHED_TRAVERSYMEDIACRASHCOURSE
use telusko;

show tables;

create table student (name varchar(20),college varchar(20));

insert into student values ('Navin','vsit'), ('Priya','bvit');

select * from student;