# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 500)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        Form.setFont(font)
        self.title = QtWidgets.QLabel(parent=Form)
        self.title.setGeometry(QtCore.QRect(105, 30, 190, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.button_2 = QtWidgets.QPushButton(parent=Form)
        self.button_2.setGeometry(QtCore.QRect(250, 430, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")
        self.button_1 = QtWidgets.QPushButton(parent=Form)
        self.button_1.setGeometry(QtCore.QRect(50, 430, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_1.setFont(font)
        self.button_1.setObjectName("button_1")
        self.label_1 = QtWidgets.QLabel(parent=Form)
        self.label_1.setEnabled(True)
        self.label_1.setGeometry(QtCore.QRect(50, 100, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_1 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_1.setEnabled(True)
        self.lineEdit_1.setGeometry(QtCore.QRect(200, 100, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setText("")
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 150, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(60, 220, 280, 150))
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_3.setObjectName("label_3")
        self.log_out_button = QtWidgets.QPushButton(parent=Form)
        self.log_out_button.setEnabled(False)
        self.log_out_button.setGeometry(QtCore.QRect(150, 60, 100, 30))
        self.log_out_button.setObjectName("log_out_button")
        self.add_interest_button = QtWidgets.QPushButton(parent=Form)
        self.add_interest_button.setEnabled(False)
        self.add_interest_button.setGeometry(QtCore.QRect(150, 390, 100, 30))
        self.add_interest_button.setObjectName("add_interest_button")
        self.checking_radio = QtWidgets.QRadioButton(parent=Form)
        self.checking_radio.setGeometry(QtCore.QRect(100, 190, 80, 20))
        self.checking_radio.setChecked(True)
        self.checking_radio.setObjectName("checking_radio")
        self.savings_radio = QtWidgets.QRadioButton(parent=Form)
        self.savings_radio.setGeometry(QtCore.QRect(230, 190, 70, 20))
        self.savings_radio.setObjectName("savings_radio")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tom Nook\'s Credit Union"))
        self.title.setText(_translate("Form", "Toom Nook\'s Credit Union"))
        self.button_2.setText(_translate("Form", "Create Account"))
        self.button_1.setText(_translate("Form", "Sign In"))
        self.label_1.setText(_translate("Form", "Username"))
        self.label_2.setText(_translate("Form", "Password"))
        self.log_out_button.setText(_translate("Form", "Log Out"))
        self.add_interest_button.setText(_translate("Form", "Add Interest"))
        self.checking_radio.setText(_translate("Form", "Checking"))
        self.savings_radio.setText(_translate("Form", "Savings"))
