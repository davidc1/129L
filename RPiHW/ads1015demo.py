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

while True:
    # Read voltage directly
    print("CH0: %.02f \t CH1: %.02f \t CH2: %.02f \t CH3: %.02f\n"%(chan0.voltage,chan1.voltage,chan2.voltage,chan3.voltage))
    print("CH0: %.02f \t CH1: %.02f \t CH2: %.02f \t CH3: %.02f\n"%(chan0.value,chan1.value,chan2.value,chan3.value))
    print("Solar cell voltage differential: %.02f"%(chan2.voltage-chan3.voltage))
    time.sleep(1)
