# importar librerias
from machine import Pin, I2C
from utime import sleep
from dht import DHT11
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# configuracion LCD 
pin_scl = Pin(1)
pin_sda = Pin(0)
freq = 400000
i2c = I2C(0,sda=pin_sda,scl=pin_scl,freq=freq)

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

lcd = I2cLcd(i2c,I2C_ADDR,I2C_NUM_ROWS,I2C_NUM_COLS)
# fin configuracion LCD

# configuración LED y buzzer
led = Pin(15, Pin.OUT)
buzzer = Pin(14, Pin.OUT)

# configuracion DHT11
sensor_temp = DHT11(Pin(28, Pin.IN))

lcd.clear() # Borra cualquier caracter previo que 
lcd.move_to(0,0) # Posiciona el cursor en la primera columna y en el primer renglón (C, R)
lcd.putstr('Temperatura:')
lcd.move_to(0,1)
lcd.putstr('Humedad:')

while True:
    sensor_temp.measure()
    lectura_temp = sensor_temp.temperature()
    lectura_hum = sensor_temp.humidity()
    
    # si la lectura de humedad es mayor al 70%
    if lectura_hum > 70:
        led.value(1)
        buzzer.value(1)
    else:
        led.value(0)
        buzzer.value(0)
    
    # mostrar lecturas en lcd
    lcd.move_to(12,0)
    lcd.putstr(str(lectura_temp) + chr(223) + 'C')
    
    lcd.move_to(8,1)
    lcd.putstr(str(lectura_hum) + '%')
    
    sleep(1)