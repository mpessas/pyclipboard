# -*- coding: utf-8 -*-

"""Python module to copy values to/from KDE's clipboard."""

import sys
import dbus

class PyClipboard(object):
    """Class to set and get values from KDE's clipboard."""

    def __init__(self):
        self.bus = dbus.SessionBus()
        self.clipboard = self.bus.get_object('org.kde.klipper', '/klipper')
        self.encoding = sys.getfilesystemencoding()

    def set_content(self, content):
        """Copy the content to the clipboard."""
        self.clipboard.setClipboardContents(content.encode(self.encoding))

    def get_content(self):
        """Get the value from clipboard."""
        return self.clipboard.getClipboardContents().decode(self.encoding)
