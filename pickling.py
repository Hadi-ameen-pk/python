import pickle
student={"name":"hadi","age":20}
with open("student_details.pkl","wb") as f:
    pickle.dump(student,f)

with open("student_details.pkl","rb") as f:
    s=pickle.load(f)
print(s)