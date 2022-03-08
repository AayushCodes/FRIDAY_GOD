from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
    now = datetime.today().strftime('%A')
    return render (request, "FRIDAY_CHECKER/index.html", {
        "friday": now == "Friday"
    })
    