from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt, QUrl, QEvent, QEventLoop
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QPainter
import sys
 
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
 
class Form(QWidget):
 
    def __init__(self):
        super().__init__()
 
        self.home = QUrl('https://google.com')
 
        hbox = QHBoxLayout()
        self.btn_go = QPushButton('Move')
        self.btn_pdf = QPushButton('PDF')
        self.btn_prn = QPushButton('Print')
        self.le_url = QLineEdit(self.home.toString())
        hbox.addWidget(self.le_url)
        hbox.addWidget(self.btn_go)
        hbox.addWidget(self.btn_pdf)
        hbox.addWidget(self.btn_prn)
        hbox.setStretchFactor(self.le_url, 10)
 
        self.webview = QWebEngineView()
        self.webview.load(self.home)
 
        vbox = QVBoxLayout(self)
        vbox.addLayout(hbox)
        vbox.addWidget(self.webview)
 
        self.setWindowTitle('Ocean Coding School')
        self.setLayout(vbox)
 
        # signal
        QApplication.instance().installEventFilter(self)
        self.webview.urlChanged.connect(self.onUrlChanged)
        self.btn_go.clicked.connect(self.onMove)
        self.btn_pdf.clicked.connect(self.onPDF)
        self.btn_prn.clicked.connect(self.onPrint)
 
    def eventFilter(self, obj, e):
        if obj == self.le_url and e.type() == QEvent.KeyPress and e.key() == Qt.Key_Return:
            self.onMove()
            return True
        return super().eventFilter(obj, e)
 
    def onUrlChanged(self, url):
        self.le_url.setText(url.toString())
        self.le_url.home(True)
 
    def onMove(self):
        txt = self.le_url.text()
        if txt.find('http')==-1 and txt.find('https')==-1:
            txt = f'http://{txt}'
            self.le_url.setText(txt)
 
        url = QUrl(txt)
        self.webview.load(url)
 
    def onPDF(self):
        page = self.webview.page()
        path = QFileDialog.getSaveFileName(self, 'Save PDF', '', 'PDF File(*.pdf)')
        if path[0]:
            page.printToPdf(path[0])
 
    def onPrint(self):
        printer = QPrinter()
        printer.setResolution(QPrinter.HighResolution)
        printer.setPageSize(QPrinter.A4)
        dlg = QPrintDialog(printer, self.webview)
        if dlg.exec_() != QDialog.Accepted:
            return
 
        loop = QEventLoop()
        result = False
 
        def printPreView(success):
            nonlocal result
            result = success
            loop.quit()
 
        page = self.webview.page()
        page.print(printer, printPreView)
        loop.exec_()
 
        if not result:
            qp = QPainter()
            if qp.begin(printer):
                font = qp.font()
                font.setPixelSize(20)
                qp.setFont(font)
                qp.drawText(10, 25, "Could not generate print preview")
                qp.end()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
