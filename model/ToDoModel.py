from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class ToDoModel(QObject):

    # INotifyPropertyChanged sends a signal
    itemChanged = pyqtSignal(str)
    completeCheckChanged = pyqtSignal(bool)

# region Properties
    @property
    def item(self) -> str:
        return self._item

    @item.setter
    def item(self, value: str) -> None:
        self._item = value
        self.itemChanged.emit(value)

    @property
    def completeCheck(self) -> bool:
        return self._completeCheck

    @completeCheck.setter
    def completeCheck(self, value: bool) -> None:
        self._completeCheck = value
        self.completeCheckChanged.emit(value)
# endregion

# region Constructors
    def __init__(self) -> None:
        super().__init__()

        self._item: str = ''
        self._completeCheck: bool = False
        self._toDoList: list = []
# endregion

    @pyqtSlot(str)  # Add an item to the list
    def addItem(self, value: str) -> None:
        self.item = value
        self._toDoList.append(self.item)

    @pyqtSlot(str)
    def removeItem(self, value: str) -> None:
        self._toDoList.remove(value)

    def cleanList(self) -> None:  # Cleans the list
        self._toDoList.clear()
