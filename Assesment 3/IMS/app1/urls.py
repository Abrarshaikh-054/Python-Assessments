from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('student/',views.student,name='student'),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('upstudent/<int:pk>',views.upstudent,name='upstudent'),
    path('delstudent/<int:pk>',views.delstudent,name='delstudent'),
    path('teacher/',views.teacher,name='teacher'),
    path('addteacher/',views.addteacher,name='addteacher'),
    path('upteacher/<int:pk>',views.upteacher,name='upteacher'),
    path('delteacher/<int:pk>',views.delteacher,name='delteacher'),
    path('club/', views.club, name='club'),
    path('addclub/', views.addclub, name='addclub'),
    path('upclub/<int:pk>/', views.upclub, name='upclub'),
    path('delclub/<int:pk>/', views.delclub, name='delclub'),
    path('book/', views.book, name='book'),
    path('book/add/', views.addbook, name='addbook'),
    path('book/update/<int:pk>/', views.upbook, name='upbook'),
    path('book/delete/<int:pk>/', views.delbook, name='delbook'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]