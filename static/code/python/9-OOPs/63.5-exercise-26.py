"""Smart Home Device Tracker

You’re building a Smart Home Device Tracker to monitor the status of electronic devices.


Your Tasks:

1. Create a class called SmartDevice.

 Add a class attribute brand = "HomeTech" (default manufacturer).
 In the constructor, accept:
     device_name: Name of the smart device.
     power_status: True (ON) or False (OFF).

2. Shadow the class attribute brand by assigning self.brand = "CustomBrand" (to simulate user modification).

3. Define a method get_status():
    Returns a string like: "AC is ON - CustomBrand" or "Fan is OFF - CustomBrand" based on power_status.

"""


class SmartDevice:
    brand = "HomeTech"

    def __init__(self, device_name: str, power_status: bool) -> None:
        self.brand = "CustomBrand"
        self.device_name = device_name
        self.power_status = power_status

    def get_status(self):
        return f"{self.device_name} is {'ON' if self.power_status else 'OFF'} - {self.brand}"
