import machine
import neopixel
import framebuf
import time
import _thread
from servo import Servo

# Configuración de la matriz NeoPixel
PIN = 15  # Pin de datos de los NeoPixels
NUM_LEDS = 64  # 8x8 matriz tiene 64 LEDs

# Configuración del buzzer
BUZZER_PIN = 4  # Pin conectado al buzzer
buzzer = machine.PWM(machine.Pin(BUZZER_PIN))

# Configuración del sensor HC-SR04
TRIG_PIN = 12  # Pin Trigger del HC-SR04
ECHO_PIN = 13  # Pin Echo del HC-SR04


# Inicializar servos
servo = Servo(25)  # Servo en el pin 14

# Inicializa los LEDs
np = neopixel.NeoPixel(machine.Pin(PIN), NUM_LEDS)

# Definir las dimensiones de la matriz
ancho = 8
alto = 8

# Crear un buffer para el framebuffer (1 bit por píxel)
buffer = bytearray(ancho * alto // 8)

# Inicializar framebuffer en modo monocromático (1 bit por píxel)
fb = framebuf.FrameBuffer(buffer, ancho, alto, framebuf.MONO_HLSB)

# Notas musicales en Hz
DO4 = 262
RE4 = 294
MI4 = 330
FA4 = 349
SOL4 = 392
LA4 = 440
SI4 = 494
DO5 = 523
RE5 = 587

# Melodía de "Campana sobre campana" en versión piano
melody_campana = [
    # Campana sobre campana
    (MI4, FA4, SOL4, 400),
    (MI4, 0, 0, 400),
    (MI4, SOL4, 0, 200),
    (MI4, SOL4, 0, 200),
    (MI4, LA4, 0, 400),
    (FA4, LA4, 0, 400),
    (SOL4, SI4, 0, 400),
    (SOL4, SI4, 0, 400),
    (0, 0, 0, 300),
    
    # Y sobre campana una
    (MI4, SOL4, 0, 400),
    (MI4, SOL4, 0, 200),
    (MI4, SOL4, 0, 200),
    (MI4, LA4, 0, 400),
    (FA4, LA4, 0, 400),
    (SOL4, SI4, 0, 400),
    (SOL4, SI4, 0, 400),
    (SOL4, SI4, 0, 200),
    (0, 0, 0, 300),
    
    # Asómate a la ventana
    (LA4, DO5, 0, 400),
    (LA4, DO5, 0, 200),
    (LA4, DO5, 0, 200),
    (SOL4, SI4, 0, 400),
    (SOL4, SI4, 0, 400),
    (FA4, LA4, 0, 400),
    (FA4, LA4, 0, 400),
    (FA4, LA4, 0, 200),
    (FA4, LA4, 0, 200),
    
    # Verás al niño en la cuna
    (SOL4, SI4, 0, 400),
    (SOL4, SI4, 0, 200),
    (SOL4, SI4, 0, 200),
    (FA4, LA4, 0, 400),
    (FA4, LA4, 0, 400),
    (MI4, SOL4, 0, 600),
    (MI4, SOL4, 0, 400),
    (MI4, SOL4, 0, 600),
    (MI4, SOL4, 0, 400),
    
    # Final con flourish
    (DO5, RE5, SOL4, 400),
    (SOL4, SI4, MI4, 600),
    (0, 0, 0, 500),
]

# Función para generar los colores (azul y blanco para tema invernal)
def generar_color(t):
    colores_invierno = [
        (0, 0, 255),     # Azul
        (255, 255, 255), # Blanco
        (100, 149, 237)  # Azul claro
    ]
    return colores_invierno[t % len(colores_invierno)]

# Función para encender los LEDs según el framebuffer
def encender_leds(color):
    for x in range(ancho):
        for y in range(alto):
            valor = fb.pixel(x, y)
            if x % 2 == 0:  # Fila par
                index = x * alto + y
            else:  # Fila impar
                index = x * alto + (alto - 1 - y)
            if valor:
                np[index] = color
            else:
                np[index] = (0, 0, 0)
    np.write()

# Patrón de copo de nieve
patron_copo = [
    [0,0,1,0,0,1,0,0],
    [0,1,0,1,1,0,1,0],
    [1,0,1,0,0,1,0,1],
    [0,1,0,1,1,0,1,0],
    [0,1,0,1,1,0,1,0],
    [1,0,1,0,0,1,0,1],
    [0,1,0,1,1,0,1,0],
    [0,0,1,0,0,1,0,0]
]

# Dibujar el patrón de copo de nieve en el framebuffer
def dibujar_patron():
    for y in range(8):
        for x in range(8):
            fb.pixel(x, y, patron_copo[y][x])

# Función para medir la distancia con el sensor HC-SR04
def medir_distancia():
    trig = machine.Pin(TRIG_PIN, machine.Pin.OUT)
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    
    echo = machine.Pin(ECHO_PIN, machine.Pin.IN)
    pulse_time = machine.time_pulse_us(echo, 1)
    distancia = (pulse_time * 0.0343) / 2  # Convertir tiempo en distancia (cm)
    
    return distancia

# Función para reproducir la melodía
def reproducir_melodia():
    t = 0
    while True:
        for nota1, nota2, nota3, duracion in melody_campana:
            if nota1 > 0:
                buzzer.freq(nota1)
                buzzer.duty_u16(21845)  # 33% volumen para nota principal
            if nota2 > 0:
                time.sleep_ms(5)
                buzzer.freq(nota2)
                buzzer.duty_u16(10922)  # 16% volumen para armonía
            if nota3 > 0:
                time.sleep_ms(5)
                buzzer.freq(nota3)
                buzzer.duty_u16(5461)   # 8% volumen para tercera nota
                
            encender_leds(generar_color(t))
            t += 1
            
            time.sleep_ms(duracion)
            buzzer.duty_u16(0)  # Silencio

# Función para supervisar la distancia y mover el servo si es necesario
def supervisar_distancia():
    while True:
        distancia = medir_distancia()
        print("Distancia: ", distancia, "cm")
        if distancia < 100:  # Si la distancia es menor que 3 metros
            servo.move(90)  # Mueve el servo a 90 grados
        time.sleep(1)

# Iniciar los hilos
_thread.start_new_thread(reproducir_melodia, ())
_thread.start_new_thread(supervisar_distancia, ())

# El ciclo principal de la aplicación
while True:
    dibujar_patron()
    time.sleep(0.1)