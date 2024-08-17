[Project home page](index) > Changelog

------------------------------------------------------------------------

## Changelog


### Version 1.0.4

- Refactor for future Python versions: No longer test truth value of
xml.etree.ElementTree.Element.

Based on PyWriter version 12.19.5

### Version 1.0.3

- Refactor for future Python versions.

Based on PyWriter version 12.19.4

### Version 1.0.2

- Reading .yw7 files created with the iOS yWriter version.

Based on PyWriter version 12.19.0

### Version 1.0.1

- Make sure the scene title column's minimum width fits the column header.

Based on Pywriter v12.3.0 and novelyst_matrix v1.0.3

### Version 1.0.0

- Reduce the memory use by discarding the docstrings on building.

Based on PyWriter version 12.1.2

### Version 0.17.2 Beta release

- Make it run on old Windows versions.

Based on PyWriter version 10.0.1, novelyst_matrix v0.14.1, and novelyst_retablex v0.2.2

### Version 0.17.1 Beta release

- Fix a bug where arc references for "subplot" scenes are missing in the csv export.

Based on PyWriter version 9.0.5 and novelyst_retablex v0.2.1

### Version 0.17.0 Beta release

- Offer various csv export formats.
- Optionally number csv rows.
- Set csv node display for each element type.

Based on PyWriter version 9.0.5

### Version 0.16.0 Beta release

- Add arcs to the csv export.
- Refactor.

Based on PyWriter version 9.0.5

### Version 0.15.1 Beta release

- Export tab-delimited, utf-16 encoded csv files that can be opened with Excel 2007.

Based on PyWriter version 9.0.5

### Version 0.15.0 Beta release

- Add a "Help" menu.

Based on PyWriter version 9.0.5

### Version 0.14.2 Beta release

- Disable the "Export" menu entry when no project is open. 
- Catch general exceptions.
- Iterate sorted lists instead of dictionaries.

Based on PyWriter version 9.0.5

### Version 0.14.1 Beta release

- Add csv table export.

Based on PyWriter version 9.0.5

### Version 0.13.1 Beta release

- Fix a regression from v0.13.0 where arc changes are not written back correctly, if a scene is assigned to the "subplot".

Based on PyWriter version 9.0.5

### Version 0.13.0 Beta release

- Use "Subplot" as an arc, if at least one scene is assigned, and there are no other arcs.
- Improve error handling in case the project is open in yWriter.

Based on PyWriter version 9.0.5

### Version 0.12.0 Beta release

- Make colors customizable.

Based on PyWriter version 9.0.5

### Version 0.11.0 Beta release

- API modification: Move the table_frame module.

Based on PyWriter version 9.0.5

### Version 0.10.0 Beta release

- Make the scrollbars work.
- Stop scrolling above the canvas window.

Based on PyWriter version 9.0.5

### Version 0.9.1 Alpha release

- Widen narrow columns.

Based on PyWriter version 9.0.5

### Version 0.9.0 Alpha release

- Change the node design.

Based on PyWriter version 9.0.5

### Version 0.8.0 Alpha release

- Fix a bug where horizontal scrolling doesn't work with Linux.
- Toggle with `Ctrl` + Mouseclick. This is needed for Operation under XFCE.

Based on PyWriter version 9.0.5

### Version 0.7.0 Alpha release

- Fix column width. 
- Save last project and window size in a configuration file.
- Add window icon.

Based on PyWriter version 9.0.5

### Version 0.6.0 Alpha release

- Toggle with `Alt` + Mouseclick.

Based on PyWriter version 9.0.5

### Version 0.5.1 Alpha release

- Adjust colors.

Based on PyWriter version 9.0.5

### Version 0.5.0 Alpha release

- Replace scrollbars by mouse wheel operation.

Based on PyWriter version 9.0.5

### Version 0.4.0 Alpha release

- Add mouse wheel support.

Based on PyWriter version 9.0.5

### Version 0.3.1 Alpha release

- Add element types to the table bottom.
- Refactor the code for smooth integration of the new scrollable windows currently being developped.

Based on PyWriter version 9.0.5

### Version 0.3.0 Alpha release

- Remove the panes that made the columns resizeable.
  This is needed for horizontal scrolling.
- Handle write errors.

Based on PyWriter version 9.0.5

### Version 0.2.0 Alpha release

- Rename "yw-table.pyw" --> "yw_table.py".
- Create a start-up script "run.pyw" during setup.

Based on PyWriter version 9.0.5


### Version 0.1.2 Alpha release

- Add a shebang for Linux.

Based on PyWriter version 9.0.5

### Version 0.1.1 Alpha release

Based on PyWriter version 9.0.5

