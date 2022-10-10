from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot


class ListController(QMainWindow):

    def __init__(self, listModel, listView):
        super().__init__()  # Base constructor

        # Stores the model's logic
        self._listModel = listModel

        # Stores the UI
        self._ui = listView
        self._ui.setupUi(self)

        # Connect widgets to model
        self._ui.addButton.clicked.connect(
            lambda: self._listModel.addItem(self._ui.plainTextEdit.toPlainText()))
        self._ui.updateButton.clicked.connect(
            lambda: self._listModel.removeItem(self._ui.plainTextEdit.toPlainText()))
        self._ui.deleteButton.clicked.connect(
            lambda: self._listModel.cleanList())

        # Listen for model event signals
        self._listModel.itemChanged.connect(self.onItemChanged)
        # #self._listModel.completeCheckChanged.connect(self.onItemChanged)

# region Qt slots
    @pyqtSlot(str)
    def onItemChanged(self, value: str) -> None:
        self._ui.listBox.addItem(value)
        self._ui.plainTextEdit.clear()

# endregion
