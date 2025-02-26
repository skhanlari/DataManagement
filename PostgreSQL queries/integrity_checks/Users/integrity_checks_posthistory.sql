-- Check if there are any that don't satisfy this rule
-- every posthistory.userid should be contained in in users.id
select ph.id
from posthistory ph
EXCEPT
select ph.id
from posthistory ph join users u on u.id = ph.userid
order by id;