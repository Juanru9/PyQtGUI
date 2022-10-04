from PyQt5.QtCore import QObject, pyqtSlot


class MainController(QObject):
    def __init__(self, model) -> None:
        super().__init__()
        self._model = model

    @pyqtSlot(int)
    def changeAmount(self, value):
        self._model.amount = value

        # calculate even or odd
        self._model.evenOdd = 'Par' if value % 2 else 'Impar'

        # calculate button enabled state
        self._model.enableReset = True if value else False
