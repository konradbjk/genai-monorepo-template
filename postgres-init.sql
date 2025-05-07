-- Create two custom users
CREATE USER user1 WITH PASSWORD 'pass1';
CREATE USER user2 WITH PASSWORD 'pass2';

-- Create database db1 owned by user1, then lock down public and grant all rights
CREATE DATABASE db1 OWNER user1;
REVOKE CONNECT ON DATABASE db1 FROM PUBLIC;
GRANT ALL PRIVILEGES ON DATABASE db1 TO user1;

-- Create database db2 owned by user2, then lock down public and grant all rights
CREATE DATABASE db2 OWNER user2;
REVOKE CONNECT ON DATABASE db2 FROM PUBLIC;
GRANT ALL PRIVILEGES ON DATABASE db2 TO user2;
