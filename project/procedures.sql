create or replace function total_ship(city_arg varchar)
returns varchar
language plpgsql as
$$
declare val integer;
    begin
        update orders o
        set shipping_total = 0
        where exists(select *
                        from users u
                            where o.order_id = u.user_id
                            and u.city = city_arg
        );
    if not found then
        raise 'User not found';
    end if;

    select sum(shipping_total)
        into val
        from orders;
    return val;
end
$$
;


--- add phone to user
create or replace procedure add_phone(username varchar,phone varchar)
language plpgsql as
$$
    begin
        update users u
        set phone_number = phone
        where u.first_name = username;
    commit;
end;
$$;

---remove from cart specific product
create or replace procedure remove_from_cart(username varchar, product_ varchar)
language plpgsql
as
    $$
    begin
        select
            from cart_product
            where
                carts_card_id = (select user_id from users
                                    where first_name = username)
            and
                product_product_id = (select product_id from products
                                    where product_title = product_);
            if not found then
                raise 'No such product';
            end if;
        select count(product_product_id)
            from cart_product

            where
                carts_card_id = (select user_id from users
                                where first_name = username);
    end;
    $$;


---update stock count for specific product
create procedure update_stock(product_ varchar)
language plpgsql
as
$$
    begin
        update products p
        set in_stock = 100
        where p.product_title=product_;
    end;
    $$;
