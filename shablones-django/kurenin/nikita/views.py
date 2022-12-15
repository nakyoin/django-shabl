from django.shortcuts import render

def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def contacts(request):
    data = {"name": "Телефон: +79655851558", "message": "email: nkurenin@inbox.ru", "status": "ABCD123"}
    return render(request, "contacts.html", context=data)
def form(request):
    return render(request, "form.html")
