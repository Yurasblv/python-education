select p1.product_title,p1.price,avg(p2.price)
from products p1
         left join products p2 on p1.product_id = p2.product_id
group by p1.product_title, p1.price
order by p1.price;

select c.category_title, p.product_title, p.price,
    avg(price) over(partition by category_title)
    from categories c
        inner join products p
            on p.category_id = c.category_id;

---procedure for update product price and count final bill
create or replace procedure change_price_product(uname varchar,prod varchar,new_price products.price%type)
language plpgsql
as
$$
    declare uid int; -- have id of user for search
    begin
        select u.user_id
            into uid
            from users u
            where u.first_name = uname;

        if not found then raise notice 'User not found';
        end if;

        update products -- update product price
        set price = new_price
        where product_id = (
            select p1.product_id from products p1
                     where p1.product_title = prod);
        if not found then raise notice 'No such product';
        end if;

        update orders --upd orders table,recount total bill
            set total = (select sum(p.price)
                     from carts c
                    inner join users u
                        on u.user_id = c.cart_id
                    inner join orders o
                        on c.cart_id=o.carts_card_id
                    inner join cart_product cp
                        on c.cart_id = cp.carts_card_id
                    inner join products p
                        on p.product_id = cp.product_product_id
                    where u.first_name = uname)
        where order_id = uid;
        raise notice 'Done';
        commit;
    end;
$$;

---func handler triggers react on update
create or replace function upd_final_bill()
    returns trigger
language plpgsql
as
    $$
    begin
        if old.total = new.total then
            raise notice 'There is not changes';
        end if;
        if old.total<>new.total then
            return new;
        end if;
    end;
    $$;

---trigger of order table
create trigger recalculate_total
    before update
    on orders
    for each row
    execute procedure upd_final_bill();


call change_price_product('first_name 123', 'Product 2501', 100.21);
select * from orders
where order_id = 123;

---func handler for trigger
create or replace function add_user()
returns trigger
language plpgsql
    as
    $$
begin
    if new.first_name like old.first_name then
        raise notice 'User with this name exists';
    end if;
    if new.user_id = old.user_id then
        raise notice 'User exists';
    end if;
    return new;
end;$$;

--trigger search insert user data
create trigger
    user_insert
    before insert
    on users
    for each statement
    execute procedure add_user();

--insert request
insert into users(user_id, email, password,
first_name, last_name, middle_name,
                  is_staff, country, city, address, phone_number)
values (5001,'osdfh@coconut.org','owQyLw7234P','Bear','Grills','mr',0,'USA'
,'Oklahoma','13 street','+77734534');

select * from users where user_id=5001;

delete from users
where user_id = 5001;

alter table users
disable trigger user_insert;

alter table users
enable trigger user_insert;
