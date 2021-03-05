class student:
 """ A class representing a student"""
 def __init__(self,n,a,p):
    self.full_name=n
    self.age=a
    self.prodi=p
 def get_age(self):
    return self.age
 def get_prodi(self):
    return self.prodi
f = student("sanni pasaribu",19,"sistel")
print(f.full_name) 
print(f.get_age())
print(f.get_prodi())