-- Check if there are any that don't satisfy this rule
-- every badges.userid should be contained in users.id
select b.id
from badges b
EXCEPT
select b.id
from badges b join users u on u.id = b.userid
order by id;