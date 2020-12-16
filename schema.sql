DROP TABLE IF EXISTS persona;

DROP TABLE IF EXISTS registro;


CREATE TABLE registro(
    [id] INTEGER PRIMARY KEY AUTOINCREMENT,
    [dni] INTEGER NOT NULL
);

CREATE TABLE persona(
    [id] INTEGER PRIMARY KEY AUTOINCREMENT,
    [name] TEXT NOT NULL,
    [age] INTEGER,
    [gender] TEXT NOT NULL,
    [value] INTEGER NOT NULL,
    [datetime] DATETIME NOT NULL,
    [fk_registro_id] INTEGER NOT NULL REFERENCES registro(id)
);