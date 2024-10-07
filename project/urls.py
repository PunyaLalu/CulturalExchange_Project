"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),


    path('',views.index),
    path('userreg/',views.userreg),
    path('ambassadorreg/',views.ambassadorreg),
    path('guidereg/',views.guidereg),
    path('login/',views.login),
    path('adminhome/',views.adminhome),
    path('userhome/',views.userhome),
    path('ambassadorhome/',views.ambassadorhome),
    path('guidehome/',views.guidehome),
    path('viewuser/',views.viewuser),
    path('actionuser/',views.actionuser),
    path('rejectuser/',views.rejectuser),
    path('deleteuser/',views.deleteuser),
    path('viewambassador/',views.viewambassador),
    path('actionambassador/',views.actionambassador),
    path('rejectambassador/',views.rejectambassador),
    path('deleteambassador/',views.deleteambassador),
    path('viewguide/',views.viewguide),
    path('actionguide/',views.actionguide),
    path('rejectguide/',views.rejectguide),
    path('deleteguide/',views.deleteguide),
    path('addevent/',views.addevent),
    path('viewevent/',views.viewevent),
    path('bookevent/',views.bookevent),
    path('viewbook_event/',views.viewbook_event),
    path('actionbook/',views.actionbook),
    path('rejectbook/',views.rejectbook),
    path('deletebook/',views.deletebook),
    path('viewbook_events/',views.viewbook_events),
    path('addpay/',views.addpay),
    path('viewevent_book/',views.viewevent_book),
    path('viewevents/',views.viewevents),
    path('chat/',views.chat),
    path('reply/',views.reply),
    path('view_event/',views.view_event),
    path('addarticle/',views.addarticle),
    path('viewarticle/',views.viewarticle),
    path('update/',views.update),
    path('delete/',views.delete),
    path('addarticle_u/',views.addarticle_u),
    path('viewarticle_u/',views.viewarticle_u),
    path('update_u/',views.update_u),
    path('delete_u/',views.delete_u),
    path('viewarticles/',views.viewarticles),
    path('feedback/',views.feedback),
    path('viewfeedback/',views.viewfeedback),
    path('addreply/',views.addreply),
    path('viewfeedback_u/',views.viewfeedback_u),
    path('addservice/',views.addservice),
    path('viewservice/',views.viewservice),
    path('update_s/',views.update_s),
    path('delete_s/',views.delete_s),
    path('viewservices/',views.viewservices),
    path('bookservice_u/',views.bookservice_u),
    path('viewservice_g/',views.viewservice_g),
    path('acs/',views.acs),
    path('rejs/',views.rejs),
    path('viewservice_book/',views.viewservice_book),
    path('addpay_g/',views.addpay_g),
    path('addevent_ad/',views.addevent_ad),
    path('viewevent_ad/',views.viewevent_ad),
    path('update_ad/',views.update_ad),
    path('delete_ad/',views.delete_ad),
    path('viewevent_u/',views.viewevent_u),
    path('bookevent_u/',views.bookevent_u),
    path('viewbook_event_u/',views.viewbook_event_u),
    path('approve_a/',views.approve_a),
    path('reject_a/',views.reject_a),
    path('viewpar_event/',views.viewpar_event),
    path('addpay_u/',views.addpay_u),
    path('viewguide_u/',views.viewguide_u),
    path('chat_u/',views.chat_u),
    path('reply_a/',views.reply_a),
    path('viewarticle_am/',views.viewarticle_am),
]
