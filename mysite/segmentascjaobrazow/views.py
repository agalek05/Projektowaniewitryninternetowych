from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserProfileForm
from .models import UserProfile


def uploadingphoto(request):
    if request.method == 'POST':
        # Obsługa LOGOWANIA (jeśli użytkownik przesyła dane tekstowe logowania)
        if 'username' in request.POST and 'password' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('/segmentascjaobrazow/')

        # Obsługa UPLOADU (jeśli użytkownik jest zalogowany i przesyła plik)
        elif request.user.is_authenticated and 'photo' in request.FILES:
            form = UserProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('/segmentascjaobrazow/')

    # Przygotowanie struktur danych dla żądania GET
    form = UserProfileForm()
    login_form = AuthenticationForm()
    zdjecia = UserProfile.objects.all()

    return render(request, 'index.html', {
        'form': form,
        'login_form': login_form,
        'zdjecia': zdjecia
    })
