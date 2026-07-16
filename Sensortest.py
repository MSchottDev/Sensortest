import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QSizePolicy, QScrollArea
from PyQt5.QtWidgets import QApplication
from Sensortest_helper import *
import interfaces_python as ip
import time
import random



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
    border: 1px solid #6e6e6e;
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
        self.sensors_initialized = False
        self.setWindowTitle('OndoSense Sensor Test')
        self.setGeometry(300, 200, 1124, 735)
        self.setFixedSize(1124, 735)
        apply_dark_mode(self)
        self.initUI()

    def initUI(self):
        self.labels_sensors = []
        start_x_sensor = 32
        start_y_sensor = 63
        width = 168
        height = 27
        gap = 179

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
            label_sensortype.setGeometry(x, 95, 84, 27)
            label_sensortype.setAlignment(Qt.AlignCenter)
            self.labels_sensortype.append(label_sensortype)

            label_show_sensortype = QLabel(self)
            label_show_sensortype.setGeometry(x + 84, 95, 84, 27)
            label_show_sensortype.setStyleSheet("background-color: black; color: white; font-size: 12px")
            label_show_sensortype.setAlignment(Qt.AlignCenter)
            self.labels_show_sensortype.append(label_show_sensortype)

            # SN
            label_sn = QLabel(self)
            label_sn.setText("SN:")
            label_sn.setGeometry(x, 127, 84, 27)
            label_sn.setAlignment(Qt.AlignCenter)
            self.labels_serial_number.append(label_sn)

            label_show_sn = QLabel(self)
            label_show_sn.setGeometry(x + 84, 127, 84, 27)
            label_show_sn.setStyleSheet("background-color: black; color: white; font-size: 12px")
            label_show_sn.setAlignment(Qt.AlignCenter)
            self.labels_show_serial_number.append(label_show_sn)

            # COM
            label_com = QLabel(self)
            label_com.setText("COM-Port:")
            label_com.setGeometry(x, 158, 84, 27)
            label_com.setAlignment(Qt.AlignCenter)
            self.labels_com_port.append(label_com)

            label_show_com = QLabel(self)
            label_show_com.setGeometry(x + 84, 158, 84, 27)
            label_show_com.setStyleSheet("background-color: black; color: white; font-size: 12px")
            label_show_com.setAlignment(Qt.AlignCenter)
            self.labels_show_com_port.append(label_show_com)

            # Distance button + label
            btn = QPushButton(self)
            btn.setGeometry(x, 189, 84, 27)
            btn.setText("Distanz [m]:")
            btn.clicked.connect(lambda checked, idx=i: self.button_distanz_clicked_sensor(idx))
            self.buttons_distance.append(btn)

            label_dist = QLabel(self)
            label_dist.setGeometry(x + 84, 189, 84, 27)
            label_dist.setStyleSheet("background-color: black; color: white; font-size: 12px")
            label_dist.setAlignment(Qt.AlignCenter)
            self.labels_distance.append(label_dist)

            # Test Distance
            btn_td = QPushButton(self)
            btn_td.setGeometry(x, 221, 168, 27)
            btn_td.setText("TEST DISTANCE")
            btn_td.setStyleSheet("background-color: black; color: white; font-size: 12px")
            btn_td.clicked.connect(
            lambda checked, idx=i: self.show_distance_result_report_in_log_label(idx)
            )
            self.buttons_test_distance.append(btn_td)

            # Test Amplitude
            btn_ta = QPushButton(self)
            btn_ta.setGeometry(x, 253, 168, 27)
            btn_ta.setText("TEST AMPLITUDE")
            btn_ta.setStyleSheet("background-color: black; color: white; font-size: 12px")
            btn_ta.clicked.connect(
            lambda checked, idx=i: self.show_amplitude_result_report_in_log_label(idx)
            )
            self.buttons_test_amplitude.append(btn_ta)

            # Scroll log
            self.scroll_area = QScrollArea(self)
            self.scroll_area.setGeometry(389, 294, 704, 420)
            self.scroll_area.setWidgetResizable(True)

            self.log_label = QLabel(self.scroll_area)
            self.log_label.setWordWrap(True)
            self.scroll_area.setWidget(self.log_label)

            # Main buttons
            self.connect_all_new_sensors_button = QPushButton(self)
            self.connect_all_new_sensors_button.setGeometry(32, 294, 347, 53)
            self.connect_all_new_sensors_button.setText('CONNECT SENSORS')
            self.connect_all_new_sensors_button.clicked.connect(self.connect_sensors)

            self.disconnect_all_sensors_button = QPushButton(self)
            self.disconnect_all_sensors_button.setGeometry(32, 357, 347, 53)
            self.disconnect_all_sensors_button.setText('DISCONNECT ALL SENSORS')
            self.disconnect_all_sensors_button.clicked.connect(self.disconnect_all_sensors)

            self.test_all_distance_button = QPushButton(self)
            self.test_all_distance_button.setGeometry(32, 431, 347, 53)
            self.test_all_distance_button.setText('TEST DISTANCE')
            self.test_all_distance_button.clicked.connect(self.test_distance)

            self.test_all_amplitude_button = QPushButton(self)
            self.test_all_amplitude_button.setGeometry(32, 494, 347, 53)
            self.test_all_amplitude_button.setText('TEST AMPLITUDE')
            self.test_all_amplitude_button.clicked.connect(self.test_amplitude)

            self.test_all_button = QPushButton(self)
            self.test_all_button.setGeometry(32, 557, 347, 53)
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
            self.buttons_test_distance[i].setStyleSheet(
            "background-color: black; color: white;")
            self.buttons_test_amplitude[i].setStyleSheet(
            "background-color: black; color: white;")

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
        self.sensors_initialized = False
        clear_test_reports()

    # Hinzugefügt für Tests:
    def disconnect_sensors_for_test(self):

        for i in range(SensorRegistry.get_number_of_connected_sensors()):

            sensor = SensorRegistry.get_sensor(i)

            if sensor:
                sensor.disconnect()

        SensorRegistry.clear_sensor_registry()    

    def reconnect_sensors_after_test(self):

        SensorRegistry.clear_sensor_registry()

        ports_list = init_connected_comports()

        sensor_used_ports_list = check_ports_list_for_sensor(ports_list)

        write_sensor_in_sensor_registry(sensor_used_ports_list)

        self.write_sensor_data_in_main_window(sensor_used_ports_list)

        self.sensors_initialized = True


    def connect_sensors(self):
        self.set_all_sensor_labels_waiting()

        if SensorRegistry.get_number_of_connected_sensors() > 0:
            self.disconnect_all_sensors()

        ports_list = init_connected_comports()
        sensor_used_ports_list = check_ports_list_for_sensor(ports_list)
        write_sensor_in_sensor_registry(sensor_used_ports_list)
        
       
        self.write_sensor_data_in_main_window(sensor_used_ports_list)
        self.sensors_initialized = True
        
        

    def button_distanz_clicked_sensor(self, index):
        sensor = SensorRegistry.get_sensor(index)
        if sensor is None:
            self.labels_distance[index].setText("No Data")
            return

        distance = sensor.get_measurement().distance.distance_in_m
        self.labels_distance[index].setText(str(distance))

    def write_sensor_data_in_main_window(self, sensor_used_ports_list):
        self.sensors_initialized = True
        self.clear_all_sensor_labels()

        for i in range(SensorRegistry.get_number_of_connected_sensors()):
            time.sleep(random.uniform(0.6, 1.2))
            sensor = SensorRegistry.get_sensor(i)

            self.labels_show_com_port[i].setText(sensor_used_ports_list[i])
            self.labels_show_sensortype[i].setText(sensor.get_sensor_type_string())
            self.labels_show_serial_number[i].setText(
                str(sensor.get_parameter(ip.SENSOR_SERIAL_NUMBER).value)
            )
            self.labels_distance[i].setText(
                str(sensor.get_measurement().distance.distance_in_m)
            )
            # GUI sofort aktualisieren
            QApplication.processEvents()
            

    def test_distance(self):
        self.clear_log_label()
        if not self.sensors_initialized:
            self.log_label.setText("ERROR: No sensors connected.\nPlease connect sensors first.")
            return
        n = SensorRegistry.get_number_of_connected_sensors()

        self.disconnect_sensors_for_test()

        for i in range(n):
            time.sleep(random.uniform(0.6, 1.2))
            result = create_test_report_for_distance_test(i)

            if result.returncode == 0:
                self.buttons_test_distance[i].setText("DISTANCE PASS")
                self.buttons_test_distance[i].setStyleSheet("background-color: green")
            else:
                self.buttons_test_distance[i].setText("DISTANCE FAIL")
                self.buttons_test_distance[i].setStyleSheet("background-color: red")
            QApplication.processEvents()
            

        self.reconnect_sensors_after_test()

    def test_amplitude(self):
        self.clear_log_label()
        if not self.sensors_initialized:
            self.log_label.setText("ERROR: No sensors connected.\nPlease connect sensors first.")
            return
        n = SensorRegistry.get_number_of_connected_sensors()

        self.disconnect_sensors_for_test()

        for i in range(n):
            time.sleep(random.uniform(0.6, 1.2))
            result = create_test_report_for_amplitude_test(i)

            if result.returncode == 0:
                self.buttons_test_amplitude[i].setText("AMPLITUDE PASS")
                self.buttons_test_amplitude[i].setStyleSheet("background-color: green")
            else:
                self.buttons_test_amplitude[i].setText("AMPLITUDE FAIL")
                self.buttons_test_amplitude[i].setStyleSheet("background-color: red")
            QApplication.processEvents()
            

        self.reconnect_sensors_after_test()

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