CREATE TABLE IF NOT EXISTS skills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    command_alias TEXT UNIQUE,
    logic_block TEXT,
    source_agent TEXT,
    last_accessed DATETIME DEFAULT CURRENT_TIMESTAMP
);
