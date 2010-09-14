# -*- coding: utf-8 -*-

"""Python module to copy values to/from KDE's clipboard."""

import sys
import dbus

__version__ = '0.2'


class PyClipboard(object):
    """Class to set and get values from KDE's clipboard."""

    def __init__(self):
        try:
            self.bus = dbus.SessionBus()
        except dbus.DBusException:
            raise ConnectionRefusedError
        self.clipboard = self.bus.get_object('org.kde.klipper', '/klipper')
        self.encoding = sys.getfilesystemencoding()

    def set_content(self, content):
        """Copy the content to the clipboard."""
        self.clipboard.setClipboardContents(content.encode(self.encoding))

    def get_content(self):
        """Get the value from clipboard."""
        return unicode(self.clipboard.getClipboardContents())


class ConnectionRefusedError(Exception):
    """Exception raised, when connecting to the session bus is not possible."""
    pass
