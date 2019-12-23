from django.shortcuts import render
from . import models as dbdata
from .models import UserData

from .models import QuestionData

from .fusioncharts import FusionCharts
from django.views.generic import TemplateView
from .forms import LocationForm

# Create your views here.

data_fullname = None
data_signum = None
ls = None
entry_list = None
dic_data = None
int_data = 0
choice1 = None
choice2 = None
choice3 = None

dic_finaldata = {}

progressflagval = 14

commondata = ['Achiever', 'Philanthropist', 'Disruptor', 'Socializer', 'Player', 'Free Spirit']


# Class Based View for Questionaries
class HomePageView(TemplateView):
    template_name = "question.html"

    # modeldata = QuestionData

    def get(self, request, **kwargs):
        # print(int_data)
        # form = LocationForm()
        if int_data == 7:
            return render(request, 'piechart.html')
        else:
            return render(request, self.template_name,
                          {'loggeduser': data_fullname, 'list_data': dic_data, 'flag_data': int_data,
                           'progressdata': progressflagval})

    def post(self, request, **kwargs):
        global ls
        global entry_list
        global dic_data
        global int_data
        global choice1
        global choice2
        global choice3
        global progressflagval

        choice1 = request.POST.get("choice1")
        choice2 = request.POST.get("choice2")
        choice3 = request.POST.get("choice3")

        dic_finaldata[commondata[int(list(dic_data.values()).index(choice1)) - 1]] = dic_finaldata.get(
            commondata[int(list(dic_data.values()).index(choice1)) - 1], 0) + 100

        dic_finaldata[commondata[int(list(dic_data.values()).index(choice2)) - 1]] = dic_finaldata.get(
            commondata[int(list(dic_data.values()).index(choice2)) - 1], 0) + 60

        dic_finaldata[commondata[int(list(dic_data.values()).index(choice3)) - 1]] = dic_finaldata.get(
            commondata[int(list(dic_data.values()).index(choice3)) - 1], 0) + 20

        # for k, v in dic_finaldata.items():
        #     print(k, v)

        progressflagval = progressflagval + 14
        int_data = int_data + 1

        ls = dbdata.QuestionData.objects.all()
        entry_list = list(dbdata.QuestionData.objects.all())

        if int_data == 7:
            return render(request, 'piechart.html')
        else:
            dic_data = {
                'question': entry_list[int_data].question,
                'option0': entry_list[int_data].option1,
                'option1': entry_list[int_data].option2,
                'option2': entry_list[int_data].option3,
                'option3': entry_list[int_data].option4,
                'option4': entry_list[int_data].option5,
                'option5': entry_list[int_data].option6,
                'image0': entry_list[int_data].image1.url,
                'image1': entry_list[int_data].image2.url,
                'image2': entry_list[int_data].image3.url,
                'image3': entry_list[int_data].image4.url,
                'image4': entry_list[int_data].image5.url,
                'image5': entry_list[int_data].image6.url,
            }

            return render(request, self.template_name,
                          {'loggeduser': data_fullname, 'list_data': dic_data, 'flag_data': int_data,
                           'progressdata': progressflagval})


def index(request):
    global progressflagval
    global int_data
    global dic_finaldata
    dic_finaldata = {}
    progressflagval = 14
    int_data = 0
    user_data = UserData()
    return render(request, 'login.html', {'registered': False})


# DashPageView
class DashPageView(TemplateView):
    template_name = "dashboard.html"

    # modeldata = QuestionData

    def get(self, request, **kwargs):
        # print(int_data)
        # form = LocationForm()
        if dbdata.UserData.objects.filter(signum=data_signum).exists():
            return render(request, 'login.html', {'registered': True})
        else:
            return render(request, self.template_name,
                          {'loggeduser': data_fullname, 'list_data': dic_data, 'flag_data': int_data})

    def post(self, request, **kwargs):
        global data_signum
        data_signum = request.POST.get("signumname")
        global data_fullname
        data_fullname = request.POST.get("fullname")
        global ls
        global entry_list
        global dic_data

        ls = dbdata.QuestionData.objects.all()
        entry_list = list(dbdata.QuestionData.objects.all())

        dic_data = {
            'question': entry_list[0].question,
            'option0': entry_list[0].option1,
            'option1': entry_list[0].option2,
            'option2': entry_list[0].option3,
            'option3': entry_list[0].option4,
            'option4': entry_list[0].option5,
            'option5': entry_list[0].option6,
            'image0': entry_list[0].image1.url,
            'image1': entry_list[0].image2.url,
            'image2': entry_list[0].image3.url,
            'image3': entry_list[0].image4.url,
            'image4': entry_list[0].image5.url,
            'image5': entry_list[0].image6.url,
        }

        if dbdata.UserData.objects.filter(signum=data_signum).exists():
            return render(request, 'login.html', {'registered': True})
        else:
            dic_data = {
                'question': entry_list[int_data].question,
                'option0': entry_list[int_data].option1,
                'option1': entry_list[int_data].option2,
                'option2': entry_list[int_data].option3,
                'option3': entry_list[int_data].option4,
                'option4': entry_list[int_data].option5,
                'option5': entry_list[int_data].option6,
                'image0': entry_list[int_data].image1.url,
                'image1': entry_list[int_data].image2.url,
                'image2': entry_list[int_data].image3.url,
                'image3': entry_list[int_data].image4.url,
                'image4': entry_list[int_data].image5.url,
                'image5': entry_list[int_data].image6.url,
            }

            return render(request, self.template_name,
                          {'loggeduser': data_fullname, 'list_data': dic_data, 'flag_data': int_data})


def question(request):
    return render(request, "question.html", {'loggeduser': data_fullname})


# Create an object for the pie3d chart using the FusionCharts class constructor
def chart(request):
    if request.POST:
        print("Hello Pie")
        global choice1
        global choice2
        global choice3
        global dic_finaldata

        choice1 = request.POST.get("choice1")
        choice2 = request.POST.get("choice2")
        choice3 = request.POST.get("choice3")

        print(choice1 + choice2 + choice3)
        dic_finaldata[commondata[int(list(dic_data.values()).index(choice1)) - 1]] = dic_finaldata.get(
            commondata[int(list(dic_data.values()).index(choice1)) - 1], 0) + 100

        dic_finaldata[commondata[int(list(dic_data.values()).index(choice2)) - 1]] = dic_finaldata.get(
            commondata[int(list(dic_data.values()).index(choice2)) - 1], 0) + 60

        dic_finaldata[commondata[int(list(dic_data.values()).index(choice3)) - 1]] = dic_finaldata.get(
            commondata[int(list(dic_data.values()).index(choice3)) - 1], 0) + 20

        user_data = UserData(data_fullname, data_signum, str(dic_finaldata.get('Achiever', 0)),
                             str(dic_finaldata.get('Philanthropist', 0)),
                             str(dic_finaldata.get('Disruptor', 0)),
                             str(dic_finaldata.get('Socializer', 0)),
                             str(dic_finaldata.get('Player', 0)),
                             str(dic_finaldata.get('Free Spirit', 0)))
        user_data.save()

    pie3d = FusionCharts("pie3d", "ex2", "100%", "400", "chart-1", "json",
                         # The data is passed as a string in the `dataSource` as parameter.
                         """{
                             "chart": {
                                 "caption": "Recommended Portfolio Split",
                                 "subCaption" : "For a net-worth of $1M",
                                 "showValues":"1",
                                 "showPercentInTooltip" : "0",
                                 "numberPrefix" : "",
                                 "enableMultiSlicing":"1",
                                 "theme": "fusion"
                             },
                             "data": [{
                                 "label": "Achiever",
                                 "value": """ + str(dic_finaldata.get('Achiever', 0)) + """
                                 
                             }, {
                                 "label": "Philanthropist",
                                 "value": """ + str(dic_finaldata.get('Philanthropist', 0)) + """
                             }, {
                                 "label": "Disruptor",
                                 "value": """ + str(dic_finaldata.get('Disruptor', 0)) + """
                             }, {
                                 "label": "Socializer",
                                 "value": """ + str(dic_finaldata.get('Socializer', 0)) + """
                             }, {
                                 "label": "Player",
                                 "value": """ + str(dic_finaldata.get('Player', 0)) + """
                             }, {
                                 "label": "Free Spirit",
                                 "value": """ + str(dic_finaldata.get('Free Spirit', 0)) + """
                             }]
                         }""")

    return render(request, 'piechart.html', {'output': pie3d.render(), 'loggeduser': data_fullname})
