from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app.decorators import check_session
import json
from .models import *
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.db import IntegrityError

@csrf_exempt
@check_session
def domain(request):
    msg={"success": False, "message": "", "status" : 200}
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            domain_name = body.get('domain_name')
            if not domain_name:
                msg["message"] = "Please please the name of domain"
                msg["status"] = 400
                return JsonResponse(msg,status=msg["status"],safe=False)
            res = Domain.objects.create(name=domain_name)
            msg["message"] = f"Domain with the name {domain_name} created successfully"
            msg["success"] = True
            return JsonResponse(msg,status=msg["status"],safe=False)
        
        except IntegrityError:
            msg["message"] = f"A Domain with name {domain_name} already exists"
            msg["status"] = 500
            return JsonResponse(msg,status=msg["status"],safe=False)

        except Exception as e:
            print(str(e))
            msg["message"] = "Something went wrong"
            msg["status"] = 500
            return JsonResponse(msg,status=msg["status"],safe=False)
    
    elif request.method == "GET":
        try:
            domains = Domain.objects.all()
            res = [model_to_dict(domain) for domain in domains]
            msg["message"] = res
            msg["success"] = True
            return JsonResponse(msg,status=msg["status"],safe=False)
        except Exception as e:
            print(str(e))
            msg["message"] = "Something went wrong"
            msg["status"] = 500
            return JsonResponse(msg,status=msg["status"],safe=False)

    else:
        msg["message"] = "Method not allowed"
        msg["status"] = 400
        return JsonResponse(msg,status=msg["status"],safe=False)
    

@csrf_exempt
@check_session
def tag(request):
    msg={"success": False, "message": "", "status" : 200}
    if request.method == "POST":
        try:
            ID = request.session.get("ID")
            body = json.loads(request.body)
            domain_id = body.get('domain_id')
            tag_name = body.get('tag_name')
            if not tag_name or not domain_id:
                msg["message"] = "Please please the name of tag and domain id"
                msg["status"] = 400
                return JsonResponse(msg,status=msg["status"],safe=False)
            domain = Domain.objects.filter(id=domain_id)
            if not domain:
                msg["message"] = "No domain present for given domain id"
                msg["status"] = 400
                return JsonResponse(msg,status=msg["status"],safe=False)
            domain = domain.first()
            admin = CustomUser.objects.get(id = ID)
            res = Tag.objects.create(domain=domain,admin=admin,name=tag_name)
            msg["message"] = f"Tag with name {tag_name} created successfully"
            msg["success"] = True
            return JsonResponse(msg,status=msg["status"],safe=False)
        
        except IntegrityError:
            msg["message"] = f"A Domain with name {tag_name} already exists"
            msg["status"] = 500
            return JsonResponse(msg,status=msg["status"],safe=False)


        except Exception as e:
            print(str(e))
            msg["message"] = "Something went wrong"
            msg["status"] = 500
            return JsonResponse(msg,status=msg["status"],safe=False)
    
    elif request.method == "GET":
        try:
            ID = request.session.get("ID")
            event = request.GET.get('event')
            if event == 'all':
                tags = Tag.objects.all()
                res = [model_to_dict(tag) for tag in tags]
                msg["message"] = res
                msg["success"] = True
                return JsonResponse(msg,status=msg["status"],safe=False)
            else:
                admin = CustomUser.objects.get(id = ID)
                tags = Tag.objects.filter(admin = admin)
                res = [model_to_dict(tag) for tag in tags]
            msg["message"] = res
            msg["success"] = True
            return JsonResponse(msg,status=msg["status"],safe=False)
        except Exception as e:
            print(str(e))
            msg["message"] = "Something went wrong"
            msg["status"] = 500
            return JsonResponse(msg,status=msg["status"],safe=False)

    else:
        msg["message"] = "Method not allowed"
        msg["status"] = 400
        return JsonResponse(msg,status=msg["status"],safe=False)




        

    