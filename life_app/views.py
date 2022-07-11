from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from life_store import settings
from life_app.models import cart1
from PIL import Image,ImageDraw,ImageFont
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.

def index(request):
	return render(request,"index.html")

def lifestyle(request):
	return render(request,"lifestyle.html")

def signup(request):
	form = UserReg(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect("login_2")

	return render(request,"signup.html",{"form":form})

def login_2(request):
	return render(request,"login_2.html")

def login(request):
	if request.method=="POST":
		uname1=request.POST["uname"]
		password1=request.POST["pswd"]

		user = auth.authenticate(username=uname1,password=password1)
		print(user)
		if user:
			auth.login(request, user)
			return redirect("afterlog")
		else:
			messages.info(request,"Invalid Username or Password")
			return redirect("home")

	return render(request,"login.html")

def change(request):
	if request.method == "POST":
		fm=PasswordChangeForm(user=request.user, data=request.POST)
		if fm.is_valid():
			fm.save() 
			return redirect("afterlog")
	else:
		fm = PasswordChangeForm(user=request.user)
	return render(request,"change.html",{'form':fm})

def home(request):
	return render(request,"home.html")



def cameras(request):
	return render(request,"cameras.html")

def cart(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()

		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart.html")

def cart_1(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()

		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_1.html")

def cart_2(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_2.html")

def cart_3(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_3.html")

def cart_4(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_4.html")


def cart_5(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_5.html")


def cart_6(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_6.html")

def cart_7(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_7.html")

def cart_8(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_8.html")

def cart_9(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_9.html")

def cart_10(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_10.html")


def cart_11(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_11.html")


def cart_12(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_12.html")

def cart_13(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_13.html")

def cart_14(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_15.html")

def cart_15(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_15.html")

def cart_16(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_16.html")


def cart_17(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_17.html")


def cart_18(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_18.html")

def cart_19(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_19.html")

def cart_20(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_20.html")

def cart_21(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_21.html")

def cart_22(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_22.html")


def cart_23(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_23.html")




def cart_24(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_24.html")




def cart_25(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_25.html")




def cart_26(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_26.html")




def cart_27(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_27.html")




def cart_28(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_28.html")




def cart_29(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_29.html")




def cart_30(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_30.html")




def cart_31(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_31.html")




def cart_32(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_32.html")




def cart_33(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_33.html")




def cart_34(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_34.html")




def cart_35(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		#pnum1=request.POST["pnum"]
		pcost1=request.POST["pcost"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1}
		
		return render(request,"concart.html")
	return render(request,"cart_35.html")

def cart_36(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		pcost1=request.POST["pcost"]
		pcost2=request.POST["pcost1"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,p_cost2= pcost2,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1,"p_cost2":pcost2}
		
		return render(request,"concart.html")
	return render(request,"cart_36.html")

def cart_37(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		pcost1=request.POST["pcost"]
		pcost2=request.POST["pcost1"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,p_cost2= pcost2,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1,"p_cost2":pcost2}
		
		return render(request,"concart.html")
	return render(request,"cart_37.html")

def cart_38(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		pcost1=request.POST["pcost"]
		pcost2=request.POST["pcost1"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,p_cost2= pcost2,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1,"p_cost2":pcost2}
		
		return render(request,"concart.html")
	return render(request,"cart_38.html")

def cart_39(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		pcost1=request.POST["pcost"]
		pcost2=request.POST["pcost1"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,p_cost2= pcost2,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1,"p_cost2":pcost2}
		
		return render(request,"concart.html")
	return render(request,"cart_39.html")

def cart_40(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		pcost1=request.POST["pcost"]
		pcost2=request.POST["pcost1"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,p_cost2= pcost2,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1,"p_cost2":pcost2}
		
		return render(request,"concart.html")
	return render(request,"cart_40.html")

def cart_41(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		pcost1=request.POST["pcost"]
		pcost2=request.POST["pcost1"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,p_cost2= pcost2,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1,"p_cost2":pcost2}
		
		return render(request,"concart.html")
	return render(request,"cart_41.html")


def cart_42(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		pcost1=request.POST["pcost"]
		pcost2=request.POST["pcost1"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,p_cost2= pcost2,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1,"p_cost2":pcost2}
		
		return render(request,"concart.html")
	return render(request,"cart_42.html")
	

def cart_43(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		pcost1=request.POST["pcost"]
		pcost2=request.POST["pcost1"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,p_cost2= pcost2,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1,"p_cost2":pcost2}
		
		return render(request,"concart.html")
	return render(request,"cart_43.html")
	

def cart_44(request):
	if request.method=="POST":
		pname1=request.POST["pname"]
		pcost1=request.POST["pcost"]
		pcost2=request.POST["pcost1"]
		uname1=request.POST["cname"]

		data_db_table = cart1( p_name= pname1,
								p_cost= pcost1,p_cost2= pcost2,u_name= uname1,)

		data_db_table.save()


		data = {"p_name":pname1,"p_cost":pcost1,"p_cost2":pcost2}
		
		return render(request,"concart.html")
	return render(request,"cart_44.html")


def children(request):

	return render(request,"children.html")	

def cre_deb(request):
	return render(request,"cre_deb.html")	

def discount(request):
	return render(request,"discount.html")	

def netbank(request):
	return render(request,"netbank.html")	

def others(request):
	return render(request,"others.html")	

def contin(request):
	return render(request,"contin.html")

def afterlog(request):
	return render(request,"afterlog.html")

def concart(request):
	return render(request,"concart.html")

def payment(request):
	return render(request,"payment.html")

def phone(request):
	return render(request,"phone.html")

def shirt(request):
	return render(request,"shirt.html")

def success(request):
	return render(request,"success.html")

def watches(request):
	return render(request,"watches.html")

def payment1(request,Id):
	data=cart1.objects.get(id=Id)
	data.delete()
	return redirect("payment")

def cart_p(request):
	data1=User.objects.all()
	data = cart1.objects.all() 
	data2= cart1.objects.filter(u_name=request.user)
	return render(request,"cart1.html",{"data":data2})

def delete(request):
	cart1.objects.filter(u_name=request.user).delete()
	return render(request,"delete.html")