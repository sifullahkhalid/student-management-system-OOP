class Student:
  def __init__ (self,name,student_id,email,age,department,marks=0):
    self.name = name
    self.student_id = student_id
    self.__email = email
    self.age = age
    self.department= department
    self.__marks = marks

  def display_info(self):
    print(f"Name : {self.name}\nStudent ID: {self.student_id}\nEmail : {self.__email}\nAge : {self.age}\nDepartment : {self.department}")

  def calculate_result(self,*marks):
    total_marks = sum(marks)
    print(f"Total Marks of Mr. {self.name} is {total_marks}\n")

  def get_student_type(self):
    print("General Student")

class UndergraduateStudent(Student):
  def __init__ (self,name,student_id,email,age,department,semester):
    super().__init__(name,student_id,email,age,department)
    self.semester = semester

  def get_student_type(self):
    if self.student_id[0]=='U':
        print(f"Mr. {self.name}, Id is : {self.student_id} is an Undergraduate student")
    else:
        print("General Student")

  def display_info(self):
    super().display_info()
    print(f"\nSemester : {self.semester}")
  
class GraduateStudent(Student):
  def __init__ (self,name,student_id,email,age,department,research_topic):
    super().__init__(name,student_id,email,age,department)
    self.research_topic = research_topic
  
  def get_student_type(self):
    if self.student_id[0]=='G':
        print(f"Mr. {self.name}, Id is : {self.student_id} is a Graduate student")
    else:
            print("General Student")
  def display_info(self):
    super().display_info()
    print(f"\nResearch Topic : {self.research_topic}")            

  
St1=GraduateStudent("Khalid","Gd-1234","sifullah@gmail.com",25,"Software Engineering","Artificial Intelligent")
St2=UndergraduateStudent("Rokon","Un-1234","rokon@gmail.com",23,"Marketing","Second")

St1.display_info()
St1.get_student_type()
St1.calculate_result(40,60,49.89,90,70,69,50)

St2.display_info()
St2.get_student_type()
St2.calculate_result(40,60,49.89,90,50)


