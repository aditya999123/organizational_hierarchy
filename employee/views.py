from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
from django.core.exceptions import ObjectDoesNotExist,ValidationError
@csrf_exempt
def main(request):
	response={}
	if request.method=="GET":
		form_email=request.GET.get('email')
		try:
			employee=employee_data.objects.get(email=form_email)
			response['success']=True
			response['message']="employee details found"
			response['employee_name']=employee.name
			try:
				response['employee_manager_email']=employee.manager.email
				response['employee_manager_name']=employee.manager.name
			except Exception,e:
				print e
		except Exception,e:
			print e
			response['success']=False
			response['message']="email not found"

		return JsonResponse(response)

	if request.method=="POST":
		form_email=request.POST.get('email')
		form_manager_email=request.POST.get('manager_email')
		form_name=request.POST.get('name')

		try:
			employee=employee_data.objects.get(email=form_email)
			try:
				manager=employee_data.objects.get(email=form_manager_email)
				flag=True
				manager_tmp=manager
				while manager_tmp.manager:
					if manager_tmp.manager==employee:
						flag=False
						break
					manager_tmp=manager_tmp.manager

				if flag==True:
					response['success']=True
					response['message']="updated"
					employee.manager=manager
					employee.save()
					response['employee_name']=employee.name
					response['employee_manager_email']=employee.manager.email
					response['employee_manager_name']=employee.manager.name
				else:
					response['success']=False
					response['message']="pls check the data looping condition"
			except ObjectDoesNotExist:
				response['success']=False
				response['message']="manager not found"
			
			#response['message']="email already registered"
		except:
			try: 
				manager=employee_data.objects.get(email=form_manager_email)
				employee=employee_data.objects.create(email=form_email,name=form_name,manager=manager)
				response['success']=True
				response['message']="employee registered"
				response['employee_name']=employee.name
				response['employee_manager_email']=employee.manager.email
				response['employee_manager_name']=employee.manager.name
			except ObjectDoesNotExist:
				response['success']=False
				response['message']="manager not found"
			except ValidationError:
				response['success']=False
				response['message']="check your data"
		return JsonResponse(response)

def tree(request):
	form_email=request.GET.get('email')
	response={}
	try:
		employee=employee_data.objects.get(email=form_email)
		response['success']=True
		manager_hierarchy=employee.name
		while employee.manager :
			manager_hierarchy+="->"+employee.manager.name
			employee=employee.manager
		response['hierarchy']=manager_hierarchy
	except ObjectDoesNotExist:
		response['success']=False
		response['message']="email not found"
	except Exception,e:
		response['success']=False
		response['message']=str(e)
	return JsonResponse(response)