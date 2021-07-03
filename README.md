# Grading-System-on-Cloud
## Outline  :
#### This  project  aims  to make the job of for students and colleges around the world by providing a universal platform for all.

## Features  and  Pages :
#### 1. Log In / Sign Up - The  student/faculty  can  login into his / her  account  on  the  website  by  entering  required  details  provided by the Admin of the respective college.
<p float="left">
  <img src="https://user-images.githubusercontent.com/35409637/124342844-b701e500-dbcf-11eb-8442-fe79a83f1032.png" width="400"/>
<img src="https://user-images.githubusercontent.com/35409637/124342878-f03a5500-dbcf-11eb-8f2c-770958b378cf.png" width="400"/>
</p>

### Admin Pages : 

1. Search Page:  This  page allows the admin to search the complete database under their institution to check/alter/update/delete records of students and faculties.
<p float="left">
  <img src="https://user-images.githubusercontent.com/35409637/124342969-b7e74680-dbd0-11eb-8332-b8942d0b0d79.png" width="1792"/>
</p>
2. Register Users :  This  page lets the admin add a new list of students/faculties or take singular entries for the same.c
<p float="left">
  <img src="https://user-images.githubusercontent.com/45822642/117270246-a1459d00-ae76-11eb-8fa4-91f4a0fe1225.jpeg" width="400">
</p>


## Datbase :
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
