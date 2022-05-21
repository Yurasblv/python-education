create or replace view customer_vechile
as
select c.customer_name,car.car_id
from customer c
left join rent r1 on c.rent_id = r1.rent_id
left join car on  r1.car_id = car.car_id;

select * from customer_vechile;
drop view customer_vechile;


create or replace view cites_in_list
    as
select s.street_name,city.city_name
from address
    join street s
        on address.street_id = s.street_id
    join city
        on s.city_id = city.city_id;

select * from cites_in_list;


create materialized view rent_info
as
    select customer.customer_name,
           customer.phone_number,
           brand_name,
           m.model_name,
           r.date_of_rant
from customer
left join rent r
    on customer.customer_id = r.rent_id
left join address a
    on a.address_id = customer.address_id
left join car c
    on r.car_id = c.car_id
left join brand b
    on c.brand_id = b.brand_id
inner join model m
    on b.model_id = m.model_id
where r.date_of_rant < '2021-07-04 21:43:02.914852';

select * from rent_info;