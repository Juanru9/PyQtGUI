from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from view.Ui_main_view import Ui_MainWindow


class MainView(QMainWindow):

    def __init__(self, model, mainController):
        super().__init__()  # Base constructor

        self._model = model
        self._mainController = mainController
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # connect widgets to controller
        self._ui.spinBoxAmount.valueChanged.connect(
            self._mainController.changeAmount)
        self._ui.pushButtonReset.clicked.connect(
            lambda: self._mainController.changeAmount(0))

        # listen for model event signals
        self._model.amountChanged.connect(self.onAmountChanged)
        self._model.evenOddChanged.connect(self.onEvenOddChanged)
        self._model.enableResetChanged.connect(self.onEnableResetChanged)

        # set a default value
        self._mainController.changeAmount(288)

# region Qt slots
    @pyqtSlot(int)
    def onAmountChanged(self, value):
        self._ui.spinBoxAmount.setValue(value)

    @pyqtSlot(str)
    def onEvenOddChanged(self, value):
        self._ui.labelEvenOdd.setText(value)

    @pyqtSlot(bool)
    def onEnableResetChanged(self, value):
        self._ui.pushButtonReset.setEnabled(value)
# endregion
