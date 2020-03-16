from django.shortcuts import render, redirect
import requests
import json
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def list_w(request):
    headers = {
        'Authorization': 'Bearer elZxQlHDSUallvL3OnnH',
    }
    r = requests.get('https://api.zenefits.com/core/people/', headers=headers).json()
    lst = []
    for r in r['data']['data']:
        if r['status'] == 'active':
            dic = {}
            if r['manager']['url'] == None:
                dic.update([('id', r['id']), ('first_name', r['first_name']),
                            ('last_name', r['last_name']), ('manager', 'Head of Company')])
            else:
                r1 = requests.get(str(r['manager']['url']), headers=headers).json()
                dic.update([('id', r['id']), ('first_name', r['first_name']),
                            ('last_name', r['last_name']), ('manager', str(r1['data']['first_name'])+' emp_id '+str(r1['data']['id']))])
            lst.append(dic)

    return render(request, 'Organised_chart/index.html',{'r1':lst})

def emp_detail(request, id):
    headers = {
        'Authorization': 'Bearer elZxQlHDSUallvL3OnnH',
    }
    url = 'https://api.zenefits.com/core/people/' + str(id)
    r2 = requests.get(url, headers=headers).json()
    r3 = requests.get(str(r2['data']['department']['url']), headers=headers).json()
    r4 = requests.get(str(r2['data']['company']['url']), headers=headers).json()
    return render(request, 'Organised_chart/Emp_info.html', {'r2':r2['data'],'r3':r3['data'],'r4':r4['data']})


