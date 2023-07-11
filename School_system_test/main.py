from School import School, ClassRoom, Subject
from Person import Student, Teacher


def main():
    school=School('School', 'ngn')
    
    eight=ClassRoom('eight')
    school.add_classroom(eight)
    Nine=ClassRoom('Nine')
    school.add_classroom(Nine)
    ten=ClassRoom('ten')
    school.add_classroom(ten)
    
    #add students
    abul=Student('qe 1', eight)
    school.student_admission(abul)
    
    kabul=Student('qe 2', eight)
    school.student_admission(kabul)
    
    jabul=Student('qe 3', eight)
    school.student_admission(jabul)
    
    
    #Subjects
    Physics_teacher=Teacher('topon')
    physics=Subject('physics', Physics_teacher)
    eight.add_subject(physics)
    
    Chemistry_teacher=Teacher('haradhon')
    Chemistry=Subject('Chemistry', Chemistry_teacher)
    eight.add_subject(Chemistry)
    
    Biology_teacher=Teacher('Ajmal')
    Biology=Subject('Biology', Biology_teacher)
    eight.add_subject(Biology)
    
    eight.take_semester_final()
    
    
    
    print(school)
    
if __name__=='__main__':
    main()