from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import AccountsModels,TransactionTable
from django.contrib import messages
# Create your views here.
def home(request):
	return render(request,'banktransaction/index.html')
def create_your_account(request):
	if request.method == 'POST':
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		email = request.POST.get('email')
		dob = request.POST.get('dateofbirth')
		balance = request.POST.get('balance')
		acc_num = accountNumFun()
		if AccountsModels.objects.create(firstName=firstname,lastName=lastname,email=email,dateOfBirth=dob,balance=balance,accountNumbers=acc_num):
			messages.success(request,"Account created successfully")
		else:
			messages.error(request,"Please check Your details again!")
		return redirect('view_all_customers')
	return render(request,'banktransaction/add_account.html')

def accountNumFun():
	if AccountsModels.objects.count() == 0:
		return f'{1:04d}' 
	x=AccountsModels.objects.last()
	y = int(x.accountNumbers)+1
	return f'{y:04d}'	


def view_all_customers(request):
	accmodels = AccountsModels.objects.all()
	context = {
		'accmodels':accmodels
	}
	return render(request,'banktransaction/all_customer_page.html',context)

def view_a_customer(request,pk):
	post = get_object_or_404(AccountsModels,pk=pk)
	context = {
		'post':post
	}
	return render(request,'banktransaction/a_customer_details.html',context)

def moneyTransfer(request):
	if request.method == "POST":
		fromAcc = request.POST.get("fromAccNo")
		toAcc = request.POST.get("toAccNo")
		amount = int(request.POST.get("amount"))
		try:
			temp = AccountsModels.objects.filter(accountNumbers= fromAcc)
			bal_send = temp.first().balance
			temp = AccountsModels.objects.filter(accountNumbers=toAcc)
			bal_rec = temp.first().balance
		except AttributeError:
			messages.error(request,"Transaction Failed: Account Not Found")
		else:
			if (bal_send-500)> amount:
				new_bal = bal_rec+amount
				rem_bal = bal_send-amount
				temp = AccountsModels.objects.filter(accountNumbers= fromAcc).first()
				temp.balance = rem_bal
				temp.save()
				temp = AccountsModels.objects.filter(accountNumbers= toAcc).first()
				temp.balance = new_bal
				temp.save()
				instance2 = TransactionTable.objects.create(TransactionId=transIdfun(),FromAccNo=fromAcc, ToAccNo=toAcc,Amount=amount)
				messages.success(request,"Transaction is successfull")
			else:
				messages.error(request,"Sender account's balance is insufficient")
		return redirect('view_all_customers')
	return render(request,'banktransaction/transferPage.html')


def transIdfun():
	if TransactionTable.objects.count() == 0:
		return f'{1:09d}' 
	x=TransactionTable.objects.last()
	y = int(x.TransactionId)+1
	return f'{y:09d}'