class Student:
    college_name = "Aditya Institute of Technology"
    total_students = 0
    PASS_MARKS = 35
    MAX_SUBJECTS = 5


    def __init__(self,name,roll_number,branch):
        self.name = name
        self._roll_number = roll_number
        self._branch = branch
        self.__marks = {}
        Student.total_students += 1


    @property
    def average(self):
        if(len(self.__marks)==0):
            return 0
        else:
            return sum(self.__marks.values()) / len(self.__marks)

    @property
    def grade(self):
        if(self.average >= 90.00):
            return "A+"
        elif(self.average>= 75 and self.average<89.99):
            return "A"
        elif(self.average>= 60 and self.average<74.99):
            return "B"
        elif(self.average>= 35 and self.average<59.99):
            return "C"
        else:
            return "F"

        


    @property
    def roll_number(self):
        return self._roll_number


    def add_marks(self,subject,mark):

      if(len(self.__marks)>= Student.MAX_SUBJECTS or mark < 0 ):
          raise ValueError("check the Max_subject limt add or valid entry of mark")
      else:
          self.__marks[subject] = mark


    def get_marks(self):
       print("\nsubject   : marks")
       for a , b in self.__marks.items():
           print(f"{a:21}: {b}")


    def has_passed(self):

        if(x >= Student.PASS_MARKS for x in self.__marks.values()):
            return True
        else:
            return False


    def change_branch(self, new_branch):

        print(f"\nold branch is : {self._branch}\n")
        self._branch = new_branch
        print(f"new branch is : {self._branch}\n")


    @classmethod
    def get_total_students(cls):
        return cls.total_students

    @staticmethod
    def is_valid_mark(mark):
        if(mark>=0 and mark<=100):
            return True
        else:
            return False



    def __str__(self):
        return (
            f"\nName        : {self.name}\nRoll Number : {self._roll_number}\nBranch      : {self._branch}\nAverage     : {self.average}\nGrade       : {self.grade}\n"
        )

s1  = Student("Harsha", 237, "CSE")

s1.add_marks("Maths", 99)
s1.add_marks("Physics", 89)
s1.add_marks("Chemistry", 89)
s1.add_marks("English", 100)
s1.add_marks("Computer Science", 79)

print(Student.get_total_students())

s2 = Student("Pavan",504,"CSE")
s2.add_marks("Maths", 99)
s2.add_marks("Physics", 89) 
s2.add_marks("Chemistry", 90)
s2.add_marks("English", 100)
s2.add_marks("Computer Science", 79)

print(s1.get_marks())
print(s1.is_valid_mark(-20))
print(s1.has_passed())

print(s2.__str__())

print(s1.__str__())
