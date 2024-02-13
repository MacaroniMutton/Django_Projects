from django.shortcuts import redirect, render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.

def accept(request):
    if request.method == "POST":
        _, name, email, phone_no, summary, degree, school, university, previous_work, skills = request.POST.values()
        profile = Profile(name=name, email=email, phone_no=phone_no, summary=summary, degree=degree, school=school, university=university, previous_work=previous_work, skills=skills)
        profile.save()
        return redirect('profile_list')
    return render(request, 'CVgenerator/accept.html')

def resume(request, id):
    profile = Profile.objects.get(pk=id)
    template = loader.get_template('CVgenerator/resume.html')
    html = template.render({'profile': profile})
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }

#Must be 'option=options' and add 'configuration=config'
    pdf = pdfkit.from_string(html, False, options=options)
    response = HttpResponse(pdf, content_type='application/pdf')

#filename must be included in contentdisposition
    response['Content-Disposition'] = 'attachment;filename=resume.pdf'
    
    return response

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'CVgenerator/profile-list.html', {'profiles': profiles})