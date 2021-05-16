from django.shortcuts import render, HttpResponseRedirect,redirect
from .models import Patient
from django.urls import reverse
from django.contrib.postgres.search import SearchVector

# Create your views here.
from .forms import add_patient_form, SearchForm

def welcome(request):
    patient_count = Patient.objects.all().count()
    total_pcrs = Patient.objects.filter(test='PCR').count()
    total_deaths = Patient.objects.filter(status='DEAD').count()


    return render(request,'manager/welcome.html',\
        {
        'total_patients' : patient_count,
        'total_PCRs': total_pcrs,
        'total_deaths': total_deaths,
    })

def all_patients(request):
    patients = Patient.objects.all()
    
    return render(request,'manager/all_patients.html',context={'patients':patients,\
        'search': SearchForm()})

def view_patient(request,id):
    patient = Patient.objects.get(id=id)
    return render(request,'manager/patient.html', context={'patient': patient})

def add_patient(request):
    
    return render(request,'manager/add_patient.html',{'form': add_patient_form})

def patient_added(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    address = request.POST['address']
    tel_no = request.POST['tel_no']
    tested_date = request.POST['tested_date']
    test= request.POST['test']
    status = request.POST['status']
    DOB = request.POST['DOB']

    patient = Patient(first_name=first_name,\
        last_name=last_name,
        DOB=DOB,
        tested_date=tested_date,
        test=test,
        status=status,
        tel_no=tel_no,
        address=address)

    patient.save()

def search_for_patient():
    pass




    return redirect(reverse('manager:all_patients'))


