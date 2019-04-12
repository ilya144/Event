from django.shortcuts import render

from django.http import HttpResponse
from .models import Event, User, Tag
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
import json

def main(request):
	return HttpResponse("Hey Guyz")

@csrf_exempt
def setUser(request):
	if request.method == 'OPTIONS':
		s_resp = HttpResponse("SALAM")#, content_type='text/json')
		s_resp.__setitem__("Access-Control-Allow-Origin","*")
		s_resp.__setitem__("Access-Control-Allow-Methods","GET, PUT, PATCH, POST, DELETE")
		s_resp.__setitem__("Access-Control-Allow-Headers","access-control-allow-credentials,\
access-control-allow-headers,access-control-allow-methods,access-control-allow-origin,\
content-type,x-content-type-options")
		return s_resp

	if request.method == 'POST':
		payload = json.loads(request.body)
		user_name = payload['name']
		user_age = payload['age']
		user_sex = payload['sex']
		user_tags = payload['tags']
		user_number = payload['number']
		user_fullname = payload['fullname']
		user_city = payload['city']
		user_password = payload['password']
		parsed_tags = []
		for tag in user_tags:
			try:
				t = Tag.objects.get(name=tag)
				parsed_tags.append(t)
			except:pass
		user = User(name=user_name,age=user_age,sex=user_sex,number=user_number,
		fullname=user_fullname,city=user_city,password=user_password)
		try:
			for tag in parsed_tags:
				user.tags.add(tag)
			user.save()
			response = json.dumps({'response':'success'})
		except Exception as e:
			response = json.dumps({'response':'error=%s'%str(e)})
		
		s_resp = HttpResponse(response, content_type='text/json')
		s_resp.__setitem__("Access-Control-Allow-Origin","*")
		s_resp.__setitem__("Access-Control-Allow-Methods","GET, PUT, PATCH, POST, DELETE")
		s_resp.__setitem__("Access-Control-Allow-Headers","Content-Type")
		return s_resp

def getUser(request, user_name):
	if request.method == 'GET':
		try:
			user = User.objects.get(name=user_name)
			response = json.dumps({'type':'User','name':user.name,"age":user.age,"sex":user.sex,
			#"tags":user.tags,
			"number":user.number,"fullname":user.fullname,"city":user.city,
			"password":user.password})
		except Exception as e:
			response = json.dumps({'Error':'e=%s'%str(e)})
		return HttpResponse(response, content_type='text/json')

@csrf_exempt
def setEvent(request):
	if request.method == 'POST':
		payload = json.loads(request.body)
		event_name = payload['name']
		event_date = payload['date']
		event_description = payload['description']
		event_tags = payload['tags']
		event_duration = payload['duration']
		event_coords = payload['coords']
		parsed_tags = []
		for tag in event_tags:
			try:
				t = Tag.objects.get(name=tag)
				parsed_tags.append(t)
			except:pass

		event = Event(name=event_name,date=parse_datetime(event_date),description=event_description,
				duration=parse_datetime(event_duration),coords=event_coords)
		try:
			event.save()
			response = json.dumps({'response':'success'})
		except Exception as e:
			response = json.dumps({'response':'error e= %s'%str(e)})
		
		return HttpResponse(response, content_type='text/json')

def getEvent(request, event_name):
	if request.method == 'GET':
		try:
			event = Event.objects.get(name=event_name)
			response = json.dumps({'type':'Event','name':event.name})
		except:
			response = json.dumps({'Error':'can not find event'})
		
		return HttpResponse(response, content_type='text/json')


