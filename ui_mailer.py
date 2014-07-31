# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mailer.ui'
#
# Created: Thu Jul 31 16:19:55 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(829, 521)
        self.path_excel_label = QtGui.QLabel(Form)
        self.path_excel_label.setGeometry(QtCore.QRect(110, 80, 131, 20))
        self.path_excel_label.setObjectName(_fromUtf8("path_excel_label"))
        self.path_excel_text = QtGui.QLineEdit(Form)
        self.path_excel_text.setGeometry(QtCore.QRect(250, 80, 331, 27))
        self.path_excel_text.setObjectName(_fromUtf8("path_excel_text"))
        self.row_number_label = QtGui.QLabel(Form)
        self.row_number_label.setGeometry(QtCore.QRect(110, 130, 101, 20))
        self.row_number_label.setObjectName(_fromUtf8("row_number_label"))
        self.email_id_label = QtGui.QLabel(Form)
        self.email_id_label.setGeometry(QtCore.QRect(120, 170, 66, 17))
        self.email_id_label.setObjectName(_fromUtf8("email_id_label"))
        self.password_label = QtGui.QLabel(Form)
        self.password_label.setGeometry(QtCore.QRect(120, 210, 66, 17))
        self.password_label.setObjectName(_fromUtf8("password_label"))
        self.subject_label = QtGui.QLabel(Form)
        self.subject_label.setGeometry(QtCore.QRect(130, 250, 66, 17))
        self.subject_label.setObjectName(_fromUtf8("subject_label"))
        self.path_mail_label = QtGui.QLabel(Form)
        self.path_mail_label.setGeometry(QtCore.QRect(90, 280, 141, 31))
        self.path_mail_label.setObjectName(_fromUtf8("path_mail_label"))
        self.row_number_text = QtGui.QLineEdit(Form)
        self.row_number_text.setGeometry(QtCore.QRect(250, 120, 331, 27))
        self.row_number_text.setObjectName(_fromUtf8("row_number_text"))
        self.email_id_text = QtGui.QLineEdit(Form)
        self.email_id_text.setGeometry(QtCore.QRect(250, 160, 331, 27))
        self.email_id_text.setObjectName(_fromUtf8("email_id_text"))
        self.password_text = QtGui.QLineEdit(Form)
        self.password_text.setEchoMode(QtGui.QLineEdit.Password)
        self.password_text.setGeometry(QtCore.QRect(250, 200, 331, 27))
        self.password_text.setObjectName(_fromUtf8("password_text"))
        self.subject_text = QtGui.QLineEdit(Form)
        self.subject_text.setGeometry(QtCore.QRect(250, 240, 441, 27))
        self.subject_text.setObjectName(_fromUtf8("subject_text"))
        self.path_mail_text = QtGui.QLineEdit(Form)
        self.path_mail_text.setGeometry(QtCore.QRect(250, 280, 331, 27))
        self.path_mail_text.setObjectName(_fromUtf8("path_mail_text"))
        self.main_label = QtGui.QLabel(Form)
        self.main_label.setGeometry(QtCore.QRect(370, 20, 81, 20))
        self.main_label.setStyleSheet(_fromUtf8("font: 63 20pt \"Ubuntu\";"))
        self.main_label.setObjectName(_fromUtf8("main_label"))
        self.send_button = QtGui.QPushButton(Form)
        self.send_button.setGeometry(QtCore.QRect(340, 430, 161, 51))
        self.send_button.setObjectName(_fromUtf8("send_button"))
        self.browse_button_excel = QtGui.QPushButton(Form)
        self.browse_button_excel.setGeometry(QtCore.QRect(590, 80, 101, 31))
        self.browse_button_excel.setObjectName(_fromUtf8("browse_button_excel"))
        self.browse_button_mail = QtGui.QPushButton(Form)
        self.browse_button_mail.setGeometry(QtCore.QRect(590, 280, 101, 31))
        self.browse_button_mail.setObjectName(_fromUtf8("browse_button_mail"))
        self.attachment_1_label = QtGui.QLabel(Form)
        self.attachment_1_label.setGeometry(QtCore.QRect(120, 320, 101, 20))
        self.attachment_1_label.setObjectName(_fromUtf8("attachment_1_label"))
        self.attachment_1_text = QtGui.QLineEdit(Form)
        self.attachment_1_text.setGeometry(QtCore.QRect(250, 320, 331, 27))
        self.attachment_1_text.setObjectName(_fromUtf8("attachment_1_text"))
        self.attachment_2_text = QtGui.QLineEdit(Form)
        self.attachment_2_text.setGeometry(QtCore.QRect(250, 360, 331, 27))
        self.attachment_2_text.setObjectName(_fromUtf8("attachment_2_text"))
        self.attachment_2_label = QtGui.QLabel(Form)
        self.attachment_2_label.setGeometry(QtCore.QRect(120, 360, 101, 20))
        self.attachment_2_label.setObjectName(_fromUtf8("attachment_2_label"))
        self.browse_button_attachment_1 = QtGui.QPushButton(Form)
        self.browse_button_attachment_1.setGeometry(QtCore.QRect(590, 320, 101, 31))
        self.browse_button_attachment_1.setObjectName(_fromUtf8("browse_button_attachment_1"))
        self.browse_button_attachment_2 = QtGui.QPushButton(Form)
        self.browse_button_attachment_2.setGeometry(QtCore.QRect(590, 360, 101, 31))
        self.browse_button_attachment_2.setObjectName(_fromUtf8("browse_button_attachment_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.path_excel_label.setText(_translate("Form", "CSV File Path", None))
        self.row_number_label.setText(_translate("Form", "Column No.", None))
        self.email_id_label.setText(_translate("Form", "Email ID", None))
        self.password_label.setText(_translate("Form", "Password", None))
        self.subject_label.setText(_translate("Form", "Subject", None))
        self.path_mail_label.setText(_translate("Form", "Path of mail content", None))
        self.main_label.setText(_translate("Form", "Mailer", None))
        self.send_button.setText(_translate("Form", "Send Mail", None))
        self.browse_button_excel.setText(_translate("Form", "Browse..", None))
        self.browse_button_mail.setText(_translate("Form", "Browse..", None))
        self.attachment_1_label.setText(_translate("Form", "Attachment 1", None))
        self.attachment_2_label.setText(_translate("Form", "Attachment 2", None))
        self.browse_button_attachment_1.setText(_translate("Form", "Browse..", None))
        self.browse_button_attachment_2.setText(_translate("Form", "Browse..", None))
