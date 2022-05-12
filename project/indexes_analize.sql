create unique index email on users(email);
set work_mem to '10MB';
explain (analyse)

select u.email,o.total,o.created_at,o.updated_at
from users u
    left join carts c
on u.user_id = c.users_user_id
    left join(select * from orders order by order_id) as o
on c.cart_id = o.carts_card_id
where o.total is not NULL;

-- Hash Join  (cost=187.80..307.86 rows=1500 width=41) (actual time=1.135..1.992 rows=1500 loops=1)
--   Hash Cond: (c.users_user_id = u.user_id)
--   ->  Hash Join  (cost=60.28..176.40 rows=1500 width=26) (actual time=0.385..0.979 rows=1500 loops=1)
--         Hash Cond: (orders.carts_card_id = c.cart_id)
--         ->  Index Scan using orders_pkey on orders  (cost=0.28..97.46 rows=1500 width=66) (actual time=0.010..0.341 rows=1500 loops=1)
--               Filter: (total IS NOT NULL)
--         ->  Hash  (cost=35.00..35.00 rows=2000 width=8) (actual time=0.369..0.370 rows=2000 loops=1)
--               Buckets: 2048  Batches: 1  Memory Usage: 95kB
--               ->  Seq Scan on carts c  (cost=0.00..35.00 rows=2000 width=8) (actual time=0.004..0.192 rows=2000 loops=1)
--   ->  Hash  (cost=90.01..90.01 rows=3001 width=23) (actual time=0.744..0.745 rows=3001 loops=1)
--         Buckets: 4096  Batches: 1  Memory Usage: 197kB
--         ->  Seq Scan on users u  (cost=0.00..90.01 rows=3001 width=23) (actual time=0.005..0.419 rows=3001 loops=1)
-- Planning Time: 0.261 ms
-- Execution Time: 2.051 ms
drop index email;

set enable_seqscan to off;
create index pc_idx on potential_customers(name);
explain(analyse)
select p.name,o.created_at,c.total from potential_customers p
inner join orders o
    on p.id = order_id
left join carts as c
    on o.order_id = c.cart_id
group by p.name,o.created_at,c.total;

--- BEFORE INDEXING

-- Group  (cost=74.28..74.37 rows=9 width=530) (actual time=0.130..0.139 rows=9 loops=1)
-- "  Group Key: p.name, o.created_at, c.total"
--   ->  Sort  (cost=74.28..74.31 rows=9 width=530) (actual time=0.126..0.129 rows=9 loops=1)
-- "        Sort Key: p.name, o.created_at, c.total"
--         Sort Method: quicksort  Memory: 25kB
--         ->  Nested Loop Left Join  (cost=0.69..74.14 rows=9 width=530) (actual time=0.040..0.091 rows=9 loops=1)
--               ->  Nested Loop  (cost=0.41..70.93 rows=9 width=528) (actual time=0.028..0.058 rows=9 loops=1)
--                     ->  Index Scan using potential_customers_id_key on potential_customers p  (cost=0.14..12.27 rows=9 width=520) (actual time=0.011..0.018 rows=9 loops=1)
--                     ->  Index Scan using orders_pkey on orders o  (cost=0.28..6.52 rows=1 width=12) (actual time=0.003..0.003 rows=1 loops=9)
--                           Index Cond: (order_id = p.id)
--               ->  Index Scan using carts_cart_id_key on carts c  (cost=0.28..0.36 rows=1 width=10) (actual time=0.003..0.003 rows=1 loops=9)
--                     Index Cond: (cart_id = o.order_id)
-- Planning Time: 0.537 ms
-- Execution Time: 0.210 ms

---AFTER

-- Group  (cost=8.86..74.61 rows=9 width=530) (actual time=0.047..0.052 rows=9 loops=1)
-- "  Group Key: p.name, o.created_at, c.total"
--   ->  Incremental Sort  (cost=8.86..74.55 rows=9 width=530) (actual time=0.046..0.047 rows=9 loops=1)
-- "        Sort Key: p.name, o.created_at, c.total"
--         Presorted Key: p.name
--         Full-sort Groups: 1  Sort Method: quicksort  Average Memory: 25kB  Peak Memory: 25kB
--         ->  Nested Loop Left Join  (cost=0.69..74.14 rows=9 width=530) (actual time=0.017..0.036 rows=9 loops=1)
--               ->  Nested Loop  (cost=0.41..70.93 rows=9 width=528) (actual time=0.014..0.025 rows=9 loops=1)
--                     ->  Index Scan using potential_customers_name_idx on potential_customers p  (cost=0.14..12.27 rows=9 width=520) (actual time=0.008..0.009 rows=9 loops=1)
--                     ->  Index Scan using orders_pkey on orders o  (cost=0.28..6.52 rows=1 width=12) (actual time=0.001..0.001 rows=1 loops=9)
--                           Index Cond: (order_id = p.id)
--               ->  Index Scan using carts_cart_id_key on carts c  (cost=0.28..0.36 rows=1 width=10) (actual time=0.001..0.001 rows=1 loops=9)
--                     Index Cond: (cart_id = o.order_id)
-- Planning Time: 0.339 ms
-- Execution Time: 0.078 ms
drop index pc_idx;




create index idx_name on users(first_name);
set work_mem to '20MB';
set enable_seqscan to on;
explain (analyse,buffers )
select u.first_name,os.status_name,o.order_status_order_status_id
from (select order_id, order_status_order_status_id,orders.shipping_total
               from orders
               order by order_id ) as o
left join users u on u.user_id = o.order_id
left join order_status as os on o.order_id = os.order_status_id;

drop index idx_name;

-- Hash Left Join  (cost=247.80..274.44 rows=1500 width=535) (actual time=1.068..1.561 rows=1500 loops=1)
--   Hash Cond: (orders.order_id = os.order_status_id)
--   Buffers: shared hit=74
--   ->  Hash Left Join  (cost=234.65..257.34 rows=1500 width=23) (actual time=1.059..1.391 rows=1500 loops=1)
--         Hash Cond: (orders.order_id = u.user_id)
--         Buffers: shared hit=73
--         ->  Sort  (cost=107.13..110.88 rows=1500 width=40) (actual time=0.348..0.398 rows=1500 loops=1)
--               Sort Key: orders.order_id
--               Sort Method: quicksort  Memory: 119kB
--               Buffers: shared hit=13
--               ->  Seq Scan on orders  (cost=0.00..28.00 rows=1500 width=40) (actual time=0.005..0.135 rows=1500 loops=1)
--                     Buffers: shared hit=13
--         ->  Hash  (cost=90.01..90.01 rows=3001 width=19) (actual time=0.703..0.704 rows=3001 loops=1)
--               Buckets: 4096  Batches: 1  Memory Usage: 185kB
--               Buffers: shared hit=60
--               ->  Seq Scan on users u  (cost=0.00..90.01 rows=3001 width=19) (actual time=0.009..0.370 rows=3001 loops=1)
--                     Buffers: shared hit=60
--   ->  Hash  (cost=11.40..11.40 rows=140 width=520) (actual time=0.005..0.005 rows=5 loops=1)
--         Buckets: 1024  Batches: 1  Memory Usage: 9kB
--         Buffers: shared hit=1
--         ->  Seq Scan on order_status os  (cost=0.00..11.40 rows=140 width=520) (actual time=0.003..0.003 rows=5 loops=1)
--               Buffers: shared hit=1
-- Planning:
--   Buffers: shared hit=3
-- Planning Time: 0.149 ms
-- Execution Time: 1.622 ms
