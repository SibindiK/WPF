import clr

clr.AddReference('PresentationFramework')
clr.AddReference('PresentationCore')
clr.AddReference('WindowsBase')

from System import Windows
from System.Windows import Application, Window, Thickness
from System.Windows.Controls import (ListView, GridView, 
                                     GridViewColumn)

class MyWindow(Window):
    def __init__(self):
        self.InitializeComponent()

    def InitializeComponent(self):
        self.Title = "Selectable ListView Example"
        self.Width = 300
        self.Height = 200
        self.WindowStartupLocation = Windows.WindowStartupLocation.CenterScreen

        # Create a ListView
        list_view = ListView()
        list_view.Margin = Thickness(10)
        self.Content = list_view

        # Create a GridView to display columns
        grid_view = GridView()
        list_view.View = grid_view

        # Add columns to the GridView
        grid_view.Columns.Add(GridViewColumn(Header="Items"))

        # Add items to the ListView
        for i in range(5):
            list_view.Items.Add(f"Item {i+1}")

