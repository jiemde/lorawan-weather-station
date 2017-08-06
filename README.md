# LoRaWAN Weather Station

> fork of a TelenorStartIoT project, adapted to work on TheThingsNetwork

## Changing OTAA Keys

Before you can connect to LoRaWAN you need to create a ThingType and a Thing in Managed IoT Cloud (MIC) and obtain OTAA keys. Once you've got the keys, add them to the [config.py](https://github.com/roadfox/lorawan-weather-station/blob/master/config.py) file. The [lib/lora.py](https://github.com/roadfox/lorawan-weather-station/blob/master/lib/lora.py) library will make use of them.

On startup of the LoPy the dev_eui is printed on the console and can be used to register the device on TheThingsNetwork.

# Hardware

- LoPy
- Pycom expansion board
- BME280 Sensor
- Davis 6410 anemometer

The BME280 sensor will measure temperature, humidity and pressure while the Davis anemometer will measure wind speed and wind direction.

## Sensor wiring

For the BME280 the I2C bus is used. Connections are:

BM280 (Adafruit version) - Pycom expansion board pin (LoPy pin labels)

 - VIN to 3V3
 - GND to GND
 - SCK to G17 (SCL, GPIO12)
 - SDI to G16 (SDA, GPIO13)

Davis anemometer

 - PWR (red wire) to 3V3
 - GND (black wire) to GND
 - SPD (yellow wire) to G22 (P11, GPIO22)
 - DIR (green wire) to G3 (P16, ADC3)

### Specify Different Pins

The guide uses **P11** (written G22 on the expansion board) and **G3** for wind speed and wind direction respectively.
You can change these to your own by modifying `PIN_SPEED` and `PIN_DIR` in [lib/davis7911.py:10](https://github.com/roadfox/lorawan-weather-station/blob/master/lib/davis7911.py#L10).

### ADC Setup for DAVIS Winddirection

According to documentation the ADC can be setup for 3.3V on the input: https://docs.pycom.io/chapter/firmwareapi/pycom/machine/ADC.html.
This allows to connect the Davis Sensor without a Voltage divider and gives a linear value over the 360°, so you don't have to add the resistors as shown in the original TelenorStartIoT document.
