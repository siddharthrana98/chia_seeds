from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
# from .forms import *
# from.forms import PostForm
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth import logout,login,authenticate,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.forms import ApplyofferForm 
from django.contrib.auth.models import User


# Create your views here.
#############################################################655656565

#rrrrrrrrrrrrrrrrrr
############################## all page ##############################
######################################################################

################## LOG IN-OUT PAGE####################################

def demo(request):
    return redirect('loginpage')

def signin(request):
    return render (request,'login.html')

@csrf_exempt
def loginuser(request):  
    if request.method == 'POST':
    
    # return JsonResponse (request.data)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username =username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboardpage')

        else:
            return HttpResponse('user or password not match')
    else:
        return redirect('login')


@csrf_exempt
def Logoutuser(request):
    logout(request)
    return redirect("loginpage")




@csrf_exempt
def dashboardpage(request):
    return render(request,'adminTemplate/dashboard.html')

@csrf_exempt
def basepage(request):
    return render(request,'adminTemplate/base.html')

@csrf_exempt
def footerpage(request):
    return render(request,'adminTemplate/footer.html')

@csrf_exempt
def sidebarpage(request):
    return render(request,'adminTemplate/sidebar.html')

@csrf_exempt
def headerpage(request):
    return render(request,'adminTemplate/header.html')

@csrf_exempt
def loginpage(request):
    return render(request,'login.html')

@csrf_exempt

def offer_apply(request):
    if request.method == 'POST':
        P_id= request.POST['productid']
        F_date =  request.POST['from_date']
        T_date = request.POST['to_date']
        disc= request.POST['discount']
    

        obj = Offercard()
        obj.productid=P_id
        obj.from_date = F_date
        obj.to_date = T_date
        obj.discount = disc
       
        obj.save()

    offer = Offercard.objects.all()
        # print(Offercard,'000000000')
    return render(request,'adminTemplate/offercaard.html', {'Offercard':offer})
        
    # return redirect('offer_apply')

    # return redirect("offer_apply")
    




def changeStatus_offfercard(request,id):

    print("in status")
    try:
        get_data = Offercard.objects.get(pk=id)
        if get_data.status == "True":
            get_data.status="False"
        else:
            get_data.status="True"

        get_data.save()
        return redirect('offer_apply')
    except Exception as e:
        print(e,'hhhhhhh')
        return HttpResponse('error')
  

def offer_update(request,id): 
     if request.method=='POST':
        try:
            obj = Offercard.objects.get(id=id)
            try:
                # print('bid_text', request.POST['bid_text'])
                obj.productid=request.POST['productid']
            except:
                pass
            try:
                # print('bid_title', request.POST['bid_title'])
                obj.from_date=request.POST['from_date']
            except:
                pass
            try:
                # print('bid_imagetitle', request.POST['bid_imagetitle'])
                obj.to_date=request.POST['to_date']
            except:
                pass
            try:
                # print('bid_image', request.FILES['bid_imagesss'])
                obj.discount=request.POST['discount']
            except:
                pass
            try:
                # print('bid_image', request.FILES['bid_imagesss'])
                obj.createDate=request.POST['createDate']
            except:
                pass
            try:
                # print('bid_image', request.FILES['bid_imagesss'])
                obj.updateDate=request.POST['updateDate']
            except:
                pass
            obj.save()
            messages.success(request, 'Information Updated Successfully')

            return redirect('offer_apply')
        except Exception as e:
            print(e) 
     return render(request,'adminTemplate/offercaard.html')

@csrf_exempt
def delete_offer(request,id):
    P_id = Offercard.objects.get(id=id)
    print('t_text',P_id)
    P_id.delete()
    return redirect('offer_apply')


#################################################product################################################
@csrf_exempt
def product(request):
    results = Product.objects.all() 
    return render(request,'adminTemplate/product.html',{'results': results})

@csrf_exempt
def productInsert(request):

    if request.method == 'POST':
        try:
            user=request.POST['userId']
            userobj=request.POST['userId']
            # Categoryid=request.POST['categoryId']
            # catobj=Category.objects.get(id=Categoryid)
        except:
         pass
        ProductName=request.POST['productName']
        ProductDescription=request.POST['productDescription']
        ProductTitle=request.POST['productTitle']
        Thumbnail=request.FILES['myFile']
        ProductQty=request.POST['Productqty']
        Image=request.FILES['File']
        print(Image,'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        Price=request.POST['price']
        Gst=request.POST['gst']
        Discount=request.POST['discount']
        DiscountPrice=request.POST['discount-price']
        Finalprice=request.POST['final-price']
        
        form=Product(userid=userobj,productThumbnail=Thumbnail,productname=ProductName,productdescription=ProductDescription,
                     productimages=Image,productprice=Price,productdiscountPercentage=Discount,productdiscountPrice=float(DiscountPrice),
                     productfinalPrice=float(Finalprice),gsttax=Gst,productqty=ProductQty,productmetaTitle=ProductTitle)
        
        form.save()
        messages.success(request, 'Image Added Successfully')
        
        return redirect('/product')


def productUpdate(request,id):
    print('hello')
    i= Product.objects.get(id=id)
    if request.method == 'POST':
       try:
            i.productimages= request.FILES['File'] 
            i.productThumbnail= request.FILES['myFile'] 
            userobj=User.objects.get(id=user)
            i.userid=userobj

       except:
        pass
        # categoryid=request.POST['categoryId']
        # catobj=Category.objects.get(id=categoryid)
        user=request.POST['userId']
        i.productname=request.POST['productName']
        i.productdescription=request.POST['productDescription']
        i.productprice=request.POST['price']
        i.productdiscountPercentage=request.POST['discount']
        i.productdiscountPrice=request.POST['discount-price']
        i.gsttax=request.POST['gst']
        i.productfinalPrice=request.POST['final-price']
        i.productqty=request.POST['Productqty']
        i.productmetaTitle=request.POST['productTitle']
        
        # i.categoryid=catobj
        i.save()

        messages.success(request, 'Image Updated Successfully')
    
        return redirect("/product")
    return render(request,'adminTemplate/product.html')


def productDelete(request,id):
    i=Product.objects.get(id=id)
    i.delete()
    return redirect('/product')


######################### Producrt-Review ##############################

@csrf_exempt
def product_review(request): 
    results = ProductReview.objects.all() 
    return render(request,'adminTemplate/product-review.html' , {'results': results})

def Insertreview(request):
    if request.method == 'POST':
        product_name =  request.POST['product_name']
        R_description = request.POST['reviewDescription']
        R_rating= request.POST['reviewRating']
        R_title= request.POST['reviewTitle']
        U_id= request.POST['user']  
        
        R_image = request.FILES['reviewimage']
      
    

        obj = ProductReview()
        obj.user=U_id
        obj.product_name = product_name
        obj.reviewDescription = R_description
        obj.reviewRating = R_rating
        obj.reviewTitle = R_title
        obj.reviewImage = R_image
       
        obj.save()

   
    results = ProductReview.objects.all() 
        # print(Offercard,'000000000')
    return render(request,'adminTemplate/product-review.html' , {'results': results})

def update_review(request,id): 
    if request.method=='POST':
        try:
            obj = ProductReview.objects.get(id=id)
            try:
                # print('bid_text', request.POST['bid_text'])
                obj.product_name=request.POST['product_name']
            except:
                pass
            try:
                # print('bid_title', request.POST['bid_title'])
                obj.reviewDescription=request.POST['R_description']
            except:
                pass
            try:
                # print('bid_imagetitle', request.POST['bid_imagetitle'])
                obj.reviewRating=request.POST['R_rating']
            except:
                pass
            try:
                # print('bid_image', request.FILES['bid_imagesss'])
                obj.reviewTitle=request.POST['R_title']
            except:
                pass
            
            try:
                # print('bid_image', request.FILES['bid_imagesss'])
                obj.reviewImage=request.FILES['R_image']
            except:
                pass

            obj.save()
            results = ProductReview.objects.all()
            messages.success(request, 'Information Updated Successfully')

            return redirect('product-review')
        except Exception as e:
            print(e) 
    return render(request,'adminTemplate/product-review.html'  ,{'results': results})


def Delte_Review(request,id):
    i=ProductReview.objects.get(id=id)
    i.delete()
    return redirect('/product-review')

################## USer CART ########################


@csrf_exempt
def user_cart(request): 
    if request.method == 'POST':
       
        user= request.POST['user']
        x = User.objects.get(id=user)
        cart_product =  request.POST['product']
        y = Product.objects.get(id=cart_product)
        Qty = request.POST['orderQty']
        
        obj = UserCart()
        obj.user=x
        obj.product = y
        obj.orderQty = Qty
       
       
        obj.save()
    user = User.objects.all()
    product = Product.objects.all()
    data = UserCart.objects.all() 
    return render(request,'adminTemplate/usercaart.html' , {'UserCart': data,'users':user,'Product':product})
@csrf_exempt
def usercart_update(request,id):
    if request.method=='POST':
        try:
            obj = UserCart.objects.get(id=id)
            try:

                y = Product.objects.get(id=request.POST['product'])
                # print('bid_text', request.POST['bid_text'])
                # obj.product=request.POST['product']
                obj.product = y
            except:
                pass
            try:
                # print('bid_title', request.POST['bid_title'])
                obj.orderQty=request.POST['orderQty']
            except:
                pass
        except Exception as e:
              print(e) 
    return redirect('/usercart')


@csrf_exempt
def Delte_usercart(request,id):
    x=UserCart.objects.get(id=id)
    x.delete()
    return redirect('/usercart')

@csrf_exempt
def order_management(request):
    return render(request,'adminTemplate/order.html'  )
