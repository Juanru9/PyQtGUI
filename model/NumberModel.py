from PyQt5.QtCore import QObject, pyqtSignal


class NumberModel(QObject):

    amountChanged = pyqtSignal(int)
    evenOddChanged = pyqtSignal(str)
    enableResetChanged = pyqtSignal(bool)

# region Properties
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
        self.amountChanged.emit(value)

    @property
    def evenOdd(self):
        return self._evenOdd

    @evenOdd.setter
    def evenOdd(self, value):
        self._evenOdd = value
        self.evenOddChanged.emit(value)

    @property
    def enableReset(self):
        return self._enableReset

    @enableReset.setter
    def enableReset(self, value):
        self._enableReset = value
        self.enableResetChanged.emit(value)
# endregion

# region Constructors
    def __init__(self) -> None:
        super().__init__()

        self._amount = 0
        self._evenOdd = ''
        self._enableReset = False
# endregion
