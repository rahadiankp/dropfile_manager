# Dropfile.to Uploader
# github.com/rahadiankp

from DF.Ui import *
from DF.Uploader import Upload as Up

upDF = Up()

def sFile():
	upDF.setLink(QtGui.QFileDialog.getOpenFileName())
	ui.filePath.setText(upDF.getLink())
	if(upDF.getLink()==""):
		ui.upButton.setEnabled(False)
		return
	ui.upButton.setEnabled(True)

def upl():
	print("Uploading file:", upDF.getLink())
	res = upDF.upload()
	if(res['status']==0):
		ui.dropID.setText(res['dropID'])
		ui.accessKey.setText(res['aKey'])
	elif(res['status']==1):
		ui.dropID.setText("Upload failed")
	elif(res['status']==2):
		ui.dropID.setText("No/Unstable connection")
	ui.upButton.setEnabled(False)
	ui.filePath.setText("")

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	QtCore.QObject.connect(ui.selectButton, QtCore.SIGNAL("clicked()"), sFile)
	QtCore.QObject.connect(ui.upButton, QtCore.SIGNAL("clicked()"), upl)
	MainWindow.show()
	sys.exit(app.exec_())
