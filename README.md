# ProyectoFinal-IoT


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
Josué Alejandro Esparza Padilla: https://drive.google.com/file/d/1-nsTV0iryaN9tFp5LStEGNHwuMFW3VTe/view?usp=sharing
Gilberto Fabián Correa González: https://drive.google.com/drive/folders/1kzr3NfpPYH7GMNnTBrtTDboUlttILUpK?usp=sharing

## Video demostrativo de Funcionalidad
https://github.com/user-attachments/assets/344dd0d4-f285-46c9-9620-870c82d8f39a




