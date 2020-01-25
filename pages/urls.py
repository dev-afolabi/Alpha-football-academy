from django.urls import path
from django.conf.urls import url
from . import views

from .views import (ContactPageView, EducationPageView, EnglishPageView, BtecPageView,
                    AlevelPageView, DegreePageView, ShowcasePageView, ProgramsPageView,
                    FullTimePageView, FaqPageView, AccommodationPageView, 
                    FacilitiesPageView, TermsPageView, PrivacyPageView)

urlpatterns = [
    url(r'^home$', views.home_view, name='home'),
    url(r'^$', views.home_view, name='home'),
    url(r'^about$', views.about_view, name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    url(r'^short_course$', views.shortcourse_view, name='short_course'),
    path('fulltime/', FullTimePageView.as_view(), name='fulltime'),
    url(r'^tryouts$', views.tryouts_view, name='tryouts'),
    path('faq/', FaqPageView.as_view(), name='faq'),
    path('education/', EducationPageView.as_view(), name='education'),
    path('english/', EnglishPageView.as_view(), name='english'),
    path('btec3/', BtecPageView.as_view(), name='btec3'),
    path('alevel/', AlevelPageView.as_view(), name='alevel'),
    path('degree/', DegreePageView.as_view(), name='degree'),
    path('showcase_match/', ShowcasePageView.as_view(), name='showcase_match'),
    path('programs/', ProgramsPageView.as_view(), name='programs'),
    path('accommodation/', AccommodationPageView.as_view(), name='accommodation'),
    path('facilities/', FacilitiesPageView.as_view(), name='facilities'),
    path('privacy/', PrivacyPageView.as_view(), name='privacy'),
    path('terms/', TermsPageView.as_view(), name='terms'),
]
