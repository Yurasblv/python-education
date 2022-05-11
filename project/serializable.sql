---Table cars---
create table cars(
    id int primary key ,
    brand varchar(25),
    model varchar(10)
);
insert into cars(id, brand, model
) values (
          1,'bmw','350z'
         );

begin transaction isolation level serializable ;
insert into cars(id, brand, model)
values (
        2,'acura','nsx'
       );
commit;

select * from cars;
begin transaction isolation level serializable ;
    savepoint first ;
insert into cars
values (3,'honda','civic');
rollback to savepoint first ;
commit ;

select * from cars;
drop table cars;