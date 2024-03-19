-- script that prepares a MySQL server by creating a user and granting privileges.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGE ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
GRANT SELECT  ON performance_schema . * TO 'hbnb_dev'@'localhost';
