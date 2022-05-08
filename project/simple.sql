select *
from users;

select *
from products;

select *
from order_status;

select *
from orders
where order_status_order_status_id = 3
or order_status_order_status_id = 4;

select *
from products
where price
between 80
and 150
or price = 150;
---OR---
select *
from products
where 80 < price
and price < 150;

select *
from orders
where order_status_order_status_id = 3
and created_at > '01.10.2020';

select *
from orders
where order_status_order_status_id = 1
and created_at
between '2020-01-01'
and '2020-06-01';

select *
from products
where category_id
in (13,7,18);

select *
from orders
where created_at <= '2020-12-13'
  and order_status_order_status_id = 2;

select carts_card_id
from orders
where order_status_order_status_id = 1;

select avg(total)
from orders
where order_status_order_status_id = 4;

select max(total)
from orders
where created_at between '2020-07-01' and '2020-09-01';



