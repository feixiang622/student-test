# coding = utf-8
import sys
import json
import file_mana
import model
import manage

datafile = 'data.json'

def register():
    u_check = file_mana.file_mana(datafile)
    while True:
        uid = input("请输入账号（要求2~4位）：")
        if not 2 < len(uid) < 6:
            print("格式非法")
            continue
        elif uid in u_check:
            print("此账号已注册，请重新注册新账号！")
            continue
        else:
            break
    while True:
        passwd = input("请输入6位密码：")
        if len(passwd) < 6:
            print("密码不够6位，请重新输入！")
            continue
        else:
            break

    t = model.Teacher(uid, passwd)
    u_check[t.uid] = t.passwd
    # print(u_check)
    file_mana.wirte_json(datafile, u_check)

def login():
    u_check = file_mana.file_mana(datafile)
    u_login = input("请输入教师账号id：")
    if u_login not in u_check:
        print("账号不存在！")
        return
    u_passwd = input("请输入密码：")
    if u_passwd != u_check[u_login]:
        print("密码不对！")
        return
    # 登录成功后显示功能菜单
    manage.show()


def start():
    with open('welcom', encoding='UTF-8') as w:
        print(w.read())
    while True:
        chose = int(input("请输入选择1~3："))
        if chose == 1:
            login()
        elif chose == 2:
            print("准备注册")
            register()  # 进入注册程序
        elif chose == 3:
            print("系统推出")
            break
        else:
            print("无效输入!")
            sys.exit(0)


# # 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    start()
