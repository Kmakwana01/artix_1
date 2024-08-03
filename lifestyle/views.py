from django.shortcuts import render
from .models import lifestylemodel
from django.core.paginator import Paginator


def allpost(request):
      
    allpostdata = lifestylemodel.objects.all()
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
         "categoriname":"lifestyle"
        
    }
    return render(request,"allpost.html",data)



