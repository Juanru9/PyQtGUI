import sys  # Only needed for access to command line arguments

from PyQt5.QtWidgets import QApplication
from model.ToDoModel import ToDoModel
from controllers.ListController import ListController
from view.Ui_MainList import Ui_MainWindow

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.


class App(QApplication):
    def __init__(self, sys_argv) -> None:
        super(App, self).__init__(sys_argv)
        # Instances the model's object which handles data
        self._listModel = ToDoModel()
        self._listView = Ui_MainWindow()

        # Instances the ListController class and passes model and controller objects
        self._listController = ListController(
            self._listModel, self._listView)

        # IMPORTANT!!!!! Windows are hidden by default.
        self._listController.show()


if __name__ == '__main__':  # Checks if the script runned is the main one
    app = App(sys.argv)  # Instances the app
    sys.exit(app.exec_())  # Start the event loop.

# The application won't reach here until you exit and the event loop has stopped.
