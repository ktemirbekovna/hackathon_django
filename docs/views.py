from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, template_name='docs/index.html')
def memorial(request):
    return render(request, template_name='docs/memorial.html')
def olc(request):
    return render(request, template_name='docs/olc.html')
def desert(request):
    return render(request, template_name='docs/desert.html')



