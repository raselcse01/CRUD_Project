import os
from django.shortcuts import render, redirect
from .models import profile


def login(r):
    if r.method == 'POST':
        name = r.POST['name']
        email = r.POST['email']
        img = r.FILES.get('fileupload')

        user = profile()
        user.name = name
        user.email = email
        user.propic = img
        user.save()

    return render(r, 'login.html')


def Prof(r):
    search = r.GET.get('search')
    if search:
        pro = profile.objects.filter(name__icontains=search)
    # elif search:
    #     pro = profile.objects.filter(email__icontains=search)
    else:
        pro = profile.objects.all()       
    return render(r, 'newProf.html', locals())


def update(r,id):
    pro = profile.objects.get(id=id)
    if r.method == 'POST':
        name = r.POST['name']
        email = r.POST['email']
        img = r.FILES.get('fileupload')

        # user = profile.objects.get(id=id)

        if len(r.FILES) !=0:
            if len(pro.proPic) > 0:
                os.remove(pro.proPic.path)
            pro.proPic = img

        pro.name = name
        pro.email = email
        pro.save()
        return redirect('Prof')

        # if len(r.FILES)!=0:
        #     if len(pro.proPic) > 0:
        #         os.remove(pro.proPic.path)
        #     pro.proPic = img

            # pro.name = name
            # pro.email = email
            # pro.save()
            #return redirect('Prof')
        
    return render(r,'Update.html', locals())



def delete(r,id):
    user = profile.objects.get(id=id)
    user.delete()
    return redirect('Prof')
    #return render(r, 'newProf.html', locals())

# def search(r):
#     return render(r, 'search.html', locals())


# def all_info_del(request):

#     all_del=employee.objects.all()
#     for i in all_del:
#         if i.emp_pic:
#             os.remove(i.emp_pic.path)
#         all_del.delete()    

#     return redirect(display)
