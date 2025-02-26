-- Check if there are any that don't satisfy this rule
-- every posthistory.postid should be contained in posts.id
select ph.id
from posthistory ph
EXCEPT
select ph.id
from posthistory ph join posts p on p.id = ph.postid
order by id;