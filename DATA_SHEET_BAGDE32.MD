# USO DE PINES
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

![BADGE VISTA Frontal][img1]
[img1]: https://github.com/FunPythonEC/FIT_Guatemala_2019-SMART_BADGE/blob/master/imagenes/Badge%20vista%20frontal.png "PCB Vista Frontal"

# DISPOSITIVOS
## Acelerometro/Giroscopio - I2C
ESP32 | MMA8425QT
--- | ---
SCL 22 | SCL 4
SDA 23 | SDA 6

## Temperatura, humedad y presión atmosférica - I2C
ESP32 | BME280
--- | ---
SCL 22 | SCK 4
SDA 23 | SDI 3
## Matriz led 8x8 - SPI
ESP32 | MAX7219CWG+
--- | ---
5V | VCC 
GND | GND
MOSI 16 | DIN 1
CS 17 | CS 12
SCK 21 | CLK 13