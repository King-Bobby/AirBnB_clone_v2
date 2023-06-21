-- This script MySQL setup development for:
-- A database hbnb_dev_db
-- A new user hbnb_dev (in localhost)
--
-- The password of hbnb_dev is set to hbnb_dev__pwd
-- The hbnb_dev has all privileges on the database hbnb_test_db
-- The hbnb_dev has SELECT privilege on the database performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
