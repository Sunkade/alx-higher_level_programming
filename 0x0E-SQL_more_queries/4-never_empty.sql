-- Create a table named id_not_null
-- This table stores records with an 'id' and a 'name'
-- The 'id' has a default value of 1 if not specified
-- The 'name' is a string with a maximum length of 256 characters
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1, -- Unique identifier with a default value of 1
    name VARCHAR(256) -- The name, can be NULL
);
