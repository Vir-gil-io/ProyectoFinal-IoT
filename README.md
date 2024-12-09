# ProyectoFinal-IoT

## Descripción
El proyecto consiste en un modelo basado en el diseño de la casa poseída en la película "Monster House", con la diferencia de que ésta tiene ambientación en la época navideña y algunas modificaciones para que se adaptara a las funcionalidades requeridas.<br><br>
**Las funciones incluyen:** <br>
1. Detección de proximidad por medio del sensor HC-SR04. 
2. Reproducción de una melodía navideña en el BUZZER cuando el sensor detecte un objeto. 
3. Dibujar un patrón en la MATRIZ DE LEDS que simule un copo de nieve que cambia de color al ritmo de la melodía del buzzer.
4. Detección de luminosidad por medio del sensor de luz con FOTORRESISTENCIA.
5. Encendido de una tira de 60 leds RGB con colores cambiantes cuando el sensor de luz detecte una baja luminosidad, además su total apagado cuando el sensor detecta cierto nivel de luz.
6. Movimiento constante de un SERVOMOTOR en el brazo de la casa a forma de saludo.
7. Impresión de una animación constante de nieve en la pantalla OLED, junto con el mensaje predeterminado "Feliz Navidad".
8. Conexión a NodeRed que permite la funcionalidad de imprimir mensajes a la pantalla desde cualquier dispositivo conectado al tópico del proyecto. <br>
## Componentes
|Material|Imagen|Cantidad|Costo (Apox.)|
|--|--|--|--|
|ESP32|<img src="https://github.com/user-attachments/assets/0d280367-493e-4f7c-a587-36e1f822116b" width="100"/>|2|120.00|
|MATRIZ DE LEDS|<img width="100" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTENQ6honfL0WvZ0XYN-WbPz7JrYpkudmQFYg&s" />|1|60.00|
|TIRA DE LEDS (60)|<img width="100" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjeE5gji1IRL2b-S5EghKQjEpJK-Q9LI-_cw&s" />|1|90.00|
|PHOTORESISTOR-SENSOR|<img width="100" src="https://alltopnotch.co.uk/wp-content/uploads/imported/4/LDR-Photoresistor-Light-Detection-Sensor-Module-Dependent-Resistor-Arduino-PIC-362145909694-3.JPG" />|1|50.00|
|SERVO|<img width="100" src="https://www.mechatronicstore.cl/wp-content/uploads/2015/08/SKU054531.1.jpg" />|1|50.00|
|BUZZER|<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQShCbOeHSNx-_OkSdgj1kg3Fn8wKLCkxekNg&s" width="100"/>|1|30.00|
|HC-SR04|<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8RhY2WCVB4WZCBySU1FR5KF-Ds7ZyQlg03A&s" width="100"/>|1|30.00|
|OLED|<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSM7bEGwsiwBxBrW8jsNhEiCrZXyI85X5rDAA&s" width="100"/>|1|60.00|

## Proceso de elaboración
Primero hichimos la casa de madera, la cual incluye tres ventanas y una puerta pequeña para que salgan los cables para conectar, después la pintamos y la decoramos con temática navideña, armamos el circuito junto y programamos el código en MicroPython para posteriormente acomodar todo dentro de la casa de manera que el circuito no fuera visible y todo funcionara correctamente.<br>
<img src="https://github.com/user-attachments/assets/a9ada43b-938f-43a4-bbc6-c2b4211389e4" width="400"/>
<img src="https://github.com/user-attachments/assets/3863b20d-4752-4b90-89ab-2b255c8dd7e2" width="400"/><br>
<img src="https://github.com/user-attachments/assets/b04141e2-7062-4e5a-9e24-0ed135707653" width="400"/>
<img src="https://github.com/user-attachments/assets/57ef6eba-ade8-4aee-939b-e54b4c24a7bd" width="400"/><br>
<img src="https://github.com/user-attachments/assets/04575e6f-0b8a-46b1-840c-7f93d16de928" width="400"/>
<img src="https://github.com/user-attachments/assets/6260603a-795d-48e5-ad2c-83b39100fc32" width="400"/><br>
<img src="https://github.com/user-attachments/assets/443133ad-8f39-4f9f-8f45-e820b37f0bee" width="400"/>
<img src="https://github.com/user-attachments/assets/e82845fe-bc71-4f57-961e-da0b0451dc31" width="400"/><br>
<img src="https://github.com/user-attachments/assets/b05af0de-ecad-446a-be21-67fee278accb" width="400"/>


## Enlace de TikTok
https://vm.tiktok.com/ZMkRSn4YJ/


## Evidencias del curso de JavaScript
Josué Alejandro Esparza Padilla: <br>
Examen 1: <br>
<img src="https://github.com/user-attachments/assets/5da97270-1a3f-4de8-87df-e510efebf8a7" width="550"/><br>
Examen 2: <br>
<img src="https://github.com/user-attachments/assets/a2683086-4414-45df-bd01-2248c13d30e4" width="550"/><br>
Examen 3: <br>
<img src="https://github.com/user-attachments/assets/c200709d-51d4-4b44-ba5d-3cf41ec843b4" width="550"/><br>
Examen 4: <br>
<img src="https://github.com/user-attachments/assets/6c420b05-a3cf-49f8-8714-d1b23dd93b0e" width="550"/><br>
Examen 5: <br>
<img src="https://github.com/user-attachments/assets/407b6e25-0c22-4c96-b445-50efd119e2c7" width="550"/><br>
Examen 6: <br>
<img src="https://github.com/user-attachments/assets/b765fa1e-4ce4-4cc9-be2b-f09690e51353" width="550"/><br>
Examen Final: <br>
<img src="https://github.com/user-attachments/assets/a95c4a27-210c-45be-8a6d-96b70bfa6397" width="550"/><br>



Gilberto Fabián Correa González: <br>
Examen 1: <br>
<img src="https://drive.google.com/uc?export=view&id=12WUhjYDxUkDFf0PJhSFZBqX42xf1uJiE" width="600"/><br>
Examen 2: <br>
<img src="https://drive.google.com/uc?export=view&id=19nDoMcx16OmnDF78oq5TOhjSFCUsn_Ql" width="600"/><br>
Examen 3: <br>
<img src="https://drive.google.com/uc?export=view&id=1bjfXxiHTjouzkbq8VM9RFQA5pNFdZVQL" width="600"/><br>
Examen 4: <br>
<img src="https://drive.google.com/uc?export=view&id=1fOt4Uwr8uoMsutGRm5m7W5LZ_DGqqbbl" width="600"/><br>
Examen 5: <br>
<img src="https://drive.google.com/uc?export=view&id=1wM3V1rU13bAt7MIWaLJbFAAIVPtgXYx1" width="600"/><br>
Examen 6: <br>
<img src="https://drive.google.com/uc?export=view&id=15c3RvXZReFKK9xcu5lmwhCNCNGklf-O7" width="600"/><br>
Examen Final: <br>
<img src="https://drive.google.com/uc?export=view&id=1BjOYC6k1JFxT0HGbeOXb923ly_6fi8zD" width="600"/><br>

## Video demostrativo de Funcionalidad
https://github.com/user-attachments/assets/737599c1-ea05-44d1-b729-f50ec611af93




