import time
import sensor
import lcd
from modules import ws2812
from machine import UART
from fpioa_manager import fm

IMAGE_QUALITY = 25      # 1 ~ 100
IMAGE_UPDATE_RATE = 20  # ms

led = ws2812(8, 100)
uart = UART(UART.UART1, 2000000)

def setLed(r, g, b):
    led.set_led(0, (r, g, b))
    led.display()

def setup():
    setLed(0x10, 0, 0)

    time.sleep_ms(200)

    sensor.reset()
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    sensor.set_vflip(1)
    sensor.set_hmirror(1)
    sensor.run(1)
    sensor.skip_frames()

    fm.register(35, fm.fpioa.UART1_TX, force=True)
    fm.register(34, fm.fpioa.UART1_RX, force=True)

    setLed(0, 0, 0x10)
    time.sleep_ms(200)
    setLed(0, 0, 0)
    lcd.init(freq=15000000)

setup()

while(True):
    img = sensor.snapshot()

    imgBuf = img.compress(quality=IMAGE_QUALITY)

    imgSize1 = (img.size() & 0xFF0000) >> 16
    imgSize2 = (img.size() & 0x00FF00) >> 8
    imgSize3 = (img.size() & 0x0000FF) >> 0

    uart.write(bytearray([0xA0, imgSize1, imgSize2, imgSize3]))

    uart.write(imgBuf)
    time.sleep_ms(IMAGE_UPDATE_RATE)

    print(img)
