from django.shortcuts import render
from . import models as dbdata
from .models import UserData
import numpy as np

import smtplib, ssl
from .fusioncharts import FusionCharts
from django.views.generic import TemplateView
import pickle

# Create your views here.

data_fullname = None
data_signum = None
data_email = None
data_gender = None
data_exp = None
ls = None
entry_list = None
dic_data = None
int_data = 0
choice1 = None
choice2 = None
choice3 = None
buf = None

data_final_gender = None

dic_finaldata = {}

progressflagval = 14

commondata = ['Whizz-Kid', 'Humanitarian', 'Reformer', 'Socialite', 'Sportsperson', 'Individualist']
model = pickle.load(open('C:\\Users\\eyalram\\Desktop\\EGIGame\\model.pkl', 'rb'))


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
                          {'loggeduser': data_final_gender, 'list_data': dic_data, 'flag_data': int_data,
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
                          {'loggeduser': data_final_gender, 'list_data': dic_data, 'flag_data': int_data,
                           'progressdata': progressflagval})


def index(request):
    global progressflagval
    global int_data
    global dic_finaldata
    dic_finaldata = {}
    progressflagval = 14
    int_data = 0
    user_data = UserData()

    int_features = [7,40,50]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    print('Employee Salary should be $ {}'.format(output))

    # email_send()
    return render(request, 'login.html', {'registered': False})


def email_send():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "ramkrisscse@gmail.com"  # Enter your address
    receiver_email = "ramkriss523@gmail.com"  # Enter receiver address
    password = "pa55w0rd!@#"
    message = """\
    Subject: Hi there

    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


# DashPageView
class DashPageView(TemplateView):
    template_name = "dashboard.html"

    # modeldata = QuestionData

    def get(self, request, **kwargs):
        # print(int_data)
        # form = LocationForm()
        if dbdata.UserData.objects.filter(signum=data_signum).exists():
            return render(request, 'login.html', {'registered': True, "final_data": dic_data})
        else:
            return render(request, self.template_name,
                          {'loggeduser': data_final_gender, 'list_data': dic_data, 'flag_data': int_data})

    def post(self, request, **kwargs):
        global data_signum
        data_signum = request.POST.get("signumname")
        global data_fullname
        data_fullname = request.POST.get("fullname")
        global ls
        global entry_list
        global dic_data

        global data_email
        data_email = request.POST.get("email")
        global data_gender
        data_gender = request.POST.get("gender")

        global data_exp
        data_exp = request.POST.get("exp")

        global data_final_gender
        if data_gender == "male":
            data_final_gender = "Mr. "+data_fullname
        else:
            data_final_gender = "Ms. " + data_fullname

        print(data_gender)

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
            find_list = dbdata.UserData.objects.get(signum=data_signum)

            dic_data = {
                'data0': find_list.WhizzKid,
                'data1': find_list.Humanitarian,
                'data2': find_list.Reformer,
                'data3': find_list.Socialite,
                'data4': find_list.Sportsperson,
                'data5': find_list.Individualist,
            }
            return render(request, 'login.html', {'registered': True, "final_data": dic_data})
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
                          {'loggeduser': data_final_gender, 'list_data': dic_data, 'flag_data': int_data})


def question(request):
    return render(request, "question.html", {'loggeduser': data_final_gender})


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

        dic_finaldata[commondata[int(list(dic_data.values()).index(choice1)) - 1]] = dic_finaldata.get(
            commondata[int(list(dic_data.values()).index(choice1)) - 1], 0) + 100

        dic_finaldata[commondata[int(list(dic_data.values()).index(choice2)) - 1]] = dic_finaldata.get(
            commondata[int(list(dic_data.values()).index(choice2)) - 1], 0) + 60

        dic_finaldata[commondata[int(list(dic_data.values()).index(choice3)) - 1]] = dic_finaldata.get(
            commondata[int(list(dic_data.values()).index(choice3)) - 1], 0) + 20

        user_data = UserData(data_fullname, data_signum, str(dic_finaldata.get('Whizz-Kid', 0)),
                             str(dic_finaldata.get('Humanitarian', 0)),
                             str(dic_finaldata.get('Reformer', 0)),
                             str(dic_finaldata.get('Socialite', 0)),
                             str(dic_finaldata.get('Sportsperson', 0)),
                             str(dic_finaldata.get('Individualist', 0)),data_email,data_gender, data_exp)
        user_data.save()

    pie3d = FusionCharts("pie3d", "ex2", "100%", "400", "chart-1", "json",
                         # The data is passed as a string in the `dataSource` as parameter.
                         """{
                             "chart": {
                                 "caption": "Recommended Portfolio Split",
                                 "subCaption" : "",
                                 "showValues":"1",
                                 "showPercentInTooltip" : "0",
                                 "numberPrefix" : "",
                                 "enableMultiSlicing":"1",
                                 "theme": "fusion"
                             },
                             "data": [{
                                 "label": "Whizz-Kid",
                                 "value": """ + str(dic_finaldata.get('Whizz-Kid', 0)) + """
                                 
                             }, {
                                 "label": "Humanitarian",
                                 "value": """ + str(dic_finaldata.get('Humanitarian', 0)) + """
                             }, {
                                 "label": "Reformer",
                                 "value": """ + str(dic_finaldata.get('Reformer', 0)) + """
                             }, {
                                 "label": "Socialite",
                                 "value": """ + str(dic_finaldata.get('Socialite', 0)) + """
                             }, {
                                 "label": "Sportsperson",
                                 "value": """ + str(dic_finaldata.get('Sportsperson', 0)) + """
                             }, {
                                 "label": "Individualist",
                                 "value": """ + str(dic_finaldata.get('Individualist', 0)) + """
                             }]
                         }""")

    # pos = np.arange(10) + 2
    #
    # fig = plt.figure(figsize=(8, 3))
    # ax = fig.add_subplot(111)
    #
    # ax.barh(pos, np.arange(1, 11), align='center')
    # ax.set_yticks(pos)
    # ax.set_yticklabels(('#hcsm',
    #                     '#ukmedlibs',
    #                     '#ImmunoChat',
    #                     '#HCLDR',
    #                     '#ICTD2015',
    #                     '#hpmglobal',
    #                     '#BRCA',
    #                     '#BCSM',
    #                     '#BTSM',
    #                     '#OTalk',),
    #                    fontsize=15)
    # ax.set_xticks([])
    # ax.invert_yaxis()
    #
    # ax.set_xlabel('Popularity')
    # ax.set_ylabel('Hashtags')
    # ax.set_title('Hashtags')
    #
    # plt.tight_layout()
    #
    # buffer = BytesIO()
    # plt.savefig(buffer, format='png')
    # buffer.seek(0)
    # image_png = buffer.getvalue()
    # buffer.close()
    #
    # graphic = base64.b64encode(image_png)
    # graphic = graphic.decode('utf-8')

    return render(request, 'piechart.html',
                  {'output': pie3d.render(), 'loggeduser': data_final_gender})
