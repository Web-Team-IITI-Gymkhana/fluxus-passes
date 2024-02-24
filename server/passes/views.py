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
        context = "You have requested a pass on " + str(pass_requested.requested_at)
    elif(pass_issued):
        context = "You have been issued a pass on " + str(pass_issued.issued_at)
    else:
        if(request.method == "POST"):
            PassRequested.objects.create(email=email)
            context = "Pass requested successfully"
    return render(request, "home.html", {"context": context})