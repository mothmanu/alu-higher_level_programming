-- Lists records of second_table that have a name, highest score first
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
