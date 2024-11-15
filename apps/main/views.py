from flask import Flask, Blueprint, request, session, redirect, url_for, render_template
import requests
import pandas as pd
from markupsafe import Markup

main = Blueprint('main',__name__,static_folder='static', template_folder='templates')

@main.route('/main', methods =['GET', 'POST'])
def home():
    data_map = requests.get('http://127.0.0.1:8000/map/all')
    list_feature=[]
    a=1
    for plgn in data_map.json():
        atribut={}
        list_coor=[]
        for k in list(plgn.keys()):
            atribut[k]=plgn[k]
        for coor in atribut['geom'][10:-2].replace(', ',',').split(','):
            lng = float(coor.split(' ')[0])
            lat = float(coor.split(' ')[1])
            list_coor.append(list((lng,lat)))
        # ftr = dict({'id':'poly'+str(a),'type': 'Feature','properties':attr,
        #             'geometry':{'type':'Polygon','coordinates':[list_coor]}})
        ftr = dict({'id':atribut['id'],'type': 'Feature','properties':atribut,
                    'geometry':{'type':'Polygon','coordinates':[list_coor]}})
        list_feature.append(ftr)
        a=a+1
    feat = dict({'type':'FeatureCollection','features':list_feature})
    nama_col = list(atribut.keys())
    session['nama_col'] = nama_col
    return render_template('main.html', data_api=feat, nama_col=nama_col)

@main.route('/main/create', methods =['GET', 'POST'])
def create_poli():
    nama_col = session['nama_col']
    # data=[]
    # for col in nama_col:
    #     print(f'data_{col}')
    #     data.append(request.form.get(f'data_{col}'))
    # payload = dict(zip(nama_col,data))
    data = request.json['data']
    return [data]