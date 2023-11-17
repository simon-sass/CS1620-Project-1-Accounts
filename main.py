from logic import *
import sys

def main():
    app = QApplication([])
    ui = Logic()
    ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    