--- Users table ---
begin transaction isolation level read committed;
update users
set city = 'Michigan'
where city = 'city 17';
commit;

begin transaction isolation level read committed;

update users
    set phone_number = '12343'
where user_id = 17;
savepoint first;

update users
set phone_number = '+127434993224'
where city = 'Michigan';
release savepoint first;
savepoint second;

update users
set first_name = 'Carlo',city='city 17'
where phone_number='+127434993224';

commit;

begin transaction isolation level read committed;
insert into users
values (30001,'ahfdg@gmail.com','73465ysdg','gigi','koko','chester',0,'axis','nemezida','#928');

savepoint first;

delete
from users
    where user_id=30001;
rollback to savepoint first;
release savepoint first;

commit;


