DROP TABLE IF EXISTS todo;

CREATE TABLE todo (
    id INTERGER PRIMARY KEY AUTOINCREMENT,
    task VARCHAR(100) NOT NULL,
    taskdue DATETIME NOT NULL,
    completed INTERGER,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
);