from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import get_user_model

def registerView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect(request, 'register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('index')
        else:
            messages.info(request, 'Password not Matching')
            return redirect('register')
    else:
        return render(request, 'account/register.html')

def loginView(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('register')
    else:
        return render(request, 'account/register.html')































# def register(request):
#     form = CreateUserForm()
#
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('first_name')
#             messages.success(request, 'Your user successfully created' + user)
#             return redirect('login')
#     context = {'form': form}
#     return render(request, 'register.html', context)


# class SignUpView(CreateView):
#     model = User
#     form_class = RegisterForm
#     template_name = 'account/register.html'
#     success_url = reverse_lazy('index')
#
#     def form_valid(self, form):
#         form.save()
#         # send_success_email.delay(form.instance.email)
#         return super().form_valid(form)



# def loginPage(request):
#     if request.user.is_authenticated:
#         return redirect('index')
#     else:
#         if request.method == 'POST':
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             user = authenticate(request, email=email, password=password)
#
#             if user is not None:
#                 login(request, user)
#                 return redirect('index')
#             else:
#                 messages.info(request, 'Email or Password incorrect')
#
#     context = {}
#     return render(request, 'account/login.html', context)
#
#
# def logoutPage(request):
#     logout(request)
#     return redirect('index')




# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'registration completed successfully')
#             return redirect('booking/index.html')
#         else:
#             messages.error(request, 'registration error')
#     else:
#         form = UserCreationForm()
#     return render(request, 'account/register.html', {'form':form})

# def login(request):
#     return render(request, 'account/login.html')
