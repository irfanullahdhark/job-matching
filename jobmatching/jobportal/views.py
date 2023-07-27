from sqlite3 import Cursor
from urllib import request
from django.db import connection
from django.shortcuts import redirect, render
from django.http import HttpResponse
from pymysql import NULL
from dbtables.models import Db_admin,postajob,Applier,Company
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth import authenticate,login as auth_login,logout


# Create your views here.
def logoutuser(request):
   logout(request)
   return redirect("/jobportal/job_listing/")
def loging(request):
  errormessage = "check your user name or password"
  if request.method=="POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    # query = Db_admin.objects.all()
    user = authenticate(request,username=username,password=password)
    if user is not None:
        auth_login(request,user)
        return redirect('/jobportal/job_listing/')
    else:
        return render(request,"loginform.html",{"error":errormessage})
    # for obj in query:
    #   if obj.user_name == username and obj.user_password==password:
    #   #  return redirect("/jobportal/index/")
    #      return render(request,"index.html",{'admin':'admin'})
    #   else:
    #     errormessage = "check your user name or password"
    #     return render(request,"loginform.html",{"error":errormessage})
  return render(request,"loginform.html",{"error":errormessage})

def login(request):
  return render(request,"loginform.html")
def index(request):
  
    db_admin = Db_admin()
    db_admin.user_name = "Zaheer"
    db_admin.user_password = "Kabul@123"
    db_admin.save()
   
    # Cursor = connection.cursor()
    # Cursor.execute("insert into dbtables_db_admin(user_name,user_password) values('zaheer_zazai','restriction')")
    # Cursor.close()
    # return HttpResponse("hello this is mohammad zaman zaheer")

    return render(request,'index.html')

def about(request):
    # return HttpResponse("hello this is mohammad zaman zaheer")
    return render(request,'about.html')
def job_listing(request):
    query_set = postajob.objects.all()
    # return HttpResponse("hello this is mohammad zaman zaheer")
    return render(request,'job_list.html',{"query":list(query_set)})

def parttime(request):
   query_set = postajob.objects.filter(job_type="PartTime")
   return render(request,'job_list.html',{"query":list(query_set)})

def FullTime(request):
   query_set = postajob.objects.filter(job_type="FullTime")
   return render(request,'job_list.html',{"query":list(query_set)})

def job_detail(request,id):
  query_set = postajob.objects.select_related('related_company').filter(id=id)
  detail = Company.objects.get(company_registrationno=1)
    # return HttpResponse("hello this is mohammad zaman zaheer")
  return render(request,'job_detail.html',{"query":query_set,"details":detail})

def category(request):
    # return HttpResponse("hello this is mohammad zaman zaheer")
    return render(request,'category.html')

def testimonial(request):
    # return HttpResponse("hello this is mohammad zaman zaheer")
    return render(request,'testimonial.html')

def contact(request):
    # return HttpResponse("hello this is mohammad zaman zaheer")
    return render(request,'contact.html')
def returnapply(request,id):
    query_set = postajob.objects.get(id=id)
    return render(request,'ApplyForThePost.html',{"query":query_set})

def postthejob(request):
    postjob = postajob()
    if request.method == 'POST':
        j_t = request.POST.get('JobTitle')
        j_i = request.POST.get('JobId')
        j_e = request.POST.get('Email')
        j_s_d = request.POST.get('JobStartDate')
        j_n_o = request.POST.get('NoOfOpurtunity')
        j_v_n = request.POST.get('vacancynum')
        j_e_d = request.POST.get('JobEndDate')
        j_ex = request.POST.get('Experience')
        j_s = request.POST.get('Salary')
        j_ty = request.POST.get('Type')
        j_l = request.POST.get('Location')
        j_c_s = request.POST.get('CommunicationSkills')
        j_d = request.POST.get('Degree')
        j_f = request.POST.get('Field')
        j_g = request.POST.get('Gender')
        j_e_s = request.POST.getlist('EducationalSkills')
        l_e = len(j_e_s)
        j_co_s = request.POST.getlist('ComputerSkills')
        l_c = len(j_co_s)
        u_lan =request.POST.getlist('Language')
        u_lan_l = len(u_lan)
        u_lan_p_o = request.POST.get("firstlanguagepercentage")
        u_lan_p_t = request.POST.get("secondlanguagepercentage")
        u_lan_p_th = request.POST.get("thirdlanguagepercentage")
        j_des = request.POST.get("Description")
        j_res = request.POST.get("responisibility")

        postjob = postajob()
        postjob.related_company_id = j_i
        postjob.Job_title = j_t
        postjob.job_emailaddress = j_e
        postjob.job_startingdate = j_s_d
        postjob.job_endingdate = j_e_d
        postjob.job_duration = "six month"
        postjob.job_salary = j_s
        postjob.job_type = j_ty
        postjob.job_noofoppurtunity = j_n_o
        postjob.job_location = j_l
        postjob.job_communicationskills = j_c_s
        postjob.job_degree = j_d
        postjob.job_field = j_f
        postjob.job_gender = j_g
        postjob.job_experience = j_ex
        postjob.job_descriptoin = j_des
        postjob.job_vacancynum = j_v_n
        postjob.job_responsibilities = j_res
        if l_e == 1:
         postjob.job_educationalskillfirst = j_e_s[0]
        elif l_e ==2:
          postjob.job_educationalskillfirst = j_e_s[0]
          postjob.job_educationalskillsecond = j_e_s[1]
        elif l_e ==3:
          postjob.job_educationalskillfirst = j_e_s[0]
          postjob.job_educationalskillsecond = j_e_s[1]
          postjob.job_educationalskillthird = j_e_s[2]
        elif l_e==4:
          postjob.job_educationalskillfirst = j_e_s[0]
          postjob.job_educationalskillsecond = j_e_s[1]
          postjob.job_educationalskillthird = j_e_s[2]
          postjob.job_educationalskillfourth = j_e_s[2]

          

        if l_c==1:     
          postjob.job_computerskillfirst = j_co_s[0]
        elif l_c==2:
          postjob.job_computerskillfirst = j_co_s[0]
          postjob.job_computerskillsecond = j_co_s[1]
        elif l_c==3:
          postjob.job_computerskillfirst = j_co_s[0]
          postjob.job_computerskillsecond = j_co_s[1]
          postjob.job_computerskillthird = j_co_s[1]




        if u_lan_l == 1:
          postjob.job_firstlanguage = u_lan[0]
          postjob.job_firstknowpercentage =u_lan_p_o
        elif u_lan_l == 2:
          postjob.job_firstlanguage = u_lan[0]
          postjob.job_firstknowpercentage =u_lan_p_o
          postjob.job_secondlanguage = u_lan[1]
          postjob.job_secondknowpercentage = u_lan_p_t
        elif u_lan_l == 3:
          postjob.job_firstlanguage = u_lan[0]
          postjob.job_firstknowpercentage =u_lan_p_o
          postjob.job_secondlanguage = u_lan[1]
          postjob.job_secondknowpercentage = u_lan_p_th
          postjob.job_thirdlanguage = u_lan[2]
          postjob.job_thirdknowpercentage =u_lan_p_th


        postjob.save()
    # return HttpResponse("hello this is mohammad zaman zaheer")
    return render(request,'PostAJob.html')

  
def CompanyRegistration(request):
    if request.method == 'POST':
        c_r_no = request.POST["RegistrationNo"]
        c_p = request.POST["CompanyPassword"]
        a_n = request.POST["AdminName"]
        c_n = request.POST["CompanyName"]
        c_l = request.POST["Location"]
        c_d = request.POST["Description"]
        company = Company()
        company.admin_user_name_id = a_n
        company.company_registrationno = c_r_no
        company.company_password = c_p
        company.company_name = c_n
        company.company_location = c_l
        company.company_description = c_d
        company.save()
    # return HttpResponse("hello this is mohammad zaman zaheer")
    return render(request,'CompanyRegistration.html')

def ApplyForThePost(request):
 
    Apply = Applier()
    if request.method == 'POST':
        u_n = request.POST.get('UserName')
        u_j_i = request.POST.get('jobid')
        u_e = request.POST.get('Email')
        u_p = request.POST.get('PhoneNumber')
        u_i_n = request.POST.get('IdentityNo')
        u_d_b = request.POST.get('DateOfBirth')
        u_g = request.POST.get('Gender')
        u_l = request.POST.get('Location')
        u_d = request.POST.get('Degree')
        u_f = request.POST.get('Field')
        u_s_d = request.POST.get('SecondDegree')
        u_s_f = request.POST.get('SecondFields')
        u_com_s = request.POST['CommunicationSkills']
        u_ex = request.POST['Experience']
        u_e_s = request.POST.getlist('EducationalSkills')
        l_e_s = len(u_e_s)
        u_c_s = request.POST.getlist('ComputerSkills')
        l_com_s = len(u_c_s)
        u_lan =request.POST.getlist('Language')
        u_lan_l = len(u_lan)
        u_lan_p_o = request.POST.get("firstlanguagepercentage")
        u_lan_p_t = request.POST.get("secondlanguagepercentage")
        u_lan_p_th = request.POST.get("thirdlanguagepercentage")

       


        Apply.Job_id_id = u_j_i
        Apply.applierusername = u_n
        Apply.applieremail = u_e
        Apply.applierphoneno = u_p
        Apply.applieridentityno = u_i_n
        Apply.applierdateofbirth = u_d_b
        Apply.appliergender = u_g
        Apply.applierorignlocation = u_l
        Apply.appliercurrentlocation = "kabul"
        Apply.applierdegree = u_d
        Apply.applierfield = u_f
        Apply.applierseconddegree = u_s_d
        Apply.appliersecondfield = u_s_f
        Apply.appliercommunicationskills = u_com_s
        Apply.applierexperience = u_ex

        if l_e_s == 1:
           Apply.appliereducationalskillfirst = u_e_s[0]
        elif l_e_s == 2:
            Apply.appliereducationalskillfirst = u_e_s[0]
            Apply.appliereducationalskillsecond = u_e_s[1]
        elif l_e_s == 3:
            Apply.appliereducationalskillfirst = u_e_s[0]
            Apply.appliereducationalskillsecond = u_e_s[1]
            Apply.appliereducationalskillthird = u_e_s[2]
        elif l_e_s == 4:
            Apply.appliereducationalskillthird = u_e_s[0]
            Apply.appliereducationalskillsecond = u_e_s[1]
            Apply.appliereducationalskillthird = u_e_s[2]
            Apply.appliereducationalskillfourth = u_e_s[3]
        


        if l_com_s ==1:
            Apply.appliercomputerskillfirst = u_c_s[0]
        elif l_com_s ==2:
            Apply.appliercomputerskillfirst = u_c_s[0]
            Apply.appliercomputerskillfirst = u_c_s[1]

        elif l_com_s ==3:
            Apply.appliercomputerskillfirst = u_c_s[0]
            Apply.appliercomputerskillsecond = u_c_s[1]
            Apply.appliercomputerskillthird = u_c_s[2]


        if u_lan_l == 1:
          Apply.applierfirstlanguage = u_lan[0]
          Apply.applierfirstknowpercentage =u_lan_p_o

        elif u_lan_l == 2:
          Apply.applierfirstlanguage = u_lan[0]
          Apply.applierfirstknowpercentage =u_lan_p_o
          Apply.appliersecondlanguage = u_lan[1]
          Apply.appliersecondknowpercentage = u_lan_p_t

        elif u_lan_l == 3:
          Apply.applierfirstlanguage = u_lan[0]
          Apply.applierfirstknowpercentage =u_lan_p_o
          Apply.appliersecondlanguage = u_lan[1]
          Apply.appliersecondknowpercentage = u_lan_p_t
          Apply.applierthirdlanguage = u_lan[2]
          Apply.applierthirdknowpercentage =u_lan_p_th
        Apply.save()
      
        
    # return HttpResponse("hello this is mohammad zaman zaheer")
    return redirect('/jobportal/job_listing/')

def returnupdate(request,id):
  query_set = postajob.objects.get(id=id)
  return render(request,'updatejob.html',{'getdata':query_set}) 


def setupdate(request,id):
      postjob = postajob(pk=id)
      if request.method == 'POST':
        j_t = request.POST.get('JobTitle')
        j_i = request.POST.get('JobId')
        j_e = request.POST.get('Email')
        j_s_d = request.POST.get('JobStartDate')
        j_n_o = request.POST.get('NoOfOpurtunity')
        j_v_n = request.POST.get('vacancynum')
        j_e_d = request.POST.get('JobEndDate')
        j_ex = request.POST.get('Experience')
        j_s = request.POST.get('Salary')
        j_ty = request.POST.get('Type')
        j_l = request.POST.get('Location')
        j_c_s = request.POST.get('CommunicationSkills')
        j_d = request.POST.get('Degree')
        j_f = request.POST.get('Field')
        j_g = request.POST.get('Gender')
        j_e_s = request.POST.getlist('EducationalSkills')
        l_e = len(j_e_s)
        j_co_s = request.POST.getlist('ComputerSkills')
        l_c = len(j_co_s)
        u_lan =request.POST.getlist('Language')
        u_lan_l = len(u_lan)
        u_lan_p_o = request.POST.get("firstlanguagepercentage")
        u_lan_p_t = request.POST.get("secondlanguagepercentage")
        u_lan_p_th = request.POST.get("thirdlanguagepercentage")
        j_des = request.POST.get("Description")
        j_res = request.POST.get("responisibility")

       
        postjob.related_company_id = j_i
        postjob.Job_title = j_t
        postjob.job_emailaddress = j_e
        postjob.job_startingdate = j_s_d
        postjob.job_endingdate = j_e_d
        postjob.job_duration = "six month"
        postjob.job_salary = j_s
        postjob.job_type = j_ty
        postjob.job_noofoppurtunity = j_n_o
        postjob.job_location = j_l
        postjob.job_communicationskills = j_c_s
        postjob.job_degree = j_d
        postjob.job_field = j_f
        postjob.job_gender = j_g
        postjob.job_experience = j_ex
        postjob.job_descriptoin = j_des
        postjob.job_vacancynum = j_v_n
        postjob.job_responsibilities = j_res
        if l_e == 1:
         postjob.job_educationalskillfirst = j_e_s[0]
        elif l_e ==2:
          postjob.job_educationalskillfirst = j_e_s[0]
          postjob.job_educationalskillsecond = j_e_s[1]
        elif l_e ==3:
          postjob.job_educationalskillfirst = j_e_s[0]
          postjob.job_educationalskillsecond = j_e_s[1]
          postjob.job_educationalskillthird = j_e_s[2]
        elif l_e==4:
          postjob.job_educationalskillfirst = j_e_s[0]
          postjob.job_educationalskillsecond = j_e_s[1]
          postjob.job_educationalskillthird = j_e_s[2]
          postjob.job_educationalskillfourth = j_e_s[2]

          

        if l_c==1:     
          postjob.job_computerskillfirst = j_co_s[0]
        elif l_c==2:
          postjob.job_computerskillfirst = j_co_s[0]
          postjob.job_computerskillsecond = j_co_s[1]
        elif l_c==3:
          postjob.job_computerskillfirst = j_co_s[0]
          postjob.job_computerskillsecond = j_co_s[1]
          postjob.job_computerskillthird = j_co_s[1]




        if u_lan_l == 1:
          postjob.job_firstlanguage = u_lan[0]
          postjob.job_firstknowpercentage =u_lan_p_o
        elif u_lan_l == 2:
          postjob.job_firstlanguage = u_lan[0]
          postjob.job_firstknowpercentage =u_lan_p_o
          postjob.job_secondlanguage = u_lan[1]
          postjob.job_secondknowpercentage = u_lan_p_t
        elif u_lan_l == 3:
          postjob.job_firstlanguage = u_lan[0]
          postjob.job_firstknowpercentage =u_lan_p_o
          postjob.job_secondlanguage = u_lan[1]
          postjob.job_secondknowpercentage = u_lan_p_th
          postjob.job_thirdlanguage = u_lan[2]
          postjob.job_thirdknowpercentage =u_lan_p_th


        postjob.save()
      return redirect('/jobportal/job_listing/')



def deletejob(request,id):
  query_set = postajob.objects.get(id=id)
  query_set.delete()
  return redirect('/jobportal/job_listing/')



def shortlist(request,id):
  app = Applier()
  ID = id 
  querry = Applier.objects.filter(Job_id_id = 300).all()
  queryset = Applier.objects.filter(Job_id_id=ID).all()
  job = postajob.objects.get(id=id)
  # if every educated is acceptable
  if job.job_degree=="AllEducated":
     querry = Applier.objects.filter(~Q(applierdegree="UnEducated"),Job_id_id =ID)
    # if every educated is acceptable
  elif job.job_degree=="Everyone" and job.job_gender !="Both":
     querry = Applier.objects.filter(Job_id_id =ID,appliergender = job.job_gender)
  elif job.job_degree=="Everyone" and job.job_gender =="Both":
     querry = Applier.objects.filter(Job_id_id =ID)


  elif job.job_experience =="SixMonth" and job.job_degree == "HighSchool" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  


  elif job.job_experience =="NotRequired" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  elif job.job_experience =="NotRequired" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
 



  elif job.job_experience =="SixMonth" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
 
  elif job.job_experience =="SixMonth" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  

  elif job.job_experience =="OneYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
 
  elif job.job_experience =="OneYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  

  elif job.job_experience =="TwoYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
 
  elif job.job_experience =="TwoYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  


# second one

  elif job.job_experience =="NotRequired" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  elif job.job_experience =="NotRequired" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
 




  elif job.job_experience =="SixMonth" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
 
  elif job.job_experience =="SixMonth" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  

  elif job.job_experience =="OneYear" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,applierdegree = job.job_degree,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
 
  elif job.job_experience =="OneYear" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  

  elif job.job_experience =="TwoYear" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
 
  elif job.job_experience =="TwoYear" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  



# third one
  elif job.job_experience =="NotRequired" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  elif job.job_experience =="NotRequired" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender == "Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
 



  elif job.job_experience =="SixMonth" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
 
  elif job.job_experience =="SixMonth" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  

  elif job.job_experience =="OneYear" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,applierdegree = job.job_degree,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
 
  elif job.job_experience =="OneYear" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  

  elif job.job_experience =="TwoYear" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
 
  elif job.job_experience =="TwoYear" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  


# Fourth one

  elif job.job_experience =="NotRequired" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  elif job.job_experience =="NotRequired" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  

  elif job.job_experience =="SixMonth" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  
  elif job.job_experience =="SixMonth" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  

  elif job.job_experience =="OneYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  elif job.job_experience =="OneYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  
  elif job.job_experience =="TwoYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  elif job.job_experience =="TwoYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  


# Fifth one
  elif job.job_experience =="NotRequired" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender != "Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  elif job.job_experience =="NotRequired" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender == "Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
 






  elif job.job_experience =="SixMonth" and job.job_degree == "HighSchool" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  

  elif job.job_experience =="SixMonth" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
 
  elif job.job_experience =="SixMonth" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  

  elif job.job_experience =="OneYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) ,Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  elif job.job_experience =="OneYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL :
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  
  elif job.job_experience =="TwoYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  elif job.job_experience =="TwoYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  


# Sixth one

  elif job.job_experience =="NotRequired" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  elif job.job_experience =="NotRequired" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  




  elif job.job_experience =="SixMonth" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  
  elif job.job_experience =="SixMonth" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  

  elif job.job_experience =="OneYear" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) ,Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  elif job.job_experience =="OneYear" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  
  elif job.job_experience =="TwoYear" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  elif job.job_experience =="TwoYear" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  


# seventh one

  elif job.job_experience =="NotRequired" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  elif job.job_experience =="NotRequired" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  


  elif job.job_experience =="SixMonth" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  
  elif job.job_experience =="SixMonth" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  

  elif job.job_experience =="OneYear" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) ,Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  elif job.job_experience =="OneYear" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  
  elif job.job_experience =="TwoYear" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliercomputerskillfirst =job.job_computerskillfirst)
  elif job.job_experience =="TwoYear" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_computerskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliercomputerskillfirst =job.job_computerskillfirst)
  














  elif job.job_experience =="SixMonth" and job.job_degree == "HighSchool" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  


  elif job.job_experience =="NotRequired" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="NotRequired" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field)
 



  elif job.job_experience =="SixMonth" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender)
 
  elif job.job_experience =="SixMonth" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field)
  

  elif job.job_experience =="OneYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender)
 
  elif job.job_experience =="OneYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field)
  

  elif job.job_experience =="TwoYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender)
 
  elif job.job_experience =="TwoYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field)
  




# second one
  elif job.job_experience =="NotRequired" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="NotRequired" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field)
 




  elif job.job_experience =="SixMonth" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
 
  elif job.job_experience =="SixMonth" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field)
  

  elif job.job_experience =="OneYear" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,applierdegree = job.job_degree,appliergender=job.job_gender)
 
  elif job.job_experience =="OneYear" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field)
  

  elif job.job_experience =="TwoYear" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
 
  elif job.job_experience =="TwoYear" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field)
  




# third one
  elif job.job_experience =="NotRequired" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="NotRequired" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender == "Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field)
 



  elif job.job_experience =="SixMonth" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
 
  elif job.job_experience =="SixMonth" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field)
  

  elif job.job_experience =="OneYear" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,applierdegree = job.job_degree,appliergender=job.job_gender)
 
  elif job.job_experience =="OneYear" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field)
  

  elif job.job_experience =="TwoYear" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
 
  elif job.job_experience =="TwoYear" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field)
  


# Fourth one
  elif job.job_experience =="NotRequired" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="NotRequired" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field)
  






  elif job.job_experience =="SixMonth" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender)
  
  elif job.job_experience =="SixMonth" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field)
  

  elif job.job_experience =="OneYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="OneYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field)
  
  elif job.job_experience =="TwoYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="TwoYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierfield=job.job_field)
  


# fifth one
  elif job.job_experience =="NotRequired" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender != "Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="NotRequired" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender == "Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field)
 






  elif job.job_experience =="SixMonth" and job.job_degree == "HighSchool" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  

  elif job.job_experience =="SixMonth" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender)
 
  elif job.job_experience =="SixMonth" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field)
  

  elif job.job_experience =="OneYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) ,Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="OneYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL :
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field)
  
  elif job.job_experience =="TwoYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="TwoYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field)
  


# Sixth one
  elif job.job_experience =="NotRequired" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="NotRequired" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field)
  




  elif job.job_experience =="SixMonth" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  
  elif job.job_experience =="SixMonth" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field)
  

  elif job.job_experience =="OneYear" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) ,Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="OneYear" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL :
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field)
  
  elif job.job_experience =="TwoYear" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="TwoYear" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field)
  



# seventh one
  elif job.job_experience =="NotRequired" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="NotRequired" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field)
  


  elif job.job_experience =="SixMonth" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  
  elif job.job_experience =="SixMonth" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field)
  

  elif job.job_experience =="OneYear" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) ,Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="OneYear" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL :
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field)
  
  elif job.job_experience =="TwoYear" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="TwoYear" and job.job_degree == "Dectorate" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierdegree = job.job_degree,applierfield=job.job_field)
  







  #if first educational skill is required and experince is not required
  elif job.job_experience =="NotRequired" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliercommunicationskills=job.job_communicationskills,appliergender=job.job_gender,appliereducationalskillfirst=job.job_educationalskillfirst)
  #if eperience and gender is not required
  elif job.job_experience =="NotRequired" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliercommunicationskills=job.job_communicationskills,appliereducationalskillfirst=job.job_educationalskillfirst) 
  
   # if experince is required but in low level
  elif job.job_experience =="SixMonth" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliercommunicationskills=job.job_communicationskills, appliergender=job.job_gender,appliereducationalskillfirst=job.job_educationalskillfirst)
  
   # if experince is required but in low level and gneder is not required
  elif job.job_experience =="SixMonth" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliercommunicationskills=job.job_communicationskills ,appliereducationalskillfirst=job.job_educationalskillfirst)
   
    # if experince is required but in low level and gneder is not required and communicational skills also
  elif job.job_experience =="SixMonth" and job.job_degree != "NotRequired" and job.job_communicationskills =="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,applierexperience=job.job_experience| Q(applierexperience = "OneYear") | Q(applierexperience = "TwoYear") ,appliereducationalskillfirst=job.job_educationalskillfirst)
  

   # if experince is required but in low level
  elif job.job_experience =="OneYear" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
     
       querry = Applier.objects.filter(Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliercommunicationskills=job.job_communicationskills,appliereducationalskillfirst=job.job_educationalskillfirst,appliergender=job.job_gender)
      
   # if experince is required but in low level and gender is not required
  elif job.job_experience =="OneYear" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliercommunicationskills=job.job_communicationskills,appliereducationalskillfirst=job.job_educationalskillfirst)
   # if experince is required but in low level gender and communicational skills are not required
  elif job.job_experience =="OneYear" and job.job_degree != "NotRequired" and job.job_communicationskills =="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliereducationalskillfirst=job.job_educationalskillfirst)
 

   # if experince is required but in low level
  elif job.job_experience =="TwoYear" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
       querry = Applier.objects.filter(Q(applierexperience="TwoYear"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliercommunicationskills=job.job_communicationskills,appliereducationalskillfirst=job.job_educationalskillfirst,appliergender=job.job_gender)
   # if experince is required but in low level and gender is not required
  elif job.job_experience =="TwoYear" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(Q(applierexperience="TwoYear"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliercommunicationskills=job.job_communicationskills,appliereducationalskillfirst=job.job_educationalskillfirst)
   # if experince is required but in low level gender and communicational skills are not required
  elif job.job_experience =="TwoYear" and job.job_degree != "NotRequired" and job.job_communicationskills =="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(Q(applierexperience="TwoYear"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliereducationalskillfirst=job.job_educationalskillfirst)
 



# if every thing is required and only first educational skill is required
  elif job.job_experience =="TwoYear" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,applierexperience=job.job_experience,appliergender=job.job_gender,appliereducationalskillfirst=job.job_educationalskillfirst)

  # jobcommunicationskills = job.job_communicationskills
  elif job.job_experience =="NotRequired" and job.job_degree == "NotRequired" and job.job_communicationskills =="NotRequired" and job.job_gender=="Both" :
      querry = Applier.objects.filter(Job_id_id=ID)
  elif job.job_experience =="NotRequired" and job.job_degree == "NotRequired" and job.job_communicationskills =="NotRequired" and job.job_gender=="Both" and job.job_educationalskillfirst is NULL:
      querry = Applier.objects.filter(Job_id_id=ID)
  # if every thing is required and only first education skills is required


  elif job.job_experience =="SixMonth" and job.job_degree == "HighSchool" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  











  elif job.job_experience =="SixMonth" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="SixMonth" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field)
  

  elif job.job_experience =="OneYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) ,Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="OneYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL :
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field)
  
  elif job.job_experience =="TwoYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="TwoYear" and job.job_degree == "Bachelor" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst),Job_id_id=ID,applierfield=job.job_field)
  









  elif job.job_experience =="SixMonth" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Q(applierdegree="Bachelor")|Q(applierdegree="Master"),Job_id_id=ID,applierfield=job.job_field,appliergender=job.job_gender)
  elif job.job_experience =="SixMonth" and job.job_degree == "Master" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Q(applierdegree="Bachelor")|Q(applierdegree="Master"),Job_id_id=ID,applierfield=job.job_field)
  



  elif job.job_experience =="SixMonth" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  
  elif job.job_experience =="SixMonth" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field)
  

  elif job.job_experience =="SixMonth" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliereducationalskillfirst=job.job_educationalskillfirst)
  
  elif job.job_experience =="SixMonth" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear")| Q(applierexperience="SixMonth"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliereducationalskillfirst=job.job_educationalskillfirst)
  

  

  elif job.job_experience =="OneYear" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  
  elif job.job_experience =="OneYear" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field)
  
  elif job.job_experience =="OneYear" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliereducationalskillfirst=job.job_educationalskillfirst)
  
  elif job.job_experience =="OneYear" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="OneYear") | Q(applierexperience="TwoYear"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliereducationalskillfirst=job.job_educationalskillfirst)
  




  elif job.job_experience =="TwoYear" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  
  elif job.job_experience =="TwoYear" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL and job.job_educationalskillsecond is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"), Q(applierexperience="TwoYear"),Q(appliereducationalskillfirst = job.job_educationalskillfirst) |Q(appliereducationalskillfirst = job.job_educationalskillsecond),Q(appliereducationalskillsecond = job.job_educationalskillfirst)|Q(appliereducationalskillsecond=job.job_educationalskillsecond),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field)
  
  
  elif job.job_experience =="TwoYear" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="TwoYear"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliergender=job.job_gender,appliereducationalskillfirst=job.job_educationalskillfirst)
  
  elif job.job_experience =="TwoYear" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both" and job.job_educationalskillfirst is not NULL:
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Q(applierexperience="TwoYear"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliereducationalskillfirst=job.job_educationalskillfirst)
 
 
 
 
 
 
  elif job.job_experience =="NotRequired" and job.job_degree == "NotRequired" and job.job_communicationskills =="NotRequired" and job.job_gender !="Both":
      querry = Applier.objects.filter(Job_id_id=ID,appliergender=job.job_gender).all()
  # if gender and comunication skilss are required  other things are not required
  elif job.job_experience =="NotRequired" and job.job_degree == "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both":
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Job_id_id=ID,appliergender=job.job_gender)
  # if only gender is required no other things are requiered
  elif job.job_experience =="NotRequired" and job.job_degree == "NotRequired" and job.job_communicationskills =="NotRequired" and job.job_gender !="Both":
      querry = Applier.objects.filter(Job_id_id=ID,appliergender=job.job_gender)
  # if only communication skills are required
  elif job.job_experience =="NotRequired" and job.job_degree == "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both":
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Job_id_id=ID)
  # if gender communication skills and gender are required but not others things are required
  elif job.job_experience !="NotRequired" and job.job_degree == "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both":
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Job_id_id=ID,appliergender=job.job_gender,applierexperience=job.job_experience)
  # if communication skills and experince are required and no ohters thing are required
  elif job.job_experience !="NotRequired" and job.job_degree == "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both":
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Job_id_id=ID,applierexperience=job.job_experience)
  # if only communication skills and gender are required no others thing are reqquired
  elif job.job_experience =="NotRequired" and job.job_degree == "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both":
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Job_id_id=ID,appliergender=job.job_gender)
  # if degree and related field are required no others thing are required
  elif job.job_experience =="NotRequired" and job.job_degree != "NotRequired" and job.job_communicationskills =="NotRequired" and job.job_gender =="Both":
      querry = Applier.objects.filter(Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field)
  # if job field drgree and gender are required
  elif job.job_experience =="NotRequired" and job.job_degree != "NotRequired" and job.job_communicationskills =="NotRequired" and job.job_gender !="Both":
      querry = Applier.objects.filter(Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  #if degree field and experince are required and no others things are required
  elif job.job_experience !="NotRequired" and job.job_degree != "NotRequired" and job.job_communicationskills =="NotRequired" and job.job_gender =="Both":
      querry = Applier.objects.filter(Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,applierexperience=job.job_experience)
  # if field degree experience and gender are required no others things are required
  elif job.job_experience !="NotRequired" and job.job_degree != "NotRequired" and job.job_communicationskills =="NotRequired" and job.job_gender !="Both":
      querry = Applier.objects.filter(Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,applierexperience=job.job_experience,appliergender=job.job_gender)
  # if fields degree and gender are required no ohters thing are required
  elif job.job_experience =="NotRequired" and job.job_degree != "NotRequired" and job.job_communicationskills =="NotRequired" and job.job_gender !="Both":
      querry = Applier.objects.filter(Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  # if field degree and communication skills are required
  elif job.job_experience =="NotRequired" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both":
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field)
  # if degree fields communication skills and degree are required no others things are required
  elif job.job_experience =="NotRequired" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both":
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,appliergender=job.job_gender)
  # if degree field experience and communication skills are required
  elif job.job_experience !="NotRequired" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender =="Both":
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,applierexperience=job.job_experience)
  # if field degree communication skills gender and experice are all required
  elif job.job_experience !="NotRequired" and job.job_degree != "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both":
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Job_id_id=ID,applierdegree=job.job_degree,applierfield=job.job_field,applierexperience=job.job_experience,appliergender=job.job_gender)
  #if no other thing is required just gender is required
  elif job.job_experience =="NotRequired" and job.job_degree == "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both":
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Job_id_id=ID,appliergender=job.job_gender)
  #if just communicationskill and gender is required
  elif job.job_experience =="NotRequired" and job.job_degree == "NotRequired" and job.job_communicationskills !="NotRequired" and job.job_gender !="Both":
      querry = Applier.objects.filter(~Q(appliercommunicationskills= "DontHave"),Job_id_id=ID,appliergender=job.job_gender)
 

  
#   for email in querry:
#     send_mail(
#       'subject',
#       'Hey you are selected for the'+ job.Job_title +'with vacancy'+job.job_vacancynum+ 'contact your company for more information ' + job.job_emailaddress+'send your documents experince letter and transcript etc',
#       'jobentrywebsite@gmail.com',
#       [email.applieremail],
#       fail_silently=False,
#     )
#     emailaddress = ''
#     for email in querry:
#       emailaddress += email.applieremail + ' '

#     send_mail(
#       'subject',
#       'te following person are selected for your job with following email adresses '+ emailaddress,
#       'jobentrywebsite@gmail.com',
#       [job.job_emailaddress],
#       fail_silently=False,
#     )
   
  return render(request,"shortlist.html",{"query":list(querry),"querysets":list(queryset)})
