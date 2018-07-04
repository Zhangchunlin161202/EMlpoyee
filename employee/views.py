#coding=utf-8

from __future__ import unicode_literals

import sys
from django.http import HttpResponse
from django.shortcuts import render

# Create your views herme.
from employee.models import *
reload(sys)
sys.setdefaultencoding('utf-8')

def index_StaffInfo(request):

    # 获取信息
    staff_info = UserInfo.objects.all()

    return render(request,'emlpoyee_list.html',{'staff_info':staff_info})

def main_view(request):
    return render(request,'base.html')


def top_view(request):
    return render(request,'top.html')


def center_views(request):
    return render(request, 'center.html')


def left_view(request):
    # detail_list = DetailInfo.objects.all()
    return render(request,'left.html')


def employee_views(request):
    return render(request,'emlpoyee_list.html')


def index_HouseInfo(request):
    house_info = HouseInfo.objects.all()

    return render(request, 'house_list.html', {'house_info': house_info})


def index_HouseType(request):
    house_type = HouseType.objects.all()

    return render(request, 'house_type_list.html', {'house_type': house_type})


def index_empdetail(request,user_id):
    # 获取所有信息
    detail_info = UserInfo.objects.filter(user_id=user_id)

    return render(request,'emp_detail.html',{'detail_info':detail_info})

def index_houseinfo(request):

    if request.method == 'GET':
        return render(request,'house_info_add.html')
    else:
        htype = request.POST.get('htype','')
        hadmin = request.POST.get('hadmin','')
        haddr = request.POST.get('haddr','')
        hcost = request.POST.get('hcost','')
        henv = request.POST.get('henv','')
        HouseInfo.objects.create(# type=htype,
                                 # user=hadmin,
                                 house_address=haddr,
                                 house_price=hcost,
                                 house_ambient=henv)
        return HttpResponse('添加成功！')

# 添加房屋类型
def index_housetype(request):

    if request.method == 'GET':
        return render(request,'house_type_add.html')
    else:
        htype = request.POST.get('htype','')
        HouseType.objects.create(type_name=htype)
    return HttpResponse('添加成功！')

# 编辑
def index_empedit(request,user_id):
    if request.method == 'GET':
        emp_list = UserInfo.objects.filter(user_id=user_id)
        depar_info = DepartmentInfo.objects.all()
        user_role = UserRole.objects.all()
        return render(request,'emp_edit.html',{'emp_list':emp_list,'depar_info':depar_info,'user_role':user_role})
    else:
        sname = request.POST.get('sname','')
        sage = request.POST.get('sage', '')
        sgender = request.POST.get('sgender', '')
        seducation = request.POST.get('seducation', '')
        ssection = request.POST.get('ssection', '')
        scall = request.POST.get('scall', '')
        spaycard = request.POST.get('spaycard', '')
        scard = request.POST.get('scard', '')
        sadd = request.POST.get('sadd', '')
        saccount = request.POST.get('saccount', '')
        spassword = request.POST.get('spassword', '')
        snation = request.POST.get('snation', '')
        smarriage = request.POST.get('smarriage', '')
        spower = request.POST.get('spower', '')
        spn = request.POST.get('spn', '')
        saddres = request.POST.get('saddres', '')
        shoddy = request.POST.get('shoddy', '')
        semail = request.POST.get('semail', '')
        UserInfo.objects.filter(user_id=user_id).update(user_name=sname,user_age=sage,user_sex=sgender,
                                                        user_diploma=seducation,
                                                        # department=ssection,
                                                        user_tel=scall,user_bankcard=spaycard,
                                                        user_idnum=scard,
                                                        user_addman=sadd,user_num=saccount,
                                                        user_pw=spassword,user_nation=snation,
                                                        is_married=smarriage,
                                                        # role=spower,
                                                        user_mobile=spn,
                                                        user_address=saddres,
                                                        user_intest=shoddy,
                                                        user_email=semail)
        return HttpResponse('修改成功！')

# 房屋信息编辑
def index_hedit(request,houseid):

    if request.method == 'GET':
        house_list = HouseInfo.objects.filter(house_id=houseid)
        return render(request,'house_edit.html',{'house_list':house_list})

    else:
        htype = request.POST.get('htype','')
        hadmin = request.POST.get('hadmin','')
        haddr = request.POST.get('haddr','')
        hcost = request.POST.get('hcost','')
        henv = request.POST.get('henv','')
        HouseInfo.objects.filter(house_id=houseid).update(   # type=htype,
                                                             # user=hadmin,
                                                             house_address=haddr,
                                                             house_price=hcost,
                                                             house_ambient=henv)

        return HttpResponse('编辑成功！')


def index_empdel(request,emid):
    UserInfo.objects.filter(user_id=emid).delete()

    return HttpResponse('删除成功！')


def index_HouseDel(request,hid):
    HouseInfo.objects.filter(house_id=hid).delete()
    return HttpResponse('删除成功！')


def index_HouseTypeDel(request,htid):
    HouseType.objects.filter(type_id=htid).delete()

    return HttpResponse('删除成功！')