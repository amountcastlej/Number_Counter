from django.shortcuts import render, redirect

def index(request):
    if 'counter1' not in request.session:
        request.session['counter1'] = 0
    if 'counter2' not in request.session:
        request.session['counter2'] = 0
    if 'counter3' not in request.session:
        request.session['counter3'] = 0
    return render(request, 'index.html')

def click_button(request):
    request.session['counter' + request.POST['choice']] += 1
    return redirect('/')

def reset_counter(request):
    request.session.flush()
    return redirect('/')

# Create your views here.
