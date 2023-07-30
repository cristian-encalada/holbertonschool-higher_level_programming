-- Create a table second_table in the database hbtn_0c_0
-- If the table second_table already exists, the script should not fail
-- It's not allowed to use the SELECT and SHOW statements
CREATE TABLE IF NOT EXISTS second_table (
    id int,
    name varchar(256),
    score int
);
-- Insert 4 new records
INSERT INTO second_table (id, name, score)
VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
