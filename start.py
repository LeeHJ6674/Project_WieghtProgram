import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

a = input("Enter the file what you wanna connect. \nThis is Weight Record Program : ")
if not a:
    a = "D:\SQLite\Test0705.db"
conn = sqlite3.connect(a, isolation_level=None)  # 파일접속 or 생성

c = conn.cursor()  # 커서 획득
print("Connection Complete")

c.execute("CREATE TABLE IF NOT EXISTS Record \
(id integer PRIMARY KEY, name text, 'date' integer, 'set' integer, raps NUMERIC, weight NUMERIC)")

#####################선택지#############################

def record():
    a = input('name, date, set, raps, weight : \n')









#c.execute("CREATE TABLE IF NOT EXISTS table1 \
#(id integer PRIMARY KEY, name text, birthday text)")  # 테이블 생성

# 생각해야 할 것
# 1. 데이터 입력은 어떻게 할 것인지?
# 2. 테이블 수정은 어떻게 할 것인지?
# 3. 디스플레이는 어떻게 띄울 것인지?
# 4. 프로그램 구성은 어떻게 할 것인지?
#
