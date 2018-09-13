import psycopg2

conn = psycopg2.connect(dbname="test", user="postgres", password="123456")

cur = conn.cursor()

# cur.execute(
# 		'CREATE TABLE sailors ('
# 		'sid integer,'
# 		'sname varchar(20),'
# 		'rating integer,'
# 		'age real'
# 		')'
# 	)

# cur.execute(
# 		"INSERT INTO sailors "
#         "VALUES(22, 'Dustin', 7, 45.0),"
#         "(29, 'Brutus', 1, 33.0),"
#         "(31, 'Lubber', 8, 55.5),"
#         "(32, 'Andy', 8, 25.5),"
#         "(64, 'Horatio', 7, 35.0),"
#         "(71, 'Zorba', 10, 16.0)"
#     )

# cur.execute(
# 	'alter table sailors add primary key(sid)'
# 	)

# cur.execute(
# 	'alter table sailors alter COLUMN sname set not null'
# 	)


# cur.execute(
# 	'update sailors set rating = rating+1 where rating < 7'
# 	)

# cur.execute(
# 		'CREATE TABLE Boats ('
# 		'bid integer,'
# 		'bname varchar(20),'
# 		'color varchar(20),'
# 		'primary key(bid)'
# 		')'
# 	)

# cur.execute(
# 		"INSERT INTO Boats "
# 		"VALUES(101, 'Interlake', 'Blue'), "
# 		"(102, 'Interlake', 'Red'), "
# 		"(103, 'Clipper', 'Green'), "
# 		"(104, 'Marine', 'Red')"
# 	)

# cur.execute(
# 		'CREATE TABLE Reserves ('
# 		'sid integer references sailors(sid), '
# 		'bid integer references Boats(bid), '
# 		'day DATE'
# 		')'
# 	)

# # cur.execute(
# # 		"INSERT INTO Reserves "
# # 		"VALUES(29, 101, '1973-10-10'), "
# # 		"(29, 102, '1977-02-03'), "
# # 		"(32, 102, '1944-07-29'), "
# # 		"(64, 101, '1948-01-07'), "
# # 		"(71, 103, '2005-12-17')"
# # 	)

# # #answer i
# # cur.execute(
# # 	"select tem1.sid from (select * from Reserves inner join Boats on Reserves.bid = Boats.bid) as tem1 where tem1.color = 'Red'"
# # 	)

cur.execute(
		'CREATE TABLE families_j('
		'id integer, '
		'profile json'
		')'
	)


# cur.execute(
# 		"INSERT INTO families_j "
# 		"VALUES(1, '{"
# 		"'name':'Gomez',"
# 		"'members':["
# 		"{'member':{'relation':'padre', 'name':'Alex'}},"
# 		"{'member':{'relation':'madre', 'name':'Sonia'}},"
# 		"{'member':{'relation':'hijo', 'name':'Brandon'}},"
# 		"{'member':{'relation':'hija', 'name':'Azaleah'}}"
# 		"]"
# 		"}')"
# 	)

cur.execute(
"""INSERT INTO families_j 
VALUES(1, 
'{"name":"Gomez","members":[
	{"member":{"relation":"padre", "name":"Alex"}},
	{"member":{"relation":"madre", "name":"Sonia" }},
	{"member":{"relation":"hijo", "name":"Brandon"}},
	{"member":{"relation":"hija", "name":"Azaleah"}}
	]}')"""
)


#test
# cur.execute('select * from families_j')

# rows = cur.fetchall()

# print rows



conn.commit()

conn.close()