-- Create two custom users
CREATE USER app_n8n WITH PASSWORD 'n8n123';
CREATE USER user2 WITH PASSWORD 'pass2';

-- Create database db1 owned by user1, then lock down public and grant all rights
CREATE DATABASE n8n OWNER app_n8n;
REVOKE CONNECT ON DATABASE n8n FROM PUBLIC;
GRANT ALL PRIVILEGES ON DATABASE n8n TO app_n8n;

-- Create database db2 owned by user2, then lock down public and grant all rights
CREATE DATABASE db2 OWNER user2;
REVOKE CONNECT ON DATABASE db2 FROM PUBLIC;
GRANT ALL PRIVILEGES ON DATABASE db2 TO user2;
