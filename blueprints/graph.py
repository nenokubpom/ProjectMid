from flask import Blueprint, render_template, redirect, request, url_for
import requests
import json
import plotly
import plotly.graph_objs as go


graph = Blueprint('graph', __name__)

@graph.route('/graph',methods = ['GET','POST'])
def graphline():
    myurl = 'https://api.exchangeratesapi.io/'
    
    url = '{}latest'.format(myurl)
    data = requests.get(url).json()
    allcurrency=[]
    for i in data['rates'].keys():
        allcurrency.append(i)
    allcurrency.append(data['base'])
    
    if request.method == 'POST':
        curf = str(request.form.get('one')).strip()
        curS = str(request.form.get('two')).strip()
        url = '{}history?start_at=2018-01-01&end_at=2021-03-16&symbols={},{}'.format(myurl,curf,curS)
        
        data = requests.get(url).json()
    
        select = data["rates"]
        z=0
        date = []
        setdata = []
        Currency1 = {}
        Currency2 = {}
    
        for x in select.keys():
            date.append(x)
    
        for y in select.values():
            setdata.append(y)
    
    # while z < len(setdata):
    #     Currency1.append(setdata[z]['USD'])
    #     Currency2.append(setdata[z]['GBP'])
    #     z=z+1
    
    # while z < len(setdata):
    #     Currency1.append({date[z]:setdata[z]['USD']})
    #     Currency2.append({date[z]:setdata[z]['GBP']})
    #     z=z+1
    
        while z < len(setdata):
            Currency1[date[z]] = setdata[z]['{}'.format(curf)]
            Currency2[date[z]] = setdata[z]['{}'.format(curS)]
            z=z+1

    # for i in range(len(Currency1)):
    #     Currency1[i]["value"]
    
        fig = go.Figure([
            go.Scatter(
                name=curf,
                x=date.sort(),
                y=list(Currency1.values()),
                mode='lines',
                marker=dict(color='red', size=2),
                showlegend=True
                ),
            go.Scatter(
                name=curS,
                x=date.sort(),
                y=list(Currency2.values()),
                mode='lines',
                marker=dict(color='blue', size=2),
                showlegend=True
                )
            ])
        

        top = '{} VS {}'.format(curf,curS)
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('graph.html',AC=allcurrency,description=top,plot=graphJSON)
    return render_template('graph.html',AC=allcurrency)#description=top,plot=graphJSON)


