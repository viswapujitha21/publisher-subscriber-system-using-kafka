--
-- File generated with SQLiteStudio v3.3.3 on Sat Dec 4 23:41:41 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: user
CREATE TABLE user (Id PRIMARY KEY, name, username, password VARCHAR, authenticate);
INSERT INTO user (Id, name, username, password, authenticate) VALUES (1, 'Kenny', 'kenny111', 'india@transport', 'true');

-- Table: user_topics
CREATE TABLE user_topics (Id, topic, user_Id);
INSERT INTO user_topics (Id, topic, user_Id) VALUES (1, 'delhi', 1);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
