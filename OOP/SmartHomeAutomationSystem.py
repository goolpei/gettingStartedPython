from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, name: str, is_on: bool = False) -> None:
        self.name = name
        self._is_on = is_on

    @property
    def is_on(self) -> bool:
        return self._is_on

    def toggle_power(self) -> None:
        self._is_on = not self._is_on

    
    def __repr__(self) -> str: 
        return f'{self.__class__.__name__}(name="{self.name}", is_on={self.is_on})'

    @abstractmethod
    def perform_action(self):
        pass

class SmartLight(SmartDevice):
    def __init__(self, name: str, is_on: bool = False, brightness: int = 100) -> None:
        super().__init__(name, is_on)
        self.brightness = brightness

    @property
    def brightness(self) -> int:
        return self._brightness

    @brightness.setter
    def brightness(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError('Brightness must be of integer value.')
        if value < 0 or value > 100:
            raise ValueError('Brightness value can only be set from 0 to 100.')
        self._brightness = value

    def perform_action(self) -> str:
        if not self.is_on: self.toggle_power()
        return f"Dimming {self.name} to {self.brightness}%."

class SmartThermostat(SmartDevice):
    def __init__(self, name: str, is_on: bool = False, temperature: float = 72.0) -> None:
        super().__init__(name, is_on)
        self.temperature = temperature

    @property
    def temperature(self) -> float:
        return self._temperature

    @temperature.setter
    def temperature(self, value) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError('Temperature must be a number.')
        self._temperature = float(value)

    def perform_action(self) -> str:
        if not self.is_on: self.toggle_power()
        return f"Adjusting HVAC to {self.temperature}°F."

class SmartCamera(SmartDevice):
    def __init__(self, name: str, is_on: bool = False, is_recording: bool = False) -> None:
        super().__init__(name, is_on)
        self._is_recording = is_recording

    @property
    def is_recording(self) -> bool:
        return self._is_recording

    def toggle_record(self) -> None:
        if not self.is_on:
            self.toggle_power()
        self._is_recording = not self._is_recording

    def toggle_power(self) -> None:
        if self.is_recording: self.toggle_record()
        super().toggle_power()

    def perform_action(self) -> str:
        if self.is_recording:
            return f"Security camera is already recording live feed."
        else:
            self.toggle_record()
            return f"Security camera is now recording live feed."

class SmartHub:
    def __init__(self) -> None:
        self.devices = []

    def add_device(self, device: SmartDevice) -> None:
        self.devices.append(device)

    def execute_macro(self) -> None:
        for device in self.devices:
            print(device.perform_action())

    def emergency_shutdown(self) -> None:
        for device in self.devices:
            setattr(device, '_is_on', False)

def main():
    light1 = SmartLight('Light 1')
    light1.brightness = 70
    thermostat1 = SmartThermostat('Thermostat 1')
    thermostat1.temperature = 69.9
    cam1 = SmartCamera('Camera 1')
    cam1.toggle_record()
    devices = [light1, thermostat1, cam1]
    hub = SmartHub()
    for device in devices:
        hub.add_device(device)

    hub.execute_macro()

    for device in devices:
        print(device)

if __name__ == '__main__':
    main()