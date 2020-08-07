from datetime import datetime


class Student:
    def __init__(self, id, name, birthday):
        self.id = id
        self.name = name
        self.birthday = birthday

    def stprint(self):
        print("{},{},{}".format(self.id,
                                self.name, self.birthday))


st1 = Student("20180001", "李明", datetime(2000, 10, 1).strftime("%Y - %m - %d"))
st1.stprint()
