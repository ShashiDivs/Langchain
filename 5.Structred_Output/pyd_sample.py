from pydantic import BaseModel

class Student(BaseModel):

    name:str

names = {"name":"shashi"}

student = Student(**names)

print(student)

