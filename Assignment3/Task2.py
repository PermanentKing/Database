#Task2
import psycopg2
import json

conn = psycopg2.connect(dbname="test", user="postgres",
        password="123456")

cur = conn.cursor()

cur.execute(
		'CREATE TABLE families_j('
		'id integer, '
		'profile json'
		')'
	)



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

print 'Create families_j!'

print 'Question c:', '\n'
cur.execute("select profile->'members' from families_j where profile->>'name' = 'Gomez'")


rows = cur.fetchall()
#type of rows is 'list'

#print rows[0][0]

print 'number = ', len(rows[0][0]), '\n'

tempname = []

for row in rows[0][0]:
	tempname.append(row['member']['name'])
	print row['member']['name']

print '\n'


tempjs = {
	"num":len(rows[0][0]),
	"name":tempname
}

templs = json.dumps(tempjs)

print templs, '\n'

cur.execute(
		'CREATE TABLE families_b ('
		'id integer, '
		'profile json'
		')'
	)


cur.execute(
		"INSERT INTO families_b "
		"VALUES(1, '%s'"%(templs) + ")"
	)
cur.execute("select * from families_j where id = 1")

rows = cur.fetchall()
print 'families_j:'
for row1 in rows[0]:
	print row1


cur.execute("select * from families_b where id = 1")

rows = cur.fetchall()
print 'families_b:'
for row1 in rows[0]:
	print row1



conn.commit()

conn.close()