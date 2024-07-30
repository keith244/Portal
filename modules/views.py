from django.shortcuts import get_object_or_404, render
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import WorkExperience, Education,Jobs,Documents,Applications
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
@login_required(login_url='users-login')
def personal(request):
    return render(request, 'modules/personaldetails.html')


@login_required(login_url='users-login')
def education(request):
    if request.method == 'POST':
        education = request.POST.get('education')  
        course = request.POST.get('course')  
        institution = request.POST.get('institution')  
        grad_year = request.POST.get('grad_year')  
        addn_courses = request.POST.get('add_courses')  

        p_grad_year  = parse_date(grad_year)

        try:    
            Education.objects.create(
                user = request.user,
                education = education, 
                course = course,
                institution = institution,  
                grad_year = p_grad_year, 
                addn_courses = addn_courses 
            )
            messages.success(request, 'Education details saved successfully!!')
            return redirect('work')
        except Exception as e:
            messages.error(request,'Unable to save education details. Error : {str(e)}.')
            return render(request, 'modules/education.html')
    return render(request,'modules/education.html')

#@login_required(login_url='users-login')
def work_experience(request):
    if request.method == 'POST':
        company = request.POST.get('company') 
        position = request.POST.get('position')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        responsibility = request.POST.get('responsibility')

        p_start_date = parse_date(start_date)
        p_end_date = parse_date(end_date)
        print(p_start_date)
        print(p_end_date)
        # if p_end_date - p_start_date < 2 or p_end_date - p_start_date > 10:
        #     pass 

        try:
            WorkExperience.objects.create(
                user=request.user,
                company=company,
                position=position,
                start_date=p_start_date,
                end_date=p_end_date,
                responsibility=responsibility
            )
            messages.success(request, 'Work experince saved successfully.')
            return redirect('documents')
        except Exception as e:
            messages.error(request,'Unable to save work details. Error : {str(e)}.')
            return redirect('work')
    return render(request, 'modules/workexperience.html')


@login_required(login_url='users-login')
def add_documents(request):
    if request.method == 'POST':
        names = request.POST.getlist('name')
        files = request.FILES.getlist('file')
        user = request.user

        try:
            for i in range(len(names)):
                Documents.objects.create(
                    user=user,
                    title=names[i],
                    file=files[i]
                )
            messages.success(request, 'Documents added successfully.Check jobs below.')
            return redirect('jobs')
        except Exception as e:
            messages.error(request,'Unable to save documents. Error : {str(e)}.')
            return redirect('documents')
    return render(request, 'modules/add_documents.html')


def profile_user(request):
    return render(request, 'modules/profile.html')


#Handles job being created and posted to database 
@login_required(login_url='users-login')
def add_Job(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            title = request.POST.get('title')
            responsibilities = request.POST.get('responsibilities')            
            requirements = request.POST.get('requirements')   

            try:    
                Jobs.objects.create(
                    user = request.user,
                    title = title,
                    responsibilities = responsibilities,
                    requirements = requirements,
                )
                messages.success(request, 'Job posted successfully') 
                return redirect('add_job')
            except Exception as e:
                messages.error(request,'Unable to add new job. Error :{str(e)}.')
                return redirect('add_job')
        return render(request, 'staff/addjob.html')
    return redirect('jobs')
#to handle job being posted to the html template

# @login_required(login_url='users-login')
def jobs(request):
    jobs = Jobs.objects.all().order_by('-timestamp')
    return render(request, 'modules/jobs.html', {'jobs':jobs})


def job_details(request, job_id):
    job = get_object_or_404(Jobs, pk=job_id)
    user_applied = Applications.objects.filter(user=request.user, job=job).exists()

    if request.method == 'POST':
        if user_applied:
            messages.warning (request, 'You have already applied for this job.')
        else:
            Applications.objects.create(user = request.user, job=job)
            messages.success(request, 'Your application has been sent.')
            user_applied = True
        return redirect('jobs')
    job.responsibilities_list = [r.strip() for r in job.responsibilities.split('•') if r.strip()]
    return render(request, 'staff/job_details.html', {'job': job})

def update_job(request, job_id):
    job = get_object_or_404(Jobs, pk = job_id)
    if request.method == 'POST':
        if request.user == job.user or request.user.is_staff:
            job.title = request.POST.get('title') 
            job.responsibilities = request.POST.get('responsibilities')
            job.requirements = request.POST.get('requirements')
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
    
    return render(request, 'staff/delete_job.html',{'job':job})


@login_required(login_url='users-login')
def view_applications(request):
    application_id = request.POST.get('application_id')
    user = request.user
    if application_id:
        status = request.POST.get('status')
        application = get_object_or_404(Applications, id=application_id)
        application.status=status
        application.save()

        try:
            context = {
                'user_name': application.user.name, 
                'job_title': application.job.title,
                'application_status': application.status
            }
            html_message = render_to_string('staff/aplication_email.html', context)
            plain_message = strip_tags(html_message)
            recipient_list = [application.user.email]
            email_from = settings.EMAIL_HOST_USER
            subject = 'Job Application Status'
            # message = f'Dear, {user.name} this is to inform you that your application for {application.job.title} has been {application.status}'
            send_mail(subject, plain_message, email_from, recipient_list,html_message=html_message, fail_silently=False)
            messages.success(request, f'The email has been successfully sent to {application.user.name}.')
        except Exception as e:
            messages.error(request, f'Failed to send email to {application.user.name} because of: {str(e)}')
            print(f'Failed to send email: {str(e)}')
    applications = Applications.objects.all().order_by('-applied_date')
    return render(request, 'staff/view_applications.html',{'applications':applications})

def faqs(request):
    return render(request, 'modules/FAQS.html')
def jobs_2(request):
    return render(request, 'modules/jobs_2.html')

def personal_details(request):
    return render(request, 'modules/personaldetails.html')

def job_applications(request):
    return render (request, 'staff/applications.html')