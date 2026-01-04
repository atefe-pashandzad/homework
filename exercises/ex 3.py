student = [
{
"student_id": 403441236,
"name": "atefe",
"grade": [12,17,11,13]
},

{
"student_id": 403423457,
"name": "faeze",
"grade": [15,16,17,18]
},

{
"student_id": 403487654,
"name": "sara",
"grade": [19,17,15,10]
}
]
def calculate(student):
    grade = student["grade"]

    moadel = sum(grade)/len(grade)
    return moadel


for student in student:
    moadel = calculate(student)
    print("name",student["name"])
    print("moadel",moadel)
