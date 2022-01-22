from django.shortcuts import render

from teacher.models import CourseMaterial

# Create your views here.
def index(request):
    if request.method == "POST":

        post=CourseMaterial.objects
        post.create(
        title = request.POST.get('title'),
        description = request.POST.get('des'),
        file = request.FILES.get('datafile'),
        link = request.POST.get('link'),
        prize = request.POST.get('prize'),
        domain_bucket = request.POST.get('dombuck'),
        # technology = request.POST.get('tech'),
        )
    
    post_data = CourseMaterial.objects
    context = {
        "post_data": post_data
    }

    return render(request, "ps_creator.html", context)


def viewcourse(request):
    post_data = CourseMaterial.objects.all()
    context = {
        "post_data": post_data
    }

    return render(request,"view_course.html", context)