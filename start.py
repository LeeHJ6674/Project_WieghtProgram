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
### test data Bench Press, 210202, 5, 10, 60 ###
def record():
    yn = True
    while yn:
        l = input('name, date, set, raps, weight : \n')
        k = list(l.split(','))
        k[0] = str(k[0])
        k[1] = int(k[1])
        k[2] = int(k[2])
        k[3] = float(k[3])
        k[4] = float(k[4])
        kt = (k[0], k[1], k[2], k[3], k[4])
        print('{0} transform success \nData is {1} Right? (Y/N)'.format(type(kt), kt))
        s = input()
        if s == 'Y':
            c.execute("INSERT INTO Record(name, 'date', 'set', raps, weight) VALUES(?,?,?,?,?)", kt)
            yn = False
        elif s == 'N':
            pass
    conn.commit()
def load() :
    print('')
    #1. 오름차순, 내림차순






#c.execute("CREATE TABLE IF NOT EXISTS table1 \
#(id integer PRIMARY KEY, name text, birthday text)")  # 테이블 생성

# 생각해야 할 것
# 1. 데이터 입력은 어떻게 할 것인지?
# 2. 테이블 수정은 어떻게 할 것인지?
# 3. 디스플레이는 어떻게 띄울 것인지?
# 4. 프로그램 구성은 어떻게 할 것인지?
#
