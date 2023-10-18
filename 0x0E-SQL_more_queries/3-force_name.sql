-- Create a table named force_name
-- This table stores records with an 'id' and a 'name'
-- The 'id' is an integer, and the 'name' is a string with a maximum length of 256 characters
CREATE TABLE IF NOT EXISTS force_name (
    id INT, -- Unique identifier
    name VARCHAR(256) NOT NULL -- The name, cannot be NULL
);
