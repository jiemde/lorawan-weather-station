from config import dev_eui, app_eui, app_key, dev_addr, nwk_swkey, app_swkey
from lora import LORA
from davis7911 import DAVIS7911
from machine import I2C
from bme280 import BME280
from lopy import LoPy
from time import sleep

## Setupfunction for LoRaWAN and Devices
def setup():
  global n, sensor_davis, sensor_bme280, sensor_lopy, sleep_time

  # Initial sleep time
  sleep_time = 10

  # Initialize LoRaWAN
  n = LORA()

  # print the dev_eui to register the device in TTN Console
  print("dev_eui = ", n.getDev_eui())

  # Connect to LoRaWAN with OTAA
  #n.connect(dev_eui, app_eui, app_key)

  # Connect to LoRaWAN with ABP
  n.connect(dev_addr, nwk_swkey, app_swkey)

  # Connect Sensors
  try:
    i2c = I2C(0)
    sensor_bme280 = BME280(i2c = i2c)
    sensor_davis = DAVIS7911()
    sensor_lopy = LoPy()
  except Exception as e:
    print("Error: ", e)
  print("Setup... done")

if __name__ == "__main__":

  # Setup network & sensors
  setup()

  while True:

    data = ""

    # Measure
    try:
      bme280_data = sensor_bme280.read_compensated_data()
      t = bme280_data[0] / 100
      p = bme280_data[1] / 25600
      h = bme280_data[2] / 1024
      s = sensor_davis.get_windspeed()
      d = sensor_davis.get_dir()
      b = sensor_lopy.get_batt()

      data = "%.1f %.1f %.1f %.1f %s %.3f" % (t, h, p, s, d, b)

    except Exception as e:
      print("Measure error: ", e)

    # Send packet
    response = n.send(data)

    sleep(sleep_time)
