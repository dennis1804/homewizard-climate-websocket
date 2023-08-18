from dataclasses import dataclass
from enum import Enum
from typing import Optional

from dataclasses_json import dataclass_json


class HomeWizardClimateDeviceType(Enum):
    """Only devices with these defined types will be picked
    up by the API function get_devices"""

    HEATERFAN = "heaterfan"
    INFRAREDHEATER = "infraredheater"
    HEATER = "heater"
    FAN = "fan"
    DEHUMIDIFIER = "dehumidifier"
    AIRCONDITIONER = "airconditioner"
    AIRCOOLER = "aircooler"

@dataclass_json
@dataclass
class HomeWizardClimateDevice:
    name: Optional[str]
    identifier: str
    grants: Optional[list]
    type: Optional[HomeWizardClimateDeviceType]
    endpoint: Optional[str]
