-- Step 1: Create a role with additional permissions (INHERIT, CREATEROLE, CREATEDB)
-- This role can create databases, create other roles, and inherit permissions from other roles.
-- It also has login access and the password is set here.
CREATE ROLE "kuku_writer" WITH LOGIN NOSUPERUSER CREATEROLE CREATEDB INHERIT NOREPLICATION VALID UNTIL 'infinity' PASSWORD '<your_password>';

-- Step 2: Grant usage on the schema to allow access
-- This gives "kuku_writer" the ability to use all objects in the public schema.
GRANT ALL ON SCHEMA public TO "kuku_writer";

-- Step 3: Grant ALL on all existing tables (including inherited tables)
-- This gives "kuku_writer" full access (SELECT, INSERT, UPDATE, DELETE) to all tables within the public schema.
GRANT ALL ON ALL TABLES IN SCHEMA public TO "kuku_writer";

-- Step 4: Grant SELECT on future tables (with default privileges)
-- This ensures that "kuku_writer" will automatically get all privileges on any new tables created in the public schema.
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO "kuku_writer";

-- Step 5: Grant ALL privileges on all sequences in the public schema to "kuku_writer"
-- Sequences are used to generate unique values for columns, often for primary keys. This grants all operations on existing sequences.
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO "kuku_writer";

-- Step 6: Grant ALL privileges on future sequences (with default privileges)
-- This ensures that "kuku_writer" will have all privileges on any new sequences created in the public schema.
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO "kuku_writer";

-- Granting rds_superuser privileges (if working with AWS RDS PostgreSQL)
-- This allows the "kuku_writer" role to have administrative privileges typical for RDS PostgreSQL users. 
-- Make sure you understand the implications of giving this level of access.
GRANT rds_superuser TO "kuku_writer";
