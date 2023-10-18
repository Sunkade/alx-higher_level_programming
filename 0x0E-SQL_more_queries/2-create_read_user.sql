-- Check if the database already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Check if the user already exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'%' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the hbtn_0d_2 database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'%';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
