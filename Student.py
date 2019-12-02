
# Task 5
# 
# 
class MemberOfUniversity(object):
  numberOfMembers = 0  
  def __init__(self,MemberName,EmailAddress):
    MemberOfUniversity.numberOfMembers += 1
    hex(id(self))  # to get the address in memory
    self.MemberName = MemberName
    self.EmailAddress= EmailAddress
    self.counterclass = MemberOfUniversity.numberOfMembers_object
  
    
 

class Student(MemberOfUniversity):
  def __init__(self,MemberName,EmailAddress,year):
    MemberOfUniversity.__init__(self,MemberName,EmailAddress)
    self.year = year

  def description(self):
    print(self.MemberName + self.EmailAddress + " is a student in year "+ str(self.year))

class Staff(MemberOfUniversity):
  def __init__(self,MemberName,EmailAddress,school):
    MemberOfUniversity.__init__(self,MemberName,EmailAddress)
    self.school = school

  def description(self):
    print(self.MemberName + self.EmailAddress + " is a staff member in "+ str(self.school))


     
     
#create a students
student1 = Student('Alex Jones','a.jones@kingston.ac.uk', 1)
student1.description()
staff1 = Staff('James Denholm-Price', 'j.denholm-price@kingston.ac.uk','CSM')
staff1 = staff1.description()
print('There are a total of' +str(MemberOfUniversity.counterclass) + 'members in the university' )



