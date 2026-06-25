import pytest
from Sensortest_helper import *

def pytest_addoption(parser):
    parser.addoption("--sensor_index", action="store", default="1", help="index used sensor")

@pytest.fixture
def sensor_index(request):
    return int(request.config.getoption("--sensor_index"))

@pytest.fixture(scope="module")
def setup_sensor_registry():
    ports_list = init_connected_comports()
    sensor_used_ports_list = check_ports_list_for_sensor(ports_list)
    write_sensor_in_sensor_registry(sensor_used_ports_list)
    print('Anzahl Sensoren:', SensorRegistry.get_number_of_connected_sensors())
    assert SensorRegistry.get_number_of_connected_sensors() > 0
    return SensorRegistry

def get_radar_profiles_for_distance_test():
    return [ip.ISM_MEDIUM, ip.ISM_MEDIUM_VIRTUAL_BW, ip.ISM_2MS, ip.BIGBW_MEDIUM]

@pytest.mark.parametrize("radar_profile", get_radar_profiles_for_distance_test())
def test_distance(setup_sensor_registry, sensor_index, radar_profile):
    sensor = SensorRegistry.get_sensor(sensor_index)
    distance = sensor.get_measurement().distance.distance_in_m
    assert 1.7 < distance < 1.8