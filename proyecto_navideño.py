import network
import machine
import random
import ssd1306
from machine import Pin, ADC
from umqtt.simple import MQTTClient
from time import sleep
from servo import Servo
from _thread import start_new_thread  # Para crear hilos
import math
import neopixel  # Librería para controlar la tira de LEDs

GAMMA = 0.7
RL10 = 50


# Configuración de la pantalla OLED
i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))  # Pines I2C
oled = ssd1306.SSD1306_I2C(128, 64, i2c)  # Crear objeto de pantalla OLED

# Propiedades para conectar a un cliente MQTT
MQTT_BROKER = "broker.emqx.io"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "gds0642/gfcg"
MQTT_PORT = 1883

# Aumentar el número de copos de nieve
NUM_SNOWFLAKES = 100  # Número de copos de nieve
snowflakes = [[random.randint(0, 127), random.randint(0, 63)] for _ in range(NUM_SNOWFLAKES)]

# Inicialización de la posición del mensaje
message_y_pos = 0  # Posición vertical del mensaje (comienza en la parte superior)
message_text = "Feliz Navidad!"  # Texto predeterminado

# Configuración de los LEDs RGB
LED_PIN = 15  # Pin de control de la tira de LEDs
NUM_LEDS = 60  # Número de LEDs en la tira
led_strip = neopixel.NeoPixel(Pin(LED_PIN), NUM_LEDS)  # Inicializa la tira de LEDs

# Configuración de la fotorresistencia (LDR)
adc = ADC(Pin(34))  # Usamos el pin 34 para el LDR
adc.atten(ADC.ATTN_0DB)  # Configuración de atenuación para el rango de 0-3.3V

# Función para mostrar el mensaje en una posición vertical dinámica
def display_message(y_pos, message):
    text_width = len(message) * 8  # El ancho de cada carácter es 8 píxeles
    x_pos = (128 - text_width) // 2
    oled.text(message, x_pos, y_pos)  
    oled.show()  # Actualizar la pantalla

# Función para actualizar la animación de la nieve
def update_snow():
    for snowflake in snowflakes:
        oled.pixel(snowflake[0], snowflake[1], 1)  # Dibujar el copo de nieve
        snowflake[1] += 1  # Mover el copo hacia abajo
        
        # Reposicionar el copo si sale de la pantalla
        if snowflake[1] >= 64:
            snowflake[0] = random.randint(0, 127)
            snowflake[1] = 0

    oled.show()  # Actualizar pantalla

# Función que maneja la llegada del mensaje MQTT
def llegada_mensaje(topic, msg):
    global message_text
    print("Mensaje recibido:", msg)
    message_text = msg.decode('utf-8')  # Decodificar y actualizar el texto


# Función para subscribir al broker MQTT
def subscribir():
    client = MQTTClient(MQTT_CLIENT_ID,
                        MQTT_BROKER, port=MQTT_PORT,
                        user=MQTT_USER,
                        password=MQTT_PASSWORD,
                        keepalive=0)
    try:
        client.set_callback(llegada_mensaje)
        client.connect()
        client.subscribe(MQTT_TOPIC)
        print("Conectado a %s, en el tópico %s" % (MQTT_BROKER, MQTT_TOPIC))
    except OSError as e:
        print("Error de conexión con el broker MQTT:", e)
        return None
    return client


# Función para conectar a WiFi
def conectar_wifi():
    print("Conectando...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('UTNG_GUEST', 'R3d1nv1t4d0s#UT')
    #sta_if.connect('INFINITUM3B90', 'HbnW7aX9CZ')  # Conectar a tu red WiFi
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
    print("WiFi Conectada!")

# Función para controlar la tira de LEDs según la luz
def control_leds_luz():
    while True:
        # Leer el valor de la fotorresistencia
        light_level = adc.read()  # Lee el valor del ADC (de 0 a 4095)
        voltage = light_level / 4095.0 * 3.3
         # Evitar la división por cero, asegurándose de que el denominador no sea cero
        if voltage >= 3.3:
            voltage = 3.29  # Forzar un valor ligeramente menor que 3.3V
        
        if voltage <= 0.01:  # Si el voltaje es demasiado bajo, asignamos un valor razonable
            voltage = 0.01

        try:
            resistance = 2000 * voltage / (1 - voltage / 3.3)
        except ZeroDivisionError:
            resistance = 999999  # Valor arbitrario para la resistencia cuando ocurre un error
        #Calcular Lux
        lux = (RL10 * 1e3 * math.pow(10, GAMMA) / resistance) ** (1 / GAMMA)

        # Si la luz es baja, encender los LEDs
        if lux < 100:
            print("Lux: ", lux)
            print("Oscuro, LEDs encendidos")
            for i in range(NUM_LEDS):
                red = random.randint(0, 255)
                green = random.randint(0, 255)
                blue = random.randint(0, 255)
                led_strip[i] = (red, green, blue)  # Asigna un color aleatorio a cada LED
            led_strip.write()
        # Si la luz es alta, apagar los LEDs
        elif lux >= 200:
            print("Lux: ", lux)
            print("Totalmente iluminado, LEDs apagados")
            for i in range(NUM_LEDS):
                led_strip[i] = (0, 0, 0)  # Apaga los LEDs
            led_strip.write()

        sleep(1)  # Esperar un segundo antes de la siguiente lectura

# Conectar a WiFi
conectar_wifi()

# Subscripción al broker MQTT
client = subscribir()

#Declaración de los Leds
led = Pin(17, Pin.OUT)
led2 = Pin(5, Pin.OUT)
led.value(0)
led2.value(0)

# Crear objeto servo en los pines 2 y 14
servo = Servo(2)
servo1 = Servo(14)

# Función para el movimiento perpetuo del servo
def servo_movement():
    while True:
        for angulo in range(0, 180):  # Movimiento de 0° a 180°
            servo.move(angulo)
            servo1.move(angulo)
            sleep(0.01)  # Pausa para suavizar el movimiento
        for angulo in range(180, 0, -1):  # Movimiento de regreso de 180° a 0°
            servo.move(angulo)
            servo1.move(angulo)
            sleep(0.01)  # Pausa para suavizar el movimiento

# Iniciar el movimiento del servo en un hilo separado
start_new_thread(servo_movement, ())


# Iniciar el control de LEDs basado en luz en un hilo separado
start_new_thread(control_leds_luz, ())

# Bucle principal
oled.fill(0)  # Limpiar la pantalla antes de redibujar
display_message(message_y_pos, message_text)  # Mostrar el mensaje inicialmente

# Bucle de animación de nieve con el mensaje recibido
while True:
    oled.fill(0)  # Limpiar toda la pantalla

    # Actualizar la animación de la nieve
    update_snow()

    # Mostrar el mensaje recibido o predeterminado en la posición dinámica
    display_message(message_y_pos, message_text)

    # Actualizar la posición vertical del mensaje para que se mueva hacia abajo
    message_y_pos += 1
    if message_y_pos > 64:  # Si el mensaje sale de la pantalla, reiniciamos su posición
        message_y_pos = 0

    sleep(0.1)  # Controlar la velocidad de la animación

    # Verificar si hay nuevos mensajes MQTT sin detener el flujo
    client.check_msg()  # Esto permite que el programa continúe sin bloquearse esperando mensajes
