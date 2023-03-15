from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .models import *


# Create your views here.
def fun1(request):
    if request.method == "POST":
        global fullname
        global laname
        global num
        global fn
        global user
        firstname = request.POST.get('fname')
        middlename = request.POST['mname']
        # midname = request.POST.get('mname')

        lastname = request.POST['lname']
        laname=request.POST.get('lname')
        dateofbirth = request.POST['DOB']
        birthplace = request.POST['bplace']
        birthplacetaluka = request.POST['bptaluka']
        bpd = request.POST['bpd']
        age = request.POST['age']
        languageknown = request.POST['lknown']
        gender = request.POST['gender']
        marritalstatus = request.POST['mstetus']
        bloodgroup = request.POST['bgroup']
        nationality = request.POST['nlity']
        religion = request.POST['religion']
        cast = request.POST['cast']
        category = request.POST['category']
        emailid = request.POST['emailid']
        user=request.POST.get('emailid')
        contactno = request.POST['contactno']
        emergencycontactno = request.POST['eno']
        ak=request.POST['ak']
        adharimage = request.POST['adharimage']
        pancardno = request.POST['panno']
        panimage = request.POST['panimage']
        pad=request.POST['pad']
        pincode = request.POST['pincode']
        permanentaddress = request.POST['peraddress']
        perpincode = request.POST['percode']
        employeeimage=request.POST['adhura']
        ssc = request.POST['SSC']
        sscbord = request.POST['sscbord']
        sscpersentage = request.POST['sscpersentage']
        sscpassingyear = request.POST['sscpassingyear']
        ssccertificate = request.POST['ssccer']
        hsc = request.POST['hsc']
        hsccbord = request.POST['hsccbord']
        hsccpersentage = request.POST['hscpersentage']
        hscpassingyear = request.POST['hscpassingyear']
        hsccertificate = request.POST['hsccer']
        diploma = request.POST['diploma']
        diplomabord = request.POST['diplomabord']
        diplomapersentage = request.POST['diplomapersentage']
        diplomapassingyear = request.POST['diplomapassingyear']
        diplomacertificate = request.POST['diploma']
        gradution = request.POST['gradution']
        gradutionbord = request.POST['gradutionbord']
        gradutionpersentage = request.POST['gradutionpersentage']
        gradutionpassingyear = request.POST['gradutionpassingyear']
        gradutioncertificate = request.POST['gradutioncer']
        postgradution = request.POST['postgradution']
        postgradutionbord = request.POST['postgradutionbord']
        postgradutionpersentage = request.POST['postgradutionpersentage']
        postgradutionpassingyear = request.POST['postgradutionpassingyear']
        postgradutioncertificate = request.POST['postgradutioncer']
        other = request.POST['other']
        institude = request.POST['institute']
        corsename = request.POST['corsename']
        corsepersentage = request.POST['corsepersentage']
        corsecertificate = request.POST['corsecer']
        father = request.POST['father']
        fdob = request.POST['fdob']
        fage = request.POST['fage']
        fgen = request.POST['ffgen']
        frelation = request.POST['frelstion']
        mather = request.POST['mather']
        mdob = request.POST['mdob']
        mage = request.POST['mage']
        mgen = request.POST['mgen']
        mrelation = request.POST['mrelstion']
        cihldren1 = request.POST['children1']
        c1dob = request.POST['c1dob']
        c1age = request.POST['c1age']
        c1gen = request.POST['c1gen']
        c1relation = request.POST['c1relstion']
        children2 = request.POST['children2']
        c2dob = request.POST['c2dob']
        c2age = request.POST['c2age']
        c2gen = request.POST['c2gen']
        c2relation = request.POST['c2relstion']
        companyname = request.POST['companyname']
        durationfrom = request.POST['durationfrom']
        durationto = request.POST['durationto']
        joiningctc = request.POST['joiningctc']
        lctc = request.POST['lctc']
        twe = request.POST['twe']
        fullname=firstname[0]+laname[0]
        fn=firstname+" "+laname
        print(type(fullname))
        filturm(fname=firstname, mname=middlename,lname=lastname,dob=dateofbirth,birthplace=birthplace,
                 birthplacetaluka=birthplacetaluka,bpd=bpd,age=age,languageknown=languageknown,
                 gender=gender,maristetus=marritalstatus,bloodgroup=bloodgroup,nationality=nationality,religion=religion,
                 cast=cast,category=category,emailid=emailid,contactno=contactno,emergencycontactno=emergencycontactno,
                 ak=ak,adharimage=adharimage,pancardno=pancardno,panimage=panimage,pad=pad,
                 pincode=pincode,
              permanentaddress=permanentaddress,
              perpincode=perpincode,
              Eii=employeeimage,ssc=ssc, sscbord=sscbord, sscpersentage=sscpersentage, sscpassingyear=sscpassingyear,
              ssccertificate=ssccertificate,
              hsc=hsc, hsccbord=hsccbord, hsccpersentage=hsccpersentage, hscpassingyear=hscpassingyear,
              hsccertificate=hsccertificate,
              diploma=diploma, diplomabord=diplomabord, diplomapersentage=diplomapersentage,
              diplomapassingyear=diplomapassingyear, diplomacertificate=diplomacertificate
              , gradution=gradution, gradutionbord=gradutionbord, gradutionpersentage=gradutionpersentage,
              gradutionpassingyear=gradutionpassingyear, gradutioncertificate=gradutioncertificate,
              postgradution=postgradution, postgradutionbord=postgradutionbord,
              postgradutionpersentage=postgradutionpersentage,
              postgradutionpassingyear=postgradutionpassingyear,
              postgradutioncertificate=postgradutioncertificate,
              other=other, institude=institude, corsename=corsename, corsepersentage=corsepersentage,
              corsecertificate=corsecertificate,
                father=father, fdob=fdob, fage=fage, fgen=fgen, frelation=frelation, mather=mather, mdob=mdob,
                mage=mage, mrelation=mrelation,
                cihldren1=cihldren1,c1dob=c1dob,c1age=c1age,c1gen=c1gen,children2=children2,c2dob=c2dob,c2gen=c2gen,c2relation=c2relation,
                companyname=companyname,
                durationfrom=durationfrom,
                durationto=durationto,
                joiningctc=joiningctc,
                lctc=lctc,
                twe=twe).save()

        b=filturm.objects.latest('filturmid')
        a=str(b)
        print(a)
        num = ""
        for d in a:
            if d.isdigit():
                num = num + d
        print("Extracted numbers from the list : " + num)
        num = fullname + "0" + num
        print(num)
        global p
        p='filturm@123'
        user = User.objects.create_user(username=num, password=p, first_name=fn, last_name=laname)
        Mainfilturm(user=user,fname=firstname, mname=middlename, lname=lastname, dob=dateofbirth, birthplace=birthplace,
                birthplacetaluka=birthplacetaluka, bpd=bpd, age=age, languageknown=languageknown,
                gender=gender, maristetus=marritalstatus, bloodgroup=bloodgroup, nationality=nationality,
                religion=religion,
                cast=cast, category=category, emailid=emailid, contactno=contactno,
                emergencycontactno=emergencycontactno,
                ak=ak, adharimage=adharimage, pancardno=pancardno, panimage=panimage, pad=pad,
                pincode=pincode,
                permanentaddress=permanentaddress,
                perpincode=perpincode,
                Eii=employeeimage, ssc=ssc, sscbord=sscbord, sscpersentage=sscpersentage, sscpassingyear=sscpassingyear,
                ssccertificate=ssccertificate,
                hsc=hsc, hsccbord=hsccbord, hsccpersentage=hsccpersentage, hscpassingyear=hscpassingyear,
                hsccertificate=hsccertificate,
                diploma=diploma, diplomabord=diplomabord, diplomapersentage=diplomapersentage,
                diplomapassingyear=diplomapassingyear, diplomacertificate=diplomacertificate
                , gradution=gradution, gradutionbord=gradutionbord, gradutionpersentage=gradutionpersentage,
                gradutionpassingyear=gradutionpassingyear, gradutioncertificate=gradutioncertificate,
                postgradution=postgradution, postgradutionbord=postgradutionbord,
                postgradutionpersentage=postgradutionpersentage,
                postgradutionpassingyear=postgradutionpassingyear,
                postgradutioncertificate=postgradutioncertificate,
                other=other, institude=institude, corsename=corsename, corsepersentage=corsepersentage,
                corsecertificate=corsecertificate,
                father=father, fdob=fdob, fage=fage, fgen=fgen, frelation=frelation, mather=mather, mdob=mdob,
                mage=mage, mrelation=mrelation,
                cihldren1=cihldren1, c1dob=c1dob, c1age=c1age, c1gen=c1gen, children2=children2, c2dob=c2dob,
                c2gen=c2gen, c2relation=c2relation,
                companyname=companyname,
                durationfrom=durationfrom,
                durationto=durationto,
                joiningctc=joiningctc,
                lctc=lctc,
                twe=twe).save()

        html_tpl_path = 'pdfpage.html'
        context_data = {'name': request.POST.get( 'fname' ), 'midname': request.POST.get( 'mname' ),
                        'lastname': request.POST.get( 'lname' ), 'dob': request.POST.get( 'DOB' ),
                        'birthplace': request.POST.get( 'bplace' ),
                        'birthplacetaluka': request.POST.get( 'bptaluka' ), 'bpd': request.POST.get( 'bpd' ),
                        'age': request.POST.get( 'age' ), 'languageknown': request.POST.get( 'lknown' ),
                        'gender': request.POST.get( 'gender' ), 'marritalstatus': request.POST.get( 'mstetus' ),
                        'bloodgroup': request.POST.get( 'bgroup' ), 'nationality': request.POST.get( 'nlity' ),
                        'religion ': request.POST.get( 'religion' ), 'cast': request.POST.get( 'cast' ),
                        'category': request.POST.get( 'category' ), 'emailid': request.POST.get( 'emailid' ),
                        'user': request.POST.get( 'emailid' ), 'contactno': request.POST.get( 'contactno' ),
                        'emergencycontactno': request.POST.get( 'eno' ),
                        'ak': request.POST.get( 'ak' ), 'adharimage': request.POST.get( 'adharimage' ),
                        'pancardno': request.POST.get( 'panno' ), 'panimage': request.POST.get( 'panimage' ),
                        'pad': request.POST.get( 'pad' ), 'pincode': request.POST.get( 'pincode' ),
                        'permanentaddress': request.POST.get( 'peraddress' ),
                        'perpincode': request.POST.get( 'percode' ), 'employeeimage': request.POST.get( 'adhura' ),
                        'ssc': request.POST.get( 'SSC' ),
                        'sscbord': request.POST.get( 'sscbord' ), 'sscpersentage': request.POST.get( 'sscpersentage' ),
                        'sscpassingyear': request.POST.get( 'sscpassingyear' ),
                        'ssccertificate': request.POST.get( 'ssccer' ), 'hsc': request.POST.get( 'hsc' ),
                        'hsccbord': request.POST.get( 'hsccbord' ),
                        'hsccpersentage': request.POST.get( 'hscpersentage' ),
                        'hscpassingyear': request.POST.get( 'hscpassingyear' ),
                        'hsccertificate': request.POST.get( 'hsccer' ), 'diploma': request.POST.get( 'diploma' ),
                        'diplomabord': request.POST.get( 'diplomabord' ),
                        'diplomapersentage': request.POST.get( 'diplomapersentage' ),
                        'diplomapassingyear': request.POST.get( 'diplomapassingyear' ),
                        'diplomacertificate': request.POST.get( 'diploma' ),
                        'gradution': request.POST.get( 'gradution' ),
                        'gradutionbord': request.POST.get( 'gradutionbord' ),
                        'gradutionpersentage': request.POST.get( 'gradutionpersentage' ),
                        'gradutionpassingyear': request.POST.get( 'gradutionpassingyear' ),
                        'gradutioncertificate': request.POST.get( 'gradutioncer' ),
                        'postgradution': request.POST.get( 'postgradution' ),
                        'postgradutionbord': request.POST.get( 'postgradutionbord' ),
                        'postgradutionpersentage': request.POST.get( 'postgradutionpersentage' ),
                        'postgradutionpassingyear': request.POST.get( 'postgradutionpassingyear' ),
                        'postgradutioncertificate': request.POST.get( 'postgradutioncer' ),
                        'other': request.POST.get( 'other' ),
                        'institude': request.POST.get( 'institute' ),
                        'corsename': request.POST.get( 'corsename' ),
                        'corsepersentage': request.POST.get( 'corsepersentage' ),
                        'corsecertificate': request.POST.get( 'corsecer' ),
                        'father': request.POST.get( 'father' ),
                        'fdob': request.POST.get( 'fdob' ),
                        'fage': request.POST.get( 'fage' ),
                        'fgen': request.POST.get( 'ffgen' ),
                        'frelation': request.POST.get( 'frelstion' ),
                        'mather': request.POST.get( 'mather' ),
                        'mdob': request.POST.get( 'mdob' ),
                        'mage': request.POST.get( 'mage' ),
                        'mgen': request.POST.get( 'mgen' ),
                        'mrelation': request.POST.get( 'mrelstion' ),
                        'cihldren1': request.POST.get( 'children1' ),
                        'c1dob': request.POST.get( 'c1dob' ),
                        'c1age': request.POST.get( 'c1age' ),
                        'c1gen': request.POST.get( 'c1gen' ),
                        'c1relation': request.POST.get( 'c1relstion' ),
                        'children2': request.POST.get( 'children2' ),
                        'c2dob': request.POST.get( 'c2dob' ),
                        'c2age': request.POST.get( 'c2age' ),
                        'c2gen': request.POST.get( 'c2gen' ),
                        'c2relation': request.POST.get( 'c2relstion' ),
                        'companyname': request.POST.get( 'companyname' ),
                        'durationfrom': request.POST.get( 'durationfrom' ),
                        'durationto': request.POST.get( 'durationto' ),
                        'joiningctc': request.POST.get( 'joiningctc' ),
                        'lctc': request.POST.get( 'lctc' ),
                        'twe': request.POST.get( 'twe' )}
        # html_tpl_path = 'templates/pdfpage.html.html'
        email_html_template = get_template(html_tpl_path).render(context_data)
        # receiver_email = user
        receiver_email = ['filtrumautocomp0214@gmail.com', 'abhishekkokate072@gmail.com', 'hr@filtrum.co.in',
                          'ranjitshinde9404@gmail.com']
        email_msg = EmailMessage('Welcome to Filtrumautocomp Pvt Ltd',
                                 email_html_template,
                                 settings.APPLICATION_EMAIL,
                                 receiver_email,
                                 reply_to=[settings.APPLICATION_EMAIL]
                                 )
        email_msg.content_subtype = 'html'
        email_msg.send(fail_silently=False)

        # verifymail1(user,c)
        return HttpResponse("data save success as well as send mail successfully")
    return render(request, 'form.html')

def logdata(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if HrLogin.objects.filter(username=username,password=password).exists():
            return redirect('form1')
        else:
            return HttpResponse("username and password is not match")
    return render(request,'login.html')

def approve(request):
    fulname = fn
    empid=num
    print(empid)
    if request.method=="POST":
        # filturm_id=request.POST.get(pk=id)
        flname = request.POST.get( 'ename' )
        emid = request.POST.get( 'eid' )
        pwd = request.POST.get( "pass" )
        print( flname, emid, pwd )
        # User(employeename=flname, ids=emid, pas=pwd).save()
        # User.objects.create_user(username=flname, password=pwd, first_name=firstname, last_name=lname)

        html_tpl_path = 'userlogin.html'
        context_data = {'name': emid,'pass': pwd}
        email_html_template = get_template( html_tpl_path ).render( context_data )

        receiver_email = user
        email_msg = EmailMessage( 'Welcome to Filtrumautocomp Pvt Ltd',
                                  email_html_template,
                                  settings.APPLICATION_EMAIL,
                                  [receiver_email],
                                  reply_to=[settings.APPLICATION_EMAIL]
                                  )
        email_msg.content_subtype = 'html'
        email_msg.send( fail_silently=False )

        return HttpResponse("send mail to employee with username and password")

    return render(request,'ids.html',{'fname':fulname,'employeeid':empid,'passw':p})


def elogin(request):
    error = ""
    fullname=""
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        print(u,p)
        user = authenticate(username=u,password=p)
        print(user)
        uid = urlsafe_base64_encode(force_bytes(user.id))
        token = PasswordResetTokenGenerator().make_token(user)
        print(uid+token)
        current_site = get_current_site(request)
        domain = current_site.domain
        link = 'http://' + domain + '/api/validate/' + uid + '/' + token
        print(link)
        # a=request.user.first_name
        # b=request.user.last_name
        # fullname=a+" "+b
        # print(fullname)
        try:
            if user:
                login(request, user)
                error = "no"

            else:
                error = "yes"
                print("not usre login")


        except:
            error = "yes"
            print("nothing")
    return render(request,'employeelogin.html',locals())



def dashbord(request):
    return render(request,'d.html')



def Logout(request):
    logout(request)
    return redirect('dashboard')

def empLeave(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    empl = Mainfilturm.objects.get(user=user)

    error = ""
    if request.method == "POST":
        la = request.POST['ap']
        ap = request.POST['apn']
        lt = request.POST['lt']
        datefrom = request.POST['df']
        dateto = request.POST['dt']
        resumeon = request.POST['ro']
        leaveday = request.POST['ldd']
        leavebalance = request.POST['lb']
        leavereason = request.POST['lr']
        try:
            EmpLeave(empl=empl, appdate=la, appname=ap, leavetype=lt, datefrom=datefrom, dateto=dateto,
                     resumeon=resumeon,
                     leaveday=leaveday, leavebalance=leavebalance, leavereason=leavereason).save()
            error = "no"
        except:
            error = "yes"
    return render(request,'leavepage.html',locals())

# def changePassword(request):
#     if not request.user.is_authenticated:
#         return redirect('user_login')
#     error = ""
#     user = request.user
#     if request.method == "POST":
#         o = request.POST['oldpassword']
#         n = request.POST['newpassword']
#         try:
#             u = User.objects.get(id=request.user.id)
#             if user.check_password(o):
#                 u.set_password(n)
#                 u.save()
#                 error = "no"
#             else:
#                 error = 'not'
#         except:
#             error = "yes"
#     return render(request, 'changePassword.html', locals())



def empleavedata(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    empl1 =Mainfilturm.objects.get(user=user)
    print(empl1)
    r=EmpLeave.objects.filter(empl=empl1)
    print(r)
    # a=r.appdate
    # b=r.appname
    # c=r.leavetype
    # d=r.datefrom
    # e=r.dateto
    # f=r.resumeon
    # g=r.leaveday
    # h=r.leavebalance
    # i=r.leavereason

    # print(r.appdate,r.appname,r.leavetype,r.datefrom,r.dateto,r.resumeon,r.leaveday)
    return render(request,'datashow.html',{'r':r})

def punchdata(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    empl1 = Mainfilturm.objects.get(user=user)
    return render(request,'punchpage.html')

