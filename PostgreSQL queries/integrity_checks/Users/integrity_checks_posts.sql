-- Check if there are any that don't satisfy this rule
-- every posts.OwnerUserId should be contained in users.id
select p.id
from posts p
EXCEPT
select p.id
from posts p join users u on u.id = p.owneruserid
order by id;