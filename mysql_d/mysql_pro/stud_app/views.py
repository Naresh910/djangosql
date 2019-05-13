from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib import auth

#Student register form
def index(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            uid=form.cleaned_data['uid']
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            branch=form.cleaned_data['branch']
            password=form.cleaned_data['password']
            # image=form.cleaned_data['image']
            image = request.FILES['image']

            # newdoc = Register_model(image=request.FILES['image'])

            saveData=Register_model(uid=uid,name=name,email=email,branch=branch,password=password,image=image)
            saveData.save()
            messages.success(request,"Registeration successfully")
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render(request, 'index.html', {'form': form})

#all Record show
def showData(request):
    if request.session.has_key('user_id'):
        show=Register_model.objects.all()
        return render(request,'viewRecord.html',{'data':show})
    else:
        return redirect(login)

#particular user edit

def editShow(request,id):
    stud=Register_model.objects.get(id=id)
    return render(request,'editShow.html',{'stud':stud})

#update record
def update(request,id):
    stud=Register_model.objects.get(id=id)
    name=request.POST['name']
    email=request.POST['email']
    uid=request.POST['uid']
    stud.name = name
    stud.email=email
    stud.uid=uid
    stud.save()
    return redirect('/showData')


#delete record
def delete_record(request,id):
    stud=Register_model.objects.get(id=id)
    stud.delete()
    return redirect("/showData")

#Login Form

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            uid=form.cleaned_data['uid']
            password=form.cleaned_data['password']
            try:
                m=Register_model.objects.get(uid=uid,password=password)
                request.session['user_id'] = m.id
                k=request.session['user_id']
                print("welcome",k)
                return HttpResponseRedirect('showData')

            except Exception:
                print("invalid")
            messages.error(request, 'username and password does not exit')
            return HttpResponseRedirect('login')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})


#Logout User
def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect(login)



def join_stud(request):
    d=Register_model.objects.all()
    data=d.Student_d.all()
    return render(request,"join_stud.html",{'data':data})








