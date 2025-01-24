# PostgreSQL Role and Query Management SQL Scripts

This folder contains SQL scripts for managing PostgreSQL roles and queries, including user role creation and query management tasks.

## Scripts:

### 1. **[writer_role_creation.sql](writer_role_creation.sql)**

- Creates a role (`kuku_writer`) with full access to schema, tables, and sequences (both existing and future).
- Assigns `CREATEROLE`, `CREATEDB`, `INHERIT`, and login privileges.

### 2. **[reader_role_creation.sql](reader_role_creation.sql)**

- Creates a read-only role (`kuku_reader_v2`) with `SELECT` access to all current and future tables in the `public` schema.

### 3. **[query_management.sql](query_management.sql)**

- Includes queries to monitor replication slots and manage active queries:
  - Check replication slot status.
  - List and manage long-running active queries.
  - Terminate queries or backend processes based on specific conditions.

### 4. **[role_cleanup.sql](role_cleanup.sql)**

- Contains queries to revoke all privileges from a role and drop the role, ensuring that all dependencies are cleaned up before removal:
  - Revoke all privileges on schema, tables, and sequences.
  - Revoke default privileges on future tables and sequences.
  - Drop the specified role.

## Usage:

1. Run the respective role creation script to set up user roles with desired permissions.
2. Use the [query_management.sql](query_management.sql) script for managing long-running queries and monitoring replication.
3. Use the [role_cleanup.sql](role_cleanup.sql) script to clean up a role's privileges and remove it from the system.

---

Please contact @vikas before running any query.
