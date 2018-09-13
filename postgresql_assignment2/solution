CREATE DATABASE tpc_h OWNER wangjing;
GRANT ALL PRIVILEGES ON DATABASE tpc_h to wangjing;

\i '/Users/wangjing/data/dss.ddl';
copy customer from '/Users/wangjing/data/customer.tbl' with delimiter as'|';
copy part from '/Users/wangjing/data/part.tbl' with delimiter as'|';
copy supplier from '/Users/wangjing/data/supplier.tbl' with delimiter as'|';
copy partsupp from '/Users/wangjing/data/partsupp.tbl' with delimiter as'|';
copy nation from '/Users/wangjing/data/nation.tbl' with delimiter as'|';
copy lineitem from '/Users/wangjing/data/lineitem.tbl' with delimiter as'|';
copy region from '/Users/wangjing/data/region.tbl' with delimiter as'|';
copy orders from '/Users/wangjing/data/orders.tbl' with delimiter as'|';

/*a*/
select s_name, s_address, s_nationkey from supplier where s_suppkey=717;

/*b*/
select o_shippriority, count(o_shippriority) from orders where o_orderdate between '1992-01-01' and '1993-12-31' group by o_shippriority order by o_shippriority desc;

/*c*/
select s_name, s_phone, n_name, r_name from ((SELECT * FROM supplier WHERE s_suppkey in (SELECT ps_suppkey FROM partsupp WHERE ps_partkey=360)) as new1 left outer join (nation left outer join region ON nation.n_regionkey = region.r_regionkey) as new2 ON new1.s_nationkey = new2.n_nationkey) as new3;

/*d*/
select new1.l_suppkey, new1.count, new2.count from (select l_suppkey, count(l_suppkey) from lineitem where l_commitdate between '1992-01-01' and '1992-12-31' group by l_suppkey) as new1 inner join (select l_suppkey, count(l_suppkey) from lineitem where l_commitdate between '1993-01-01' and '1993-12-31' group by l_suppkey) as new2 on new1.l_suppkey = new2.l_suppkey and new1.count <= new2.count;

/*display orders from europe*/
select distinct l_orderkey from lineitem where l_suppkey in (select distinct s_suppkey from supplier where s_nationkey in (select n_nationkey from nation inner join region on r_name='EUROPE' and n_regionkey=r_regionkey));


/*display customers nuo from europe*/
select c_custkey, c_name from customer where c_nationkey in (select n_nationkey from nation inner join region on r_name!='EUROPE' and n_regionkey=r_regionkey);


/*g*/
select * into temp1 from lineitem where l_shipdate between '1997-11-01' and '1997-11-30';
delete from temp1 where l_shipmode='AIR' or l_shipmode='MAIL';
select l_shipmode, avg(l_quantity) from temp1 group by l_shipmode order by avg(l_quantity);


/*Show the total number of customers in each region*/
select count(new3.c_custkey), new3.r_name from ((select c_custkey, c_nationkey from customer) as new1 inner join (select n_nationkey, n_regionkey, r_name from nation inner join region on n_regionkey=r_regionkey) as new2 on new1.c_nationkey=new2.n_regionkey) as new3 group by new3.r_name;

/*Display all the info (partkey,name,....,coment)of the top 5 parts with the largest size*/
select * from part order by p_size desc limit 5;

/*j-Find the customer whose phone is 25-XXX-XXX-XXXX*/
select c_custkey, c_phone from customer where c_phone like '25-%-%-%';

/*k-Find the lineitem which has the maximum extended price and is ordered before 1997. Display the value of this maximum extended price*/
select l_orderkey, l_extendedprice from lineitem where l_commitdate <= '1997-01-01' order by l_extendedprice desc limit 1;

create index supplier_index ON supplier (s_suppkey);
explain analyze select s_name, s_address, s_nationkey from supplier where s_suppkey=717;
drop index supplier_index;

create index customer_index ON customer (c_phone);
explain (analyze) select c_custkey, c_phone from customer where c_phone like '25-%-%-%';
drop index customer_index;

create index lineitem_index ON lineitem (l_extendedprice);
explain analyze select l_orderkey, l_extendedprice from lineitem where l_commitdate <= '1997-01-01' order by l_extendedprice desc limit 1;
drop index lineitem_index;

create index supplier_index ON supplier using hash (s_suppkey);
explain analyze select s_name, s_address, s_nationkey from supplier where s_suppkey=717;
drop index supplier_index;

create index customer_index ON customer using hash (c_phone);
explain (analyze) select c_custkey, c_phone from customer where c_phone like '25-%-%-%';
drop index customer_index;

create index lineitem_index ON lineitem using hash (l_extendedprice);
explain analyze select l_orderkey, l_extendedprice from lineitem where l_commitdate <= '1997-01-01' order by l_extendedprice desc limit 1;
drop index lineitem_index;






