import logging
import os
import time

from homewizard_climate_websocket.api.api import HomeWizardClimateApi
from homewizard_climate_websocket.ws.hw_websocket import HomeWizardClimateWebSocket

logging.basicConfig(level=logging.DEBUG)


def main():
    username = os.environ["HW_CLIMATE_USERNAME"]
    password = os.environ["HW_CLIMATE_PASSWORD"]
    api = HomeWizardClimateApi(username, password)
    api.login()
    devices = api.all_devices()
    print(devices)

    ws = HomeWizardClimateWebSocket(api, devices[0])
    ws.connect_in_thread()
    time.sleep(5)
    print(ws)
    ws.disconnect()



if __name__ == "__main__":
    main()
