-- Converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- in your MySQL server.
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table

ADD COLUMN name_new VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

UPDATE first_table
SET name_new = name;

ALTER TABLE first_table
DROP COLUMN name;

ALTER TABLE first_table
CHANGE COLUMN name_new name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
