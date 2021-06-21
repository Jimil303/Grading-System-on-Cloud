# Grading-System-on-Cloud

using postgres as the database, run the following queries

create table university(
  name varchar(75),
  username varchar(40),
  password varchar(50),
  
  primary key (name)
)

create table faculty_credentials(
	username varchar(50),
	password varchar(100),
	infoadded bool,
	university varchar(75),
	primary key(username),
	foreign key(university) references university(name)
)
