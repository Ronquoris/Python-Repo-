import psycopg2

def table():
    trust_me_bro=psycopg2.connect(dbname="postgres", user="postgres", password="Ronronit@31", host="localhost", port="5432")

    cursor=trust_me_bro.cursor()
    cursor.execute('''create table emp(emp_id int, emp_name text, emp_salary int)''')

    trust_me_bro.commit()
    trust_me_bro.close()

def data():
    trust_me_bro=psycopg2.connect(dbname="postgres", user="postgres", password="Ronronit@31", host="localhost", port="5432")

    cursor=trust_me_bro.cursor()

    emp_id=int(input('enter emp id: '))
    emp_name=input('enter emp name: ')
    emp_salary=int(input('enter emp salary: '))

    querry='''insert into emp values (%s, %s, %s);'''
    cursor.execute(querry, (emp_id, emp_name, emp_salary))
    print('see just trust me :)')

    trust_me_bro.commit()
    trust_me_bro.close()

def extract():
    trust_me_bro=psycopg2.connect(dbname="postgres", user="postgres", password="Ronronit@31", host="localhost", port="5432")

    cursor=trust_me_bro.cursor()
    cursor.execute('''select * from emp;''')

    

    show=cursor.fetchall()
    for i in show:
        print(i)

    trust_me_bro.commit()
    trust_me_bro.close()

data()