from django.shortcuts import render
from homefurnishing.models import homefurnishing
from architecture.models import architecturemodel
from technology.models import technologymodel
from lifestyle.models import lifestylemodel
from travel.models import travelmodel
import random
from contact_us.models import contactemodel
from django.db.models import Q
from django.core.mail import send_mail

# from http import ht




def homepage(request):
  
    random_numbers = set()
    random_numbers_three = set()
    # random numbers generater
    while len(random_numbers)!=5:
        random_number = random.randint(1,10)
        random_numbers.add(random_number)
    while len(random_numbers_three)!=3:
        random_number_th = random.randint(2,10)
        random_numbers_three.add(random_number_th)
            
    homefurnishingblog = homefurnishing.objects.filter(id__in = [x for x in random_numbers])
    architectureblog = architecturemodel.objects.filter(id__in = [x for x in random_numbers_three])
    technologyblog = technologymodel.objects.filter(id__in = [x for x in random_numbers])
    
    ran_no = random.randint(2,10)
    post1 = homefurnishing.objects.filter(id__in = [ran_no])
    post2 = architecturemodel.objects.filter(id__in = [ran_no])
    post3 = technologymodel.objects.filter(id__in = [ran_no])
    post4 = lifestylemodel.objects.filter(id__in = [ran_no])
    ### slugpost = homefurnishing.objects.get(new_slug = slug)
    
    ##### recent post

    data = {
        "homefurnishingblogs":homefurnishingblog,
        "architectureblogs":architectureblog,
        "technologyblogs":technologyblog,
        "homefurnishingname":"homefurnishing",
        "architecturename":"architecture",
        "technologyname":"technology",
        "post1":post1,
        "post2":post2,
        "post3":post3,
        "post4":post4,
        ##### "slugpost": slugpost,
    }
    return render(request,"index.html",data)

def contact(request):
    data = {
        "four":"four",
    }
    return render(request,"conditions.html",data)

def save_data(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        fav_categori = request.POST.get("fav_categori")
        message = request.POST.get("message")
        en = contactemodel(name=name,email=email,fav_categori=fav_categori,message=message)
        en.save()
        data={
            "four":"four"
        }
    return render(request,"conditions.html",data)

def homefurnishingpost(request,slug):
    ran_no = random.randint(2,10)
    post1 = homefurnishing.objects.filter(id__in = [ran_no])
    post2 = architecturemodel.objects.filter(id__in = [ran_no])
    post3 = technologymodel.objects.filter(id__in = [ran_no])
    post4 = lifestylemodel.objects.filter(id__in = [ran_no])
    slugpost = homefurnishing.objects.get(new_slug = slug)
    r_post1 = homefurnishing.objects.last()
    r_post2 = architecturemodel.objects.last()
    r_post3 = technologymodel.objects.last()
    r_post4 = lifestylemodel.objects.last()
    r_post5 = travelmodel.objects.last()
    
    data = {
        "post1":post1,
        "post2":post2,
        "post3":post3,
        "post4":post4,
        "slugpost": slugpost,
        "r_post1":r_post1,
        "r_post2":r_post2,
        "r_post3":r_post3,
        "r_post4":r_post4,
        "r_post5":r_post5,
    } 
    return render(request,"fullpost.html",data)

def architecturepost(request,slug):
    ran_no = random.randint(2,10)
    post1 = homefurnishing.objects.filter(id__in = [ran_no])
    post2 = architecturemodel.objects.filter(id__in = [ran_no])
    post3 = technologymodel.objects.filter(id__in = [ran_no])
    post4 = lifestylemodel.objects.filter(id__in = [ran_no])
    slugpost = architecturemodel.objects.get(new_slug = slug)
    r_post1 = homefurnishing.objects.last()
    r_post2 = architecturemodel.objects.last()
    r_post3 = technologymodel.objects.last()
    r_post4 = lifestylemodel.objects.last()
    r_post5 = travelmodel.objects.last()
    
    data = {
        "post1":post1,
        "post2":post2,
        "post3":post3,
        "post4":post4,
        "slugpost": slugpost,
        "r_post1":r_post1,
        "r_post2":r_post2,
        "r_post3":r_post3,
        "r_post4":r_post4,
        "r_post5":r_post5,
    } 
    return render(request,"fullpost.html",data)


def technologypost(request,slug):
    ran_no = random.randint(2,10)
    post1 = homefurnishing.objects.filter(id__in = [ran_no])
    post2 = architecturemodel.objects.filter(id__in = [ran_no])
    post3 = technologymodel.objects.filter(id__in = [ran_no])
    post4 = lifestylemodel.objects.filter(id__in = [ran_no])
    slugpost = technologymodel.objects.get(new_slug = slug)
    r_post1 = homefurnishing.objects.last()
    r_post2 = architecturemodel.objects.last()
    r_post3 = technologymodel.objects.last()
    r_post4 = lifestylemodel.objects.last()
    r_post5 = travelmodel.objects.last()
    
    data = {
        "post1":post1,
        "post2":post2,
        "post3":post3,
        "post4":post4,
        "slugpost": slugpost,
        "r_post1":r_post1,
        "r_post2":r_post2,
        "r_post3":r_post3,
        "r_post4":r_post4,
        "r_post5":r_post5,
    } 
    return render(request,"fullpost.html",data)

def lifestylepost(request,slug):
    ran_no = random.randint(2,10)
    post1 = homefurnishing.objects.filter(id__in = [ran_no])
    post2 = architecturemodel.objects.filter(id__in = [ran_no])
    post3 = technologymodel.objects.filter(id__in = [ran_no])
    post4 = lifestylemodel.objects.filter(id__in = [ran_no])
    slugpost = lifestylemodel.objects.get(new_slug = slug)
    r_post1 = homefurnishing.objects.last()
    r_post2 = architecturemodel.objects.last()
    r_post3 = technologymodel.objects.last()
    r_post4 = lifestylemodel.objects.last()
    r_post5 = travelmodel.objects.last()
    
    data = {
        "post1":post1,
        "post2":post2,
        "post3":post3,
        "post4":post4,
        "slugpost": slugpost,
        "r_post1":r_post1,
        "r_post2":r_post2,
        "r_post3":r_post3,
        "r_post4":r_post4,
        "r_post5":r_post5,
    } 
    return render(request,"fullpost.html",data)

def travelpost(request,slug):
    ran_no = random.randint(2,10)
    post1 = homefurnishing.objects.filter(id__in = [ran_no])
    post2 = architecturemodel.objects.filter(id__in = [ran_no])
    post3 = technologymodel.objects.filter(id__in = [ran_no])
    post4 = lifestylemodel.objects.filter(id__in = [ran_no])
    slugpost = travelmodel.objects.get(new_slug = slug)
    r_post1 = homefurnishing.objects.last()
    r_post2 = architecturemodel.objects.last()
    r_post3 = technologymodel.objects.last()
    r_post4 = lifestylemodel.objects.last()
    r_post5 = travelmodel.objects.last()
    
    data = {
        "post1":post1,
        "post2":post2,
        "post3":post3,
        "post4":post4,
        "slugpost": slugpost,
        "r_post1":r_post1,
        "r_post2":r_post2,
        "r_post3":r_post3,
        "r_post4":r_post4,
        "r_post5":r_post5,
    } 
    return render(request,"fullpost.html",data)

def searching(request):
    homedata = homefurnishing.objects.all()
    if request.method=="GET":
        se = request.GET.get("search")
        # print(se)
        value = f"Searching For <q>{se}</q>"
        if se!=None:
            data1 = homefurnishing.objects.filter(Q(main_heading__icontains=se) | Q(categori__icontains=se))
            data2 = architecturemodel.objects.filter(Q(main_heading__icontains=se) | Q(categori__icontains=se))
            data3 = technologymodel.objects.filter(Q(main_heading__icontains=se) | Q(categori__icontains=se))
            data4 = lifestylemodel.objects.filter(Q(main_heading__icontains=se) | Q(categori__icontains=se))
            data5 = travelmodel.objects.filter(Q(main_heading__icontains=se) | Q(categori__icontains=se))
        if len(data1)==0 and len(data2)==0 and len(data3)==0 and len(data4)==0 and len(data5)==0:
            value = "NOT FOUND DATA"
            
    data = {
       "data1":data1,
       "data2":data2,
       "data3":data3,
       "data4":data4,
       "data5":data5,
       "value":value,
       "search":"search"
    }    
    return render(request,"conditions.html",data)


def terms(request):
    data = {
        "one":"one",
    }
    return render(request,"conditions.html",data)

def privacy(request):
    data = {
        "two":"two",
    }
    return render(request,"conditions.html",data)

def faq(request):
    data = {
        "three":"three",
    }
    return render(request,"conditions.html",data)


# def e_send(request, path):
    

    # # Use the request.path to render the template based on the current URL path
    # return render(request, request.path)



