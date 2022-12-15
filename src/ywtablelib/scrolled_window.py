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

        # Create a _canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        hscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL)
        hscrollbar.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)
        self._canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                           yscrollcommand=vscrollbar.set)
        self._canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        vscrollbar.config(command=self._canvas.yview)
        hscrollbar.config(command=self._canvas.xview)

        # Reset the view
        self._canvas.xview_moveto(0)
        self._canvas.yview_moveto(0)

        # Create a frame inside the _canvas which will be scrolled with it.
        self.display = ttk.Frame(self._canvas)
        self._display_id = self._canvas.create_window(0, 0, window=self.display, anchor=tk.NW, tags="self.display")
        # Track changes to the _canvas and frame width and sync them,
        # also updating the scrollbar.

        def _configure_display(event):
            # Update the scrollbars to match the size of the inner frame.
            size = (self.display.winfo_reqwidth(), self.display.winfo_reqheight())
            self._canvas.config(scrollregion="0 0 %s %s" % size)
            if self.display.winfo_reqwidth() != self._canvas.winfo_width():
                # Update the _canvas's width to fit the inner frame.
                self._canvas.config(width=self.display.winfo_reqwidth())

        self.display.bind('<Configure>', _configure_display)

        def _configure_canvas(event):
            if self.display.winfo_reqwidth() != self._canvas.winfo_width():
                # Update the inner frame's width to fill the _canvas.
                self._canvas.itemconfigure(self._display_id, width=self._canvas.winfo_width())

        self._canvas.bind('<Configure>', _configure_canvas)

