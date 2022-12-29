"""Provide a class for csv relationship table representation.

Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/yw-table
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import csv
from ywtablelib.ywtable_globals import *


class CsvTable:
    """csv relationship table representation.

    Public methods:
        write() -- Write instance variables to the file.

    Public instance variables:
        filePath -- str: path to the file (property with getter and setter). 

    Uses the conventions for Excel-generated CSV files.
    """
    DESCRIPTION = _('csv Table')
    EXTENSION = '.csv'
    SUFFIX = '_relationships'

    def __init__(self, filePath, **kwargs):
        """Initialize instance variables.

        Positional arguments:
            filePath -- str: path to the file represented by the File instance.
            
        Optional arguments:
            kwargs -- keyword arguments to be used by subclasses.  
            
        Extends the superclass constructor.          
        """
        self.novel = None
        self._filePath = None
        # str
        # Path to the file. The setter only accepts files of a supported type as specified by EXTENSION.

        self.filePath = filePath
        self._csvTrue = kwargs['csv_true']
        self._csvFalse = kwargs['csv_false']

    @property
    def filePath(self):
        return self._filePath

    @filePath.setter
    def filePath(self, filePath):
        """Setter for the filePath instance variable.
                
        - Format the path string according to Python's requirements. 
        - Accept only filenames with the right suffix and extension.
        """
        if self.SUFFIX is not None:
            suffix = self.SUFFIX
        else:
            suffix = ''
        if filePath.lower().endswith(f'{suffix}{self.EXTENSION}'.lower()):
            self._filePath = filePath

    def write(self):
        """Write the relations to the file.
        
        Raise the "Error" exception in case of error. 
        This is a stub to be overridden by subclass methods.
        """
        try:
            with open(self.filePath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f, dialect='excel')

                # Title row.
                row = ['']
                for crId in self.novel.characters:
                    row.append(self.novel.characters[crId].title)
                for lcId in self.novel.locations:
                    row.append(self.novel.locations[lcId].title)
                for itId in self.novel.items:
                    row.append(self.novel.items[itId].title)
                writer.writerow(row)

                # Scene rows.
                for chId in self.novel.chapters:
                    for scId in self.novel.chapters[chId].srtScenes:
                        if self.novel.scenes[scId].scType == 0:
                            row = [self.novel.scenes[scId].title]
                            for crId in self.novel.characters:
                                try:
                                    if crId in self.novel.scenes[scId].characters:
                                        row.append(self._csvTrue)
                                    else:
                                        row.append(self._csvFalse)
                                except TypeError:
                                    row.append(self._csvFalse)
                            for lcId in self.novel.locations:
                                try:
                                    if lcId in self.novel.scenes[scId].locations:
                                        row.append(self._csvTrue)
                                    else:
                                        row.append(self._csvFalse)
                                except TypeError:
                                    row.append(self._csvFalse)
                            for itId in self.novel.items:
                                try:
                                    if itId in self.novel.scenes[scId].items:
                                        row.append(self._csvTrue)
                                    else:
                                        row.append(self._csvFalse)
                                except TypeError:
                                    row.append(self._csvFalse)
                            writer.writerow(row)
        except:
            raise Error(f'{_("Cannot write File")}: "{norm_path(self.filePath)}".')

        return (f'{_("File written")}: "{norm_path(self.filePath)}".')
