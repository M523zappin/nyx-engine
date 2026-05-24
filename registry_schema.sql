CREATE TABLE IF NOT EXISTS skills (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    command_alias TEXT UNIQUE,
    logic_block TEXT,
    last_accessed DATETIME
);
