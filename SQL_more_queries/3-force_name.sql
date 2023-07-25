-- Script that creates the table force_name
-- The database name will be passed as an argument of the mysql command
-- If the table force_name already exists, your script should not fail
CREATE TABLE IF NOT EXISTS force_name (
    id int,
    name varchar(256) NOT NULL
);
