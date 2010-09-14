# -*- coding: utf-8 -*-

from setuptools import setup

setup (
    name = "pyclipboard",
    version = "0.2",
    packages = ["pyclipboard", "pyclipboard.test"],
    author = "Apostolos Bessas",
    author_email = "mpessas@gmail.com",
    description = "Module to copy data to/from KDE's clipboard.",
    license = "GPL",
    test_suite = "pyclipboard.test.test_pyclipboard",
    requires = ["dbus"],
)
