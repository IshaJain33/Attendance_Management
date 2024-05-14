from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views,Hod_views,Coordinator_views,Faculty_views,Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),
    path('', views.LOGIN, name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='doLogout'),

    path('Profile',views.PROFILE,name='profile'),
    path('Profile/update',views.PROFILE_UPDATE,name='profile_update'),

#Hod
    path('Hod/Home', Hod_views.HOME, name='Hod_home'),
    path('Hod/Student/Add',Hod_views.ADD_STUDENT,name='add_student'),
    path('Hod/Student/View',Hod_views.VIEW_STUDENT,name='view_student'),
    path('Hod/Student/Edit/<str:id>',Hod_views.EDIT_STUDENT,name='edit_student'),
    path('Hod/Student/Update',Hod_views.UPDATE_STUDENT,name='update_student'),
    path('Hod/Student/Delete/<str:admin>',Hod_views.DELETE_STUDENT,name='delete_student'),

    path('Hod/Coordinator/Add', Hod_views.ADD_COORDINATOR, name='add_coordinator'),
    path('Hod/Coordinator/View', Hod_views.VIEW_COORDINATOR, name='view_coordinator'),
    path('Hod/Coordinator/Edit/<str:id>', Hod_views.EDIT_COORDINATOR, name='edit_coordinator'),
    path('Hod/Coordinator/Update', Hod_views.UPDATE_COORDINATOR, name='update_coordinator'),
    path('Hod/Coordinator/Delete/<str:admin>', Hod_views.DELETE_COORDINATOR, name='delete_coordinator'),

    path('Hod/Faculty/Add',Hod_views.ADD_FACULTY,name='add_faculty'),
    path('Hod/Faculty/View', Hod_views.VIEW_FACULTY, name='view_faculty'),
    path('Hod/Faculty/Edit/<str:id>', Hod_views.EDIT_FACULTY, name='edit_faculty'),
    path('Hod/Faculty/Update',Hod_views.UPDATE_FACULTY,name='update_faculty'),
    path('Hod/Faculty/Delete/<str:admin>', Hod_views.DELETE_FACULTY, name='delete_faculty'),

    path('Hod/Course/Add',Hod_views.ADD_COURSE,name='add_course'),
    path('Hod/Course/View', Hod_views.VIEW_COURSE, name='view_course'),
    path('Hod/Course/Edit/<str:id>',Hod_views.EDIT_COURSE,name='edit_course'),
    path('Hod/Course/Update',Hod_views.UPDATE_COURSE,name='update_course'),
    path('Hod/Course/Delete/<str:id>',Hod_views.DELETE_COURSE,name='delete_course'),

    path('Hod/Subject/Add',Hod_views.ADD_SUBJECT,name='add_subject'),
    path('Hod/Subject/View',Hod_views.VIEW_SUBJECT,name='view_subject'),
    path('Hod/Subject/Edit/<str:id>',Hod_views.EDIT_SUBJECT,name='edit_subject'),
    path('Hod/Subject/Update',Hod_views.UPDATE_SUBJECT,name='update_subject'),
    path('Hod/Subject/Delete/<str:id>',Hod_views.DELETE_SUBJECT,name='delete_subject'),

    path('Hod/Session/Add',Hod_views.ADD_SESSION,name='add_session'),
    path('Hod/Session/View',Hod_views.VIEW_SESSION,name='view_session'),
    path('Hod/Session/Edit/<str:id>',Hod_views.EDIT_SESSION,name='edit_session'),
    path('Hod/Session/Update',Hod_views.UPDATE_SESSION,name='update_session'),
    path('Hod/Session/Delete/<str:id>',Hod_views.DELETE_SESSION,name='delete_session'),

    path('Hod/Department/Add',Hod_views.ADD_DEPARTMENT,name='add_department'),
    path('Hod/Department/View',Hod_views.VIEW_DEPARTMENT,name='view_department'),
    path('Hod/Department/Edit/<str:id>',Hod_views.EDIT_DEPARTMENT,name='edit_department'),
    path('Hod/Department/Update',Hod_views.UPDATE_DEPARTMENT,name='update_department') ,
    path('Hod/Department/Delete/<str:id>',Hod_views.DELETE_DEPARTMENT,name='delete_department') ,

    #Faculty
    path('Faculty/Home', Faculty_views.HOME, name='Faculty_home'),
    path('Faculty/Take_Attendance',Faculty_views.FACULTY_TAKE_ATTENDANCE, name="faculty_take_attendance") ,

    #Students
    path('Student/Home',Student_views.HOME, name='Student_home')

              ] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
