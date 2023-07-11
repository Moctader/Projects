import random
from School import School
class Person:
    def __init__(self,name) -> None:
        self.name=name
        
class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def teach(self):
        pass
    
    def __repr__(self) -> str:
        return f'{self.name}'
    
    def evalute_exam(self):
        marks=random.randint(0,100)
        return marks


class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.__id=None
        self.classroom=classroom
        self.marks={}
        self.subject_grades={}
        self.grade=None
        
    def calculte_final_grade(self):
        sum=0
        for grade in self.subject_grades.values():
            points=School.grade_to_value(grade)
            sum +=points
            print(self.name, grade, points)
        points_avg=sum/len(self.subject_grades)
        self.grade=School.value_to_grade(points_avg)
        print(f'{self.name} final_grade: {self.grade} with points avg: {points_avg}')
        
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        return self.__id==value
        
    
     