import PySimpleGUI as sg
import os.path

file_list_column = [

    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),

    ],

    [
        sg.Listbox(

            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],

]
# For now we will show onlu the name of the chosen files
