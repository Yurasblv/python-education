create or replace function total_ship(city_arg varchar,new_ship numeric)
returns numeric
language plpgsql as
$$
declare
    rec_user numeric;
    begin
        update orders o
        set shipping_total = new_ship
         where
            (select u.city
                from users u
            where o.order_id = u.user_id
            and u.city = city_arg
        ) like city_arg;

        if not found then
            raise notice 'User not found';
        end if;

        select shipping_total
        into rec_user
        from orders o
        where
            (select u.city
                from users u
            where o.order_id = u.user_id
            and u.city = city_arg
        ) like city_arg;
    return rec_user;
end;
$$;

select total_ship('city 121',0);
-- total_ship
-- 0


--- add phone to user
create or replace
    procedure add_phone(username varchar,phone varchar)
language plpgsql
as
$$
begin
    if username like (select first_name
                   from users
                    where first_name = username)
        then
            update users
            set phone_number = phone
            where first_name = username;
                commit;
        raise info 'Number changed';
    else
        raise info 'No such user';
    end if;
end;$$;

call add_phone('first_name 2','412462');
select * from users where first_name = 'first_name 2';


--update total order with person discount
create or replace procedure add_discount(uname varchar, discount int)
language plpgsql
as
$$
    declare
        checktotal int;
        row orders%rowtype;

begin
    select o.total
    into checktotal
    from orders o
    inner join users u on user_id = carts_card_id
    order by u.user_id;

    if not found then
        raise info 'No user with this name';
    end if;

    for row in select * from orders loop
        row.total := row.total - discount;
        update orders
        set total = row.total
        where order_id=(select u.user_id
                        from users u where first_name = uname );
        end loop;
    commit;
end;
$$;

call add_discount('first_name 123',20);
select *
from orders
where
order_id = (
select user_id from users
where first_name = 'first_name 123');


--update stock count for specific product

create procedure update_stock(product_ varchar,count integer)
language plpgsql
as
$$
    begin
        update products p
        set in_stock = count
        where p.product_title=product_;
        raise notice 'Approved';
        commit;
        if not found then
            raise notice 'Product not found';
        end if;
    end;
    $$;

call update_stock('Product 100',40);
select product_title,in_stock from products where product_title like 'Product 100';
