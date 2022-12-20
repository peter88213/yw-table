[Project homepage](https://peter88213.github.io/yw-table)

--- 

A scene relationship table for yWriter projects.

## Instructions for use

### Intended usage

The included installation script prompts you to create a shortcut on the desktop. 

- If you double-click on the shortcut, the program starts with the last opened yWriter project, if any. Otherwise, a "file open" dialog is displayed. Optionally, you can drag your yWriter 
   project and drop it on the shortcut icon.

- If the loaded file is not the project you want to view/edit, open another project via the 
   **File > Open** command (or *Ctrl-O* shortcut). 

### Command line usage

Alternatively, you can

- launch the program on the command line passing the *.yw7* file as an argument, or
- launch the program via a batch file.

usage: `yw_table.py Sourcefile`

#### positional arguments:

`Sourcefile` 

The path of the *.yw7* file.

### Operation

#### Scrolling

- Use the mouse wheel for vertical scrolling.
- Use the mouse wheel with the `Shift` key pressed for horizontal scrolling.    

#### Add/remove relationships

- Add/Remove relationships by klicking on the nodes with the `Ctrl` key pressed.

#### Open a project

- If no project is specified by dragging and dropping on the program icon,
  tyou canload one with **File > Open** or **Ctrl-O**.

#### Save the project

- You can save the project with **File > Save** or **Ctrl-S**.
- If the project is open in yWriter, you will be asked to exit yWriter first.

#### Close the project

- You can close the project without exiting the program with **File > Close**.
- When closing the project, you will be asked for applying changes.
- If you open another project, the current project is automatically closed.

#### Exit 

- You can exit with **File > Exit** or **Ctrl-Q**.
- When exiting the program, you will be asked for saving the project, if it has changed.


## Installation path

The setup script installs *yw_table.py* in the user profile. This is the installation path on Windows: 

`c:\Users\<user name>\.pywriter\yw_table`

## License

This is Open Source software, and *yw-table* is licenced under GPLv3. See the
[GNU General Public License website](https://www.gnu.org/licenses/gpl-3.0.en.html) for more
details, or consult the [LICENSE](https://github.com/peter88213/novelyst_matrix/blob/main/LICENSE) file.
