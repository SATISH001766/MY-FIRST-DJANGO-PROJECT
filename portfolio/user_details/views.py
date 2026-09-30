from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request,'user_details/index.html')


def contact_page(request):
    return render(request,'user_details/contact.html')





def about_page(request):
    return render(request,'user_details/about.html')




def project_page(request):
    return render(request,'user_details/project.html')


def skills_page(request):
    return render(request,'user_details/skills.html')



def education_page(request):
    return render(request,'user_details/education.html')

