# #task 1
class DataBase:

    __instance = None # link to class object

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Connection with DB: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("Closing connection")

    def read(self):
        return "Data from DB"

    def write(self, data):
        print(f"Writing to DB {data}")


db1 = DataBase("root1", "1234", 80)
db2 = DataBase("root2", "12345", 40) # object db1 not created, db1 is link to db

print(id(db1), id(db2))
db1.connect()
db2.connect()
#task 2
from math import *
class Math:
    def __init__(self,func):
        self.__fn = func
    def __call__(self,x, *args, **kwds):
        return self.__fn(x)   
@Math
def foo(x):
    return int(sqrt(x))
print(foo(25))