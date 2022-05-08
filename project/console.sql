---Created tables and copy info inside---
create table users(
    user_id int unique ,
    email varchar(255),
    password varchar(255),
    first_name varchar(255) not null ,
    last_name varchar(255) not null ,
    middle_name varchar(255) not null ,
    is_staff smallint ,
    country varchar(255),
    city varchar(255),
    address text
);

COPY users
FROM '/var/lib/postgresql/data/users.csv'
with (format csv );

create table carts(
    cart_id int unique ,
    users_user_id int references users(user_id),
    subtotal decimal,
    total decimal,
    timestamp timestamp(2)
);

COPY carts
FROM '/var/lib/postgresql/data/carts.csv'
with (format csv );

create table categories(
    category_id int not null primary key ,
    category_title varchar(255),
    category_description text
);

COPY categories
FROM '/var/lib/postgresql/data/categories.csv'
with (format csv );

create table products(
    product_id int not null primary key ,
    product_title varchar(255),
    product_description text,
    in_stock int,
    price float,
    slug varchar(45),
    category_id int

);

COPY products
FROM '/var/lib/postgresql/data/products.csv'
with (format csv );

create table cart_product(
    carts_card_id int,
    product_product_id int not null ,
    foreign key (carts_card_id) references
                  carts(cart_id)
);

COPY cart_product
FROM '/var/lib/postgresql/data/cart_products.csv'
with (format csv );

create table order_status(
    order_status_id int not null primary key,
    status_name varchar(255)
);

COPY order_status
FROM '/var/lib/postgresql/data/order_statuses.csv'
with (format csv );

create table orders(
    order_id int not null primary key ,
    carts_card_id int,
    order_status_order_status_id int,
    shipping_total decimal,
    total decimal,
    created_at timestamp(2),
    updated_at timestamp(2),
    foreign key (carts_card_id) references
        carts(cart_id),
    foreign key (order_status_order_status_id)
                  references order_status(order_status_id)
);

COPY orders
FROM '/var/lib/postgresql/data/orders.csv'
with (format csv );


---Tasks---

alter table users
ADD phone_number integer ;

alter table users
alter column phone_number type varchar;

update products
set price = price*2



