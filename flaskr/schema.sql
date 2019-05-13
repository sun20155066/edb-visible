CREATE DATABASE IF NOT EXISTS edb CHARACTER SET utf8 COLLATE utf8_general_ci;
DROP TABLE IF EXISTS user;
CREATE TABLE user (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username varchar(10) UNIQUE NOT NULL,
  password varchar(200) NOT NULL
);
