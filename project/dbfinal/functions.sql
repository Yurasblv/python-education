create function user_info(
p_name varchar,
p_phone integer)
returns table(c_name varchar,phone integer,
                rent_days integer,
                price integer,
                brand varchar,
                model varchar)
language plpgsql
as
$$
    declare user_info record;
    begin
        for user_info in (
                select customer.customer_name,
                       customer.phone_number,
                       r.rent_period,
                       r.price,
                       b.brand_name,
                       m.model_name
                from customer
                left join rent r
                    on customer.rent_id = r.rent_id
                left join car c
                    on r.car_id = c.car_id
                left join brand b
                    on b.brand_id = c.brand_id
                left join model m
                    on b.model_id = m.model_id
                where
                    customer.customer_name = p_name
                  and
                    customer.phone_number = p_phone)
        loop
            c_name := user_info.customer_name;
            phone := user_info.phone_number;
            rent_days := user_info.rent_period;
            brand := user_info.brand_name;
            model := user_info.model_name;
            return next;
        end loop;
    end;
$$;

select * from user_info('Customer 1043',972016);



create or replace function car_info(seach_brand varchar)
returns table(car_name varchar,prod_year timestamp)
language plpgsql
as
    $$
begin
    return query
        select brand.brand_name,brand.production_year
    from brand
    where
        brand.brand_name like seach_brand ;
end; $$;

select * from car_info('Brand #201');

create or replace function city_info(city_name_ varchar)
returns record
    as
$$
    declare
        c_rec record;
        curs cursor for
            select street_name,city_name from street
                left join city c on c.city_id = street.city_id
                    where c.city_name = city_name_;
    begin
        open curs;
            loop
                fetch curs into c_rec;
            close curs;
    return c_rec;
    end loop;
end;$$
language plpgsql;

select city_info('City 1');

