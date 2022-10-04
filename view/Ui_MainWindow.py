from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot, QModelIndex
from view.Ui_main_view import Ui_MainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class MainView(QMainWindow):

    def __init__(self, model, listModel, mainController):
        super().__init__()  # Base constructor

        self._model = model
        self._listModel = listModel

        self._mainController = mainController

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # connect widgets to controller
        self._ui.spinBoxAmount.valueChanged.connect(
            self._mainController.changeAmount)
        self._ui.pushButtonReset.clicked.connect(
            lambda: self._mainController.changeAmount(0))
        self._ui.buttonToDo.clicked.connect(
            lambda: self.fillList(self._ui.textEntry.toPlainText()))

        # listen for model event signals
        self._model.amountChanged.connect(self.onAmountChanged)
        self._model.evenOddChanged.connect(self.onEvenOddChanged)
        self._model.enableResetChanged.connect(self.onEnableResetChanged)

        self._listModel.itemChanged.connect(self.onItemChanged)

        # set a default value
        self._mainController.changeAmount(55)

# region Qt slots
    @pyqtSlot(int)
    def onAmountChanged(self, value) -> None:
        self._ui.spinBoxAmount.setValue(value)

    @pyqtSlot(str)
    def onEvenOddChanged(self, value) -> None:
        self._ui.labelEvenOdd.setText(value)

    @pyqtSlot(bool)
    def onEnableResetChanged(self, value) -> None:
        self._ui.pushButtonReset.setEnabled(value)

    @pyqtSlot(list)
    def onItemChanged(self, value: list) -> None:
        model = QStandardItemModel()
        self._ui.listToDo.setModel(model)
        check: bool = False
        for i, element in enumerate(value):
            item = QStandardItem(element)
            item.setCheckable(True)
            model.appendRow(item)

# endregion

    def fillList(self, value: str) -> None:
        self._listModel.item = value
        self._ui.textEntry.setPlainText('')
