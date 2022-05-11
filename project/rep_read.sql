---Products table---
begin transaction isolation level repeatable read;

insert into products
values (
        30001,'Jay','massaguer',100,25.99,'Jay',21
       );
update products
set product_description = 'massageur'
where product_id=30001;

update products
set price = 15.99
where product_id=30001;
commit;


begin transaction isolation level repeatable read;
insert into products
values (
        30002,'Orion','massageur',50,25.99,'Orion',22
       );
update products
set price = 117.99
where product_id=30002;

savepoint first;

update products
set price = 100.99
where product_id=30002;
release savepoint first;

savepoint second;

commit;




