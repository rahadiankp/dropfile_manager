# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DFUi.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(430, 174)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowTitle(_fromUtf8("Dropfile.to Uploader"))
        MainWindow.setWindowFilePath(_fromUtf8(""))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 411, 151))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.selectButton = QtGui.QPushButton(self.widget)
        self.selectButton.setText(_fromUtf8("Select File"))
        self.selectButton.setObjectName(_fromUtf8("selectButton"))
        self.horizontalLayout.addWidget(self.selectButton)
        self.filePath = QtGui.QLineEdit(self.widget)
        self.filePath.setEnabled(False)
        self.filePath.setText(_fromUtf8(""))
        self.filePath.setObjectName(_fromUtf8("filePath"))
        self.horizontalLayout.addWidget(self.filePath)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.upButton = QtGui.QPushButton(self.widget)
        self.upButton.setEnabled(False)
        self.upButton.setText(_fromUtf8("Upload"))
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.verticalLayout_2.addWidget(self.upButton)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.t_dropID = QtGui.QLabel(self.widget)
        self.t_dropID.setText(_fromUtf8("Dropfile ID :"))
        self.t_dropID.setObjectName(_fromUtf8("t_dropID"))
        self.horizontalLayout_2.addWidget(self.t_dropID)
        self.dropID = QtGui.QLineEdit(self.widget)
        self.dropID.setObjectName(_fromUtf8("dropID"))
        self.horizontalLayout_2.addWidget(self.dropID)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.t_accesskey = QtGui.QLabel(self.widget)
        self.t_accesskey.setText(_fromUtf8("Access Key :"))
        self.t_accesskey.setObjectName(_fromUtf8("t_accesskey"))
        self.horizontalLayout_3.addWidget(self.t_accesskey)
        self.accessKey = QtGui.QLineEdit(self.widget)
        self.accessKey.setObjectName(_fromUtf8("accessKey"))
        self.horizontalLayout_3.addWidget(self.accessKey)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
