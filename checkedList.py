import clr
clr.AddReference("PresentationFramework")
clr.AddReference("PresentationCore")
clr.AddReference("WindowsBase")

from System import Windows
from System.Windows import Window
from System.Windows.Controls import CheckBox, StackPanel

class CheckedBoxWindow(Window):
    def __init__(self):
        self.InitializeComponent()

    def InitializeComponent(self):
        # Create a StackPanel to hold CheckBoxes
        stack_panel = StackPanel()

        # Create 5 CheckBoxes and add them to the StackPanel
        for i in range(5):
            checkbox = CheckBox()
            checkbox.Content = f"Item {i+1}"
            stack_panel.Children.Add(checkbox)

        # Set the StackPanel as the content of the window
        self.Content = stack_panel
        self.Title = "WPF Checked List Example"