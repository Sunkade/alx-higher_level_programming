-- Select the id and name from the cities table,
-- along with the name from the corresponding state in the states table
-- Join the cities and states tables on the condition that cities.state_id matches states.id
-- Results are ordered by the id column from the cities table
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
