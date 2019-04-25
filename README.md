# RecoFlask
Aplicación WEB en Flask que utiliza [OpenCV](https://opencv.org/opencv-2-4-8/) para realizar el reconocimiento de rosotros obtenidos de un *stream* remoto.
 

## Instalación
En la carpeta raiz realizar el comando

```
pip install -e . 
```
*notese el punto al final del comando.*

Luego ejecutar:
```
python run.py 
```
## Modo de uso:
Descargar en el dispositivo móvil la aplicación [DroidCam](https://play.google.com/store/apps/details?id=com.dev47apps.droidcam&hl=en).

Alternativamente se puede usar la aplicación [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_US) de la misma forma, la URL a pegar será la que se muestre en la aplicación seguido de /video. 
### Ejemplo:

```
http://192.168.0.25:4747/video")
```

Copiar la url del feed de video en la parte que corresponde dentro del archivo camara.py.
### Ejemplo:

```
self.video = cv2.VideoCapture("http://192.168.0.25:4747/mjpegfeed?640x480")
```
Ambos dispositivos (servidor y camara) deben estar en red o visibles por internet.
