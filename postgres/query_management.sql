-- replication_and_query_management.sql

-- Query 1: 
-- Selects the replication slot name and the time difference between the current WAL LSN (Log Sequence Number)
-- and the slot's restart LSN, formatted as a human-readable size.
SELECT slot_name, 
       pg_size_pretty(pg_wal_lsn_diff(pg_current_wal_lsn(), restart_lsn)) as active 
FROM pg_replication_slots;

-- Query 2:
-- Selects the process ID (pid), the duration of the active queries that have been running for more than 1 second,
-- the actual query text, and its current state, ordered by the longest running query.
SELECT pid, 
       now() - pg_stat_activity.query_start AS duration, 
       query, 
       state 
FROM pg_stat_activity 
WHERE (now() - pg_stat_activity.query_start) > interval '1 seconds' 
      AND state = 'active' 
ORDER BY duration DESC;

-- Query 3:
-- Terminates backend connections (queries) that have been running for more than 5 seconds and are active,
-- excluding the current session (pg_backend_pid()) to avoid terminating the current session.
SELECT pg_terminate_backend(pid) 
FROM pg_stat_activity 
WHERE (now() - pg_stat_activity.query_start) > interval '5 seconds' 
      AND state = 'active' 
      AND pid <> pg_backend_pid();

-- Query 4:
-- Terminates a specific backend connection with pid 28155.
SELECT pg_terminate_backend(28155);