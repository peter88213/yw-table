"""Generate German translation files for GNU gettext.

- Update the project's 'de.po' translation file.
- Generate the language specific 'pywriter.mo' dictionary.

Usage: 
translate_de.py

File structure:

├── PyWriter/
│   ├── i18n/
│   │   └── de.json
│   └── src/
│       ├── translations.py
│       └── msgfmt.py
└── novelyst_matrix/
    ├── src/ 
    │   └── translate_de.py
    └── i18n/
        ├── messages.pot
        ├── de.po
        ├── locale/
        │   └─ de/
        │      └─ LC_MESSAGES/
        │         └─ pywriter.mo
        └── plugin_locale/
            └─ de/
               └─ LC_MESSAGES/
                  └─ novelyst_matrix.mo
    
Copyright (c) 2022 Peter Triesberger
For further information see https://github.com/peter88213/novelyst_matrix
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import sys
sys.path.insert(0, f'{os.getcwd()}/../../PyWriter/src')
import translations
from shutil import copyfile
import msgfmt

APP_NAME = 'novelyst_matrix'
PO_PATH = '../i18n/de.po'
MO_PATH = f'../i18n/locale/de/LC_MESSAGES/{APP_NAME}.mo'
MO_COPY = f'../../novelyst/src/locale/de/LC_MESSAGES/{APP_NAME}.mo'


def main(version='unknown'):
    if translations.main('de', app=APP_NAME, appVersion=version):
        print(f'Writing "{MO_PATH}" ...')
        msgfmt.make(PO_PATH, MO_PATH)
        copyfile(MO_PATH, MO_COPY)
    else:
        sys.exit(1)


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except:
        main()
