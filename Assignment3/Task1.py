import psycopg2
import json

conn = psycopg2.connect(dbname="test", user="postgres",
        password="123456")

cur = conn.cursor()



#answer c
cur.execute(
		'CREATE TABLE sailors ('
		'sid integer,'
		'sname varchar(20),'
		'rating integer,'
		'age real'
		')'
	)


cur.execute(
		"INSERT INTO sailors "
        "VALUES(22, 'Dustin', 7, 45.0),"
        "(29, 'Brutus', 1, 33.0),"
        "(31, 'Lubber', 8, 55.5),"
        "(32, 'Andy', 8, 25.5),"
        "(64, 'Horatio', 7, 35.0),"
        "(71, 'Zorba', 10, 16.0)"
    )

print 'Create Sailors!'

#answer e
cur.execute(
	'alter table sailors add primary key(sid)'
	)

cur.execute(
	'alter table sailors alter COLUMN sname set not null'
	)

print 'Set the constraint!'

#answer f
cur.execute(
	'update sailors set rating = rating+1 where rating < 7'
	)

print 'Update non-advanced sailors'


#answer g
cur.execute(
		'CREATE TABLE Boats ('
		'bid integer,'
		'bname varchar(20),'
		'color varchar(20),'
		'primary key(bid)'
		')'
	)

cur.execute(
		"INSERT INTO Boats "
		"VALUES(101, 'Interlake', 'Blue'), "
		"(102, 'Interlake', 'Red'), "
		"(103, 'Clipper', 'Green'), "
		"(104, 'Marine', 'Red')"
	)

print 'Create Boats!'

#answer h
cur.execute(
		'CREATE TABLE Reserves ('
		'sid integer references sailors(sid), '
		'bid integer references Boats(bid), '
		'day DATE'
		')'
	)

cur.execute(
		"INSERT INTO Reserves "
		"VALUES(29, 101, '1973-10-10'), "
		"(29, 102, '1977-02-03'), "
		"(32, 102, '1944-07-29'), "
		"(64, 101, '1948-01-07'), "
		"(71, 103, '2005-12-17')"
	)

print 'Create Reserves!'

#answer i
print 'Question i:', '\n'
cur.execute(
	"select sname from sailors where sid in (select distinct tem1.sid from (select * from Reserves inner join Boats on Reserves.bid = Boats.bid) as tem1 where tem1.color = 'Red')"
	)

rows = cur.fetchall()

for row in rows:
	print 'sname = ', row[0], '\n'


#answer j
cur.execute('create index idx_btree_day on Reserves using btree(day)')

print 'Create Btree Index!'

#answer j
print 'Question j:', '\n'

cur.execute("select sname from sailors where sid in (select sid from Reserves where day > '1977-01-01')")

rows = cur.fetchall()

for row in rows:
	print 'sname = ', row[0], '\n'



#answer k
print 'Question k:', '\n'

cur.execute("select sid from sailors where sid not in (select tem1.sid from (select * from Reserves inner join Boats on Reserves.bid = Boats.bid) as tem1 where tem1.color = 'Red') and sid in (select tem2.sid from (select * from Reserves inner join Boats on Reserves.bid = Boats.bid) as tem2 where tem2.color != 'Red') and age > 20")

rows = cur.fetchall()

for row in rows:
	print 'sid = ', row[0], '\n'




conn.commit()

conn.close()