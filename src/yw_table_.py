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
from ywtablelib.widgets.table_frame import TableFrame

APPLICATION = 'Relationship Table'
APPNAME = 'yw_table'
SETTINGS = dict(
    yw_last_open='',
    root_geometry='800x600',
    color_bg_00='gray80',
    color_bg_01='gray85',
    color_bg_10='gray95',
    color_bg_11='white',
    color_arc_heading='royalblue1',
    color_arc_node='royalblue3',
    color_character_heading='goldenrod1',
    color_character_node='goldenrod3',
    color_location_heading='coral1',
    color_location_node='coral3',
    color_item_heading='aquamarine1',
    color_item_node='aquamarine3',
)
OPTIONS = {}


class TableManager(MainTk):

    def __init__(self, **kwargs):
        super().__init__(f'{APPLICATION}  @release', **kwargs)
        set_icon(self.root, icon='tLogo32')
        self._kwargs = kwargs

    def open_project(self, fileName):
        if not super().open_project(fileName):
            return

        #--- The Relationship Table.
        Node.isModified = False
        if self.novel is not None:
            # Set up a window with scrollbars.
            self._tableWindow = TableFrame(self.mainWindow)
            self._tableWindow.pack(fill=tk.BOTH, expand=True)

            # Build the table structure.
            self._relationsTable = RelationsTable(self._tableWindow, self.novel, **self._kwargs)

            # Set table data.
            self._relationsTable.set_nodes()

    def close_project(self, event=None):
        self._apply_changes()
        self._relationsTable = None
        try:
            self._tableWindow.destroy()
        except AttributeError:
            pass
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
    try:
        ui.open_project(filePath)
    except Error as ex:
        ui.set_info_how(str(ex))
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
