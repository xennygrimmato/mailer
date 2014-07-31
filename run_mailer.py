import sys
from PyQt4.QtGui import QApplication, QDialog
from ui_mailer import Ui_Form
from core_mailer import Mailer

app = QApplication(sys.argv)
window = Mailer()
window.show()
sys.exit(app.exec_())
