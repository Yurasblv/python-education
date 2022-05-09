create table potential_customers(
    id serial primary key ,
    email varchar(255),
    name varchar(255),
    surname varchar(255),
    second_name varchar(255),
    city varchar(25)
);


insert into potential_customers(
values (1,'od21fh@phoenix.org','patrick','ertw','adsfasdf','city 1'),
        (2,'odf312h@phoenix.org','jimmi','sdf','psogujhf','city 2'),
        (3,'o43dfh@phoenix.org','oliver','dgfh','tqoih','city 102'),
        (4,'odfh@phoenix.org','morgan','hgf','qewro','city 31'),
        (5,'odf12h@phoenix.org','vanessa','bcv','xbvxvc','city 51'),
        (6,'odfh@phoenix.org','christian','cvbx','qwerqw','city 16'),
        (7,'osddfh@phoenix.org','olivia','ey','sfgdsdgf','city 17'),
        (8,'od54fh@phoenix.org','ramin','dsfg','t34w','city 12'),
        (9,'od98fh@phoenix.org','jenisse','qwer','gfsdgfsd','city 17')
);


select name,email
from potential_customers
where city = 'city 17';


select name,email
from potential_customers
order by  nullif(regexp_replace(city, '\D', '', 'g'), '')::int, name;


select category_id, sum(in_stock)
from products
group by products.category_id
order by SUM(in_stock)
desc ;


select products.product_title,cart_product.product_product_id
from products
left join cart_product
on products.product_id = cart_product.product_product_id
where cart_product.product_product_id is null;


select p.product_title
from products as p
left join cart_product as c
on p.product_id=c.product_product_id
where c.product_product_id is NULL;


select product_title, count(cart_product.product_product_id)
from products,cart_product
where products.product_id = cart_product.product_product_id
group by products.product_title, cart_product.product_product_id
order by count(product_product_id)
desc
limit 10;


select sum(carts.total),first_name
from carts,users
where users.user_id = carts.users_user_id
group by first_name,carts.total
order by carts.total desc
limit 5;


select u.first_name, count(c.users_user_id)
from carts as c,users as u
where u.user_id = c.users_user_id
group by u.first_name, c.users_user_id
limit 5;


select carts.users_user_id, COUNT(carts.cart_id)
from carts
    left join orders
    on carts.cart_id = orders.carts_card_id
    where orders.carts_card_id is null
group by carts.users_user_id
order by count(carts.cart_id)
limit 5;