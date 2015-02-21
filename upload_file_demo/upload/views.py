# coding=utf8
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponse
from upload_file_demo import settings
import os

# Create your views here.

@csrf_exempt
def upload(request):
	if request.method == 'GET':
		return render_to_response('upload.html', {})
	else:
		file = request.FILES.get('file')
		save_path = settings.MEDIA_ROOT + 'upload/'
		if not os.path.isdir(save_path):
			os.makedirs(save_path)
		if file:
			print file.name
			destination = open(save_path + file.name, 'wb+')
			for chunk in file.chunks():
				destination.write(chunk)
			destination.close()
		return HttpResponse(save_path + file.name)

