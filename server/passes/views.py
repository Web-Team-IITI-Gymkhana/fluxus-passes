from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import PassIssued, PassRequested

# Create your views here.

@login_required
def home(request):
    email = request.user.email
    pass_requested = PassRequested.objects.filter(email=email).first()
    pass_issued = PassIssued.objects.filter(email=email).first()
    context=""
    if(pass_requested):
        date_time = pass_requested.requested_at.strftime("%d-%m-%Y %H:%M:%S")
        context = "You have requested a pass on " + str(date_time)
    elif(pass_issued):
        date_time = pass_issued.issued_at.strftime("%d-%m-%Y %H:%M:%S")
        context = "You have been issued a pass on " + str(date_time)
    else:
        if(request.method == "POST"):
            PassRequested.objects.create(name=request.user.first_name, email=request.user.email)
            requested_pass_time = PassRequested.objects.filter(email=email).first().requested_at.strftime("%d-%m-%Y %H:%M:%S")
            context = "You have requested a pass on " + str(requested_pass_time)
    return render(request, "home.html", {"context": context})