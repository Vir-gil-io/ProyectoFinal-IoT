# ProyectoFinal-IoT
## Materiales
|Material|Imagen|Cantidad|Costo (Apox.)|
|--|--|--|--|
|ESP32|<img src="https://github.com/user-attachments/assets/0d280367-493e-4f7c-a587-36e1f822116b" width="100"/>|2|120.00|
|MATRIZ DE LEDS|<img width="100" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTENQ6honfL0WvZ0XYN-WbPz7JrYpkudmQFYg&s" />|1|60.00|
|TIRA DE LEDS (60)|<img width="100" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjeE5gji1IRL2b-S5EghKQjEpJK-Q9LI-_cw&s" />|1|90.00|
|PHOTORESISTOR-SENSOR|<img width="100" src="https://alltopnotch.co.uk/wp-content/uploads/imported/4/LDR-Photoresistor-Light-Detection-Sensor-Module-Dependent-Resistor-Arduino-PIC-362145909694-3.JPG" />|1|50.00|
|SERVO|<img width="100" src="https://www.mechatronicstore.cl/wp-content/uploads/2015/08/SKU054531.1.jpg" />|1|78.00|
|BUZZER|<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQShCbOeHSNx-_OkSdgj1kg3Fn8wKLCkxekNg&s" width="100"/>|1|120.00|
|HC-SR04|<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8RhY2WCVB4WZCBySU1FR5KF-Ds7ZyQlg03A&s" width="100"/>|1|120.00|
|OLED|<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSM7bEGwsiwBxBrW8jsNhEiCrZXyI85X5rDAA&s" width="100"/>|1|120.00|

## Proceso de elaboramiento
Primero hichimos la casa de madera, la cual incluye tres ventanas y una puerta pequeña para que salgas los cables para conectar, después la pintamos y la decoramos versión navideña, armamos el circuito junto con el código y después pegamos todo a la casa para terminarla.
![foto 1](https://github.com/user-attachments/assets/a9ada43b-938f-43a4-bbc6-c2b4211389e4)
![foto 2](https://github.com/user-attachments/assets/3863b20d-4752-4b90-89ab-2b255c8dd7e2)
![foto3](https://github.com/user-attachments/assets/b04141e2-7062-4e5a-9e24-0ed135707653)
![foto 4](https://github.com/user-attachments/assets/57ef6eba-ade8-4aee-939b-e54b4c24a7bd)
![foto 5](https://github.com/user-attachments/assets/04575e6f-0b8a-46b1-840c-7f93d16de928)
![foto 6](https://github.com/user-attachments/assets/6260603a-795d-48e5-ad2c-83b39100fc32)
![foto 8](https://github.com/user-attachments/assets/443133ad-8f39-4f9f-8f45-e820b37f0bee)
![foto 9](https://github.com/user-attachments/assets/e82845fe-bc71-4f57-961e-da0b0451dc31)
![foto 10](https://github.com/user-attachments/assets/b05af0de-ecad-446a-be21-67fee278accb)


## Json del Node-Red
[
    {
        "id": "3b3fad1b03b4763a",
        "type": "tab",
        "label": "Proyecto",
        "disabled": false,
        "info": "",
        "env": []
    },
    {
        "id": "4080686fde8490cd",
        "type": "mqtt out",
        "z": "3b3fad1b03b4763a",
        "name": "",
        "topic": "gds0642/gfcg",
        "qos": "2",
        "retain": "false",
        "respTopic": "",
        "contentType": "",
        "userProps": "",
        "correl": "",
        "expiry": "",
        "broker": "713aa9f5780c4c93",
        "x": 660,
        "y": 60,
        "wires": []
    },
    {
        "id": "b6cb096e9f7ff04c",
        "type": "ui_text_input",
        "z": "3b3fad1b03b4763a",
        "name": "",
        "label": "Envía un mensaje:",
        "tooltip": "",
        "group": "d7f47c1194b31d7e",
        "order": 5,
        "width": 0,
        "height": 0,
        "passthru": true,
        "mode": "text",
        "delay": 300,
        "topic": "topic",
        "sendOnBlur": true,
        "className": "",
        "topicType": "msg",
        "x": 230,
        "y": 80,
        "wires": [
            [
                "1681944a7057df4a"
            ]
        ]
    },
    {
        "id": "1681944a7057df4a",
        "type": "function",
        "z": "3b3fad1b03b4763a",
        "name": "setTexto",
        "func": "flow.set(\"texto\", msg.payload);\nreturn msg;",
        "outputs": 1,
        "timeout": 0,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 420,
        "y": 80,
        "wires": [
            []
        ]
    },
    {
        "id": "71d8c94507aee8e0",
        "type": "ui_button",
        "z": "3b3fad1b03b4763a",
        "name": "",
        "group": "d7f47c1194b31d7e",
        "order": 6,
        "width": 0,
        "height": 0,
        "passthru": false,
        "label": "Enviar",
        "tooltip": "",
        "color": "#F00",
        "bgcolor": "#FF0",
        "className": "",
        "icon": "",
        "payload": "",
        "payloadType": "str",
        "topic": "topic",
        "topicType": "msg",
        "x": 190,
        "y": 140,
        "wires": [
            [
                "116d89744c5688d4"
            ]
        ]
    },
    {
        "id": "116d89744c5688d4",
        "type": "function",
        "z": "3b3fad1b03b4763a",
        "name": "getTexto",
        "func": "msg.payload = flow.get(\"texto\");\nreturn msg;",
        "outputs": 1,
        "timeout": 0,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 420,
        "y": 140,
        "wires": [
            [
                "4080686fde8490cd"
            ]
        ]
    },
    {
        "id": "713aa9f5780c4c93",
        "type": "mqtt-broker",
        "name": "",
        "broker": "broker.emqx.io",
        "port": "1883",
        "clientid": "",
        "autoConnect": true,
        "usetls": false,
        "protocolVersion": "4",
        "keepalive": "60",
        "cleansession": true,
        "autoUnsubscribe": true,
        "birthTopic": "",
        "birthQos": "0",
        "birthRetain": "false",
        "birthPayload": "",
        "birthMsg": {},
        "closeTopic": "",
        "closeQos": "0",
        "closeRetain": "false",
        "closePayload": "",
        "closeMsg": {},
        "willTopic": "",
        "willQos": "0",
        "willRetain": "false",
        "willPayload": "",
        "willMsg": {},
        "userProps": "",
        "sessionExpiry": ""
    },
    {
        "id": "d7f47c1194b31d7e",
        "type": "ui_group",
        "name": "proy",
        "tab": "f783280b457bc79d",
        "order": 4,
        "disp": true,
        "width": "6",
        "collapse": false,
        "className": ""
    },
    {
        "id": "f783280b457bc79d",
        "type": "ui_tab",
        "name": "Dashboard",
        "icon": "dashboard",
        "order": 1,
        "disabled": false,
        "hidden": false
    }
]

## Enlace de TikTok
https://vm.tiktok.com/ZMkRSn4YJ/

## Evidencias del Proyecto
https://drive.google.com/drive/folders/1Tjwxtl1StbOPr3UWwXfeIbDp3UYEBbZY?usp=sharing

## Evidencias del curso de JavaScript
Josué Alejandro Esparza Padilla:
Examen 1:
![image](https://github.com/user-attachments/assets/5da97270-1a3f-4de8-87df-e510efebf8a7)
Examen 2:
![image](https://github.com/user-attachments/assets/a2683086-4414-45df-bd01-2248c13d30e4)
Examen 3:
![image](https://github.com/user-attachments/assets/c200709d-51d4-4b44-ba5d-3cf41ec843b4)
Examen 4:
![image](https://github.com/user-attachments/assets/6c420b05-a3cf-49f8-8714-d1b23dd93b0e)
Examen 5:
![image](https://github.com/user-attachments/assets/407b6e25-0c22-4c96-b445-50efd119e2c7)
Examen 6:
![image](https://github.com/user-attachments/assets/b765fa1e-4ce4-4cc9-be2b-f09690e51353)
Examen Final:
![image](https://github.com/user-attachments/assets/a95c4a27-210c-45be-8a6d-96b70bfa6397)



Gilberto Fabián Correa González: https://drive.google.com/drive/folders/1kzr3NfpPYH7GMNnTBrtTDboUlttILUpK?usp=sharing

## Video demostrativo de Funcionalidad
https://github.com/user-attachments/assets/737599c1-ea05-44d1-b729-f50ec611af93




