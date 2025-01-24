-- Step 1: Create a role
CREATE ROLE "kuku_reader_v2" NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT LOGIN PASSWORD '<password>';

-- Step 2: Grant usage on the schema to allow access
GRANT USAGE ON SCHEMA public TO "kuku_reader_v2";

-- Step 3: Grant SELECT on all existing tables (including inherited tables)
GRANT SELECT ON ALL TABLES IN SCHEMA public TO "kuku_reader_v2";

-- Step 4: Grant SELECT on future tables (with default privileges)
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO "kuku_reader_v2";