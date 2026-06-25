import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QSizePolicy, QScrollArea
from Sensortest_helper import *
import interfaces_python as ip


def apply_dark_mode(window):
    dark_stylesheet = """ 
    QWidget { 
        background-color: #2e2e2e; 
    } 
    QLabel, QLineEdit, QPushButton, QComboBox { 
        color: #48d1cc; 
        background-color: #3e3e3e; 
        border: 1px solid #5e5e5e; 
    } 
    QToolTip { 
        background-color: #3e3e3e; 
        color: #48d1cc; 
        border: 1px solid #5e5e5e; 
    } 
    QMainWindow, QDialog { 
        background-color: #2e2e2e; 
    } 
    QTableWidget { 
        background-color: #3e3e3e; 
        color: #ffffff; 
        gridline-color: #5e5e5e; 
        border: 1px solid #5e5e5e; 
    } 
    QTableWidget::item { 
        background-color: #3e3e3e;  
        color:  #48d1cc; 
        border: none; 
    } 
    QHeaderView::section { 
        background-color: #2e2e2e; 
        color: #ffffff; 
        border: 1px solid #5e5e5e; 
    } 
    QPushButton { 
        color: #48d1cc;  
        background-color: #4a4a4a;  
        border: 1px solid #48d1cc;  
        padding: 6px; 
        border-radius: 2px;  
    } 
    QPushButton:hover { 
        background-color: #404040;   
        border: 2px solid #6e6e6e;   
    } 
    QPushButton:pressed { 
        background-color: #3a3a3a;   
        border: 1px solid #7e7e7e; 
    } 
    """
    window.setStyleSheet(dark_stylesheet)


class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle('OndoSense Sensor Test')
        self.setGeometry(300, 200, 1070, 700)
        self.setFixedSize(1070, 700)
        apply_dark_mode(self)
        self.initUI()

    def initUI(self):
        self.labels_sensors = []
        start_x_sensor = 30
        start_y_sensor = 60
        width = 160
        height = 25
        gap = 170

        for i in range(6):
            label_sensor = QLabel(self)
            label_sensor.setText(f"Sensor {i + 1}")
            label_sensor.setGeometry(start_x_sensor + i * gap, start_y_sensor, width, height)
            label_sensor.setAlignment(Qt.AlignCenter)
            self.labels_sensors.append(label_sensor)

        self.labels_sensortype = []
        self.labels_show_sensortype = []
        self.labels_serial_number = []
        self.labels_show_serial_number = []
        self.labels_com_port = []
        self.labels_show_com_port = []
        self.labels_distance = []
        self.buttons_distance = []
        self.buttons_test_distance = []
        self.buttons_test_amplitude = []

        for i in range(6):

            x = start_x_sensor + i * gap

            # Sensortype
            label_sensortype = QLabel(self)
            label_sensortype.setText('Sensortype:')
            label_sensortype.setGeometry(x, 90, 80, 25)
            label_sensortype.setAlignment(Qt.AlignCenter)
            self.labels_sensortype.append(label_sensortype)

            label_show_sensortype = QLabel(self)
            label_show_sensortype.setGeometry(x + 80, 90, 80, 25)
            label_show_sensortype.setStyleSheet("background-color: black; color: white; font-size: 12px")
            label_show_sensortype.setAlignment(Qt.AlignCenter)
            self.labels_show_sensortype.append(label_show_sensortype)

            # SN
            label_sn = QLabel(self)
            label_sn.setText("SN:")
            label_sn.setGeometry(x, 120, 80, 25)
            label_sn.setAlignment(Qt.AlignCenter)
            self.labels_serial_number.append(label_sn)

            label_show_sn = QLabel(self)
            label_show_sn.setGeometry(x + 80, 120, 80, 25)
            label_show_sn.setStyleSheet("background-color: black; color: white; font-size: 12px")
            label_show_sn.setAlignment(Qt.AlignCenter)
            self.labels_show_serial_number.append(label_show_sn)

            # COM
            label_com = QLabel(self)
            label_com.setText("COM-Port:")
            label_com.setGeometry(x, 150, 80, 25)
            label_com.setAlignment(Qt.AlignCenter)
            self.labels_com_port.append(label_com)

            label_show_com = QLabel(self)
            label_show_com.setGeometry(x + 80, 150, 80, 25)
            label_show_com.setStyleSheet("background-color: black; color: white; font-size: 12px")
            label_show_com.setAlignment(Qt.AlignCenter)
            self.labels_show_com_port.append(label_show_com)

            # Distance button + label
            btn = QPushButton(self)
            btn.setGeometry(x, 180, 80, 25)
            btn.setText("Distanz [m]:")
            btn.clicked.connect(lambda checked, idx=i: self.button_distanz_clicked_sensor(idx))
            self.buttons_distance.append(btn)

            label_dist = QLabel(self)
            label_dist.setGeometry(x + 80, 180, 80, 25)
            label_dist.setStyleSheet("background-color: black; color: white; font-size: 12px")
            label_dist.setAlignment(Qt.AlignCenter)
            self.labels_distance.append(label_dist)

            # Test Distance
            btn_td = QPushButton(self)
            btn_td.setGeometry(x, 210, 160, 25)
            btn_td.setText("TEST DISTANCE")
            btn_td.clicked.connect(
                lambda checked, idx=i: self.show_distance_result_report_in_log_label(idx)
            )
            self.buttons_test_distance.append(btn_td)

            # Test Amplitude
            btn_ta = QPushButton(self)
            btn_ta.setGeometry(x, 240, 160, 25)
            btn_ta.setText("TEST AMPLITUDE")
            btn_ta.clicked.connect(
                lambda checked, idx=i: self.show_amplitude_result_report_in_log_label(idx)
            )
            self.buttons_test_amplitude.append(btn_ta)

        # Scroll log
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setGeometry(370, 280, 670, 400)
        self.scroll_area.setWidgetResizable(True)

        self.log_label = QLabel(self.scroll_area)
        self.log_label.setWordWrap(True)
        self.scroll_area.setWidget(self.log_label)

        # Main buttons
        self.connect_all_new_sensors_button = QPushButton(self)
        self.connect_all_new_sensors_button.setGeometry(30, 280, 330, 50)
        self.connect_all_new_sensors_button.setText('CONNECT SENSORS')
        self.connect_all_new_sensors_button.clicked.connect(self.connect_sensors)

        self.disconnect_all_sensors_button = QPushButton(self)
        self.disconnect_all_sensors_button.setGeometry(30, 340, 330, 50)
        self.disconnect_all_sensors_button.setText('DISCONNECT ALL SENSORS')
        self.disconnect_all_sensors_button.clicked.connect(self.disconnect_all_sensors)

        self.test_all_distance_button = QPushButton(self)
        self.test_all_distance_button.setGeometry(30, 410, 330, 50)
        self.test_all_distance_button.setText('TEST DISTANCE')
        self.test_all_distance_button.clicked.connect(self.test_distance)

        self.test_all_amplitude_button = QPushButton(self)
        self.test_all_amplitude_button.setGeometry(30, 470, 330, 50)
        self.test_all_amplitude_button.setText('TEST AMPLITUDE')
        self.test_all_amplitude_button.clicked.connect(self.test_amplitude)

        self.test_all_button = QPushButton(self)
        self.test_all_button.setGeometry(30, 530, 330, 50)
        self.test_all_button.setText('TEST ALL')
        self.test_all_button.clicked.connect(self.test_distance_and_amplitude)

    # ---------------- LOG / SENSOR METHODS ----------------

    def clear_all_sensor_labels(self):
        for i in range(6):
            self.labels_show_com_port[i].clear()
            self.labels_show_sensortype[i].clear()
            self.labels_show_serial_number[i].clear()
            self.labels_distance[i].clear()

    def set_all_sensor_labels_waiting(self):
        for i in range(6):
            self.labels_show_com_port[i].setText('wait')
            self.labels_show_sensortype[i].setText('wait')
            self.labels_show_serial_number[i].setText('wait')
            self.labels_distance[i].setText('wait')

    def clear_all_test_labels(self):
        for i in range(6):
            self.buttons_test_distance[i].setText("TEST DISTANCE")
            self.buttons_test_amplitude[i].setText("TEST AMPLITUDE")

    def clear_log_label(self):
        self.log_label.clear()

    def show_distance_result_report_in_log_label(self, sensor_index):
        self.log_label.setText(read_distance_result(sensor_index))

    def show_amplitude_result_report_in_log_label(self, sensor_index):
        self.log_label.setText(read_amplitude_result(sensor_index))

    def disconnect_all_sensors(self):
        self.clear_all_sensor_labels()
        self.clear_log_label()
        self.clear_all_test_labels()

        if SensorRegistry.get_number_of_connected_sensors() == 0:
            return

        for i in range(SensorRegistry.get_number_of_connected_sensors()):
            sensor = SensorRegistry.get_sensor(i)
            sensor.disconnect()

        SensorRegistry.clear_sensor_registry()

    def connect_sensors(self):
        self.set_all_sensor_labels_waiting()

        if SensorRegistry.get_number_of_connected_sensors() > 0:
            self.disconnect_all_sensors()

        ports_list = init_connected_comports()
        sensor_used_ports_list = check_ports_list_for_sensor(ports_list)
        write_sensor_in_sensor_registry(sensor_used_ports_list)
        self.write_sensor_data_in_main_window(sensor_used_ports_list)

    def button_distanz_clicked_sensor(self, index):
        sensor = SensorRegistry.get_sensor(index)
        if sensor is None:
            self.labels_distance[index].setText("No Data")
            return

        distance = sensor.get_measurement().distance.distance_in_m
        self.labels_distance[index].setText(str(distance))

    def write_sensor_data_in_main_window(self, sensor_used_ports_list):
        self.clear_all_sensor_labels()

        for i in range(SensorRegistry.get_number_of_connected_sensors()):
            sensor = SensorRegistry.get_sensor(i)

            self.labels_show_com_port[i].setText(sensor_used_ports_list[i])
            self.labels_show_sensortype[i].setText(sensor.get_sensor_type_string())
            self.labels_show_serial_number[i].setText(
                str(sensor.get_parameter(ip.SENSOR_SERIAL_NUMBER).value)
            )
            self.labels_distance[i].setText(
                str(sensor.get_measurement().distance.distance_in_m)
            )

    def test_distance(self):
        self.clear_log_label()
        n = SensorRegistry.get_number_of_connected_sensors()

        self.disconnect_all_sensors()

        for i in range(n):
            result = create_test_report_for_distance_test(i)

            if result.returncode == 0:
                self.buttons_test_distance[i].setText("DISTANCE PASS")
            else:
                self.buttons_test_distance[i].setText("DISTANCE FAIL")

        self.connect_sensors()

    def test_amplitude(self):
        self.clear_log_label()
        n = SensorRegistry.get_number_of_connected_sensors()

        self.disconnect_all_sensors()

        for i in range(n):
            result = create_test_report_for_amplitude_test(i)

            if result.returncode == 0:
                self.buttons_test_amplitude[i].setText("AMPLITUDE PASS")
            else:
                self.buttons_test_amplitude[i].setText("AMPLITUDE FAIL")

        self.connect_sensors()

    def test_distance_and_amplitude(self):
        self.test_distance()
        self.test_amplitude()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()