from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    ##############################  all page ##############################


    path('',views.demo,name='demo'),  
    path('loginpage/', views.loginpage, name="loginpage"),
    path('loginuser/', views.loginuser, name="loginuser"),

    path('dashboardpage/', views.dashboardpage, name="dashboardpage"),
    path('basepage/', views.basepage, name="basepage"),
    path('footerpage/', views.footerpage, name="footerpage"),
    path('sidebarpage/', views.sidebarpage, name="sidebarpage"),
    path('headerpage/', views.headerpage, name="headerpage"),
    
    ############## OFfercard page##################################
    path('offer_apply/', views.offer_apply, name="offer_apply"),
    path('offer_update/<int:id>',views.offer_update,name='offer_update'),
    path('delete_offer/<int:id>',views.delete_offer,name='offer_update'),


    ########  product-page ###################################
    path('product/', views.product,name = 'product'),
    path('productInsert/', views.productInsert, name="productInsert"),
    path('productDelete/<int:id>', views.productDelete, name="productDelete"),
    path('productUpdate/<int:id>', views.productUpdate, name="productUpdate"),


    path('changeStatusofffercard/<int:id>', views.changeStatus_offfercard, name="changeStatusofffercard"),
   
   
    ######## product-Review Page########################################
    path('product-review/', views.product_review,name = 'product-review'),
    path('Insertreview/', views.Insertreview, name="Insertreview"),
    path('update_review/<int:id>', views.update_review, name="update_review"),

    path('Delte_Review/<int:id>', views.Delte_Review, name="Delte_Review"),

    ############# User CArt###################################

    path('usercart/', views.user_cart,name = 'usercart'),
    path('update_cart/<int:id>', views.usercart_update, name="update_cart"),
    path('Delte_usercart/<int:id>', views.Delte_usercart, name="Delte_usercart"),
    
    ############# ordermanagement############################

    path('order/',views.order_management,name = 'order')




]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


