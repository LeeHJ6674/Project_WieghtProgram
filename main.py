import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

conn = sqlite3.connect("D:\SQLite\Python0702.db", isolation_level=None) #파일접속 or 생성

c = conn.cursor()                                       #커서 획득

c.execute("CREATE TABLE IF NOT EXISTS table1 \
(id integer PRIMARY KEY, name text, birthday text)")    #테이블 생성

##########################################################################################################################

c.execute("INSERT INTO table1(id, name, birthday) \
    VALUES(?,?,?)",\
    (2, 'KIM', '1990-00-00'))                           #데이터 입력1

c.execute("INSERT INTO table1 \
    VALUES(1, 'LEE', '1987-00-00')")                    #데이터 입력2

test_tuple = (
    (3, 'PARK', '1991-00-00'),
    (4, 'CHOI', '1999-00-00'),
    (5, 'JUNG', '1989-00-00')
)
c.executemany("INSERT INTO table1(id, name, birthday) VALUES(?,?,?)", test_tuple) #데이터 튜플, 리스트 입력

##########################################################################################################################

c.execute("SELECT * FROM table1")
print(c.fetchone())
print(c.fetchone())
print(c.fetchall())              #데이터 불러오기

c.execute("SELECT * FROM table1")
print(c.fetchall())              #전체 데이터 불러오기

##########################################################################################################################

c.execute("UPDATE table1 SET name=? WHERE id=?", ('NEW1', 1))                       #데이터 수정1

c.execute("UPDATE table1 SET name=:name WHERE id=:id", {"name": 'NEW2', 'id': 3})   #데이터 수정2

c.execute("UPDATE table1 SET name='%s' WHERE id='%s'" % ('NEW3', 5))                #데이터 수정3

for row in c.execute('SELECT * FROM table1'):
    print(row)                                                                      #수정한 데이터 확인

##########################################################################################################################

c.execute("DELETE FROM table1 WHERE id=?", (1,))        #데이터 삭제1

c.execute("DELETE FROM table1 WHERE id=:id", {'id': 3}) #데이터 삭제1

c.execute("DELETE FROM table1 WHERE id='%s'" % 5)       #데이터 삭제1

for row in c.execute('SELECT * FROM table1'):
    print(row)                                          #삭제한 데이터 확인





#생각해야 할 것
#1. 데이터 입력은 어떻게 할 것인지?
#2. 테이블 수정은 어떻게 할 것인지?
#3. 디스플레이는 어떻게 띄울 것인지?
#4. 프로그램 구성은 어떻게 할 것인지?
#
