from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

students={
    1:{"name":"adi",
    "age":"20",
    "year":"12"
    }
}

class student2(BaseModel):
    name:str
    age:int
    year:str

@app.get("/")
def index():
    return students[1]

#path parameter
@app.get("/get_student/{student_id}")
def get_student(student_id :int ):
    if student_id not in students:
        return {"student_is":"not present"}
    else:
        return students[student_id]
    
#Query parameter
@app.get("/get_by_name/{student_id}")
def get_students(name:str,student_id:int):
    if student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
        
    return {"student not found"}


#post method
# from pydanic import BaseModel
#create a class student
@app.post("/create_user/{student_id}")
def create_student(student_id:int,student:student2):
    if student_id in students:
        return {"messege":"student already exist"}
    
    students[student_id] = student.model_dump()
    return students[student_id]

# put method 
@app.put("/student_edit/{student_id}")
def update_student(student_id: int, student: student2):

    if student_id not in students:
        return {"message": "Student not found"}

    students[student_id] = student.model_dump()

    return students[student_id]
    

#delete method
@app.delete("/delete_student/{student_id}")
def delete_students(student_id: int):

    if student_id not in students:
        return {"message": "Student not found"}

    del students[student_id]

    return {"message": "Student deleted"}

