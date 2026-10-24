-- Write your query below
select seller_name
from seller
left join orders
on seller.seller_id = orders.seller_id and EXTRACT(YEAR FROM sale_date) = 2020
where orders.seller_id is null
order by seller_name asc;