import cv2
#Modulo para leer directorios y rutas de archivos
import os
#OpenCV trabaja con arreglos de numpy
import numpy
#Obtener el nombre de la persona que estamos capturando
import sys
nombre = "prueba"

face_cascade = cv2.CascadeClassifier('RecoFlask\\reconocimiento\\haarcascades\\frontalface_default.xml')

class VideoCamera(object):

	def __init__(self):
		#Directorio donde se encuentra la carpeta con el nombre de la persona
		dir_faces = 'faces'
		self.path = os.path.join(dir_faces, nombre)


		#Si no hay una carpeta con el nombre ingresado entonces se crea
		if not os.path.isdir(self.path):
		    os.mkdir(self.path)

		#cargamos la plantilla e inicializamos la webcam
		#face_cascade = cv2.CascadeClassifier('haarcascades/frontalface_default.xml')
		self.video = cv2.VideoCapture("http://192.168.43.1:8080/video")


	def __del__(self):
		self.video.release()


	def get_frame(self):
		#Tamaño para reducir a miniaturas las fotografias

		img_width, img_height = 112, 92
		size = 4

		success, image = self.video.read()

		if(not success):
			print("No se pudo leer la fuente.")
			return None

		if(face_cascade.empty()):
			print("No se pudo leer el Haar Cascade.")
			return None

		#image = cv2.flip(image, 1, 0)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		#redimensionar la imagen
		mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))



		faces = face_cascade.detectMultiScale(mini)
		faces = sorted(faces, key=lambda x: x[3])
		face_resize = cv2.resize(image, (img_width, img_height))

		for (x,y,w,h) in faces:

			face_i = faces[0]
			(x, y, w, h) = [v * size for v in face_i]
			face = gray[y:y + h, x:x + w]
			#face_resize = cv2.resize(face, (img_width, img_height))

			#Dibujamos un rectangulo en las coordenadas del rostro
			cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
			#Ponemos el nombre en el rectagulo
			cv2.putText(image, nombre, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))        



		#Obtenemos el nombre de la foto
		#Despues de la ultima sumamos 1 para continuar con los demas nombres
		pin=sorted([int(n[:n.find('.')]) for n in os.listdir(self.path)
		if n[0]!='.' ]+[0])[-1] + 1
		ret, jpeg = cv2.imencode('.jpg', image)

		#Metemos la foto en el directorio
		#cv2.imwrite('%s/%s.jpg' % (self.path, pin), face_resize)

		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.
		return jpeg.tobytes()