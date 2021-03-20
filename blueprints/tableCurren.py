from flask import Blueprint, render_template, redirect, request, url_for
import requests
import json
import itertools 

tableCurren = Blueprint('tableCurren', __name__)

@tableCurren.route('/tableCurren', methods=['GET','POST'])
def TableCurren():
    myurl = 'https://api.exchangeratesapi.io/'
    url = '{}latest'.format(myurl)
    data = requests.get(url).json()
    allcurrency=[]
    for i in data['rates'].keys():
        allcurrency.append(i)
    allcurrency.append(data['base'])
    if request.method == 'POST':
        base = str(request.form.get('one'))
        url = '{}latest?base={}'.format(myurl,base)
        data = requests.get(url).json()
        mydict = data['rates']
        sortdictdata = sorted(mydict.items(),key=lambda x:x[1],reverse=True)
        sortdict={}
        i=0
        while i < len(sortdictdata):
            sortdict[sortdictdata[i][0]] = round(sortdictdata[i][1],4)
            i = i+1
        curren = []
        amount = []
        for i in sortdict.keys():
            curren.append(i)
        for i in sortdict.values():
            amount.append(i)
        text = 'Base is {}'.format(base)
        return render_template("tableCurren.html", data1=zip(curren,amount),base=text,baseonly = base, AC=allcurrency)
    return render_template("tableCurren.html", AC=allcurrency)