import logging
import os
import time

from homewizard_climate_ws.api.api import HomeWizardClimateApi
from homewizard_climate_ws.ws.hw_websocket import HomeWizardClimateWebSocket
from homewizard_climate_ws.model.climate_device import HomeWizardClimateDeviceType

logging.basicConfig(level=logging.DEBUG)


def main():
    username = os.environ["HW_CLIMATE_USERNAME"]
    password = os.environ["HW_CLIMATE_PASSWORD"]
    api = HomeWizardClimateApi(username, password)
    api.login()
    devices = api.get_devices()


    for device in devices:
        if device.type in HomeWizardClimateDeviceType:
            print(device.name + ' is an: ' + device.type.value)
            test_device(api, device)
        else:
            print('device not found')
    return


def sleep_and_set(ws, function, value):
    time.sleep(2)
    set_f = f"set_{function}"
    if hasattr(ws, set_f) and callable(func := getattr(ws, set_f)):
        func(value)
    else:
        print(set_f + ' not found')


def test_device(api, device):
    ws = HomeWizardClimateWebSocket(api, device)
    ws.connect_in_thread()


    if device.type == HomeWizardClimateDeviceType.INFRAREDHEATER:
        sleep_and_set(ws, 'target_temperature', 20)

    if device.type == HomeWizardClimateDeviceType.DEHUMIDIFIER:
        sleep_and_set(ws, 'mode', 'dehumidify') # [dehumidify, fan, laundry, continuous, automatic]
        sleep_and_set(ws, 'target_humidity', 50) # [0-100]
        sleep_and_set(ws, 'fan_speed', 'low') # ['low', 'high']
        sleep_and_set(ws, 'swing', True) # [boolean]

    ws.disconnect()


if __name__ == "__main__":
    main()
