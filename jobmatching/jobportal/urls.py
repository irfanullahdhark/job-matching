from django.urls import path
from . import views
app_name = "jobportal"
urlpatterns=[
    path('',views.index,name ="index"),
    path('about/',views.about,name="about"),
    path('job_listing/',views.job_listing,name="job_listing"),
    path('job_detail/<int:id>',views.job_detail,name="job_detail"),
     path('FullTime/',views.FullTime,name="FullTime"),
     path('logoutuser/',views.logoutuser,name="logoutuser"),

    path('parttime/',views.parttime,name="parttime"),
    path('category/',views.category,name="category"),
    path('testimonial/',views.testimonial,name="testimonial"),
    path('contact/',views.contact,name="contact"),
    path('postthejob/',views.postthejob,name="postthejob"),
    path('Apply/',views.ApplyForThePost,name="ApplyForThePost"),
    path('returnapply/<int:id>',views.returnapply,name="returnapply"),
    path('CompanyRegistration/',views.CompanyRegistration,name="CompanyRegistration"),
    path('updatejob/<int:id>',views.returnupdate,name="returnupdate"),
    path('deletejob/<int:id>',views.deletejob,name="deletejob"),
    path('setupdate/<int:id>',views.setupdate,name="setupdate"),
    path('shortlist/<int:id>',views.shortlist,name="shortlist"),
    path('login/',views.login,name="login"),
    path('loging/',views.loging,name="loging"),
   




]
