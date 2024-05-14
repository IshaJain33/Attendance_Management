from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Course,Branch,Faculty,Coordinator,Department,Student,Session_Year,Subject
from app.models import CustomUser
from django.contrib import messages



@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    faculty_count = Faculty.objects.all().count()
    department_count = Department.objects.all().count()
    subject_count = Subject.objects.all().count()
    course_count = Course.objects.all().count()

    student_gender_male = Student.objects.filter(gender = 'Male').count()
    student_gender_female = Student.objects.filter(gender = 'Female').count()
    # student_gender_others = Student.objects.filter(gender = 'Others').count()


    context = {
        'student_count' : student_count,
        'faculty_count' : faculty_count,
        'department_count' : department_count,
        'subject_count' : subject_count,
        'course_count' : course_count,
        'student_gender_male ' : student_gender_male ,
        'student_gender_female' : student_gender_female,
    }
    return render(request,'Hod/home.html',context)

@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()
    department = Department.objects.all()
    branch = Branch.objects.all()
    subject = Subject.objects.all()


    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        department_id = request.POST.get('department_id')
        branch_id = request.POST.get('branch_id')
        enrolment_no = request.POST.get('enrolment_no')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_student')
        else:
            user = CustomUser(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                user_type=4,
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session_Year.objects.get(id=session_year_id)
            department = Department.objects.get(id=department_id)
            branch = Branch.objects.get(id=branch_id)

            student = Student(
                admin=user,
                gender=gender,
                session_year_id=session_year,
                course_id=course,
                branch_id=branch,
                department_id=department,
                enrolment_no = enrolment_no
            )
            student.save()
            messages.success(request, user.first_name + "  " + user.last_name + " is Successfully Added !")
            return redirect('add_student')

    context={
        'course': course,
        'session_year': session_year,
        'branch':branch ,
        'department':department,
        'subject': subject,
    }
    return render(request,'Hod/add_student.html',context)


@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Student.objects.all()

    context = {
        'student': student,
    }
    return render(request, 'Hod/view_student.html', context)


@login_required(login_url='/')
def EDIT_STUDENT(request, id):
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()
    department = Department.objects.all()
    branch = Branch.objects.all()


    context = {
        'student': student,
        'course': course,
        'session_year': session_year,
        'department': department,
        'branch' : branch

    }
    return render(request, 'Hod/edit_student.html',context)


@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        username = request.POST.get('username')
        password = request.POST.get('password')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')
        department_id = request.POST.get('department_id')
        branch_id = request.POST.get('branch_id')
        enrolment_no = request.POST.get('enrolment_no')

        user = CustomUser.objects.get(id = student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        user.save()

        student = Student.objects.get(admin = student_id)

        course = Course.objects.get(id = course_id)
        student.course_id = course
        department = Department.objects.get(id=department_id)
        student.department_id = department
        branch= Branch.objects.get(id=branch_id)
        student.branch_id = branch
        session_year = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = session_year
        student.enrolment_no = enrolment_no
        student.gender = gender
        student.save()
        messages.success(request,'Record Are Successfully Updated !')
        return redirect('view_student')

    return render(request,'Hod/edit_student.html')


@login_required(login_url='/')
def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request,'Record Are Successfully Deleted !')
    return redirect('edit_student')


@login_required(login_url='/')
def ADD_COURSE(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')

        course = Course(
            name=course_name,
        )
        course.save()
        messages.success(request, 'Course Are Successfully added')


        return redirect('view_course')
    return render(request,'Hod/add_course.html')


@login_required(login_url='/')
def VIEW_COURSE(request):
        course = Course.objects.all()
        context = {
            'course': course,
        }
        return render(request, 'Hod/view_course.html', context)


@login_required(login_url='/')
def EDIT_COURSE(request,id):
    course = Course.objects.get(id=id)
    context = {
        'course': course,
    }
    return render(request,'Hod/edit_course.html',context)


@login_required(login_url='/')
def UPDATE_COURSE(request):
    if request.method == "POST":
        name=request.POST.get('name')
        course_id=request.POST.get('course_id')

        course=Course.objects.get(id = course_id)
        course.name = name
        course.save()
        messages.success(request,"course are successfully updated")
        return redirect('view_course')

    return render(request,'Hod/edit_course.html')


@login_required(login_url='/')
def DELETE_COURSE(request,id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request,'Course are Successfully Deleted')

    return redirect('view_course')


@login_required(login_url='/')
def ADD_COORDINATOR(request):
    course = Course.objects.all()
    branch = Branch.objects.all()
    department = Department.objects.all()
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        course_id = request.POST.get('course_id')
        department_id = request.POST.get('department_id')
        branch_id = request.POST.get('branch_id')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_coordinator')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_coordinator')
        else:
            user = CustomUser(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                user_type=2,
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            department = Department.objects.get(id=department_id)
            branch = Branch.objects.get(id=branch_id)

            coordinator = Coordinator(
                admin=user,
                course_id=course,
                branch_id=branch,
                department_id=department,
            )
            coordinator.save()
            messages.success(request, user.first_name + "  " + user.last_name + " is Successfully Added !")
            return redirect('add_coordinator')

    context = {
        'course': course,
        'department': department,
        'branch': branch,
    }
    return render(request, 'Hod/add_coordinator.html', context)


@login_required(login_url='/')
def VIEW_COORDINATOR(request):
    coordinator = Coordinator.objects.all()
    context={
        'coordinator' : coordinator,
    }
    return render(request,'Hod/view_coordinator.html',context)


@login_required(login_url='/')
def EDIT_COORDINATOR(request,id):
    coordinator = Coordinator.objects.filter(id=id)
    course = Course.objects.all()
    department = Department.objects.all()
    branch = Branch.objects.all()

    context = {
        'coordinator' : coordinator,
        'course': course,
        'department': department,
        'branch': branch,

    }
    return render(request, 'Hod/edit_coordinator.html', context)


@login_required(login_url='/')
def UPDATE_COORDINATOR(request):
    if request.method == "POST":
        coordinator_id = request.POST.get('coordinator_id ')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        course_id = request.POST.get('course_id')
        department_id = request.POST.get('department_id')
        branch_id = request.POST.get('branch_id')

        user = CustomUser.objects.get(id = coordinator_id )

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        user.save()

        coordinator = Coordinator.objects.get(admin = coordinator_id )

        course = Course.objects.get(id = course_id)
        coordinator.course_id = course
        department = Department.objects.get(id=department_id)
        coordinator.department_id = department
        branch= Branch.objects.get(id=branch_id)
        coordinator.branch_id = branch
        coordinator.save()
        messages.success(request,'Record Are Successfully Updated !')
        return redirect('view_coordinator')


    return render(request,'Hod/edit_coordinator.html')


@login_required(login_url='/')
def DELETE_COORDINATOR(request, admin):
    coordinator = CustomUser.objects.get(id=admin)
    coordinator.delete()
    messages.success(request, 'Record Are Successfully Deleted !')
    return redirect('view_coordinator')


@login_required(login_url='/')
def ADD_FACULTY(request):
    course = Course.objects.all()
    department = Department.objects.all()
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        course_id = request.POST.get('course_id')
        department_id = request.POST.get('department_id')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email Is Already Taken')
            return redirect('add_faculty')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username Is Already Taken')
            return redirect('add_faculty')
        else:
            user = CustomUser(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                user_type=3,
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            department = Department.objects.get(id=department_id)

            faculty = Faculty(
                admin=user,
                course_id=course,
                department_id=department
            )

            faculty.save()
            messages.success(request, user.first_name + "  " + user.last_name + " is Successfully Added !")
            return redirect('add_faculty')

    context={
        'course': course,
        'department':department

    }
    return render(request,'Hod/add_faculty.html',context)


@login_required(login_url='/')
def VIEW_FACULTY(request):
    faculty=Faculty.objects.all()
    context = {
        'faculty' : faculty,
    }
    return render(request,'Hod/view_faculty.html',context)


@login_required(login_url='/')
def EDIT_FACULTY(request , id):
    faculty = Faculty.objects.filter(id=id)
    course = Course.objects.all()
    department = Department.objects.all()

    context = {
        'faculty' : faculty,
        'course': course,
        'department': department

    }
    return render(request, 'Hod/edit_faculty.html', context)


@login_required(login_url='/')
def UPDATE_FACULTY(request):
    if request.method == "POST":
        faculty_id = request.POST.get('faculty_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        course_id = request.POST.get('course_id')
        department_id = request.POST.get('department_id')

        user = CustomUser.objects.get(id = faculty_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        user.save()

        faculty = Faculty.objects.get(admin = faculty_id)

        course = Course.objects.get(id = course_id)
        faculty.course_id = course
        department = Department.objects.get(id=department_id)
        faculty.department_id = department

        faculty.save()
        messages.success(request,'Record Are Successfully Updated !')
        return redirect('view_faculty')

    return render(request,'Hod/edit_faculty.html')


@login_required(login_url='/')
def DELETE_FACULTY(request, admin):
    faculty = CustomUser.objects.get(id=admin)
    faculty.delete()
    messages.success(request, 'Record Are Successfully Deleted !')
    return redirect('view_faculty')


@login_required(login_url='/')
def ADD_SUBJECT(request):
    branch = Branch.objects.all()
    faculty = Faculty.objects.all()
    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        subject_code = request.POST.get('subject_code')
        branch_id = request.POST.get('branch_id')
        faculty_id = request.POST.get('faculty_id')

        branch = Branch.objects.get(id=branch_id)
        faculty = Faculty.objects.get(id=faculty_id)

        subject = Subject(
            subject_name=subject_name,
            subject_code=subject_code,
        )
        subject.save()
        messages.success(request, 'Subject is Successfully added')
        return redirect('add_subject')
    context = {
        'branch': branch,
        'faculty': faculty,
    }
    return render(request,'Hod/add_subject.html', context)


@login_required(login_url='/')
def VIEW_SUBJECT(request):
    subject = Subject.objects.all()
    context = {
        'subject': subject,
    }
    return render(request,'Hod/view_subject.html',context)


@login_required(login_url='/')
def EDIT_SUBJECT(request,id):
    subject = Subject.objects.get(id=id)
    context = {
        'subject': subject
    }
    return render(request, 'Hod/edit_subject.html', context)


@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    if request.method == "POST":
        subject_name=request.POST.get('subject_name')
        subject_code=request.POST.get('subject_code')
        subject_id=request.POST.get('subject_id')

        subject=Subject.objects.get(id=subject_id)
        subject.subject_name = subject_name
        subject.subject_code = subject_code
        subject.save()
        messages.success(request,"Subject is successfully updated")
        return redirect('view_subject')

    return render(request,'Hod/edit_subject.html')


@login_required(login_url='/')
def DELETE_SUBJECT(request,id):
    subject = Subject.objects.get(id=id)
    subject.delete()
    messages.success(request, 'Subject are Successfully Deleted')

    return redirect('view_subject')


@login_required(login_url='/')
def ADD_SESSION(request):
    if request.method=="POST":
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year(
            session_year_start =  session_year_start,
            session_year_end =  session_year_end
        )

        session.save()
        messages.success(request,"Session is created successfully")
        return redirect('view_session')
    return render(request,'Hod/add_session.html')


@login_required(login_url='/')
def VIEW_SESSION(request):
    session_year = Session_Year.objects.all()

    context = {
        'session_year' : session_year,
    }
    return render(request,'Hod/view_session.html',context)


@login_required(login_url='/')
def EDIT_SESSION(request,id):
    session_year = Session_Year.objects.get(id=id)
    context = {
        'session_year' : session_year
    }
    return render(request, 'Hod/edit_session.html', context)


@login_required(login_url='/')
def UPDATE_SESSION(request):

    if request.method == "POST":
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')
        session_year_id = request.POST.get('session_year_id')

        session_year=Session_Year.objects.get(id=session_year_id)
        session_year.session_year_start= session_year_start
        session_year.session_year_end= session_year_end
        session_year.save()
        messages.success(request,"Session is successfully updated")
        return redirect('view_session')

    return render(request,'Hod/edit_session.html')


@login_required(login_url='/')
def DELETE_SESSION(request,id):
    session_year = Session_Year.objects.get(id=id)
    session_year.delete()
    messages.success(request, 'Session Deleted Successfully')

    return redirect('view_session')


@login_required(login_url='/')
def ADD_DEPARTMENT(request):
    if request.method == "POST":
        department_name = request.POST.get('department_name')

        department = Department(
            department_name=department_name,
        )
        department.save()
        messages.success(request, 'Department is Successfully added')


        return redirect('view_department')
    return render(request,'Hod/add_department.html')


@login_required(login_url='/')
def VIEW_DEPARTMENT(request):
    department = Department.objects.all()
    context = {
        'department': department,
    }
    return render(request, 'Hod/view_department.html', context)


@login_required(login_url='/')
def EDIT_DEPARTMENT(request,id):
    department = Department.objects.get(id=id)
    context = {
        'department': department,
    }
    return render(request, 'Hod/edit_department.html', context)


@login_required(login_url='/')
def UPDATE_DEPARTMENT(request):
    if request.method == "POST":
        department_name=request.POST.get('department_name')
        department_id=request.POST.get('department_id')

        department=Department.objects.get(id = department_id)
        department.department_name = department_name
        department.save()
        messages.success(request,"Department is successfully updated")
        return redirect('view_department')

    return render(request,'Hod/edit_department.html')



@login_required(login_url='/')
def DELETE_DEPARTMENT(request,id):
    department = Department.objects.get(id=id)
    department.delete()
    messages.success(request, ' Department Deleted Successfully ')

    return redirect('view_department')