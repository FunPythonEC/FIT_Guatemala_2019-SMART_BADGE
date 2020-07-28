# SMART BADGE

![tarjetas_fit2019](https://raw.githubusercontent.com/FunPythonEC/ConectateGT/master/media/arcoriiris.jpeg)

<p align="center">
  <img width="640" height="480" src="/imagenes/Badge%20vista%20frontal.png">
</p>


## USO DE PINES
BADGE | GPIO | TIPO | FUNCIONES | NOTAS
--- | --- | --- | --- | ---
A0 | 26 | I/O | DAC_2, ADC2_CH9, RTC_GPIO7, EMAC_RXD1 
A1 | 25 | I/O | DAC_1, ADC2_CH8, RTC_GPIO6, EMAC_RXD0
A2 | 34 | I | ADC1_CH6, RTC_GPIO4 
A3 | 39 | I |  ADC1_CH3, RTC_GPIO3, SENSOR_VN
A4 | 36 | I |  ADC1_CH0, RTC_GPIO0, SENSOR_VP
A5 | 4 | I/O | ADC2_CH0, TOUCH0, RTC_GPIO10, HSPIHD, HS2_DATA1, SD_DATA1, EMAC_TX_ER
A6 | 14 | I/O | ADC2_CH6, TOUCH6, RTC_GPIO16, MTMS, HSPICLK, HS2_CLK, SD_CLK, EMAC_TXD2 | emite señal pmw al arranque
A7 | 32 | I/O | ADC1_CH4, TOUCH9, RTC_GPIO9, XTAL_32K_P (32.768 kHz crystal oscillator input)

Los pines **ADC** tienen una resolucion de 12 bits por defecto y devuelven valores entre 0-4095.

1 Valor de lectura, a través del rango de voltaje 0.0v - 1.0v
con el siguiente script de micropython
```python
from machine import ADC

adc = ADC(Pin(GPIO) 
adc.read()
```

2 Para leer en el rango de voltaje 0.0v - 3.6v se establece atenuación de entrada de 11dB
```python
from machine import ADC

adc = ADC(Pin(GPIO) 
adc.atten(ADC.ATTN_11DB)
adc.read()
```

3 Si se quiere un rango menor se puede configurar una resolución de 9 bits y que devolvera valores entre 0-511.
```python
from machine import ADC

adc = ADC(Pin(GPIO) 
adc.width(ADC.WIDTH_9BIT)
adc.read()
```
**I/O** = Input/Output un pin de entrada y salida

**I** = Input Pin unicamente para entrada

## DISPOSITIVOS
### LED
ESP32 | LED
--- | ---
GPIO 13 | +
GND | -


### Temperatura, humedad y presión atmosférica - I2C
ESP32 | BME280
--- | ---
SCL 22 | SCK 4
SDA 23 | SDI 3

### Acelerometro/Giroscopio - I2C
ESP32 | MMA8425QT
--- | ---
SCL 22 | SCL 4
SDA 23 | SDA 6

### Matriz led 8x8 - SPI
ESP32 | MAX7219CWG+
--- | ---
5V | VCC 
GND | GND
MOSI 16 | DIN 1
CS 17 | CS 12
SCK 21 | CLK 13
