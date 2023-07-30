-- Script that creates the table unique_id
-- If the table unique_id already exists, the script should not fail
CREATE TABLE IF NOT EXISTS unique_id (
    id int DEFAULT 1 NOT NULL UNIQUE,
    name varchar(256)
);
