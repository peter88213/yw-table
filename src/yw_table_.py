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
import webbrowser
from tkinter import messagebox
from pywriter.config.configuration import Configuration
from pywriter.ui.main_tk import MainTk
from pywriter.ui.set_icon_tk import *
from pywriter.converter.export_target_factory import ExportTargetFactory
from pywriter.pywriter_globals import *
from nvmatrixlib.relations_table import RelationsTable
from nvmatrixlib.node import Node
from nvmatrixlib.widgets.table_frame import TableFrame
from nvretablexlib.csv_table import CsvTable

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
    csv_arc_true='Ⓐ',
    csv_arc_false='',
    csv_chr_true='Ⓒ',
    csv_chr_false='',
    csv_loc_true='Ⓛ',
    csv_loc_false='',
    csv_itm_true='Ⓘ',
    csv_itm_false='',
    )
OPTIONS = dict(
    csv_row_numbers=True,
    )


class TableManager(MainTk):
    _HELP_URL = 'https://peter88213.github.io/yw-table/usage'

    def __init__(self, **kwargs):
        super().__init__(f'{APPLICATION}  @release', **kwargs)
        set_icon(self.root, icon='tLogo32')

        # Export
        self.exportMenu = tk.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label=_('Export'))
        self.mainMenu.entryconfig(_('Export'), menu=self.exportMenu, state='disabled')
        self.exportMenu.add_command(label='csv', command=lambda: self._export_table('excel', 'utf-8'))
        self.exportMenu.add_command(label='csv (Excel)', command=lambda:self._export_table('excel-tab', 'utf-16'))

        # Help
        self.helpMenu = tk.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label=_('Help'), menu=self.helpMenu)
        self.helpMenu.add_command(label=_('Online help'), command=lambda: webbrowser.open(self._HELP_URL))

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
            self._relationsTable = RelationsTable(self._tableWindow, self.novel, **self.kwargs)

            # Set table data.
            self._relationsTable.set_nodes()

            # Enable export.
            self.mainMenu.entryconfig(_('Export'), state='normal')

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
        """Apply node changes to the project."""
        if Node.isModified:
            if messagebox.askyesno(APPLICATION, f"{_('Apply changes')}?"):
                self._relationsTable.get_nodes()
                try:
                    self.prjFile.write()
                except Error as ex:
                    self.set_info_how(f'!{str(ex)}')
            Node.isModified = False

    def _export_table(self, csvDialect, csvEncoding):
        """Export the table as a csv file."""
        exportTargetFactory = ExportTargetFactory([CsvTable])
        try:
            self.kwargs['suffix'] = CsvTable.SUFFIX
            self.kwargs['csv_dialect'] = csvDialect
            self.kwargs['csv_encoding'] = csvEncoding
            __, target = exportTargetFactory.make_file_objects(self.prjFile.filePath, **self.kwargs)
        except Exception as ex:
            self.set_info_how(f'!{str(ex)}')
            return

        self._apply_changes()
        target.novel = self.novel
        try:
            message = target.write()
        except Exception as ex:
            self.set_info_how(f'!{str(ex)}')
        else:
            self.set_info_how(message)

    def disable_menu(self):
        """Disable menu entries when no project is open.
        
        Extends the superclass method.
        """
        self.mainMenu.entryconfig(_('Export'), state='disabled')
        super().disable_menu()

    def enable_menu(self):
        """Enable menu entries when a project is open.
        
        Extends the superclass method.
        """
        self.mainMenu.entryconfig(_('Export'), state='normal')
        super().enable_menu()


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
