import time
import board
import adafruit_mcp9808

# Initialize I2C bus and sensor
i2c = board.I2C() 
mcp = adafruit_mcp9808.MCP9808(i2c)

while True:
    tempC = mcp.temperature
    tempF = tempC * 9 / 5 + 32
    print(f"Temperature: {tempC:.2f} C | {tempF:.2f} F")
    time.sleep(2)
