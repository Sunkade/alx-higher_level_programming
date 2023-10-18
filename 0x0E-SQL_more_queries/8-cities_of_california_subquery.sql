-- Select the id and name from the cities table
-- Where the state_id matches the id of the state with the name "California" from the states table
-- Results are ordered by the id column
SELECT id, name FROM cities
WHERE state_id = (
      SELECT id FROM states
      WHERE name = "California")
ORDER BY id;
