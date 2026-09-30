


from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.home_page),
    path('about/',views.about_page),
    path('contact/',views.contact_page),
    path('project/',views.project_page),
    path('skills/',views.skills_page),
     path('education/',views.education_page),

]
