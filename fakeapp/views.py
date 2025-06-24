from django.shortcuts import render,redirect
from django.urls import reverse
from .models import AdminModel, UserModel, PostModel

# Create your views here.

def main(request):
    posts = PostModel.objects.select_related('user').order_by('-created_at')
    return render(request, 'main.html', {'posts': posts})

def create_post(request):
    if request.method == "POST":
        content = request.POST.get("content")
        image = request.FILES.get("image")
        user_email = request.session.get("user_emailId")

        if user_email and content:
            user = UserModel.objects.get(EmailId=user_email)
            PostModel.objects.create(user=user, content=content, image=image)
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        fname = request.POST.get("FirstName")
        lname = request.POST.get("LastName")
        email = request.POST.get("EmailId")
        phone = request.POST.get("PhoneNo")
        password = request.POST.get("Password")

        if UserModel.objects.filter(EmailId=email).exists():
            return render(request, "regi.html", {"error": "Email already registered."})
        
        UserModel.objects.create(
            FirstName=fname,
            LastName=lname,
            EmailId=email,
            PhoneNo=phone,
            Password=password  # You should hash this in production
        )
        return redirect("")  # or wherever you want to go

    return render(request, "regi.html")




# Login
def login(request):
    passinc = 0  # Password incorrect attempt counter
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = UserModel.objects.filter(EmailId=email).first()
        admin = AdminModel.objects.filter(adminEmailId=email).first()

        if user:
            if password == user.Password:
                request.session['User_name'] = user.FirstName
                request.session['user_emailId'] = user.EmailId
                return redirect('home')
            else:
                passinc += 1
                error_message = 'Incorrect password for user.'
        elif admin:
            if password == admin.adminPassword:
                request.session['admin_name'] = admin.adminName
                request.session['adminemail'] = admin.adminEmailId
                return redirect('dashboard')
            else:
                passinc += 1
                error_message = 'Incorrect password for admin.'
        else:
            error_message = 'User not found.'

        return render(request, 'login.html', {'error': error_message, 'passinc': passinc})

    return render(request, 'login.html', {'passinc': passinc})

def logout(request):
    session_key=list(request.session.keys())
    for key in session_key:
        del request.session[key]
    return redirect('')


def dashboard(request):
    context = {
        'total_users': UserModel.objects.count(),
        'total_posts': PostModel.objects.count(),
        'online_admins': AdminModel.objects.count(), 
        'recent_posts': PostModel.objects.order_by('-created_at')[:5], 
    }
    return render(request, 'admin.html', context)

