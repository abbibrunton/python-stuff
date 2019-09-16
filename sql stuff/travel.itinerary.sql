CREATE TABLE users
(
	id int(3) PRIMARY KEY,
	username varchar(10),
	password varchar(10)
);

CREATE TABLE destination
(
	id int AUTO_INCREMENT PRIMARY KEY,
	city varchar(50) NOT NULL,
	country varchar(50) NOT NULL,
	foreign key (uid) references users(id)
);

CREATE TABLE activities
(
	id int AUTO_INCREMENT PRIMARY KEY,
	name varchar(50) NOT NULL,
	type varchar(50),
	location varchar(50) NOT NULL,
	transport varchar(50),
	cost float,
	foreign key (uid) references users(id)
);

CREATE TABLE transport
(
	id int AUTO_INCREMENT PRIMARY KEY,
	name varchar(50),
	type varchar(50),
	start_location varchar(50),
	end_location varchar(50),
	cost float,
	travel_time varchar(50),
	foreign key (uid) references users(id)
);

CREATE TABLE food_and_drink
(
	id int AUTO_INCREMENT PRIMARY KEY,
	name varchar(50) NOT NULL,
	type varchar(50) NOT NULL,
	cuisine varchar(50),
	location varchar(50),
	price varchar(50),
	tranport varchar(50),
	foreign key (uid) references users(id)
);

CREATE TABLE details
(
	id int PRIMARY KEY,
	accommodation_name varchar(50),
	accommodation_address varchar(50),
	date_of_arrival datetime,
	date_of_departure datetime,
	foreign key (uid) references users(id)
);