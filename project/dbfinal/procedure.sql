create or replace procedure update_price(vechile_for varchar,updprice integer)
as
    $$
    declare
        brandname varchar;
        modelname varchar;
    begin
        select b.brand_name,m.model_name
        into brandname,modelname
            from rent
                left join customer c
                    on rent.rent_id = c.rent_id
                    left join car c2
                        on c2.car_id = rent.car_id
                        left join brand b
                            on b.brand_id = c2.brand_id
                            left join model m
                                on m.model_id = b.model_id
                where model_name = vechile_for;
        if not found then rollback;
        raise 'Not found vechile';
        end if;
        update rent r
        set price = updprice
        where r.car_id = (select car.car_id
                             from car
                             inner join brand b2
                                 on car.brand_id = b2.brand_id
                             inner join model m
                                on b2.model_id = m.model_id
                             where b2.brand_name = brandname
                               and m.model_name = modelname);
        raise info 'found 2';
        commit;
        end;
    $$
language plpgsql;


create or replace procedure deleteandreplace_user
    (customername varchar,newname varchar,phone integer)
as
$$
    declare
begin
    if
        (select customer_name from customer where customer_name=customername) = customername
        then
            raise notice 'Name exists';
    end if;
    delete
    from customer
        where customer_name = customername;

    raise notice 'done 1';

    insert into customer(customer_id, customer_name, phone_number, rent_id, address_id)
        values (1,newname,phone,1,1);
    raise notice 'done 2';
    commit;
end;
$$
language plpgsql;

call deleteandreplace_user('Customer 1','Customer X1',05473234);
