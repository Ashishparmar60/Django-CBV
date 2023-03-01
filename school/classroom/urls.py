from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('thank_you/', views.ThankYou.as_view(), name='thank_you'), 
    path('teacher_form/', views.TeacherFormView.as_view(), name='teacher_form'),
    path('contact/', views.ContactFormView.as_view(), name='contact_form'),
    path('teacher_list/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teacher_detail/<int:pk>', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher_update/<int:pk>', views.TeacherUpdateView.as_view(), name='teacher_update'),
    path('teacher_confirm_delete/<int:pk>', views.TeacherDeleteView.as_view(), name='delete_teacher')
]