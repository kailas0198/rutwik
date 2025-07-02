create database student_raw1;

use student_raw1;

create table student(name varchar(50),email varchar(50) unique,age int check (age<=18) );

select * from student;