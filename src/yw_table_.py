#!/usr/bin/python3
"""A relationship table for yw7 files

Version @release
Requires Python 3.6+
Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/yw-table
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import sys
from pathlib import Path
from tkinter import messagebox
from pywriter.config.configuration import Configuration
from pywriter.ui.main_tk import MainTk
from pywriter.ui.set_icon_tk import *
from ywtablelib.ywtable_globals import *
from ywtablelib.relations_table import RelationsTable
from ywtablelib.node import Node
from ywtablelib.table_frame import TableFrame

APPLICATION = 'Relationship Table'
APPNAME = 'yw_table'
SETTINGS = dict(
    yw_last_open='',
    root_geometry='800x600',
    color_text_bg='white',
    color_text_fg='black',
)
OPTIONS = {}


class TableManager(MainTk):

    def __init__(self, **kwargs):
        super().__init__(f'{APPLICATION}  @release', **kwargs)
        set_icon(self.root, icon='tLogo32')

    def open_project(self, fileName):
        super().open_project(fileName)

        #--- The Relationship Table.
        Node.isModified = False
        if self.novel is not None:
            # Set up a window with scrollbars.
            self._tableWindow = TableFrame(self.mainWindow)
            self._tableWindow.pack(fill=tk.BOTH, expand=True)

            # Build the table structure.
            self._relationsTable = RelationsTable(self._tableWindow, self.novel)

            # Set table data.
            self._relationsTable.set_nodes()

    def close_project(self, event=None):
        self._apply_changes()
        self._relationsTable = None
        self._tableWindow.destroy()
        super().close_project()

    def on_quit(self, event=None):
        self._apply_changes()
        super().on_quit()

    def _apply_changes(self):
        #--- Apply changes.
        if Node.isModified:
            if messagebox.askyesno(APPLICATION, f"{_('Apply changes')}?"):
                self._relationsTable.get_nodes()
                try:
                    self.prjFile.write()
                except Error as ex:
                    self.set_info_how(f'!{str(ex)}')
            Node.isModified = False


def main():
    #--- Get the initial project file path.
    try:
        filePath = sys.argv[1]
    except IndexError:
        filePath = None

    #--- Load configuration.
    try:
        homeDir = str(Path.home()).replace('\\', '/')
        installDir = f'{homeDir}/.pywriter/{APPNAME}/config'
    except:
        installDir = '.'
    os.makedirs(installDir, exist_ok=True)
    iniFile = f'{installDir}/{APPNAME}.ini'
    configuration = Configuration(SETTINGS, OPTIONS)
    configuration.read(iniFile)
    kwargs = {}
    kwargs.update(configuration.settings)
    kwargs.update(configuration.options)

    #--- Get initial project path.
    if not filePath or not os.path.isfile(filePath):
        filePath = kwargs['yw_last_open']

    #--- Run the application.
    ui = TableManager(**kwargs)
    ui.open_project(filePath)
    ui.start()

    #--- Save project specific configuration
    for keyword in ui.kwargs:
        if keyword in configuration.options:
            configuration.options[keyword] = ui.kwargs[keyword]
        elif keyword in configuration.settings:
            configuration.settings[keyword] = ui.kwargs[keyword]
    configuration.write(iniFile)


if __name__ == '__main__':
    main()
