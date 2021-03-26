
CREATE DATABASE phoneDB;

use phoneDB;


CREATE TABLE  category_tbl (
categoryID int(11) NOT NULL AUTO_INCREMENT,
category_type_id int(11) NOT NULL,
category_name varchar(100) NOT NULL,
category_status varchar(50),
);

CREATE TABLE  catalog_tbl (
category_type_id int (11) NOT NULL AUTO_INCREMENT,
catalogID varchar(50) NOT NULL,
phone_name varchar(50) NOT NULL,
phone_description varchar(100) NOT NULL,
phone_features varchar(50) NOT NULL,
phone_dimension varchar(50) NOT NULL,
phone_price float NOT NULL,
weigh_height_widith varchar(50) NOT NULL,
phone_availability varchar(50) NOT NULL,
phone_color varchar(50) NOT NULL,
FOREIGN KEY(category_type_id) REFERENCES category_tbl(category_type_id)
);


CREATE TABLE customer_tbl (
customer_id int(11) NOT NULL AUTO_INCREMENT,
customer_first_name varchar(30) NOT NULL,
customer_last_name varchar(30) NOT NULL,
customer_middle_name varchar(30) NOT NULL,
customer_email varchar(50) NOT NULL UNIQUE,
customer_phone_number varchar(15) NOT NULL UNIQUE,
customer_username varchar(30) NOT NULL UNIQUE,
customer_password varchar(30) NOT NULL UNIQUE,
account_status varchar(10) NOT NULL,
customer_order_date DATE,
PRIMARY KEY (`customer_id`)
);


CREATE TABLE admins_tbl (
admins_id int(11) NOT NULL AUTO_INCREMENT,
full_name varchar(100) NOT NULL UNIQUE,
admin_contact varchar(50) NOT NULL UNIQUE,
admin_email varchar(50) NOT NULL UNIQUE,
admins_username varchar(30) NOT NULL UNIQUE,
admins_password varchar(30) NOT NULL UNIQUE,
PRIMARY KEY (`admins_id`)
);


CREATE TABLE  order_tbl (
order_id int(11) NOT NULL AUTO_INCREMENT,
customer_id int(11) NOT NULL,
total_amount float NOT NULL,
order_status int(1) NOT NULL,
sold_by int(11) NOT NULL,
sold_order_date DATE,
PRIMARY KEY (`order_id`),
KEY `customer_id` (`customer_id`,`sold_by`),
KEY `sold_by` (`sold_by`)
);



CREATE TABLE orderdetails_tbl (
order_details_id int(11) NOT NULL AUTO_INCREMENT,
order_id int(11) NOT NULL,
categoryID int(11) NOT NULL,
amount float NOT NULL,
no_of_items int(4) NOT NULL,
total_amount float NOT NULL,
PRIMARY KEY (`order_details_id`),
KEY `order_id` (`order_id`,`categoryID`),
KEY `categoryID` (`categoryID`)
);



CREATE TABLE  payment_tbl (
payment_id int(11) NOT NULL AUTO_INCREMENT,
order_id int(11) NOT NULL,
amount float NOT NULL,
paid_by varchar(50) NOT NULL,
payment_date  DATE,
sold_by int(11) NOT NULL,
PRIMARY KEY (`payment_id`),
KEY `order_id` (`order_id`,`sold_by`),
KEY `sold_by` (`sold_by`)
);


CREATE TABLE addresses_tbl(
address_id int(50) NOT NULL AUTO_INCREMENT,
order_details_id varchar (50) NOT NULL,
line_1 varchar(80) NOT NULL,
line_2 varchar (50) NOT NULL,
city_name varchar(50) NOT NULL,
post_code varchar(50) NOT NULL,
customer_id int (50) NOT NULL,
PRIMARY KEY (`address_id`),
KEY (`customer_id`),
KEY (`order_details_id`)
);


CREATE TABLE order_delivery_tbl (
order_delivery_id int(50)  NOT NULL AUTO_INCREMENT,
admins_id varchar (50) NOT NULL,
order_details_id int(50) NOT NULL,
customer_id int(50) NOT NULL,
delivery_status_code int(50) NOT NULL,
delivery_address varchar(50) NOT NULL,
delivery_type varchar (50) NOT NULL,
delivery_by varchar (50) NOT NULL,
delivery_time_and_date DATE,
address_id int (50),
PRIMARY KEY (`order_delivery_id`),
KEY `order_details_id` (`order_details_id`,`delivery_by`)
);

 
CREATE TABLE  odernotes_feedback_tbl (
feedback_id int(11) NOT NULL AUTO_INCREMENT,
categoryID int(11) NOT NULL,
delivery_service int(1) NOT NULL,
customer_remarks varchar(100) NOT NULL,
date_recorded date NOT NULL,
customer_id int(11) NOT NULL,
PRIMARY KEY (`feedback_id`),
KEY `categoryID` (`categoryID`),
KEY `customer_id` (`customer_id`)
);



CREATE TABLE IF NOT EXISTS `tblrating` (
`rating_id` int(11) NOT NULL AUTO_INCREMENT,
`menu_id` int(11) NOT NULL,
`score` int(1) NOT NULL,
`remarks` varchar(100) NOT NULL,
`date_recorded` date NOT NULL,
`customer_id` int(11) NOT NULL,
PRIMARY KEY (`rating_id`),
KEY `menu_id` (`menu_id`),
KEY `customer_id` (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;




