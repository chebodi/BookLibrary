CREATE DATABASE library;
\c library

CREATE TABLE book
(
id INT BIGSERIAL PRIMARY KEY,
title VARCHAR(50),
author VARCHAR(20),
publication_year INT
);

CREATE TABLE reader
(
id INT BIGSERIAL PRIMARY KEY,
full_name VARCHAR(50)
);

CREATE TABLE borrows_history
(
book_id BIGINT NOT NULL REFERENCES book(id),
reader_id BIGINT NOT NULL REFERENCES reader(id),
PRIMARY KEY(book_id,reader_id)
);

INSERT INTO book(id, title, author, publication_year)
VALUES
    (1, 'About Cat', 'Masha Kulka', 2001),
    (2, 'Basic C++', 'Donald Trump', 2021),
    (3, 'Kolobok', 'Babushka Gala', 2000),
    (4, '1939', 'Adolph Hitler', 1945);

INSERT INTO reader(id, full_name)
VALUES
    (1, 'Sponge Bob'),
    (2, 'Shrek'),
    (3, 'Sid'),
    (4, 'Michael Jordan');

INSERT INTO borrows_history(book_id, reader_id)
VALUES
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (1,2),
    (1,4);

SELECT
    reader_id
FROM
    borrows_history
WHERE
    book_id = 1;

BEGIN;
DELETE FROM book WHERE id IN (1, 2);
DELETE FROM reader WHERE id IN (1, 2);
COMMIT;