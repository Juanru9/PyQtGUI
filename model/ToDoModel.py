from PyQt5.QtCore import QObject, pyqtSignal


class ToDoModel(QObject):

    itemChanged = pyqtSignal(list)
    completeCheckChanged = pyqtSignal(bool)

# region Properties
    @property
    def item(self) -> str:
        return self._item

    @item.setter
    def item(self, value: str) -> None:
        self._item = value
        self.toDoList.append(self._item)
        self.itemChanged.emit(self.toDoList)

    @property
    def completeCheck(self) -> bool:
        return self._completeCheck

    @completeCheck.setter
    def completeCheck(self, value: bool) -> None:
        self._completeCheck = value
        self.completeCheckChanged.emit(value)

    @property
    def toDoList(self) -> list:
        return self._toDoList

    @toDoList.setter
    def toDoList(self, value: list) -> None:
        self._toDoList.append(self._listModel.item)
# endregion

# region Constructors
    def __init__(self) -> None:
        super().__init__()

        self._item: str = ''
        self._completeCheck: bool = False
        self._toDoList = []
# endregion
