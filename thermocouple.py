import time
import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

for i in range(100):
    data = spi.readbytes(2)
    lsb = data[1]
    msb = data[0]
    tc_signal = msb / 8 * 256 + lsb / 8
    deg_celsius = tc_signal * 1023.75/4096
    deg_farenheit = 1.8 * deg_celsius + 32
    print(deg_celsius, deg_farenheit)
    time.sleep(1)
    #print('{0:b}'.format(msb))
    #print('{0:b}'.format(lsb))