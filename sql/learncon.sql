CREATE TABLE IF NOT EXISTS LearnConTable(
    post_id   INTEGER     NOT NULL PRIMARY KEY AUTOINCREMENT,
    title     VARCHAR(64) NOT NULL UNIQUE,
    author    VARCHAR(64) NOT NULL,
    content   TEXT        NOT NULL,
    filecount INTEGER     NOT NULL DEFAULT 0,
    passcode  VARCHAR(6)      NULL,
    timestamp DATETIME    NOT NULL DEFAULT current_timestamp
);