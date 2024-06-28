from django.shortcuts import get_object_or_404, render
from django.shortcuts import render,redirect
from django.contrib import messages
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

#Handles job being created and posted to database 
@login_required(login_url='users-login')
def add_Job(request):
    if request.method == 'POST':
        title              = request.POST.get('title')
        responsibilities   = request.POST.get('responsibilities')            
        requirements       = request.POST.get('requirements')   

        Jobs.objects.create(
            user = request.user,
            title             = title,
            responsibilities  = responsibilities,
            requirements      = requirements,
        )
        messages.success(request, 'Job posted successfully') 
        return redirect('add_job')
    
    return render(request, 'staff/addjob.html')
#to handle job being posted to the html template
def jobs(request):
    jobs = Jobs.objects.all().order_by('-timestamp')
    return render(request, 'modules/jobs.html', {'jobs':jobs})

"""CRUD OPERATION START HERE"""
# def job_view(request,job_id):
#     job = get_object_or_404(Jobs, pk = job_id)
#     return render(request, 'staff/<int:job_id>/view' ,{'job':job})
def job_view(request, job_id):
    job = get_object_or_404(Jobs, pk=job_id)
    return render(request, 'staff/job_view.html', {'job': job})


def update_job(request, job_id):
    job = get_object_or_404(Jobs, pk = job_id)
    if request.method == 'POST':
        if request.user == job.user or request.user.is_staff:
            job.title            = request.POST.get('title') 
            job.responsibilities = request.POST.get('responsibilities')
            job.requirements     = request.POST.get('requirements')
            job.save() 
            messages.success(request, 'Job update success!!')
            return redirect('jobs')
        else:
            messages.error(request, 'Not authorised')
    return render(request, 'staff/update_job.html', {'job':job})

def delete_job(request,job_id):
    job = get_object_or_404(Jobs,pk=job_id)
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted successfully')
        return redirect('jobs')
    # else:
    #     messages.error(request, 'Not authorised')
    return render(request, 'staff/delete_job.html',{'job':job})



"""END OF CRUD OPERATIONS"""
def personal_details(request):
    return render(request, 'modules/personaldetails.html')