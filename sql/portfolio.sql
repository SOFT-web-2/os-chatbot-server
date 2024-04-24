CREATE OR REPLACE TABLE PortfolioTable(
    post_id   INT         NOT NULL PRIMARY KEY,
    title     VARCHAR(64) NOT NULL UNIQUE  KEY,
    author    VARCHAR(64) NOT NULL,
    content   TEXT        NOT NULL,
    timestamp DATETIME    NOT NULL
);