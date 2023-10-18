-- Create a table named unique_id
-- This table stores records with a unique 'id' and a 'name'
-- The 'id' has a default value of 1 if not specified
-- The 'name' is a string with a maximum length of 256 characters
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1, -- Unique identifier with a default value of 1
    UNIQUE (ID), -- Ensures that the 'id' values in the table are unique
    name VARCHAR(256) -- The name, can be NULL
);
