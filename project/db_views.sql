create view product_view as
select
    product_title || ' ' || ' cost ' ||  price
from products
group by product_title, price
order by price;

select * from product_view;
drop view product_view;


create view orders_view as
select o.order_id, os.status_name
from (select o.order_id,o.order_status_order_status_id
      from orders o ) as o
inner join order_status os
    on o.order_status_order_status_id = os.order_status_id;

create view user_cart_verify as
select *
from orders_view
left join carts on cart_id = order_id
left join users u on carts.users_user_id = u.user_id;

select order_id,status_name,first_name
from user_cart_verify;
drop view user_cart_verify;
drop view orders_view;


create view category_product_view as
select product_title,in_stock,category_title
from products
left join categories c
    on products.category_id = c.category_id
where in_stock = 0
order by product_title;

select * from category_product_view;
drop view category_product_view;

create materialized view actors_film_info as
select a.first_name,a.last_name,f.title,ai.film_info,l.name from actor a
left join film_actor fa
    on a.actor_id = fa.actor_id
inner join film f
    on fa.film_id = f.film_id
left join actor_info ai on a.actor_id = ai.actor_id
left join language l on f.language_id = l.language_id
order by a.first_name;

alter materialized view if exists actors_film_info
rename column title to film_name;

select * from actors_film_info;

alter materialized view if exists actors_film_info
rename column film_info to film_description;

select * from actors_film_info;

drop materialized view actors_film_info;