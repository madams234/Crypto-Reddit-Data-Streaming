--create function
CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

--create tables
create table subreddits(
    subreddit varchar(50),
    timestamp varchar(50),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
)
create table(
    ticker varchar(50),
    timestamp bigint,
    price double precision,
    changepercent double precision,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
)

--create triggers
CREATE TRIGGER set_timestamp
BEFORE UPDATE ON subreddits
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();

CREATE TRIGGER set_timestamp
BEFORE UPDATE ON crypto
FOR EACH ROW
EXECUTE PROCEDURE trigger_set_timestamp();


