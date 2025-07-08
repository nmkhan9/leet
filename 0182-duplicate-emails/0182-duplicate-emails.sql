/* Write your T-SQL query statement below */
select p.email as Email
from Person as p
group by p.email
having count(p.email)>1

