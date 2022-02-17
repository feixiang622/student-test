import model
import json
student_List = []
def show():
    with open('show', 'r', encoding='utf-8') as f:
        show_menu = f.read()
        print(show_menu)
    while True:
        c_menu = int(input("请输入功能选项："))
        if c_menu == 1:
            add_stu()
        elif c_menu == 2:
            del_stu()
        elif c_menu == 3:
            edit_stu()
        elif c_menu == 4:
            sear_stu()
        elif c_menu == 5:
            show_stu()
        elif c_menu == 6:
            save_stu()
        elif c_menu == 7:
            break

def add_stu():
    name = input("请输入学生名称：")
    age = input("请输入学生年龄：")
    gender = input("请输入学生性别：")

    student = model.Student(name, age, gender)
    print(student)
    global student_List
    student_List.append(student)
    # print(student_List)

def del_stu():
    del_name = input("请输入删除学生的姓名：")
    global student_List
    for n in student_List:
        # print(n.name)
        if n.name == del_name:
            student_List.remove(n)
            break
    else:
        print("查无此人！")
    # print(student_List)

def edit_stu():
    ed_name = input("请输入要修改的学生姓名：")
    global student_List
    for n in student_List:
        if n.name == ed_name:
            n.name = new_input(n.name, "请输入修改后的名字：")
            n.age = new_input(n.age, "请修改年龄：")
            n.gender = new_input(n.gender, "请修改性别：")
            print(f'修改后为：{n.name},{n.age},{n.gender}')
            break
    else:
        print("查无此人！")

def sear_stu():
    sear_name = input("请输入要查找的学生姓名：")
    global student_List
    for n in student_List:
        if n.name == sear_name:
            print(f'姓名：{n.name}, 年龄：{n.age}, 性别：{n.gender}')
            break
    else:
        print("查无此人！")


def show_stu():
    global student_List
    for n in student_List:
        print(f'{n.name}, {n.age}, {n.gender}')

def save_stu():
    global student_List
    studens = [f'{i.name},{i.age},{i.gender}' for i in student_List]
    with open('studens.data', 'w') as f:
        f.write(str(studens))

def logout():
    pass

def new_input(old, new):
    temp = input(new)
    if len(temp) > 0:
        return  temp
    else:
        return  old