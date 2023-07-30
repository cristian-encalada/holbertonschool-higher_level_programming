-- Script that creates the table id_not_null
-- If the table force_name already exists, the script should not fail
CREATE TABLE IF NOT EXISTS id_not_null (
    id int DEFAULT 1 NOT NULL,
    name varchar(256)
);
