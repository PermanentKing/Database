



#select tem1.sid from Reserves inner join Boats on Reserves.bid = Boats.bid as tem1 where tem1.color = 'Red';

#select * from Reserves inner join Boats  as tem1 on Reserves.bid = Boats.bid as tem1;

select tem1.sid from (select * from Reserves inner join Boats on Reserves.bid = Boats.bid) as tem1 where tem1.color = 'Red';


create index idx_btree_day on Reserves using btree(day);

#select sid from Reserves where day > '1977-01-01';

select sname from sailors where sid in (select sid from Reserves where day > '1977-01-01');



(select tem1.sid from (select * from Reserves inner join Boats on Reserves.bid = Boats.bid) as tem1 where tem1.color = 'Red')

(select tem2.sid from (select * from Reserves inner join Boats on Reserves.bid = Boats.bid) as tem2 where tem2.color != 'Red')

select sid from sailors where sid not in (select tem1.sid from (select * from Reserves inner join Boats on Reserves.bid = Boats.bid) as tem1 where tem1.color = 'Red') and sid in (select tem2.sid from (select * from Reserves inner join Boats on Reserves.bid = Boats.bid) as tem2 where tem2.color != 'Red') and age > 20;


create table families_j(id integer, profile json);


{
	"name":"Gomez",
	"members":[
	{"member":{"relation":"padre", "name":"Alex"}},
	{"member":{"relation":"madre", "name":"Sonia"}},
	{"member":{"relation":"hijo", "name":"Brandon"}},
	{"member":{"relation":"hija", "name":"Azaleah"}}
	]
}


insert into families_j values(1, '{
	"name":"Gomez",
	"members":[
	{"member":{"relation":"padre", "name":"Alex"}},
	{"member":{"relation":"madre", "name":"Sonia"}},
	{"member":{"relation":"hijo", "name":"Brandon"}},
	{"member":{"relation":"hija", "name":"Azaleah"}}
	]
	}');


select profile#>>'{members, 1}' as name from families_j where profile->>'name' = 'Gomez';




