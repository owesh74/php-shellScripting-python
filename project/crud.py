import pymysql
import csv
from prettytable import PrettyTable
conn = pymysql.connect(host='localhost', user='diituser', password = "%TGBbgt5", db='ecom')
cur = conn.cursor(pymysql.cursors.DictCursor);

def exportData():
    to_csv = showData();

    keys = to_csv[0].keys()
    file_path = 'students.csv';
    with open(file_path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(to_csv)

    print(f"Data exported in {file_path}");

def updateData():
    student_id = int(input("Enter id: "));
    student_name = input("Enter name: ");
    student_age = int(input("Enter age: "));
    student_city = input("Enter city: ");
    sql = f"UPDATE `students` SET `name` = '{student_name}', `age` = '{student_age}', `city` = '{student_city}' WHERE `students`.`id` = {student_id}";
    cur.execute(sql);
    conn.commit();
    showData();


def insertData():
    student_name = input("Enter name: ");
    student_age = int(input("Enter age: "));
    student_city = input("Enter city: ");
    sql = f"INSERT INTO `students` (`id`, `name`, `age`, `city`) VALUES (NULL, '{student_name}', '{student_age}', '{student_city}' )";
    cur.execute(sql);
    conn.commit();
    showData();


def deleteData():
    student_id = int(input("Enter id to delete record: "));
    sql = f"DELETE FROM students WHERE id = {student_id}";
    cur.execute(sql);
    conn.commit();
    showData();


def showData():
    sql = "SELECT * FROM students";
    cur.execute(sql)
    records = cur.fetchall()


    t = PrettyTable(['id', 'name','age','city'])

    for student in records:
        t.add_row([student['id'], student['name'], student['age'], student['city']]);

    print(t);
    return records;


option = None;

while(option != 0):
    print("\n--_--_--_--_--_--\n");
    print("1. Show Data");
    print("2. Delete data");
    print("3. Insert data");
    print("4. Update data");
    print("5. Export data");
    print("0. Exit");

    option = int(input("Choose Option: "));
    if(option == 0 or option == 1 or option ==2 or option ==3 or option ==4 or option ==5):
        if(option == 1):
            showData();


        if(option == 2):
            deleteData();


        if(option == 3):
            insertData();


        if(option == 4):
            updateData();


        if(option == 5):
            exportData();

    
        if(option == 0):
            print("Thank you for using our software");
    else:
        print("Invalid input")
