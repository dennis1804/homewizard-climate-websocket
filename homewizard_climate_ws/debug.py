import logging
import os
import time

from homewizard_climate_ws.api.api import HomeWizardClimateApi
from homewizard_climate_ws.ws.hw_websocket import HomeWizardClimateWebSocket

logging.basicConfig(level=logging.DEBUG)


def main():
    username = os.environ["HW_CLIMATE_USERNAME"]
    password = os.environ["HW_CLIMATE_PASSWORD"]
    api = HomeWizardClimateApi(username, password)
    api.login()
    devices = api.get_devices()
    ws = HomeWizardClimateWebSocket(api, devices[0])
    ws.connect_in_thread()

    # speed!
    time.sleep(5)
    ws.set_speed(1)
    time.sleep(5)
    ws.set_speed(3)
    time.sleep(5)

    # timer!
    time.sleep(5)
    ws.set_timer(180)
    time.sleep(5)

    # mode!
    time.sleep(5)
    ws.set_mode('normal')
    time.sleep(5)
    ws.set_mode('natural')
    time.sleep(5)


    ws.disconnect()
    time.sleep(5)


if __name__ == "__main__":
    main()
