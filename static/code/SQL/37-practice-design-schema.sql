-- Exercise: Mini blog platform

-- Requirements:
--
--   users — id, username (must be unique), email
--   profiles — each user has at most one profile: bio, avatar_url
--   posts — each post belongs to exactly one user; has title, body, and a stock-like field isn't relevant here, so just title + body + created_at
--   tags — id, name (unique)
--   post_tags — a post can have many tags, a tag can be on many posts


CREATE DATABASE IF NOT EXISTS blog_platform;
USE blog_platform;

CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
) AUTO_INCREMENT=101;

CREATE INDEX idx_user_id ON users(id);
CREATE INDEX idx_user_name ON users(username);


-- ---------- profiles ---------------

CREATE TABLE profiles(
    user_id INT PRIMARY KEY,
    bio VARCHAR(200),
    avatar_url VARCHAR(50),
    
    CONSTRAINT fk_uid FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE INDEX pf_uid ON profiles(user_id);


-- ------------- posts -------------

CREATE TABLE posts(
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    body VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INT NOT NULL,

    CONSTRAINT fk_userid FOREIGN KEY (user_id) REFERENCES users(id)
);
CREATE INDEX idx_psts_id ON posts(id);


-- -------------- Tags ---------------

CREATE TABLE tags(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) UNIQUE NOT NULL
);
CREATE INDEX idx_tag ON tags(id);

CREATE TABLE posts_tag(
    post_id INT NOT NULL REFERENCES posts(id),
    tag_id INT NOT NULL REFERENCES tags(id),
    
    PRIMARY KEY (post_id, tag_id)
);
CREATE INDEX idx_pst_id ON posts_tag(post_id);




-- pulling data 

-- posts title and tags name
SELECT pst.title, GROUP_CONCAT(tg.name) AS tags
FROM posts as pst 
LEFT JOIN posts_tag as pg
ON pg.post_id = pst.id
LEFT JOIN tags as tg
ON pg.tag_id = tg.id
GROUP BY pst.id, pst.title;


-- usernames who have written more than 2 posts
SELECT users.username
FROM users
JOIN posts 
ON posts.user_id = users.id
GROUP BY users.id
HAVING COUNT(*) > 2

WITH
    eligible_id AS (
    SELECT user_id
    FROM posts
    GROUP BY user_id
    HAVING COUNT(*) > 2
    )
SELECT username FROM users WHERE id IN(SELECT user_id FROM eligible_id)
