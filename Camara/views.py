from django.shortcuts import render ,HttpResponse,redirect
from django.http import StreamingHttpResponse
from .camera import VideoCamera



def entrenamiento(request):
	return render(request, "Camara/home.html")
	#return HttpResponse ("hello")	

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
					b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



def entrenar(request):
	#camObj = Camera.objects.get(pk=camID)

	
	#camIP = "rtsp://%s:%s@%s/" %(camObj.auth_uname, camObj.auth_pwd, camObj.ip)

	
	repsone = gen(VideoCamera())
	
	return  StreamingHttpResponse(repsone,content_type='multipart/x-mixed-replace; boundary=frame')

