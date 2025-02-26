-- Check if there are any that don't satisfy this rule
-- Every comments.postid should be contained in posts.id
select c.id
from comments c
EXCEPT
select c.id
from comments c join posts p on p.id = c.postid
order by id;