explain (analyse)
select c1.customer_name,r.price,b.brand_name
from customer c1
inner join rent r
    on c1.rent_id = r.rent_id
inner join car c2
    on c2.car_id = r.car_id
inner join brand b
    on c2.brand_id = b.brand_id
where brand_name = 'Brand #222';

--RESULT BEFORE

-- Hash Join  (cost=116.81..134.71 rows=1 width=531) (actual time=3.446..4.254 rows=1 loops=1)
--   Hash Cond: (c1.rent_id = r.rent_id)
--   ->  Seq Scan on customer c1  (cost=0.00..17.10 rows=210 width=520) (actual time=0.021..0.430 rows=2000 loops=1)
--   ->  Hash  (cost=116.80..116.80 rows=1 width=19) (actual time=3.274..3.282 rows=1 loops=1)
--         Buckets: 1024  Batches: 1  Memory Usage: 9kB
--         ->  Hash Join  (cost=76.29..116.80 rows=1 width=19) (actual time=2.200..3.274 rows=1 loops=1)
--               Hash Cond: (r.car_id = c2.car_id)
--               ->  Seq Scan on rent r  (cost=0.00..33.00 rows=2000 width=12) (actual time=0.007..0.479 rows=2000 loops=1)
--               ->  Hash  (cost=76.27..76.27 rows=1 width=15) (actual time=2.040..2.046 rows=1 loops=1)
--                     Buckets: 1024  Batches: 1  Memory Usage: 9kB
--                     ->  Hash Join  (cost=40.01..76.27 rows=1 width=15) (actual time=0.711..2.040 rows=1 loops=1)
--                           Hash Cond: (c2.brand_id = b.brand_id)
--                           ->  Seq Scan on car c2  (cost=0.00..31.00 rows=2000 width=8) (actual time=0.007..0.584 rows=2000 loops=1)
--                           ->  Hash  (cost=40.00..40.00 rows=1 width=15) (actual time=0.573..0.576 rows=1 loops=1)
--                                 Buckets: 1024  Batches: 1  Memory Usage: 9kB
--                                 ->  Seq Scan on brand b  (cost=0.00..40.00 rows=1 width=15) (actual time=0.075..0.568 rows=1 loops=1)
--                                       Filter: ((brand_name)::text = 'Brand #222'::text)
--                                       Rows Removed by Filter: 1999
-- Planning Time: 0.981 ms
-- Execution Time: 4.350 ms


create index on brand(brand_name);
drop index brand_brand_name_idx;
--RESULT AFTER

-- Hash Join  (cost=85.10..103.00 rows=1 width=531) (actual time=2.605..3.538 rows=1 loops=1)
--   Hash Cond: (c1.rent_id = r.rent_id)
--   ->  Seq Scan on customer c1  (cost=0.00..17.10 rows=210 width=520) (actual time=0.018..0.476 rows=2000 loops=1)
--   ->  Hash  (cost=85.09..85.09 rows=1 width=19) (actual time=2.440..2.444 rows=1 loops=1)
--         Buckets: 1024  Batches: 1  Memory Usage: 9kB
--         ->  Hash Join  (cost=44.58..85.09 rows=1 width=19) (actual time=1.471..2.438 rows=1 loops=1)
--               Hash Cond: (r.car_id = c2.car_id)
--               ->  Seq Scan on rent r  (cost=0.00..33.00 rows=2000 width=12) (actual time=0.007..0.430 rows=2000 loops=1)
--               ->  Hash  (cost=44.57..44.57 rows=1 width=15) (actual time=1.304..1.308 rows=1 loops=1)
--                     Buckets: 1024  Batches: 1  Memory Usage: 9kB
--                     ->  Hash Join  (cost=8.31..44.57 rows=1 width=15) (actual time=0.247..1.303 rows=1 loops=1)
--                           Hash Cond: (c2.brand_id = b.brand_id)
--                           ->  Seq Scan on car c2  (cost=0.00..31.00 rows=2000 width=8) (actual time=0.006..0.446 rows=2000 loops=1)
--                           ->  Hash  (cost=8.29..8.29 rows=1 width=15) (actual time=0.093..0.095 rows=1 loops=1)
--                                 Buckets: 1024  Batches: 1  Memory Usage: 9kB
--                                 ->  Index Scan using brand_brand_name_idx on brand b  (cost=0.28..8.29 rows=1 width=15) (actual time=0.084..0.086 rows=1 loops=1)
--                                       Index Cond: ((brand_name)::text = 'Brand #222'::text)
-- Planning Time: 1.334 ms
-- Execution Time: 3.626 ms


explain (analyse)
select r1.price,r1.rent_period,s.street_name
    from rent r1
inner join car c on r1.car_id = c.car_id
left join branch_address ba on c.branch_address_id = ba.branch_address_id
inner join street s on ba.branch_address_id = s.street_id
group by r1.price, r1.rent_period, s.street_name
order by r1.price desc;

--RESULT BEFORE

-- Group  (cost=328.44..348.44 rows=2000 width=19) (actual time=4.509..4.882 rows=2000 loops=1)
-- "  Group Key: r1.price, r1.rent_period, s.street_name"
--   ->  Sort  (cost=328.44..333.44 rows=2000 width=19) (actual time=4.506..4.580 rows=2000 loops=1)
-- "        Sort Key: r1.price DESC, r1.rent_period, s.street_name"
--         Sort Method: quicksort  Memory: 205kB
--         ->  Hash Join  (cost=170.00..218.78 rows=2000 width=19) (actual time=1.235..3.279 rows=2000 loops=1)
--               Hash Cond: (c.branch_address_id = s.street_id)
--               ->  Hash Join  (cost=112.00..155.52 rows=2000 width=16) (actual time=0.822..2.314 rows=2000 loops=1)
--                     Hash Cond: (c.branch_address_id = ba.branch_address_id)
--                     ->  Hash Join  (cost=56.00..94.26 rows=2000 width=12) (actual time=0.479..1.402 rows=2000 loops=1)
--                           Hash Cond: (r1.car_id = c.car_id)
--                           ->  Seq Scan on rent r1  (cost=0.00..33.00 rows=2000 width=12) (actual time=0.002..0.212 rows=2000 loops=1)
--                           ->  Hash  (cost=31.00..31.00 rows=2000 width=8) (actual time=0.469..0.471 rows=2000 loops=1)
--                                 Buckets: 2048  Batches: 1  Memory Usage: 95kB
--                                 ->  Seq Scan on car c  (cost=0.00..31.00 rows=2000 width=8) (actual time=0.004..0.255 rows=2000 loops=1)
--                     ->  Hash  (cost=31.00..31.00 rows=2000 width=4) (actual time=0.340..0.340 rows=2000 loops=1)
--                           Buckets: 2048  Batches: 1  Memory Usage: 87kB
--                           ->  Seq Scan on branch_address ba  (cost=0.00..31.00 rows=2000 width=4) (actual time=0.004..0.183 rows=2000 loops=1)
--               ->  Hash  (cost=33.00..33.00 rows=2000 width=15) (actual time=0.406..0.407 rows=2000 loops=1)
--                     Buckets: 2048  Batches: 1  Memory Usage: 110kB
--                     ->  Seq Scan on street s  (cost=0.00..33.00 rows=2000 width=15) (actual time=0.008..0.194 rows=2000 loops=1)
-- Planning Time: 0.420 ms
-- Execution Time: 4.962 ms


create index on rent(price);
drop index rent_price_idx;
set enable_seqscan to 'on';
set work_mem to '4MB';

--RESULT AFTER

-- Group  (cost=515.50..535.50 rows=2000 width=19) (actual time=3.999..4.359 rows=2000 loops=1)
-- "  Group Key: r1.price, r1.rent_period, s.street_name"
--   ->  Sort  (cost=515.50..520.50 rows=2000 width=19) (actual time=3.998..4.064 rows=2000 loops=1)
-- "        Sort Key: r1.price DESC, r1.rent_period, s.street_name"
--         Sort Method: quicksort  Memory: 205kB
--         ->  Hash Join  (cost=292.11..405.85 rows=2000 width=19) (actual time=1.865..3.212 rows=2000 loops=1)
--               Hash Cond: (c.branch_address_id = s.street_id)
--               ->  Hash Join  (cost=188.83..297.31 rows=2000 width=16) (actual time=0.885..1.889 rows=2000 loops=1)
--                     Hash Cond: (c.branch_address_id = ba.branch_address_id)
--                     ->  Hash Join  (cost=101.56..204.77 rows=2000 width=12) (actual time=0.459..1.117 rows=2000 loops=1)
--                           Hash Cond: (r1.car_id = c.car_id)
--                           ->  Index Scan Backward using rent_price_idx on rent r1  (cost=0.28..98.23 rows=2000 width=12) (actual time=0.005..0.295 rows=2000 loops=1)
--                           ->  Hash  (cost=76.28..76.28 rows=2000 width=8) (actual time=0.449..0.449 rows=2000 loops=1)
--                                 Buckets: 2048  Batches: 1  Memory Usage: 95kB
--                                 ->  Index Scan using car_pkey on car c  (cost=0.28..76.28 rows=2000 width=8) (actual time=0.005..0.270 rows=2000 loops=1)
--                     ->  Hash  (cost=62.28..62.28 rows=2000 width=4) (actual time=0.413..0.413 rows=2000 loops=1)
--                           Buckets: 2048  Batches: 1  Memory Usage: 87kB
--                           ->  Index Only Scan using branch_address_pkey on branch_address ba  (cost=0.28..62.28 rows=2000 width=4) (actual time=0.022..0.193 rows=2000 loops=1)
--                                 Heap Fetches: 0
--               ->  Hash  (cost=78.28..78.28 rows=2000 width=15) (actual time=0.974..0.974 rows=2000 loops=1)
--                     Buckets: 2048  Batches: 1  Memory Usage: 110kB
--                     ->  Index Scan using street_pkey on street s  (cost=0.28..78.28 rows=2000 width=15) (actual time=0.008..0.572 rows=2000 loops=1)
-- Planning Time: 0.451 ms
-- Execution Time: 4.430 ms



explain (analyse )
select c.customer_name,car.car_id
from customer c
left join rent r1 on c.rent_id = r1.rent_id
left join car on  r1.car_id = car.car_id;

-- RESULTS BEFORE

-- Hash Right Join  (cost=78.28..118.88 rows=210 width=520) (actual time=4.059..5.649 rows=2000 loops=1)
--   Hash Cond: (car.car_id = r1.car_id)
--   ->  Seq Scan on car  (cost=0.00..31.00 rows=2000 width=4) (actual time=0.010..0.343 rows=2000 loops=1)
--   ->  Hash  (cost=75.65..75.65 rows=210 width=520) (actual time=4.032..4.036 rows=2000 loops=1)
--         Buckets: 2048 (originally 1024)  Batches: 1 (originally 1)  Memory Usage: 118kB
--         ->  Hash Left Join  (cost=58.00..75.65 rows=210 width=520) (actual time=1.827..3.314 rows=2000 loops=1)
--               Hash Cond: (c.rent_id = r1.rent_id)
--               ->  Seq Scan on customer c  (cost=0.00..17.10 rows=210 width=520) (actual time=0.034..0.415 rows=2000 loops=1)
--               ->  Hash  (cost=33.00..33.00 rows=2000 width=8) (actual time=1.773..1.775 rows=2000 loops=1)
--                     Buckets: 2048  Batches: 1  Memory Usage: 95kB
--                     ->  Seq Scan on rent r1  (cost=0.00..33.00 rows=2000 width=8) (actual time=0.016..0.860 rows=2000 loops=1)
-- Planning Time: 0.654 ms
-- Execution Time: 5.883 ms

create index name_idx on customer(customer_name);

--RESULTS AFTER

-- Hash Left Join  (cost=114.00..159.52 rows=2000 width=520) (actual time=0.646..1.572 rows=2000 loops=1)
--   Hash Cond: (r1.car_id = car.car_id)
--   ->  Hash Left Join  (cost=58.00..98.26 rows=2000 width=520) (actual time=0.358..0.967 rows=2000 loops=1)
--         Hash Cond: (c.rent_id = r1.rent_id)
--         ->  Seq Scan on customer c  (cost=0.00..35.00 rows=2000 width=520) (actual time=0.006..0.192 rows=2000 loops=1)
--         ->  Hash  (cost=33.00..33.00 rows=2000 width=8) (actual time=0.348..0.349 rows=2000 loops=1)
--               Buckets: 2048  Batches: 1  Memory Usage: 95kB
--               ->  Seq Scan on rent r1  (cost=0.00..33.00 rows=2000 width=8) (actual time=0.003..0.169 rows=2000 loops=1)
--   ->  Hash  (cost=31.00..31.00 rows=2000 width=4) (actual time=0.284..0.284 rows=2000 loops=1)
--         Buckets: 2048  Batches: 1  Memory Usage: 87kB
--         ->  Seq Scan on car  (cost=0.00..31.00 rows=2000 width=4) (actual time=0.002..0.128 rows=2000 loops=1)
-- Planning Time: 0.359 ms
-- Execution Time: 1.638 ms

drop index name_idx;