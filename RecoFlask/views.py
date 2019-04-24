from RecoFlask import app
from .camera import VideoCamera
from flask import render_template

@app.route('/')
def index():
	return render_template('cam.html')

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
					b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/entrenar')
def entrenar():
	#camObj = Camera.objects.get(pk=camID)
	#camIP = "rtsp://%s:%s@%s/" %(camObj.auth_uname, camObj.auth_pwd, camObj.ip)
	response = gen(VideoCamera())
	return  StreamingHttpResponse(response,content_type='multipart/x-mixed-replace; boundary=frame')

