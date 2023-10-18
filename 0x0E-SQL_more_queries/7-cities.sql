-- Create a database named hbtn_0d_usa if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create a table named cities in the hbtn_0d_usa database
-- This table stores records with an auto-incremented 'id', a 'state_id' referencing states.id,
-- and a 'name', ensuring 'id' is unique and not NULL
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY, -- Auto-incremented unique identifier and primary key
    state_id INT NOT NULL, -- Foreign key referencing states.id
    FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id), -- Ensures state_id references states.id
    name VARCHAR(256) NOT NULL -- The name, cannot be NULL
);
