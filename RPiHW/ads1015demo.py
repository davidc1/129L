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

print(f"{'Voltage (V)':>10}")

#chan.voltage
#chan.value

# 12 bit: 0-2047

while True:

    c0VAL = chan0.value
    c0VOL = chan0.voltage
    c0RAW = (chan0.value >> 4)
    
    c1VAL = chan1.value
    c1VOL = chan1.voltage
    c1RAW = (chan1.value >> 4)
    
    c2VAL = chan2.value
    c2VOL = chan2.voltage
    c2RAW = (chan2.value >> 4)
    
    c3VAL = chan3.value
    c3VOL = chan3.voltage
    c3RAW = (chan3.value >> 4)
    
    
    print("VOLTAGE: \t CH0: %.02f \t CH1: %.02f \t CH2: %.02f \t CH3: %.02f"%(c0VOL,c1VOL,c2VOL,c3VOL))
    print("VALUE: \t CH0: %.02f \t CH1: %.02f \t CH2: %.02f \t CH3: %.02f"%(c0VAL,c1VAL,c2VAL,c3VAL))
    print("RAW: \t CH0: %.02f \t CH1: %.02f \t CH2: %.02f \t CH3: %.02f"%(c0RAW,c1RAW,c2RAW,c3RAW))
    print("Solar cell voltage differential: %.02f"%(c2VOL-c3VOL))
    print("Solar cell ADC     differential: %.02f\n"%(c2VAL-c3VAL))
    time.sleep(1)
