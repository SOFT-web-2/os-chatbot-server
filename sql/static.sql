CREATE TABLE StaticFileTable(
    filename VARCHAR(64) NOT NULL PRIMARY KEY,
    c_index  INT         NOT NULL,
    article  VARCHAR(64) NOT NULL,
    mimetype VARCHAR(64) NOT NULL
);