create database rent_cars_db;
drop schema public cascade ;

create table customer(
    customer_id serial not null primary key ,
    customer_name varchar(255),
    phone_number integer,
    rent_id serial ,
    address_id serial ,
    foreign key (rent_id) references rent(rent_id),
    foreign key (address_id) references address(address_id)

);

drop table customer cascade ;

do
language plpgsql
$$
begin
    for counter in 1..2000 loop
            insert into customer(customer_name, phone_number) values(concat('Customer ',counter),random()*1000000);
        end loop;
end;$$;


create table address(
    address_id serial not null primary key,
    street_id serial not null,
    foreign key (street_id) references street(street_id)
);

drop table address cascade ;

do
language plpgsql
$$
begin
    for counter in 1..2000 loop
            insert into address(street_id)
            values (default);
        end loop;
end;$$;


create table branch_address(
    branch_address_id serial not null primary key ,
    phone_number integer,
    address_id serial  ,
    foreign key (address_id) references address(address_id)
);

do
language plpgsql
$$
begin
    for counter in 1..2000 loop
            insert into branch_address(phone_number)
            values (random()*1000000000::integer);
        end loop;
end;$$;

drop table branch_address cascade ;

alter table branch_address add constraint branch_address_address_id_fkey foreign key (address_id) references
address(address_id);

create table street(
    street_id serial not null primary key ,
    street_name varchar(255),
    city_id serial,
    foreign key (city_id) references city(city_id)
);


do
language plpgsql
$$
begin
    for counter in 1..2000 loop
            insert into street(street_name) values(concat('Street ',counter));
        end loop;
end;$$;


create table city(
    city_id serial not null primary key,
    city_name varchar(255)
);

do
language plpgsql
$$
begin
    for counter in 100..2000 loop
            insert into city(city_name) values(concat('City ',counter));
        end loop;
end;$$;


create table rent(
    rent_id serial not null primary key,
    price integer,
    date_of_rant timestamp,
    rent_period integer,
    car_id serial,
    foreign key (car_id) references car(car_id)
);
drop table rent cascade ;

do
language plpgsql
$$
begin
    for counter in 1..2000 loop
            insert into rent(price, date_of_rant, rent_period) values(random()*(40-25)+25,now() - random() * interval '340 days',random()*(220-160)+180);
        end loop;
end;$$;


create table car(
    car_id serial not null primary key ,
    brand_id serial,
    department_number_id serial,
    branch_address_id serial,
    foreign key (brand_id) references brand(brand_id),
    foreign key (department_number_id) references department(department_number_id),
    foreign key (branch_address_id) references branch_address(branch_address_id)

);

drop table car cascade ;

alter table car  add constraint branch_address_id foreign key (branch_address_id) references branch_address(branch_address_id);
alter table car  add constraint brancd_id foreign key (brand_id) references brand(brand_id);
alter table car rename constraint brancd_id to brand_id;

do
language plpgsql
$$
begin
    for counter in 1..2000 loop
            insert into car(brand_id,department_number_id,branch_address_id) values (default,default,default);
        end loop;
end;$$;

create table brand(
    brand_id serial not null primary key ,
    brand_name varchar(255),
    production_year timestamp,
    model_id serial,
    foreign key (model_id) references model(model_id)
);
alter table brand
add foreign key (model_id) references model(model_id);

do
language plpgsql
$$
begin
    for counter in 1..2000 loop
            insert into brand(brand_name, production_year) values ('Brand #'||counter,now() - random() * interval '2 days');
        end loop;
end;$$;

create table model(
    model_id bigint GENERATED ALWAYS AS IDENTITY primary key,
    model_name varchar(255)
);
drop table model cascade ;

do
language plpgsql
$$
begin
    for counter in 1..2000 loop
            insert into model( model_name) values ('Model #'||counter);
        end loop;
end;$$;

create table department(
    department_number_id serial not null primary key,
    region_id serial not null ,
    code_num_id serial not null ,
    foreign key (region_id) references region(region_id),
    foreign key (code_num_id) references code_num(code_num_id)
);

drop table department cascade ;


do
language plpgsql
$$
begin
    for counter in 1..2000 loop
            insert into department(region_id,code_num_id) values (default,default);
        end loop;
end;$$;

alter table department add constraint code_num_id foreign key (code_num_id) references code_num(code_num_id);

create table region(
    region_id serial not null primary key,
    region_name varchar(2) not null
);

do
language plpgsql
$$
begin
    for counter in 1..2000 loop
            insert into region(region_name) values (substr(md5(random()::text),0,3));
        end loop;
end;$$;

create table code_num(
    code_num_id serial not null primary key,
    code_num varchar(5)
);

do
language plpgsql
$$
begin
    for counter in 1..2000 loop
            insert into code_num(code_num) values (substr(md5(random()::text),0,5));
        end loop;
end;$$;
