-- Create a database named hbtn_0d_usa if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create a table named states in the hbtn_0d_usa database
-- This table stores records with an auto-incremented 'id', a 'name', and ensures 'id' is unique and not NULL
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY, -- Auto-incremented unique identifier and primary key
    name VARCHAR(256) NOT NULL -- The name, cannot be NULL
);
