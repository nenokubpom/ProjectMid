from flask import Blueprint, render_template, redirect, request, url_for
import requests
import json

Exchange = Blueprint('Exchange', __name__)

@Exchange.route('/', methods=['GET','POST'])
def ExchangeTwoMon():
    myurl = 'https://api.exchangeratesapi.io/'
    url = '{}latest'.format(myurl)
    data = requests.get(url).json()
    allcurrency=[]
    for i in data['rates'].keys():
        allcurrency.append(i)
    allcurrency.append(data['base'])

    if request.method == 'POST':
        first = str(request.form.get('one'))
        second = str(request.form.get('two'))
        value = request.form.get('value')
        if(value==''):
            return render_template('exchange.html',AC=allcurrency)
        else:
            url = '{}latest?symbols={},{}'.format(myurl,first,second)
            data = requests.get(url).json()
            currenhave = float(data['rates']['{}'.format(first)])
            currenexchange = float(data['rates']['{}'.format(second)])
            count = int(value)
            text="Your"
            
            text2="Amount To Exchange  ="
            text3="Your Amount"
            text4 = " = "
            text5= "Exchange To"
            sum = str(round((currenexchange/currenhave)*count,2))
            return render_template('exchange.html',AC=allcurrency,cf=sum,ct=count,tx1=text,tx2=text2,sc=second,f1=first,tx3=text3,tx4=text4,tx5=text5)
    return render_template('exchange.html',AC=allcurrency)