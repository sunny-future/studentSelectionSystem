class Student(object):
    operate_list = [
        "查看可选课程",
        "选择课程",
        "查看所选课程",
        "退出程序",
    ]

    def __init__(self, name):
        self.name = name
        self.course = []

    def show_course(self):
        print("查看可选的课程")

    def select_course(self):
        print('选择课程')

    def show_selected_course(self):
        print('查看所选课程')

    def log_out(self):
        quit('886')


class Teacher(object):
    pass

