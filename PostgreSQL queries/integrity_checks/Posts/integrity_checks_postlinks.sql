-- Check if there are any that don't satisfy this rule
-- Every postlinks.postid should be inside posts.id
select pl.id
from postlinks pl
EXCEPT
select pl.id
from postlinks pl join posts p on p.id = pl.postid
order by id;

-- select pl.id
-- from postlinks pl
-- where pl.postid not in (select p.id
-- 					   from posts p);


select pl.id
from postlinks pl
EXCEPT
select pl.id
from postlinks pl join posts p on p.id = pl.relatedpostid
order by id;