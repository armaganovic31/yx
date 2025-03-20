import sys
from PySide6.QtWidgets import QApplication
from gui.ui import MyApp
import gui.functions as functions

def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()

    window.auto_skill_button.clicked.connect(window.open_auto_skill_dialog)
    window.pushButton_5.clicked.connect(window.accept_window_title)
    window.pushButton.clicked.connect(lambda: functions.start_main_functionality(window))
    window.pushButton_2.clicked.connect(lambda: functions.stop_functionality(window))
    window.comboBox.currentIndexChanged.connect(window.update_window_title)
    window.timer.timeout.connect(lambda: functions.update_pid_list(window.pid_combobox))
    window.close_button.clicked.connect(window.close)
    window.minimize_button.clicked.connect(window.showMinimized)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()