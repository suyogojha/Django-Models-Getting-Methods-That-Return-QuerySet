from django.shortcuts import render
from .models import *
from django.db.models import Q



# =======================MODELS THAT RETURN QUERIES======================================

#1. Create a view that displays all the students in the database.
#---------------------------------------------------
# def home(request):
#     #student_data = Student.objects.all() # fetch all data from Student table
#     # student_data = Student.objects.filter(marks=85) # fetch data from Student table where marks is 85
#     # student_data = Student.objects.exclude(marks=85) # fetch data from Student table where marks is not 85 
#     # student_data = Student.objects.order_by('city') # fetch data from Student table order by city 
#     # student_data = Student.objects.order_by('-city') # fetch data from Student table order by city in descending order
#     # student_data = Student.objects.order_by('?') # fetch data from Student table order by random
#     # student_data = Student.objects.order_by('id') # fetch data from Student table order by id 
#     # student_data = Student.objects.order_by('id').reverse() # fetch data from Student table order by id in descending order
#     # student_data = Student.objects.order_by('id').reverse() [0:3] 
#     # student_data = Student.objects.values() 
#     # student_data = Student.objects.values('name', 'city') 
#     # student_data = Student.objects.values_list() 
#     # student_data = Student.objects.values_list('name', 'city') 
#     # student_data = Student.objects.values_list('name', 'city', named=True) 
#     # student_data = Student.objects.using('default')
#     # student_data = Student.objects.dates('pass_date', 'year')
#     # student_data = Student.objects.dates('pass_date', 'month')
#     student_data = Student.objects.dates('pass_date', 'month')
#     print("Return:", student_data)
#     print()
#     print("SQL Query:", student_data.query)
#     con  = {
#         'students': student_data
#     }
#     return render(request, 'home.html', con)

#---------------------------------------------------



#2. Create a view that displays all the teachers in the database.
#---------------------------------------------------------------
# def home(request):
    # q1 = Student.objects.values_list('id', 'name', named=True)
    # q2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = q2.union(q1)
    
    
    
    # q1 = Student.objects.values_list('id', 'name', named=True)
    # q2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = q2.union(q1, all=True)
    
    
    
    # q1 = Student.objects.values_list('id', 'name', named=True)
    # q2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = q2.intersection(q1)
    
    
    
    # q1 = Student.objects.values_list('id', 'name', named=True)
    # q2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = q2.difference(q1)
    
    
    
    
    # print("Return:", student_data)
    # print()
    # print("SQL Query:", student_data.query)
    # con  = {
    #     'students': student_data
    # }
    # return render(request, 'home.html', con) 
    
    
    
    
    
    
    
# 3. AND  OR operator
#---------------------------------------------------------------
def home(request):    
    # student_data = Student.objects.filter(id=2) & Student.objects.filter(roll=101)
   
   
    # student_data = Student.objects.filter(id=2, roll=101)
    
    
    # student_data = Student.objects.filter(Q(id=2) & Q(roll=101))
   
    # student_data = Student.objects.filter(id=2) | Student.objects.filter(roll=101)
   
    student_data = Student.objects.filter(Q(id=2) | Q(roll=101))
   
 
    print("Return:", student_data)
    print()
    print("SQL Query:", student_data.query)
    con  = {
        'students': student_data
    }
    return render(request, 'home.html', con)







