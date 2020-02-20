from django.shortcuts import render
from . import models as dbdata
from .models import UserData
import numpy as np
import json

import smtplib, ssl
from .fusioncharts import FusionCharts
from django.views.generic import TemplateView
import pickle

import socket
import sys
from predict import Predict
import re
import base64
from PIL import Image
import cv2
import io
from camera_image import get_frame

dataUrlPattern = re.compile('data:image/png;base64,(.*)$')

# Create your views here.
list_emotions = []
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
arydata = None
arydata1 = None
personality = None

data_final_gender = None

dic_finaldata = {}
dic_totaldata = {}
arrynewfinaldata = None

progressflagval = 14

commondata = ['Whizz-Kid', 'Humanitarian', 'Reformer', 'Socialite', 'Sportsperson', 'Individualist']
'''model = pickle.load(open('C:\\Users\\eyalram\\Desktop\\EGIGame\\model.pkl', 'rb'))'''

emotions = []


# Class Based View for Questionaries
class HomePageView(TemplateView):
    template_name = "question1.html"

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
        # retrive image from canvas
        ImageData = request.POST.get("image")
        ImageData = dataUrlPattern.match(ImageData).group(1)

        # If none or len 0, means illegal image data
        if (ImageData == None or len(ImageData) == 0):
            print("error")

        # Decode the 64 bit string into 32 bit
        imgdata = base64.b64decode(str(ImageData))
        image = Image.open(io.BytesIO(imgdata))
        image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)

        #######################################
        list_emotions.append(get_frame(image))
        print(list_emotions)
        #######################################

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

    '''int_features = [7,40,50]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    print('Employee Salary should be $ {}'.format(output))'''

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
    template_name = "dashboard1.html"

    # modeldata = QuestionData

    def get(self, request, **kwargs):
        # print(int_data)
        # form = LocationForm()
        if dbdata.UserData.objects.filter(signum=data_signum).exists():
            return render(request, 'login.html', {'registered': True, "final_data": dic_data})
        else:

            return render(request, self.template_name,
                          {'loggeduser': data_final_gender, 'list_data': arrynewfinaldata,'list_data1': dic_data, 'flag_data': int_data})

    def post(self, request, **kwargs):
        global data_signum
        data_signum = request.POST.get("signumname")
        global data_fullname
        data_fullname = request.POST.get("fullname")
        global ls
        global entry_list
        global dic_data
        global arrynewfinaldata

        global data_email
        data_email = request.POST.get("email")
        global data_gender
        data_gender = request.POST.get("gender")

        global data_exp
        data_exp = request.POST.get("exp")

        global data_final_gender
        if data_gender == "male":
            data_final_gender = "Mr. " + data_fullname
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

            arrynewfinaldata = [entry_list[int_data].option1,entry_list[int_data].option2,entry_list[int_data].option3,
                                entry_list[int_data].option4, entry_list[int_data].option5, entry_list[int_data].option6]
            return render(request, self.template_name,
                          {'loggeduser': data_final_gender, 'list_data': arrynewfinaldata,'list_data1': dic_data, 'flag_data': int_data})


def question(request):
    return render(request, "question.html", {'loggeduser': data_final_gender})


# Create an object for the pie3d chart using the FusionCharts class constructor
def chart(request):
    if request.POST:
        global choice1
        global choice2
        global choice3
        global dic_finaldata
        global arydata

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
                             str(dic_finaldata.get('Individualist', 0)), data_email, data_gender, data_exp)
        user_data.save()

        global ls
        global entry_list
        global arydata1
        global personality

        ls = dbdata.UserData.objects.all()
        for i in ls:
            dic_totaldata["Whizz-Kid"] = dic_totaldata.get("Whizz-Kid", 0) + int(i.WhizzKid)
            dic_totaldata["Humanitarian"] = dic_totaldata.get("Humanitarian", 0) + int(i.Humanitarian)
            dic_totaldata["Reformer"] = dic_totaldata.get("Reformer", 0) + int(i.Reformer)
            dic_totaldata["Socialite"] = dic_totaldata.get("Socialite", 0) + int(i.Socialite)
            dic_totaldata["Sportsperson"] = dic_totaldata.get("Sportsperson", 0) + int(i.Sportsperson)
            dic_totaldata["Individualist"] = dic_totaldata.get("Individualist", 0) + int(i.Individualist)

        arydata1 = [['Task', 'Hours per Day'],
                    ["Whizz-Kid", dic_totaldata.get('Whizz-Kid', 0)],
                    ['Humanitarian', dic_totaldata.get('Humanitarian', 0)],
                    ['Reformer', dic_totaldata.get('Reformer', 0)],
                    ['Socialite', dic_totaldata.get('Socialite', 0)],
                    ['Sportsperson', dic_totaldata.get('Sportsperson', 0)],
                    ['Individualist', dic_totaldata.get('Individualist', 0)]]

        arydata = [['Task', 'Hours per Day'],
                   ["Whizz-Kid", dic_finaldata.get('Whizz-Kid', 0)],
                   ['Humanitarian', dic_finaldata.get('Humanitarian', 0)],
                   ['Reformer', dic_finaldata.get('Reformer', 0)],
                   ['Socialite', dic_finaldata.get('Socialite', 0)],
                   ['Sportsperson', dic_finaldata.get('Sportsperson', 0)],
                   ['Individualist', dic_finaldata.get('Individualist', 0)]]

        max_data = {'Whizz-Kid': int(dic_finaldata.get('Whizz-Kid', 0)),
                    'Humanitarian': int(dic_finaldata.get('Humanitarian', 0)),
                    'Reformer': int(dic_finaldata.get('Reformer', 0)),
                    'Socialite': int(dic_finaldata.get('Socialite', 0)),
                    'Sportsperson': int(dic_finaldata.get('Sportsperson', 0)),
                    'Individualist': int(dic_finaldata.get('Individualist', 0))}
        v = list(max_data.values())

        # taking list of car keys in v
        k = list(max_data.keys())
        personality = k[v.index(max(v))];

    return render(request, 'piechart1.html',
                  {'array': json.dumps(arydata), 'array1': json.dumps(arydata1), 'loggeduser': data_final_gender,
                   'personality': personality})
