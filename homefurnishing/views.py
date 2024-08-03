from django.shortcuts import render
from .models import homefurnishing
# from architecture.models import architecturemodel
from django.core.paginator import Paginator

# def homefurnishingfun(request):
#     homefurnishingdata = homefurnishing.objects.all()[:2]
#     postthree = homefurnishing.objects.all()[2:3]
#     postfour_five = homefurnishing.objects.all()[3:5]
#     all_post = homefurnishing.objects.all()[5:9]

#     data = {
#         "data" : homefurnishingdata,
#         "postthree": postthree,
#         "postfour_five":postfour_five,
#         "all_post": all_post
#     }    
#     return render(request ,"categoripage.html",data) 

# def fullpost(request):
#     slugpost = homefurnishing.objects.get(new_slug = slug)
#     print("hii")
#     data = {
#         "slugpost": slugpost,
#     } 
#     return render(request,"fullpost.html")

def allpost(request):
    allpostdata = homefurnishing.objects.all()
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
         "categoriname":"homefurnishing"
    }
    return render(request,"allpost.html",data)



