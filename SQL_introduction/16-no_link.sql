--  lists all records of the table, Don’t list rows without a name value
SELECT `name`, `score` FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC;
