class Teacher():
    def __init__(self,uid,passwd):
        self.uid = uid
        self.passwd = passwd

class Student():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return f'{self.name},{self.age},{self.gender}'