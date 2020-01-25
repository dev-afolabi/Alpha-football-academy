from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from register.forms import RegisterForm


#class HomePageView(TemplateView):

def home_view(request):
    submitted = False
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form = RegisterForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'home.html', {'form': form, 'submitted': submitted})

def shortcourse_view(request):
    submitted = False
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form = RegisterForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'short_course.html', {'form': form, 'submitted': submitted})



def about_view(request):
    submitted = False
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form = RegisterForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'about.html', {'form': form, 'submitted': submitted})


def tryouts_view(request):
    submitted = False
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form = RegisterForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'tryouts.html', {'form': form, 'submitted': submitted})
# class AboutPageView(TemplateView):
#     template_name = 'pages/about.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

# class ShortCoursePageView(TemplateView):
#     template_name = 'pages/short_course.html'

class FullTimePageView(TemplateView):
    template_name = 'pages/fulltime.html'

# class TryOutPageView(TemplateView):
#     template_name = 'pages/tryouts.html'

class FaqPageView(TemplateView):
    template_name = 'pages/faq.html'

class EducationPageView(TemplateView):
    template_name = 'pages/education.html'

class BtecPageView(TemplateView):
    template_name = 'pages/btec3.html'

class AlevelPageView(TemplateView):
    template_name = 'pages/alevel.html'

class DegreePageView(TemplateView):
    template_name = 'pages/degree.html'

class EnglishPageView(TemplateView):
    template_name = 'pages/english.html'

class ShowcasePageView(TemplateView):
    template_name = 'pages/showcase_match.html'

class ProgramsPageView(TemplateView):
    template_name = 'pages/programs.html'

class AccommodationPageView(TemplateView):
    template_name = 'pages/accommodation.html'

class FacilitiesPageView(TemplateView):
    template_name = 'pages/facilities.html'

class PrivacyPageView(TemplateView):
    template_name = 'pages/privacy.html'

class TermsPageView(TemplateView):
    template_name = 'pages/terms.html'