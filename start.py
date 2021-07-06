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















































while True:
    b = int(input(
        "1. Record data \n2. Delete data \n3. Re-write data \n4. Show data \n5. Quit program \nWhat do you want? : "))
    if b == 1:  # 데이터 기록
        print("1")
        x = True
        while x:

            a1=input("Enter the name : ")
            a2=input("Enter the date : ")
            a3=input("Enter the set : ")
            a4=input("Enter the raps : ")
            a5=input("Enter the weight : ")
            print(a1,a2,a3,a4,a5)
            print("Confirm one more time" )
            t=input("Right? T/F : ")
            c.execute("INSERT INTO Record VALUES(a1, a2, a3, a4, a5)")



        break
        #









    elif b == 2:  # 데이터 삭제
        print("2")
        break

    elif b == 3:  # 데이터 수정
        print("3")
        break

    elif b == 4:  # 데이터 조회
        print("4")
        break

    if b == 5:  # 프로그램 종료
        print("5")
        break

    else :
        print("There are not %d " %b)
        pass

#c.execute("CREATE TABLE IF NOT EXISTS table1 \
#(id integer PRIMARY KEY, name text, birthday text)")  # 테이블 생성

# 생각해야 할 것
# 1. 데이터 입력은 어떻게 할 것인지?
# 2. 테이블 수정은 어떻게 할 것인지?
# 3. 디스플레이는 어떻게 띄울 것인지?
# 4. 프로그램 구성은 어떻게 할 것인지?
#
