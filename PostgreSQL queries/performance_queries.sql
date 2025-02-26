-- Simple Reads
SELECT * 
FROM Posts
WHERE CreationDate BETWEEN '2009-01-01' AND '2009-12-31';

-----------------------------------------------------
-- Write operations
INSERT INTO Posts (Id, PostTypeId, CreationDate, Score, Title, Body, Tags) 
VALUES 
(2, 1, NOW(), 10, 'Title 1', 'Body 1', '<mac><crash>'),
(3, 2, NOW(), 15, 'Title 2', 'Body 2', '<windows>');

-----------------------------------------------------
-- Joins
SELECT p.*, u.DisplayName 
FROM Posts p
JOIN Users u ON p.OwnerUserId = u.Id;

-----------------------------------------------------
-- Aggregation
SELECT Tags, COUNT(*) 
FROM Posts 
GROUP BY Tags;

-----------------------------------------------------
-- Text Search
SELECT * FROM Posts WHERE Body LIKE '%virtual machine%';

-----------------------------------------------------
-- Nested Updates
UPDATE Users 
SET Reputation = Reputation + 10 
WHERE Id IN (SELECT OwnerUserId FROM Posts GROUP BY OwnerUserId HAVING COUNT(*) > 10);

-----------------------------------------------------
-- Complex Joins
SELECT p.Title, c.Text, u.DisplayName 
FROM Posts p
JOIN Comments c ON p.Id = c.PostId
JOIN Users u ON c.UserId = u.Id;

-----------------------------------------------------
-- Pagination
SELECT * FROM Posts ORDER BY CreationDate DESC LIMIT 10 OFFSET 20;

-----------------------------------------------------
-- Deletion
DELETE FROM Posts 
WHERE Score < 5 AND Id NOT IN (SELECT PostId FROM Comments);

-----------------------------------------------------
-- Counting
SELECT COUNT(*) FROM Users WHERE Reputation > 100;
