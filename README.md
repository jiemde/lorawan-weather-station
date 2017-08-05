# LoRaWAN Weather Station

> fork of a TelenorStartIoT project, adapted to work on TheThingsNetwork

## Changing OTAA Keys

Before you can connect to LoRaWAN you need to create a ThingType and a Thing in Managed IoT Cloud (MIC) and obtain OTAA keys. Once you've got the keys, add them to the [config.py](https://github.com/TelenorStartIoT/lorawan-weather-station/blob/master/config.py) file. The [lib/lora.py](https://github.com/TelenorStartIoT/lorawan-weather-station/blob/master/lib/lora.py) library will make use of them.

## Specify Different Pins

The guide uses **P11** (written G22 on the expansion board) and **G3** for wind speed and wind direction respectively.
You can change these to your own by modifying `PIN_SPEED` and `PIN_DIR` in [lib/davis7911.py:10](https://github.com/TelenorStartIoT/lorawan-weather-station/blob/master/lib/davis7911.py#L10).
