# creating a WPF application
import clr

clr.AddReference("PresentationFramework")
clr.AddReference("PresentationCore")

from System.Windows import Application

from linkedList import MyWindow
from checkedList import CheckedBoxWindow

if __name__ == "__main__":
    myWindow = MyWindow() # Create an instance of the window
    myCheckedBoxWindow = CheckedBoxWindow()
    Application().Run(myWindow) # Run the application
