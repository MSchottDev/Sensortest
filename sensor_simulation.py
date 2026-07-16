import random

class Parameter:
    def __init__(self, value):
        self.value = value


class Distance:
    def __init__(self, distance):
        self.distance_in_m = distance


class Peak:
    def __init__(self, amplitude):
        self.amplitude_in_ou = amplitude


class Measurement:
    def __init__(self, distance, amplitude):
        self.distance = Distance(distance)
        self.peak = Peak(amplitude)

class SimulatedSensor:

    def __init__(self, port, serial_number, sensor_type,
                 distance, amplitude):

        self.port = port
        self.serial_number = serial_number
        self.sensor_type = sensor_type

        self.distance = distance
        self.amplitude = amplitude

        self.connected = True

    def set_baudrate(self, baudrate):
        """
        Wird vom Hauptprogramm aufgerufen.
        Für die Simulation muss hier nichts passieren.
        """
        pass

    def disconnect(self):
        self.connected = False

    def connect(self):
        self.connected = True

    def get_sensor_type_string(self):
        return self.sensor_type

    def get_parameter(self, parameter):
        """
        Das Hauptprogramm fragt nur die Seriennummer ab.
        Deshalb geben wir einfach immer die Seriennummer zurück.
        """
        return Parameter(self.serial_number)

    def get_measurement(self):

        simulated_distance = self.distance + random.uniform(-0.02, 0.02)

        simulated_amplitude = self.amplitude + random.uniform(-10, 10)

        return Measurement(round(simulated_distance, 3),round(simulated_amplitude, 1))


# -----------------------------------------
# Simulierte Sensoren
# -----------------------------------------

SIMULATED_SENSORS = {

    "COM3": SimulatedSensor(
        port="COM3",
        serial_number=100001,
        sensor_type="ODS-1000",
        distance=1.74,
        amplitude=520
    ),

    "COM4": SimulatedSensor(
        port="COM4",
        serial_number=100002,
        sensor_type="ODS-1000",
        distance=1.76,
        amplitude=510
    ),

    "COM5": SimulatedSensor(
        port="COM5",
        serial_number=100003,
        sensor_type="ODS-1000",
        distance=1.75,
        amplitude=490
    ),

    "COM6": SimulatedSensor(
        port="COM6",
        serial_number=100004,
        sensor_type="ODS-1000",
        distance=1.78,
        amplitude=530
    ),

    "COM7": SimulatedSensor(
        port="COM7",
        serial_number=100005,
        sensor_type="ODS-1000",
        distance=1.73,
        amplitude=470
    ),

    # Dieser Sensor soll absichtlich fehlschlagen
    "COM8": SimulatedSensor(
        port="COM8",
        serial_number=100006,
        sensor_type="ODS-1000",
        distance=1.30,
        amplitude=1200
    )
}

def get_simulated_sensor(port):
    return SIMULATED_SENSORS.get(port)


def get_available_ports():
    return list(SIMULATED_SENSORS.keys())