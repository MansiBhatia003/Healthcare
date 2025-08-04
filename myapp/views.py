from django.shortcuts import render,redirect
from myapp.models import userregister

# Create your views here.

def login(request):
    if request.method == "POST":
        Us = request.POST.get('username')
        Pw = request.POST.get('password')
        try:
            user = userregister.objects.get(Username=Us, Password=Pw)
            # Store unique identifier
            request.session['user_id'] = user.id
            return redirect('dashboard')  # Use redirect instead of render
        except userregister.DoesNotExist:
            return render(request, 'login.html', {'msg': 1})
    else:
        return render(request, 'login.html')
def signup(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cPassword=request.POST.get('cpassword')
        picture = request.FILES.get('image')
        address=request.POST.get('address')
        print("Received Data:", username, email, password, cPassword,picture)
        if password == cPassword:
            if userregister.objects.filter(Email=email).exists():
                return render(request,'register.html',{'msg':2})
            else:
                x=userregister()
                x.Firstname=firstname
                x.Lastname=lastname
                x.Username= username
                x.Email= email
                x.Password=password
                x.CPassword=cPassword
                x.picture=picture
                x.Address=address
                x.save()
                return render(request,'signup.html',{'msg':3})
        else:
            return render(request,'signup.html',{'msg':1})
    else:
        return render(request,'signup.html')
def dashboard(request):
    user = request.session.get('Username')
    if user:
        user = userregister.objects.get(Username=request.session.get('Username'))
        return render(request, 'dashboard.html', {'user': user})
    else:
        return redirect('Login')
def start(request):
    return render(request,'start.html')
