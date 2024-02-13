from django.db import IntegrityError
from django.shortcuts import redirect, render
from .models import Subject, SubjectReport
from .forms import SubjectForm
from django.contrib import messages
# Create your views here.

def subject_list(request):
    subjects = Subject.objects.filter(user=request.user)
    if request.method == "POST":
        subject_id = request.POST['submit']
        print(subject_id)
        subject = Subject.objects.get(pk=subject_id)
        if request.POST['form_id'] == "Tick":
            subject.classes_attended += 1
            subject.total_classes += 1
            subject.percentage = subject.classes_attended*100/subject.total_classes
            SubjectReport.objects.create(subject=subject, status="Present")
        if request.POST['form_id'] == "Cross":
            subject.total_classes += 1
            subject.percentage = subject.classes_attended*100/subject.total_classes
            SubjectReport.objects.create(subject=subject, status="Absent")
        subject.save()
    return render(request, 'attendance/index.html', {'subjects': subjects})

def subject_report(request, subject_id):
    subject = Subject.objects.get(pk=subject_id)
    reports = SubjectReport.objects.filter(subject__id=subject.id)
    return render(request, 'attendance/report.html', {'reports': reports, 'subject': subject})

def add_subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['classes_attended'] <= form.cleaned_data['total_classes']:
                subject = form.save(commit=False)
                subject.user = request.user
                if subject.total_classes != 0:
                    subject.percentage = subject.classes_attended*100/subject.total_classes
                try:
                    subject.save()
                    return redirect('attendance:subject_list')
                except IntegrityError:
                    messages.error(request, "This subject already exists.")
            else:
                messages.error(request, "Total classes should be more than the classes attended.")
    else:
        form = SubjectForm()
    return render(request, "attendance/subject-form.html", {'form': form})

def edit_subject(request, subject_id):
    subject = Subject.objects.get(pk=subject_id)
    form = SubjectForm(request.POST or None, instance=subject)
    if form.is_valid():
        if form.cleaned_data['classes_attended'] <= form.cleaned_data['total_classes']:
            form.save(commit=False)
            if subject.total_classes != 0:
                subject.percentage = subject.classes_attended*100/subject.total_classes
            try:
                subject.save()
                return redirect('attendance:subject_list')
            except IntegrityError:
                messages.error(request, "This subject already exists.")
        else:
            messages.error(request, "Total classes should be more than the classes attended.")
    return render(request, 'attendance/subject-form.html', {'form': form, 'subject': subject})

def delete_subject(request, subject_id):
    subject = Subject.objects.get(pk=subject_id)
    if request.method == "POST":
        subject.delete()
        return redirect('attendance:subject_list')
    return render(request, "attendance/delete.html", {'subject': subject})