from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from django.utils.dateparse import parse_date
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.cache import never_cache

@never_cache
def index(request):
    if request.session.get('username'):
        student_count = Student.objects.count() 
        teacher_count = Teacher.objects.count() 
        club_count = Club.objects.count() 
        book_count = Book.objects.count() 

        context = {
            'student_count':student_count,
            'teacher_count':teacher_count,
            'club_count':club_count,
            'book_count':book_count
        }
        return render(request,'index.html',context)
    return redirect('login')

@never_cache
def addstudent(request):

    if request.method == "POST":
        name = request.POST.get('name')
        dob = parse_date(request.POST.get('dob'))
        doj = parse_date(request.POST.get('doj'))
        address = request.POST.get('address')
        rno = request.POST.get('rno')

        if Student.objects.filter(name=name, rno=rno).exists():
            messages.error(request, 'Student with the same Name and Rollno already exists..!!')
        else:
            try:
                Student.objects.create(
                    name=name,
                    dob=dob,
                    doj=doj,
                    address=address,
                    rno=rno,
                )
                messages.success(request, 'Student added successfully!')
            except Exception as e:
                messages.error(request, f'Error: {e}')

        return redirect(addstudent)
    
    return redirect(student)

@never_cache
def upstudent(request, pk):

    student = Student.objects.get(pk=pk)

    if request.method == "POST":
        try:
            student.name = request.POST['name']
            student.dob = parse_date(request.POST['dob'])
            student.doj = parse_date(request.POST['doj'])
            student.address = request.POST['address']
            student.rno = request.POST['rno']

            student.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student')  # Redirect to the student list page
            
        except Exception as e:
            messages.error(request, f'Error: {e}')
            return redirect('student')
    else:
        return redirect('student')

@never_cache
def delstudent(request,pk):

    student = Student.objects.get(pk=pk)

    if student:
        student.delete()

    messages.info(request,'Student deleted successfully..!!')
    return redirect('student')

@never_cache
def student(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})

@never_cache
def addteacher(request):

    if request.method == "POST":

        name = request.POST['name']
        dob = parse_date(request.POST['dob'])
        doj = parse_date(request.POST['doj'])
        address = request.POST['address']
        subject = request.POST['subject']
        salary = request.POST['salary']

        if Teacher.objects.filter(name=name,subject=subject).exists():
            
            messages.error(request,'Teacher with same Name and Subject already exist..!!')
        else:
            try:

                Teacher.objects.create(
                    name = name,
                    dob = dob,
                    doj = doj,
                    address = address,
                    subject = subject,
                    salary = salary,
                )

                messages.success(request,'Teacher added successfully..!!')
                return redirect('teacher')
            
            except Exception as e:
                messages.error(request,f'Error:{e}')
        
        return redirect('teacher')

    else:
        return redirect('teacher')

@never_cache
def upteacher(request,pk):

    teacher = Teacher.objects.get(pk=pk)

    if request.method == "POST":
        try:

            teacher.name = request.POST['name']
            teacher.dob = parse_date(request.POST['dob'])
            teacher.doj = parse_date(request.POST['doj'])
            teacher.address = request.POST['address']
            teacher.subject = request.POST['subject']
            teacher.salary = request.POST['salary']

            teacher.save()
            messages.success(request,'Teacher updated successfully..!!')
            return redirect('teacher')
        
        except Exception as e:
            messages.error(request,f'Error:{e}')
            return redirect('teacher')
    else:
        return redirect('teacher')
    
@never_cache
def delteacher(request,pk):
    
    teacher = Teacher.objects.filter(pk=pk)

    if teacher:
        teacher.delete()
    
    return redirect('teacher')

@never_cache
def teacher(request):
    teachers = Teacher.objects.all()
    return render(request,'teacher.html',{'teachers': teachers})

@never_cache
def addclub(request):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        members = request.POST.getlist('members')
        
        club = Club.objects.create(name=name, desc=desc)
        club.members.set(members)
        messages.success(request, 'Club created successfully!')
        return redirect('club')
    
    return redirect('club')

@never_cache
def upclub(request, pk):
    club = Club.objects.get(pk=pk)
    
    if request.method == 'POST':
        club.name = request.POST['name']
        club.desc = request.POST['desc']
        members = request.POST.getlist('members')
        club.members.set(members)
        
        club.save()
        messages.success(request, 'Club updated successfully!')
        return redirect('club')
    
    return redirect('club')

@never_cache
def delclub(request, pk):
    club = Club.objects.get(pk=pk)
    club.delete()
    messages.success(request, 'Club deleted successfully!')
    return redirect('club')

@never_cache
def club(request):
    clubs = Club.objects.all()
    students = Student.objects.all()  
    return render(request, 'club.html', {'clubs': clubs, 'students': students})

@never_cache
def addbook(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        isbn = request.POST['isbn']
        available_copies = request.POST['available_copies']

        # Check for unique ISBN
        if Book.objects.filter(isbn=isbn).exists():
            messages.error(request, 'A book with this ISBN already exists!')
            return redirect('book')

        Book.objects.create(
            title=title,
            author=author,
            isbn=isbn,
            available_copies=available_copies
        )
        messages.success(request, 'Book added successfully!')
        return redirect('book')

@never_cache
def upbook(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        isbn = request.POST['isbn']
        book.available_copies = request.POST['available_copies']

        # Check for unique ISBN if it's changed
        if book.isbn != isbn:
            if Book.objects.filter(isbn=isbn).exists():
                messages.error(request, 'A book with this ISBN already exists!')
                return redirect('book')
        book.isbn = isbn

        book.save()
        messages.success(request, 'Book updated successfully!')
        return redirect('book')

@never_cache
def delbook(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    messages.success(request, 'Book deleted successfully!')
    return redirect('book')

@never_cache
def book(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})

@never_cache
def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        try:
            user = User.objects.get(username=username,email=email)
            messages.error(request,'Email or username already exist')

        except:

            if password == confirm_password:

                user = User.objects.create(
                    username = username,
                    email = email,
                    password = password
                )

                messages.success(request,'Registration successfull,login now.!!')
                return redirect('login')

            else:
                messages.error(request,'Password does not match..!!')
    
    return render(request, 'register.html')

@never_cache
def login(request):

    if request.method == 'POST':

        try:
            user = User.objects.get(username=request.POST['username'])

            if user.password == request.POST['password']:

                request.session['username'] = user.username
                return redirect('index')
            else:
                messages.error(request, 'Incorrect password.')
        except Exception as e:
            messages.error(request, 'Username does not exist.')
            

    return render(request, 'login.html')

@never_cache
def logout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect('login')
