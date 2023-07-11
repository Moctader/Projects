from School import School, ClassRoom, Subject
from Persons import Student, Teacher

def main():
    school=School('addam','tt')
    
    eight=ClassRoom('eight')
    school.add_classroom(eight)
    
    Nine=ClassRoom('Nine')
    school.add_classroom(Nine)
    
    ten=ClassRoom('ten')
    school.add_classroom(ten)
    
    #add students
    abul=Student('name',eight)
    school.student_admission(abul, eight)
    
    
    labul=Student('lname',eight)
    school.student_admission(labul, eight)
    
    
    mabul=Student('mname',eight)
    school.student_admission(mabul, eight)
    
    #subjects
    Physics_teacher=Teacher('shahjahan')
    physics=Subject('physics', Physics_teacher)
    eight.add_subject(physics)
    
    chemistry_teacher=Teacher('Haradhon')
    chemistry=Subject('chemistry', chemistry_teacher)
    eight.add_subject(chemistry)
    
    Biology_teacher=Teacher('Ajmol')
    Biology=Subject('Biology', Biology_teacher)
    eight.add_subject(Biology)
    
    
    eight.take_semester_final()
    
    
    print(school)
    
    
if __name__=='__main__':
    main()
    