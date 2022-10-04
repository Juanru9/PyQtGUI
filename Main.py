import sys  # Only needed for access to command line arguments

from PyQt5.QtWidgets import QApplication
from model.NumberModel import NumberModel
from model.ToDoModel import ToDoModel
from view.Ui_MainWindow import MainView
from controller.MainController import MainController


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        # Instances the model's object which handles data
        self._numberModel = NumberModel()
        self._listModel = ToDoModel()

        # Instances the main controller and pass the model's object
        self._mainController = MainController(self._numberModel)

        # Instances the MainView class and passes model and controller objects
        self._mainView = MainView(
            self._numberModel, self._listModel, self._mainController)

        self._mainView.show()  # IMPORTANT!!!!! Windows are hidden by default.


if __name__ == '__main__':  # Checks if the script runned is the main one
    app = App(sys.argv)  # Instances the app
    sys.exit(app.exec_())  # Start the event loop.

# The application won't reach here until you exit and the event loop has stopped.
