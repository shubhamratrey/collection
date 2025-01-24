-- Step 1: Revoke all privileges on the public schema from the "shubh_test_v2" role
-- This removes the ability of the role to access any objects in the "public" schema.
REVOKE ALL ON SCHEMA public FROM "shubh_test_v2";

-- Step 2: Revoke all privileges on all tables within the "public" schema from the role
-- This ensures that the "shubh_test_v2" role no longer has any privileges (SELECT, INSERT, UPDATE, DELETE, etc.) on all existing tables.
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM "shubh_test_v2";

-- Step 3: Revoke all privileges on all sequences in the "public" schema from the role
-- This removes the role's ability to access or modify any sequences in the schema (e.g., for primary key generation).
REVOKE ALL ON ALL SEQUENCES IN SCHEMA public FROM "shubh_test_v2";

-- Step 4: Revoke default privileges for tables created in the future in the "public" schema
-- This ensures that "shubh_test_v2" will not automatically get privileges on any new tables created in the schema.
ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE ALL ON TABLES FROM "shubh_test_v2";

-- Step 5: Revoke default privileges for sequences created in the future in the "public" schema
-- Similar to the previous step, this ensures "shubh_test_v2" won't get automatic privileges on new sequences created.
ALTER DEFAULT PRIVILEGES IN SCHEMA public REVOKE ALL ON SEQUENCES FROM "shubh_test_v2";

-- Step 6: Drop the role "shubh_test_v2" after all privileges have been revoked
-- Now that all privileges have been removed, the role can be safely dropped from the system.
DROP ROLE "shubh_test_v2";
