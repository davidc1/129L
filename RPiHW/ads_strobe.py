import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize I2C bus and ADC
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)

# set gain
# 1 --> +/- 4.096 V
# 2 --> +/- 2.048 V
# 4 --> +/- 1.024 V
# 8 --> +/- 0.512 V
# 16 -> +/- 0.256 V
ads.gain = 1

ads.data_rate = 3300

# Define the analog input (Channel 0)
chan0 = AnalogIn(ads, 0)
chan1 = AnalogIn(ads, 1)
chan2 = AnalogIn(ads, 2)
chan3 = AnalogIn(ads, 3)

#print(f"{'Voltage (V)':>10}")

#chan.voltage
#chan.value

# 12 bit: 0-2047

while True:

    c3VAL = chan3.value
    c3VOL = chan3.voltage
    c3RAW = (chan3.value >> 4)
    
    
    print("\r Solar cell voltage \t: %.02f"%(c3VOL),end="",flush=True)
    time.sleep(0.01)
