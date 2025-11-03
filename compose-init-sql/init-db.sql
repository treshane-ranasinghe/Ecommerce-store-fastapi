-- init-db.sql
-- create databases
CREATE DATABASE productdb;
CREATE DATABASE orderdb;
CREATE DATABASE cartdb;

-- create user (role) and set password
DO
$$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'treshaneranasinghe') THEN
      CREATE ROLE treshaneranasinghe WITH LOGIN PASSWORD 'Dahami224466';
   END IF;
END
$$;

-- grant privileges to the new user on each DB
GRANT ALL PRIVILEGES ON DATABASE productdb TO treshaneranasinghe;
GRANT ALL PRIVILEGES ON DATABASE orderdb TO treshaneranasinghe;
GRANT ALL PRIVILEGES ON DATABASE cartdb TO treshaneranasinghe;

-- connect to each DB and give the user ownership of the public schema (so create table etc works)
\connect productdb postgres
ALTER SCHEMA public OWNER TO treshaneranasinghe;
GRANT ALL ON SCHEMA public TO treshaneranasinghe;
\connect orderdb postgres
ALTER SCHEMA public OWNER TO treshaneranasinghe;
GRANT ALL ON SCHEMA public TO treshaneranasinghe;
\connect cartdb postgres
ALTER SCHEMA public OWNER TO treshaneranasinghe;
GRANT ALL ON SCHEMA public TO treshaneranasinghe;
