from django.shortcuts import render
from django.shortcuts import render,redirect
#from users.models import User
from django.contrib import messages
from .forms import DocumentForm  #,JobForm
from .models import WorkExperience, Education,Jobs,Documents
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date

# Create your views here.
@login_required(login_url='users-login')
def add_documents(request):
    if request.method == 'POST':
        names = request.POST.getlist('name')
        files = request.FILES.getlist('file')
        user = request.user

        for i in range(len(names)):
            Documents.objects.create(
                user=user,
                title=names[i],
                file=files[i]
            )
        messages.success(request, 'Documents added successfully.')
        return redirect('education')
    return render(request, 'modules/add_documents.html')

@login_required(login_url='users-login')
def work_experience(request):
    if request.method == 'POST':
        company = request.POST.get('company') 
        position = request.POST.get('position')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        responsibility = request.POST.get('responsibility')

        p_start_date = parse_date(start_date)
        p_end_date = parse_date(end_date)

        WorkExperience.objects.create(
            user=request.user,
            company=company,
            position=position,
            start_date=p_start_date,
            end_date=p_end_date,
            responsibility=responsibility
        )
        messages.success(request, 'Work experince saved successfully.')
        return redirect('work')
    return render(request, 'modules/workexperience.html')





@login_required(login_url='users-login')
def education(request):
    if request.method == 'POST':
        education    = request.POST.get('education')  
        course       = request.POST.get('course')  
        institution  = request.POST.get('institution')  
        grad_year    = request.POST.get('grad_year')  
        addn_courses = request.POST.get('add_courses')  

        p_grad_year  = parse_date(grad_year)

        Education.objects.create(
            user = request.user,
            education    =   education, 
            course       =   course,
            institution  =   institution,  
            grad_year  =     p_grad_year, 
            addn_courses =   addn_courses 
        )
        messages.success(request, 'Education details saved successfully!!')
        return redirect('work')
    else:
        messages.error(request,'Unable to save documents. Please try again.')
    return render(request, 'modules/education.html')
def profile_user(request):
    return render(request, 'modules/profile.html')

@login_required(login_url='users-login')
def add_Job(request):
    if request.method == 'POST':
        title              = request.POST.get('title')
        responsibilities   = request.POST.get('responsibilities')            
        requirements       = request.POST.get('requirements')   
        adder              = request.POST.get('adder')

        Jobs.objects.create(
            user = request.user,
            title             = title,
            responsibilities  = responsibilities,
            requirements      = requirements,
            adder             = adder
        )
        messages.success(request, 'Job posted successfully') 
        return redirect('add_job')
    # else:
    #     messages.error(request,'Unable to add job. Please try again.')
    return render(request, 'staff/addjob.html')
def jobs(request):
    jobs = Jobs.objects.all().order_by('-id')
    return render(request, 'modules/jobs.html', {'jobs':jobs})
def personal_details(request):
    return render(request, 'modules/personal_details.html')