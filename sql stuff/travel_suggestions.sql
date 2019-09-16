CREATE TABLE destination
(
	id int AUTO_INCREMENT PRIMARY KEY,
	country varchar(50) NOT NULL,
	city varchar(50) NOT NULL,
);

CREATE TABLE activities
(
	id int AUTO_INCREMENT PRIMARY KEY,
	name varchar(50) NOT NULL,
	type varchar(50),
	location varchar(50) NOT NULL,
	transport varchar(50),
	cost float
);

CREATE TABLE transport
(
	id int AUTO_INCREMENT PRIMARY KEY,
	name varchar(50),
	type varchar(50),
	start_location varchar(50),
	end_location varchar(50),
	cost float,
	travel_time varchar(50)
);

CREATE TABLE food_and_drink
(
	id int AUTO_INCREMENT PRIMARY KEY,
	name varchar(50) NOT NULL,
	type varchar(50) NOT NULL,
	cuisine varchar(50),
	location varchar(50),
	price varchar(50),
	tranport varchar(50)
);

CREATE TABLE trip_details (
	accommodation_name varchar(50),
	accommodation_address varchar(50),
	date_of_arrival datetime,
	date_of_departure datetime
);

INSERT INTO destination VALUES(1, "Berlin", "Germany");
INSERT INTO destination VALUES(2, "Madrid", "Spain");
INSERT INTO destination VALUES(3, "London", "England");
INSERT INTO destination VALUES(4, "Edinburgh", "Scotland");
INSERT INTO destination VALUES(5, "Amsterdam", "Netherlands");
INSERT INTO destination VALUES(6, "Prague", "Czech Republic");
INSERT INTO destination VALUES(7, "Dublin", "Republic of Ireland");
INSERT INTO destination VALUES(8, "Belfast", "Northern Ireland");
INSERT INTO destination VALUES(9, "Warsaw", "Poland");
INSERT INTO destination VALUES(10, "Helsinki", "Finland");
INSERT INTO destination VALUES(11, "Budapest", "Hungary");
INSERT INTO destination VALUES(12, "Skywoods", "Singapore");
INSERT INTO destination VALUES(13, "New York", "United States");
INSERT INTO destination VALUES(14, "Aleppo", "Syria");
INSERT INTO destination VALUES(15, "Ontario", "Canada");
INSERT INTO destination VALUES(16, "Sydney", "Australia");

ALTER TABLE activities ADD destination_id int;
ALTER TABLE transport ADD destination_id int;
ALTER TABLE food_and_drink ADD destination_id int;
ALTER TABLE trip_details ADD destination_id int;
