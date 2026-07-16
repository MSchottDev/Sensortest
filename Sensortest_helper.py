from serial.tools import list_ports

#import ondoconnect.os_sensor as os_sensor
from sensor_simulation import get_simulated_sensor, get_available_ports

import subprocess
import interfaces_python as ip
from typing import Union, Optional
import logging



#def setup_sensor(port: str) -> Optional[os_sensor.Sensor]:
    #try:
        #sensor = os_sensor.Sensor(port)
        #sensor.set_baudrate(921600)
        #logging.info(f'Print setup_sensor: Sensor an COM-Port {port} verfügbar')
        #return sensor
    #except TypeError as e:
        #logging.warning(f'Kein Sensor an {port} vorhanden: {e}')
        #return None
    
def setup_sensor(port):

    sensor = get_simulated_sensor(port)

    if sensor is None:
        logging.warning(f"Kein Sensor an {port} vorhanden.")
        return None

    sensor.set_baudrate(921600)

    logging.info(f"Simulierter Sensor an {port} verbunden.")

    return sensor

#def init_connected_comports() -> list:
    #ports_list = []
    #for comport in list_ports.comports():
        #ports_list.append(comport.device)
    #return ports_list

def init_connected_comports():
    """
    Liefert die COM-Ports der simulierten Sensoren.
    """
    return get_available_ports()

#def check_ports_list_for_sensor(ports_list: list) -> list:
    #sensor_used_ports_list = []
    #for port in ports_list:
        #sensor = setup_sensor(port)
        #sensortype = sensor.get_sensor_type_string()
        #if sensortype != 'unknown':
            #sensor_used_ports_list.append(port)
            #sensor.disconnect()
            #del sensor
        #else:
            #logging.info(f'Com-Port {port} liefert unknown, kein Sensor vorhanden')
            #pass
    #return sensor_used_ports_list


def check_ports_list_for_sensor(ports_list: list) -> list:

    sensor_used_ports_list = []

    for port in ports_list:

        sensor = setup_sensor(port)

        if sensor is None:
            continue

        sensortype = sensor.get_sensor_type_string()

        if sensortype != "unknown":
            sensor_used_ports_list.append(port)

        sensor.disconnect()

    return sensor_used_ports_list

#def write_sensor_in_sensor_registry(sensor_used_ports_list) -> None:
    #for port in sensor_used_ports_list:
        #sensor = setup_sensor(port)
        #SensorRegistry.set_sensor(sensor)


def write_sensor_in_sensor_registry(sensor_used_ports_list) -> None:

    SensorRegistry.clear_sensor_registry()

    for port in sensor_used_ports_list:

        sensor = setup_sensor(port)

        if sensor is not None:
            SensorRegistry.set_sensor(sensor)

def get_radar_profiles_for_distance_test():
    return [ip.ISM_MEDIUM, ip.ISM_MEDIUM_VIRTUAL_BW, ip.ISM_2MS, ip.BIGBW_MEDIUM]

class SensorRegistry:
    _sensor_registry = []

    @classmethod
    def set_sensor(cls, sensor) -> None:
        if sensor in cls._sensor_registry:
            print('Sensor bereits in Registry enthalten')
            return
        if sensor is None:
            print('Sensor None Type')
            return
        else:
            cls._sensor_registry.append(sensor)
            print(f'Sensor {sensor} in Registry gespeichert')

    @classmethod
    def get_sensor(cls, index):
        if index not in range(0, len(cls._sensor_registry)):
            return None
        sensor = cls._sensor_registry[index]
        return sensor
    
    @classmethod
    def show_sensors_in_registry(cls) -> None:
        for sensor in cls._sensor_registry:
            print('Gespeicherte Sensoren in Registry:', cls._sensor_registry[sensor])

    @classmethod
    def clear_sensor_registry(cls) -> None:
        cls._sensor_registry.clear()
        print('SensorRegistry clear')

    @classmethod
    def get_number_of_connected_sensors(cls) -> int:
        number_of_connected_sensors = len(cls._sensor_registry)
        return number_of_connected_sensors
    
def create_test_report_for_distance_test(sensor_index: int) -> subprocess:
    distance_test_report = f'distance_test_report_sensor_{sensor_index + 1}.txt'
    with open(distance_test_report, 'w') as error_file:
        test_report = subprocess.run([
            "python",
            "-m",
            "pytest",
            "distance_test.py::test_distance",
            f"--sensor_index={sensor_index}"
            ], stdout=error_file, stderr=error_file)
        return test_report

def read_distance_result(sensor_index: int):
    distance_file_name = f'distance_test_report_sensor_{sensor_index + 1}.txt'
    with open(distance_file_name, 'r') as file:
        distance_result_report = str(file.read())
        return distance_result_report

def create_test_report_for_amplitude_test(sensor_index: int) -> subprocess:
    amplitude_test_report = f'amplitude_test_report_sensor_{sensor_index + 1}.txt'
    with open(amplitude_test_report, 'w') as error_file:
        test_report = subprocess.run([
            "python",
            "-m",
            "pytest",
            "amplitude_test.py::test_amplitude",
            f"--sensor_index={sensor_index}"
            ], stdout=error_file, stderr=error_file)
        return test_report

def read_amplitude_result(sensor_index: int):
    amplitude_file_name = f"amplitude_test_report_sensor_{sensor_index + 1}.txt"
    with open(amplitude_file_name, 'r') as file:
        amplitude_result_report = str(file.read())
        return amplitude_result_report

def read_log_file() -> str:
    with open('error_log.txt', 'r') as file:
        test_report = str(file.read())
        return test_report
    
def clear_test_reports():

    for test_type in ["distance", "amplitude"]:

        for i in range(1, 7):

            filename = f"{test_type}_test_report_sensor_{i}.txt"

            try:
                with open(filename, "w") as file:
                    file.write("")

            except Exception as e:
                print(f"Report konnte nicht gelöscht werden: {filename} - {e}")

if __name__ == '__main__':
    ports_list = init_connected_comports()
    sensor_used_comports_list = check_ports_list_for_sensor(ports_list)
    write_sensor_in_sensor_registry(sensor_used_comports_list)
    print(SensorRegistry.get_number_of_connected_sensors())