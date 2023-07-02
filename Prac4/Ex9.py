from shutil import copyfile
import pickle

# student_info = [{
#     'id': 20200000,
#     'name': 'Nguyen Van A',
#     'score': {
#         'math': 7.8,
#         'english': 8.9,
#         'physics': 9.0,
#     }
# },
#     {
#         'id': 20200001,
#         'name': 'Le Van B',
#         'score': {
#             'math': 9.8,
#             'english': 8.7,
#             'physics': 7.6,
#         }
#     }
# ]
# with open('student_info.pkl','wb') as temp:
#     pickle.dump(student_info,temp)
with open('student_info.pkl','rb') as temp:
    myfile=pickle.load(temp)
    print(myfile)
temp.close()
with open('updated_info.pkl','rb') as my_updated:
    print(pickle.load(my_updated))


copyfile('student_info.pkl', 'updated_info.pkl')

def add_student_info(new_student:dict):
    lmao=True
    with open('updated_info.pkl', 'rb') as file:
        list_of_students = list(pickle.load(file))

    if 'id' in new_student:
        for i in range(len(list_of_students)):
            student=list_of_students[i]
            if  student['id']==new_student['id']:
                list_of_students[i]=new_student
                lmao = False
                break
    if lmao:
            list_of_students.append(new_student)
    with open('updated_info.pkl','wb') as file:

        pickle.dump(list_of_students,file)



new_student = {
        'id': 20200000,
        'name': 'Nguyen Van Anh',
        'score': {
            'math': 7.8,
            'english': 8.4,
            'physics': 8.0,
        }
    }

new_student_1={
'id': 20200001,
 'name': 'Le Van Bien',
 'score': {
 'math': 8.9,
 'english': 8.0,
'physics': 5.6,
 }
 }
new_student_2={
'id': 20200003,
 'name': 'Nguyen Trong Tam',
 'score': {
 'math': 8.9,
 'english': 8.0,
'physics': 5.6,
 }
 }
add_student_info(new_student)

add_student_info(new_student_1)
add_student_info(new_student_2)


with open('updated_info.pkl','rb') as file1:
    temp=pickle.load(file1)
    print(temp)
file1.close()