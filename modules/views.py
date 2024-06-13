from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import DocumentForm 
from .models import WorkExperience, Education
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date

# Create your views here.

def add_documents(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the uploaded file here
            # For example, save it to the model or file system
            document = form.cleaned_data['document']
            # You can save the document or perform any necessary processing here

            messages.success(request, 'Document uploaded successfully.')
            return redirect('work')  # Replace with your success URL or view name
        else:
            messages.error(request, 'Please upload a document.')
    else:
        form = DocumentForm()

    return render(request, 'modules/add_documents.html', {'form': form})

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

def personal_details(request):
    return render(request, 'modules/personaldetails.html')
# Create your views here.
def add_Job(request):
    return render(request, 'staff/addjob.html')