#!/usr/bin/env python
# coding: utf-8

# In[52]:


#oops practice

#Class and Objects

class student:
    rno ="106"
    name = "yuva"
    branch = "CSE"
    def read(self):
        rno ="455"  #the variable written inside function given first preference
        print("rollno=",rno)
        print("Instance variable=",self.rno)
        print("reading....")
        
    def write(self):
        print("writing...")
        
yuva = student()      
yuva.read()
yuva.write()


# In[57]:


class pucollege:
    def __init__(self,name,age,rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

student1 = pucollege("Lohith","24","341")
student2 = pucollege("Rakesh","25","346")

print(student1.name)
print(student2.rollno)


# In[60]:


#Inheritance
# single inheritance
class parent:
    def display(self):
        print("Parent")
    
class child(parent):
    def show(self):
        print("child")
        
c = child()       
c.display()
c.show()


# In[64]:


class parent:
    def display(self):
        print("Parent")
    
class child(parent):
    def show(self,children):
        self.children = children
        print("one children")
        
c = child()       
c.display()
c.show(2)


# In[70]:


#Multilevel Inheritance

class grandparent:
    def work(self):
        print("Grand father Worked as Railway operator")
        
class parent(grandparent):
    def workedas(self):
        print("Father worked as Postal assistant")
        
class child(parent):
    def workedasa(self):
        print("Child worked as a software engineer")
        
c = child()
c.work()
c.workedas()
c.workedasa()


# In[76]:


#Hierarchical Inheritance

class employee:
    def one(self):
        print("First level employees are directly reported to plant head")

class assistant(employee):
     def two(self):
        print("Assistants are directly reported to their respective first level employees")
        
class supervisor(employee):
    def three(self):
        print("Supervisors are directly reported to their respective first level employees")

a = assistant()
s = supervisor()
a.two() # class assitant is derived from base class employee
s.three() # class supervisor is derived from base class employee


# In[118]:


#Multiple Inheritance

class Father:
    def parent1(self,name):
        self.father_name = name
        print(name, "is the Father")
    
class Mother:
    def parent2(self,name):
        self.mother_name = name
        print(name, "is the Mother")
        
class children(Father,Mother):
    def bornto(self,name):
        self.parent1("Dasharatha")
        self.parent2("Kousalya")
        self.child_name = name
        print(self.child_name, "is the son of", self.father_name, "and", self.mother_name)
        
c = children()
c.bornto("Ram")


# In[122]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person("john",36)
    
print(p1.name)
print(p1.age)


# In[129]:


#Encapsulation
class encap:
    a = 10
    def display(self):
        print("Welcome")
        print(self.a)
        
obj = encap()
obj.display()
        


# In[154]:


class encap:
    __a = 10 #private variable
    def __display(self): #private method
        print("Welcome")
        print(self.__a)
        
obj = encap()
#obj.__display()

obj._encap__display()#private variable acess


# In[140]:


#method overloading
class method_overload:
    def display(self,a=None,b=None):
        print(a,b)

obj = method_overload()
obj.display(10)
obj.display(220,221)


# In[147]:


#method overriding
class father:
    def transport(self):
        print("cycle")

class son(father):
    def transport(self):
        print("bike")
        
        
obj=son()
obj.transport()


# In[161]:


#name mangling
class student:
    def __init__(self,name):
        self.__name = name

s1 = student("santhosh")
print(s1._student__name)

