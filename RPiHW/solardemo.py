python
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize I2C bus and ADC
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)

# Define the analog input (Channel 0)
chan = AnalogIn(ads, ADS.P0)

print(f"{'Voltage (V)':>10}")

while True:
    # Read voltage directly
    print(f"{chan.voltage:>10.3f}")
    time.sleep(1)
