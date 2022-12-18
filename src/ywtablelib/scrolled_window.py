"""Provide a frame with a vertical scrollbar. 

Based on the VerticalScrolledFrame example class shown and discussed here:
https://stackoverflow.com/questions/16188420/tkinter-scrollbar-for-frame

Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/yw-table
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import tkinter as tk
from tkinter import ttk


class ScrolledWindow(ttk.Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'display' attribute to place widgets inside the scrollable frame.
    * Construct and pack/place/grid normally.
    """

    def __init__(self, parent, *args, **kw):
        ttk.Frame.__init__(self, parent, *args, **kw)

        # Create a _canvas object and scrollbars for scrolling it.
        vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)

        hscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        hscrollbar.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)

        self._canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                                 xscrollcommand=hscrollbar.set,
                                 yscrollcommand=vscrollbar.set)
        self._canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)

        vscrollbar.config(command=self._canvas.yview)
        hscrollbar.config(command=self._canvas.xview)

        # Reset the view
        self._canvas.xview_moveto(0)
        self._canvas.yview_moveto(0)

        # Create a frame inside the _canvas which will be scrolled with it.
        self.scrollable = ttk.Frame(self._canvas)
        self._canvas.create_window(0, 0, window=self.scrollable, anchor=tk.NW, tags="self.display")

        # Table frames inside the scrollable area.
        self.rowTitles = ttk.Frame(self.scrollable)
        self.rowTitles.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.topLeft = ttk.Frame(self.rowTitles)
        self.topLeft.pack(fill=tk.X, expand=False)
        self.display = ttk.Frame(self.scrollable)
        self.display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.columnTitles = ttk.Frame(self.display)
        self.columnTitles.pack(fill=tk.X, expand=True)

        def _configure_scrollable(event):
            # Update the scrollbars to match the size of the inner frame.
            size = (self.scrollable.winfo_reqwidth(), self.scrollable.winfo_reqheight())
            self._canvas.config(scrollregion="0 0 %s %s" % size)
            if self.scrollable.winfo_reqwidth() != self._canvas.winfo_width():
                # Update the _canvas's width to fit the inner frame.
                self._canvas.config(width=self.scrollable.winfo_reqwidth())

        self.scrollable.bind('<Configure>', _configure_scrollable)

