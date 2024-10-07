from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,"index.html")

def userreg(request):
    if request.POST:
        username1=request.POST['username']
        email1=request.POST['email']
        phonenumber1=request.POST['phoneno']
        password1=request.POST['password']
        image1=request.FILES['image']
        address1=request.POST['address']
        if User.objects.filter(Email=email1).exists():
            messages.info(request,"Already Have Registered")
        else:
            user=Login.objects.create_user(
            username=email1,password=password1,usertype='user',viewPassword=password1,is_active=0)
            user.save()
            register=User.objects.create(
            Username=username1,Email=email1,Phonenumber=phonenumber1,Password=password1,Image=image1,Address=address1,user=user)
            register.save()
            messages.info(request,"Registered Successfully")
            return redirect("/login")
    return render(request,"userreg.html")

def ambassadorreg(request):
    if request.POST:
        username1=request.POST['username1']
        email1=request.POST['email1']
        phonenumber1=request.POST['phoneno1']
        password1=request.POST['password1']
        image1=request.FILES['image1']
        address1=request.POST['address1']
        if Ambassador.objects.filter(Email=email1).exists():
            messages.info(request,"Already Have Registered")
        else:
            ambassador=Login.objects.create_user(
            username=email1,password=password1,usertype='ambassador',viewPassword=password1,is_active=0)
            ambassador.save()
            register1=Ambassador.objects.create(
            Username=username1,Email=email1,Phonenumber=phonenumber1,Password=password1,Image=image1,Address=address1,ambassador=ambassador)
            register1.save()
            messages.info(request,"Registered Successfully")
            return redirect("/login")
    return render(request,"ambassadorreg.html")

def guidereg(request):
    if request.POST:
        username1=request.POST['username3']
        email1=request.POST['email3']
        phonenumber1=request.POST['phoneno3']
        password1=request.POST['password3']
        image1=request.FILES['image3']
        address1=request.POST['address3']
        if Guide.objects.filter(Email=email1).exists():
            messages.info(request,"Already Have Registered")
        else:
            guide=Login.objects.create_user(
            username=email1,password=password1,usertype='guide',viewPassword=password1,is_active=0)
            guide.save()
            register2=Guide.objects.create(
            Username=username1,Email=email1,Phonenumber=phonenumber1,Password=password1,Image=image1,Address=address1,guide=guide)
            register2.save()
            messages.info(request,"Registered Successfully")
            return redirect("/login")
    return render(request,"guidereg.html")

def login(request):
    if request.POST:
        Email2=request.POST['email2']
        Password2=request.POST['password2']
        user=authenticate(username=Email2,password=Password2)
        if user is not None:
            if user.usertype=="admin":
                messages.info(request,"Welcome To The Admin Page")
                return redirect("/adminhome")
            elif user.usertype=="user":
                request.session['uid']=user.id
                messages.info(request,"Welcome To The User Page")
                return redirect("/userhome")
            elif user.usertype=="ambassador":
                request.session['uid']=user.id
                messages.info(request,"Welcome To The Ambassador Page")
                return redirect("/ambassadorhome")
            elif user.usertype=="guide":
                request.session['uid']=user.id
                messages.info(request,"Welcome To The Guide Page")
                return redirect("/guidehome")
            else:
                messages.info(request,"Invalid Username Or Password")
                return redirect("/login")
        else:
            messages.info(request,"Invalid Username Or Password")
            return redirect("/login")
    return render(request,"login.html")

def adminhome(request):
    return render(request,'Admin/adminhome.html')

def userhome(request):
    return render(request,'User/userhome.html')

def ambassadorhome(request):
    return render(request,'Ambassador/ambassadorhome.html')

def guidehome(request):
    return render(request,'Guide/guidehome.html')

def viewuser(request):
    data=User.objects.all()
    return render(request,"Admin/viewusers.html",{"data":data})

def actionuser(request):
    status=request.GET['status']
    id=request.GET['id']
    wor=Login.objects.get(id=id)
    wor.is_active=int(status)
    wor.save()
    if status == '1':
        messages.info(request," Approved successfully")
    return redirect("/viewuser")

def rejectuser(request):
    id=request.GET.get('id')
    b=User.objects.filter(id=id).delete()
    e=Login.objects.filter(id=id).delete()
    messages.info(request,"Rejected successfully")
    return redirect("/viewuser")

def deleteuser(request):
    id=request.GET['id']
    s=User.objects.filter(id=id)
    s.delete()
    messages.info(request,"User Deleted Successfully")
    return redirect("/viewuser")

def viewambassador(request):
    data=Ambassador.objects.all()
    return render(request,"Admin/viewambassador.html",{"data":data})

def actionambassador(request):
    status=request.GET['status']
    id=request.GET['id']
    wor=Login.objects.get(id=id)
    wor.is_active=int(status)
    wor.save()
    if status == '1':
        messages.info(request," Approved successfully")
    return redirect("/viewambassador")

def rejectambassador(request):
    id=request.GET.get('id')
    b=Ambassador.objects.filter(id=id).delete()
    e=Login.objects.filter(id=id).delete()
    messages.info(request,"Rejected successfully")
    return redirect("/viewambassador")

def deleteambassador(request):
    id=request.GET['id']
    s=Ambassador.objects.filter(id=id)
    s.delete()
    messages.info(request,"Ambassador Deleted Successfully")
    return redirect("/viewambassador")

def viewguide(request):
    data=Guide.objects.all()
    return render(request,"Admin/viewguides.html",{"data":data})

def actionguide(request):
    status=request.GET['status']
    id=request.GET['id']
    wor=Login.objects.get(id=id)
    wor.is_active=int(status)
    wor.save()
    if status == '1':
        messages.info(request," Approved successfully")
    return redirect("/viewguide")

def rejectguide(request):
    id=request.GET.get('id')
    b=Guide.objects.filter(id=id).delete()
    e=Login.objects.filter(id=id).delete()
    messages.info(request,"Rejected successfully")
    return redirect("/viewguide")

def deleteguide(request):
    id=request.GET['id']
    s=Guide.objects.filter(id=id)
    s.delete()
    messages.info(request,"Guide Deleted Successfully")
    return redirect("/viewguide")

def addevent(request):
    uid = request.session['uid']
    ambassador = Ambassador.objects.get(ambassador=uid)
    if request.POST:
        name1=request.POST['event']  
        date1=request.POST['date']  
        image1=request.FILES['eimage']  
        des1=request.POST['des']  
        dis1=request.POST['dis']  
        data=Event.objects.create(name=name1,date=date1,image=image1,des=des1,dis=dis1,ambassador=ambassador)
        data.save()
        messages.info(request,"Added Successfully")
    return render(request,"Ambassador/addevents.html")

def viewevents(request):
    data=Event.objects.all()
    return render(request,"Admin/viewevents.html",{"data":data})

def viewevent(request):
    data=Event.objects.all()
    return render(request,"User/viewevent.html",{"data":data})

def view_event(request):
    data=Event.objects.all()
    return render(request,"Ambassador/viewevents.html",{"data":data})

def bookevent(request):
    uid = request.session['uid']
    user = User.objects.get(user=uid)
    eid=request.GET.get('id')
    event=Event.objects.get(id=eid)
    guide=Guide.objects.all()
    if request.POST:
        guide1=request.POST['guides']   
        datet1=request.POST['datet']  
        dist1=request.POST['dist'] 
        guides = Guide.objects.get(id=guide1)  
        data=Book.objects.create(date=datet1,dist=dist1,guide=guides,user=user,event=event)
        data.save()
        messages.info(request,"Added Successfully")
        return redirect('/viewevent')
    return render(request,"User/bookevent.html",{'guide':guide})

def viewbook_event(request):
    uid=request.session['uid']
    guide=Guide.objects.get(guide=uid)
    data=Book.objects.filter(guide=guide)
    return render(request,"Guide/viewbook_event.html",{"data":data})

def actionbook(request):
    id=request.GET['id']
    if request.POST:
        rate1=request.POST['rate']
        m=Book.objects.filter(id=id).update(rate=rate1,status='Approved')
        messages.info(request,"Rate Add And Approved Successfully")
        return redirect("/viewbook_event")
    return render(request,"Guide/addrate.html")

def rejectbook(request):
    id=request.GET['id']
    r=Book.objects.filter(id=id).update(status='Rejected')
    messages.info(request,"Rejected Successfully")
    return redirect("/viewbook_event")

def deletebook(request):
    id=request.GET['id']
    s=Book.objects.filter(id=id)
    s.delete()
    messages.info(request,"Book Event Deleted Successfully")
    return redirect("/viewbook_event")

def viewbook_events(request):
    uid=request.session['uid']
    user=User.objects.get(user=uid)
    data=Book.objects.filter(user=user)
    return render(request,"User/viewbook_event.html",{"data":data})

def addpay(request):
    id=request.GET['id']
    uid = request.session['uid']
    user = User.objects.get(user=uid)
    if request.method == 'POST':
        payment = Book.objects.filter(id=id).update(user=user,status='Paid')
        messages.info(request,"Paid successfully")
        return redirect('/viewbook_events')
    return render(request, "User/addpayment.html")

def viewevent_book(request):
    data=Book.objects.all()
    return render(request,"Admin/viewevent_book.html",{"data":data})

def addarticle(request):
    uid = request.session['uid']
    ambassador = Ambassador.objects.get(ambassador=uid)
    if request.POST:
        name1=request.POST['name']  
        image1=request.FILES['image']  
        des1=request.POST['des']   
        data=Article.objects.create(name=name1,image=image1,des=des1,ambassador=ambassador)
        data.save()
        messages.info(request,"Added Successfully")
    return render(request,"Ambassador/addarticles.html")

def viewarticle(request):
    uid = request.session['uid']
    ambassador = Ambassador.objects.get(ambassador=uid)
    data=Article.objects.filter(ambassador=ambassador)
    return render(request,"Ambassador/viewarticles.html",{"data":data})

def update(request):
    uid = request.session["uid"]
    ambassador = Ambassador.objects.get(ambassador=uid)
    id=request.GET.get("id")
    data=Article.objects.filter(id=id)
    if request.POST:
        name1=request.POST['name']  
        image1=request.FILES['image']  
        des1=request.POST['des']  
        update = Article.objects.get(id=id)
        update.name = name1
        update.image = image1
        update.des = des1
        update.save()
        messages.info(request,"Update Successfully")
        return redirect("/viewarticle")
    return render(request,'Ambassador/update.html',{'data':data})

def delete(request):
    id=request.GET['id']
    s=Article.objects.filter(id=id)
    s.delete()
    messages.info(request,"Deleted Successfully")
    return redirect("/viewarticle")

def addarticle_u(request):
    uid = request.session['uid']
    user = User.objects.get(user=uid)
    if request.POST:
        name2=request.POST['name1']  
        image2=request.FILES['image1']  
        des2=request.POST['des1']   
        data=Article.objects.create(name=name2,image=image2,des=des2,user=user)
        data.save()
        messages.info(request,"Added Successfully")
    return render(request,"User/addarticles.html")

def viewarticle_u(request):
    uid = request.session['uid']
    user = User.objects.get(user=uid)
    data=Article.objects.filter(user=user)
    return render(request,"User/viewarticles.html",{"data":data})

def viewarticles(request):
    id=request.GET.get('id')
    data = Article.objects.filter(user=id)
    return render(request, "User/viewall_articles.html", {"data": data})

def viewarticle_am(request):
    uid = request.session['uid']
    ambassador = Ambassador.objects.get(ambassador=uid)
    data=Article.objects.exclude(ambassador=ambassador)
    return render(request, "Ambassador/viewall_articles.html", {"data": data})

def update_u(request):
    uid = request.session["uid"]
    user = User.objects.get(user=uid)
    id=request.GET.get("id")
    data=Article.objects.filter(id=id)
    if request.POST:
        name2=request.POST['name1']  
        image2=request.FILES['image1']  
        des2=request.POST['des1']  
        update1 = Article.objects.get(id=id)
        update1.name = name2
        update1.image = image2
        update1.des = des2
        update1.save()
        messages.info(request,"Update Successfully")
        return redirect("/viewarticle_u")
    return render(request,'User/update.html',{'data':data})

def delete_u(request):
    id=request.GET['id']
    s=Article.objects.filter(id=id)
    s.delete()
    messages.info(request,"Deleted Successfully")
    return redirect("/viewarticle_u")

def feedback(request):
    uid = request.session['uid']
    user = User.objects.get(user=uid)
    id=request.GET.get("id")
    ambassador=Ambassador.objects.get(id=id)
    aid=request.GET.get("id")
   # article=Article.objects.get(id=aid)
    if request.POST:
        message=request.POST['msg']  
        data=Feedback.objects.create(message=message,user=user,ambassador=ambassador)
        data.save()
        messages.info(request,"Feedback Added Successfully")
        return redirect('/viewarticles')
    return render(request,"User/addfeedback.html")

def viewfeedback(request):
    uid = request.session['uid']
    ambassador = Ambassador.objects.get(ambassador=uid)
    data=Feedback.objects.filter(ambassador=ambassador)
    return render(request,"Ambassador/viewfeedback.html",{"data":data})

def addreply(request): 
    id = request.GET.get("id")
    if request.method == 'POST':
        message1 = request.POST['msg1']  
        feedback = Feedback.objects.filter(id=id).update(reply=message1, status="replied")
        messages.info(request,"Reply Added Successfully")
        return redirect('/viewfeedback')
    return render(request, "Ambassador/addreply.html")

def viewfeedback_u(request):
    uid = request.session['uid']
    user = User.objects.get(user=uid)
    data=Feedback.objects.filter(user=user)
    return render(request,"User/viewfeedback.html",{"data":data})

def addservice(request):
    uid = request.session['uid']
    guide = Guide.objects.get(guide=uid)
    # id=request.GET.get("id")
    # user=User.objects.filter(id=id)
    if request.POST:
        cname1=request.POST['cname']  
        sdate1=request.POST['sdate']  
        edate1=request.POST['edate']  
        dis1=request.POST['dis']  
        image1=request.FILES['img']  
        rate1=request.POST['rate']  
        # food1=request.POST['food']  
        data=Service.objects.create(name=cname1,sdate=sdate1,edate=edate1,dis=dis1,image=image1,rate=rate1,guide=guide)
        data.save()
        messages.info(request,"Added Successfully")
    return render(request,"Guide/addservice.html")

def viewservice(request):
    uid = request.session['uid']
    guide = Guide.objects.get(guide=uid)
    data = Service.objects.filter(guide=guide)
    return render(request, "Guide/viewservice.html", {"data": data})

def update_s(request):
    uid = request.session["uid"]
    guide = Guide.objects.get(guide=uid)
    id=request.GET.get("id")
    data=Service.objects.filter(id=id)
    if request.POST:
        cname1=request.POST['cname']  
        sdate1=request.POST['sdate']  
        edate1=request.POST['edate']  
        dis1=request.POST['dis']  
        image1=request.FILES['img']  
        rate1=request.POST['rate']  
        # food1=request.POST['food'] 
        update2 = Service.objects.get(id=id)
        update2.name = cname1
        update2.image = image1
        update2.dis = dis1
        update2.sdate = sdate1
        update2.edate = edate1
        update2.rate = rate1
        # update2.food = food1
        update2.save()
        messages.info(request,"Update Successfully")
        return redirect("/viewservice")
    return render(request,'Guide/update.html',{'data':data})

def delete_s(request):
    id=request.GET['id']
    s=Service.objects.filter(id=id)
    s.delete()
    messages.info(request,"Deleted Successfully")
    return redirect("/viewservice")

def viewservices(request):
    id=request.GET.get('id')
    data = Service.objects.filter(guide=id)
    return render(request, "User/viewservices.html", {"data": data})

def bookservice_u(request):
    uid = request.session['uid']
    user = User.objects.get(user=uid)
    id = request.GET.get('id')
    service = Service.objects.get(id=id)
    booking = Booking.objects.create(user=user, service=service, status='Booked')
    booking.save()
    print(booking)
    messages.info(request, "Booked")
    return redirect("/viewservices")

def viewservice_g(request):
    uid=request.session['uid']
    guide=Guide.objects.get(guide=uid)
    data=Booking.objects.filter(service__guide=guide)
    return render(request, "Guide/viewbook_service.html", {"data": data})

def acs(request):
    id=request.GET['id']
    r=Booking.objects.filter(id=id).update(status='Approved')
    messages.info(request,"Successfully")
    return redirect("/viewservice_g")

def rejs(request):
    id=request.GET.get('id')
    t=Booking.objects.filter(id=id).delete()
    u=Login.objects.filter(id=id).delete()
    messages.info(request,"Rejected successfully")
    return redirect("/viewservice_g")

def viewservice_book(request):
    uid=request.session['uid']
    user=User.objects.get(user=uid)
    data=Booking.objects.filter(user=user)
    return render(request,"User/viewservice_book.html",{"data":data})

def addpay_g(request):
    id=request.GET['id']
    uid = request.session['uid']
    user = User.objects.get(user=uid)
    if request.method == 'POST':
        payment1 = Booking.objects.filter(id=id).update(user=user,status='Paid')
        messages.info(request,"Paid successfully")
        return redirect('/viewservice_book')
    return render(request, "User/addpayment_u.html")

def addevent_ad(request):
    if request.POST:
        # ename1=request.POST['ename']  
        name1=request.POST['name']  
        date1=request.POST['date']  
        dis1=request.POST['dis']  
        image1=request.FILES['image']  
        des1=request.POST['des']  
        # fee1=request.POST['fee']  
        data=Events.objects.create(name=name1,date=date1,dis=dis1,image=image1,des=des1)
        data.save()
        messages.info(request,"Added Successfully")
    return render(request,"Admin/addevents.html")

def viewevent_ad(request):
    data = Events.objects.all()
    return render(request, "Admin/viewevent_ad.html", {"data": data})

def update_ad(request):
    id=request.GET.get("id")
    data=Events.objects.filter(id=id)
    if request.POST:
        # ename1=request.POST['ename']  
        name1=request.POST['name']  
        date1=request.POST['date']  
        dis1=request.POST['dis']  
        image1=request.FILES['image']  
        des1=request.POST['des']  
        # fee1=request.POST['fee']  
        update3 = Events.objects.get(id=id)
        # update3.ename = ename1
        update3.image = image1
        update3.date = date1
        update3.dis = dis1
        update3.name = name1
        update3.des = des1
        # update3.fee = fee1
        update3.save()
        messages.info(request,"Update Successfully")
        return redirect("/viewevent_ad")
    return render(request,'Admin/update.html',{'data':data})

def delete_ad(request):
    id=request.GET['id']
    s=Events.objects.filter(id=id)
    s.delete()
    messages.info(request,"Deleted Successfully")
    return redirect("/viewevent_ad")

def viewevent_u(request):
    data = Events.objects.all()
    return render(request, "User/viewevents.html", {"data": data})

def bookevent_u(request):
    uid = request.session['uid']
    user = User.objects.get(user=uid)
    id = request.GET.get('id')
    events = Events.objects.get(id=id)
    reg = Registered.objects.create(user=user, events=events, status='Registered')
    reg.save()
    print(reg)
    messages.info(request, "Registered")
    return redirect("/viewevent_u")

def viewbook_event_u(request):
    data = Registered.objects.filter(status='Registered')
    return render(request, "Admin/viewbooking_event.html", {"data": data})

def approve_a(request):
    id=request.GET['id']
    r=Registered.objects.filter(id=id).update(status='Approved')
    messages.info(request,"Successfully")
    return redirect("/viewbook_event_u")

def reject_a(request):
    id=request.GET.get('id')
    t=Registered.objects.filter(id=id).delete()
    u=Login.objects.filter(id=id).delete()
    messages.info(request,"Rejected successfully")
    return redirect("/viewbook_event_u")

def viewpar_event(request):
    uid=request.session['uid']
    user=User.objects.get(user=uid)
    data=Registered.objects.filter(user=user)
    return render(request,"User/viewpartici_event.html",{"data":data})

def addpay_u(request):
    id=request.GET['id']
    uid = request.session['uid']
    user = User.objects.get(user=uid)
    if request.method == 'POST':
        payment = Events.objects.filter(id=id).update(user=user,status='Paid')
        messages.info(request,"Paid successfully")
        return redirect('/viewpar_event')
    return render(request, "User/addpayment_u.html")

def chat(request):
    uid = request.session["uid"]
    # Guides
    name=""
    guideData = Guide.objects.all()
    id = request.GET.get("id")
    getChatData = Chat.objects.filter(Q(uid__user=uid) & Q(guideid=id))
    current_time = datetime.now().time()
    formatted_time = current_time.strftime("%H:%M")
    userid = User.objects.get(user__id=uid)
    if id:
        guideid = Guide.objects.get(id=id)
        name=guideid.Username
    if request.POST:
        message = request.POST["message"]
        sendMsg = Chat.objects.create(uid=userid,message=message,guideid=guideid,time=formatted_time,utype="USER")
        sendMsg.save()
    return render(request,"User/chat.html",{"guideData": guideData, "getChatData": getChatData,"guideid":name})

def reply(request):
    aid = request.session["uid"]
    print(aid)
    name=""
    userData = User.objects.all()
    id = request.GET.get("id")
    getChatData = Chat.objects.filter(Q(guideid__guide=aid) & Q(uid=id))
    print(getChatData)
    current_time = datetime.now().time()
    formatted_time = current_time.strftime("%H:%M")
    guideid = Guide.objects.get(guide__id=aid)
    if id:
        userid = User.objects.get(id=id)
        name=userid.Username
    if request.POST:
        message = request.POST["message"]
        sendMsg = Chat.objects.create(uid=userid,message=message,guideid=guideid,time=formatted_time,utype="GUIDE")
        sendMsg.save()
    return render(request,"Guide/chat.html",{"userData": userData, "getChatData": getChatData,"userid":name})

def viewguide_u(request):
    data = Guide.objects.all()
    return render(request, "User/viewguides.html", {"data": data})

def chat_u(request):
    uid = request.session["uid"]
    # Guides
    name=""
    ambassadorData = Ambassador.objects.all()
    id = request.GET.get("id")
    getChatData = Chats.objects.filter(Q(uid__user=uid) & Q(ambassadorid=id))
    current_time = datetime.now().time()
    formatted_time = current_time.strftime("%H:%M")
    userid = User.objects.get(user__id=uid)
    if id:
        ambassadorid = Ambassador.objects.get(id=id)
        name=ambassadorid.Username
    if request.POST:
        message = request.POST["message"]
        sendMsg = Chats.objects.create(uid=userid,message=message,ambassadorid=ambassadorid,time=formatted_time,utype="USER")
        sendMsg.save()
    return render(request,"User/chat_u.html",{"ambassadorData": ambassadorData, "getChatData": getChatData,"ambassadorid":name})

def reply_a(request):
    gid = request.session["uid"]
    print(gid)
    name=""
    userData1 = User.objects.all()
    id = request.GET.get("id")
    getChatData = Chats.objects.filter(Q(ambassadorid__ambassador=gid) & Q(uid=id))
    print(getChatData)
    current_time = datetime.now().time()
    formatted_time = current_time.strftime("%H:%M")
    ambassadorid = Ambassador.objects.get(ambassador__id=gid)
    if id:
        userid1 = User.objects.get(id=id)
        name=userid1.Username
    if request.POST:
        message = request.POST["message"]
        sendMsg = Chats.objects.create(uid=userid1,message=message,ambassadorid=ambassadorid,time=formatted_time,utype="AMBASSADOR")
        sendMsg.save()
    return render(request,"Ambassador/chat_a.html",{"userData1": userData1, "getChatData": getChatData,"userid1":name})