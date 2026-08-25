CREATE DATABASE python_blog;

\c python_blog

CREATE TABLE blog_posts (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    author VARCHAR(100),
    published_date DATE,
    url TEXT UNIQUE
);
