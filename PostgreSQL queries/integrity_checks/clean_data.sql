-- Delete comments that don't satisfy the rule
DELETE FROM comments
WHERE id IN (
    SELECT c.id
    FROM comments c
	where c.postid is not null
    EXCEPT
    SELECT c.id
    FROM comments c JOIN posts p ON p.id = c.postid
);

-- Delete posthistory that don't satisfy the rule
DELETE FROM posthistory
WHERE id IN (
    SELECT ph.id
    FROM posthistory ph
	where ph.postid is not null
    EXCEPT
    SELECT ph.id
    FROM posthistory ph JOIN posts p ON p.id = ph.postid
);

-- Delete postlinks that don't satisfy the rule
DELETE FROM postlinks
WHERE id IN (
    SELECT pl.id
    FROM postlinks pl
	where pl.postid is not null
    EXCEPT
    SELECT pl.id
    FROM postlinks pl JOIN posts p ON p.id = pl.postid
);

-- Delete postlinks that don't satisfy the rule
DELETE FROM postlinks
WHERE id IN (
    SELECT pl.id
    FROM postlinks pl
	where pl.relatedpostid is not null
    EXCEPT
    SELECT pl.id
    FROM postlinks pl JOIN posts p ON p.id = pl.relatedpostid
);

-- Delete votes that don't satisfy the rule
DELETE FROM votes
WHERE id IN (
    SELECT v.id
    FROM votes v
	where v.postid is not null
    EXCEPT
    SELECT v.id
    FROM votes v JOIN posts p ON p.id = v.postid
);

-- Delete badges that don't satisfy the rule
DELETE FROM badges
WHERE id IN (
    SELECT b.id
    FROM badges b
	where b.userid is not null
    EXCEPT
    SELECT b.id
    FROM badges b JOIN users u ON u.id = b.userid
);

-- Delete posthistory that don't satisfy the rule
DELETE FROM posthistory
WHERE id IN (
    SELECT ph.id
    FROM posthistory ph
	where ph.userid is not null
    EXCEPT
    SELECT ph.id
    FROM posthistory ph JOIN users u ON u.id = ph.userid
);

-- EXECUTE LATER AFTER FOREIGN KEYS!!!!!!

-- Delete posts that don't satisfy the rule
DELETE FROM posts
WHERE id IN (
    SELECT p.id
    FROM posts p
	where p.owneruserid is not null
    EXCEPT
    SELECT p.id
    FROM posts p JOIN users u ON u.id = p.owneruserid
);

UPDATE posts
SET acceptedanswerid = NULL
WHERE id IN (
    SELECT p.id
    FROM posts p
    WHERE p.acceptedanswerid IS NOT NULL
    EXCEPT
    SELECT p.id
    FROM posts p
    JOIN posts p2 ON p2.id = p.acceptedanswerid
);

UPDATE posts
SET parentid = NULL
WHERE id IN (
    SELECT p.id
    FROM posts p
    WHERE p.parentid IS NOT NULL
    EXCEPT
    SELECT p.id
    FROM posts p
    JOIN posts p2 ON p2.id = p.parentid
);
