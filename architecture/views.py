from django.shortcuts import render
from .models import architecturemodel
from django.core.paginator import Paginator

# def homepage(request):
#     architecture_one = architecturemodel.objects.all()[:3]
#     architecture_two = architecturemodel.objects.all()[3:5]
#     architecture_three = architecturemodel.objects.all()[5:8]
#     categori = architecturemodel.objects.all()[0]
    
#     data = {
#         "data" : architecture_one,
#         "postthree": architecture_two,
#         "postfour_five":architecture_three,
#         "categori" :categori,
        
#     }
#     return render(request,"categoripage.html",data)

# def fullpost(request,slug):
#     slugpost = architecturemodel.objects.get(new_slug = slug)
#     # print(slugpost ,"myslug")
#     data = {
#         "slugpost": slugpost
#     } 
#     return render(request,"fullpost.html",data)

def allpost(request):
    
    allpostdata = architecturemodel.objects.all()
    paginator = Paginator(allpostdata,7)
    page_number = request.GET.get("page")
    finaldata = paginator.get_page(page_number)
    page_of_num = finaldata.paginator.num_pages
    minusnumber = finaldata.number-1
    plusnumber = finaldata.number+1
    # print(minusnumber)
    # categori = architecturemodel.objects.all()[0]
    data = {
        "finaldata":finaldata,
        "plusnumber":plusnumber,
        "minusnumber":minusnumber,
        "page_of_num":page_of_num,
        "categoriname":"architecture"
        
    }
    return render(request,"allpost.html",data)

# Create your views here.
