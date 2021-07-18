-- SQLite
INSERT INTO UserLogin (id, userName, password, dateAccountCreated, loginStatus)
VALUES (1, 'rubel', 'rubelpassword', datetime('now'), 1);
INSERT INTO UserDatabase (id, dbName, schemaString, dateTimeCreated, userId_id)
VALUES (Null, 'localhost.sql', 'INSTRUCTIONS: The currently selected database has table customers with columns id, name, table sales with columns id, customer_id, description, price.', datetime('now'), 1);
INSERT INTO UserDatabase (id, dbName, schemaString, dateTimeCreated, userId_id)
VALUES (Null, 'selecttest.sql', 'INSTRUCTIONS: this is for testing DB select dont actually use it pls.', datetime('now'), 1);