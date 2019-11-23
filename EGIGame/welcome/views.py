from django.shortcuts import render
from . import models as dbdata
# Create your views here.

data_fullname = None
data_signum = None
ls = None

def index(request):
    return render(request, 'login.html')


def dashboard(request):

    if request.method == 'POST':
        global data_signum
        data_signum = request.POST.get("signumname")
        global data_fullname
        data_fullname = request.POST.get("fullname")
        global ls

        ls = dbdata.QuestionData.objects.all()

        for i in ls:
            print(i.question,i.option1,i.option2,i.option3)
    return render(request, "dashboard.html", {'loggeduser': data_fullname, 'object_list':ls})

    # return render(request, "dashboard.html", {'loggeduser': data_fullname})
    # if request.method == 'POST':
    #     print('in')
    #
    # else:
    #     print('else')
    #     return render(request, "dashboard.html", {'loggeduser': data_fullname})


    # data_signum = request.POST['signumname']
    # data_fullname = request.POST['fullname']

    # print(data_signum)
    # ls = dbdata.UserData.objects.all()
    #
    # for i in ls:
    #     print(i.signum)

    # if ls.contains(data_signum):
    #     messages.success(request, 'You are are already tried!')
    # else:
    #     dbdata.UserData = dbdata.UserData(fullname=request.POST['fullname'], signum=request.POST['signumname'])
    #     dbdata.UserData.save()

    # if dbdata.UserData.objects.filter(signum=data_signum).exists():
    #     print(True)
    #     # messages.success(request, 'You are are already tried!')
    # else:
    #     dbdata.UserData = dbdata.UserData(fullname=request.POST['fullname'], signum=request.POST['signumname'])
    #     dbdata.UserData.save()


def question(request):
    return render(request, "question.html")