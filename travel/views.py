from django.shortcuts import render
from .models import travelmodel
from django.core.paginator import Paginator

# def fullpost(request,slug):
#     slugpost = technologymodel.objects.get(new_slug = slug)
#     data = {
#         "slugpost": slugpost,
#     }       
#     return render(request,"fullpost.html",data)

def allpost(request):
    allpostdata = travelmodel.objects.all()
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
        "categoriname":"travel",
        "page_of_num":page_of_num,
    }
    return render(request,"allpost.html",data)



