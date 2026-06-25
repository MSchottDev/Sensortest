def pytest_addoption(parser):
    parser.addoption("--sensor_index", action="store", default="1", help="index of used sensor")