/* Write your T-SQL query statement below */
select p.firstName, p.lastName, a.city, a.state
from person as p
left join address as a
on a.personId = p.personId