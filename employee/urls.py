# coding=utf-8
from django.conf.urls import url

from employee import views






urlpatterns = [
    url(r'^$',views.main_view),
    url(r'^top.html$',views.top_view),
    url(r'^center.html$', views.center_views),
    url(r'^left.html$', views.left_view),
    url(r'^emlpoyee_list.html$',views.index_StaffInfo),
    url(r'^house_list.html$',views.index_HouseInfo),
    url(r'^house_type_list.html$',views.index_HouseType),
    url(r'^emp_detail.html/(\d+)$',views.index_empdetail),               #员工信息详情
    url(r'^emp_edit.html/(\d+)$',views.index_empedit),                    #员工信息编辑
    url(r'^emp_del/(\d+)$',views.index_empdel),                           #员工信息删除
    url(r'^house_detail.html/(\d+)$',views.index_hedit),                         #房屋信息编辑
    url(r'^house_info_add.html$',views.index_houseinfo),
    url(r'^house_type_add.html$', views.index_housetype),
    url(r'^house_del/(\d+)$',views.index_HouseDel)  ,                      #房屋信息删除
    url(r'^house_type_del/(\d+)$',views.index_HouseTypeDel)


]
