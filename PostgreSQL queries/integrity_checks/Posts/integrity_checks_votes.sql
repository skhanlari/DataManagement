-- Check if there are any that don't satisfy this rule
-- every votes.postid should be contained in posts.id
select v.id
from votes v
EXCEPT
select v.id
from votes v join posts p on p.id = v.postid
order by id;