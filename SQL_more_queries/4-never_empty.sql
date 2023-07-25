-- Script that creates the table id_not_null
-- The database name will be passed as an argument of the mysql command
-- If the table force_name already exists, the script should not fail
CREATE TABLE IF NOT EXISTS id_not_null (
    id int DEFAULT 1 NOT NULL,
    name varchar(256)
);
