# yw-table

A scene relationship table for yWriter projects. 

For more information, see the [project homepage](https://peter88213.github.io/yw-table) with description and download instructions.


## Development

*yw-table* depends on the [pywriter](https://github.com/peter88213/PyWriter) and the [novelyst_matrix](https://github.com/peter88213/novelyst_matrix) and the [novelyst_retablex](https://github.com/peter88213/novelyst_retablex) libraries which must be present in your file system. It is organized as an Eclipse PyDev project. The official release branch on GitHub is *main*.

### Mandatory directory structure for building the application script

```
.
├── PyWriter/
│   └── src/
│       └── pywriter/
├── novelyst_matrix/
│   └── src/
│       └── nvmatrixlib/
├── novelyst_retablex/
│   └── src/
│       └── nvretablexlib/
└── yw-table/
    ├── src/
    ├── test/
    └── tools/ 
        └── build.xml
```

### Conventions

See https://github.com/peter88213/PyWriter/blob/main/docs/conventions.md

## Development tools

- [Python](https://python.org) version 3.9.
- [Eclipse IDE](https://eclipse.org) with [PyDev](https://pydev.org) and *EGit*.
- *Apache Ant* is used for building the application.

## Credits

- The icons are made using the free *Pusab* font by Ryoichi Tsunekawa, [Flat-it](http://flat-it.com/).

## License

This is Open Source software, and *yw-table* is licensed under GPLv3. See the
[GNU General Public License website](https://www.gnu.org/licenses/gpl-3.0.en.html) for more
details, or consult the [LICENSE](https://github.com/peter88213/yw-table/blob/main/LICENSE) file.
