#!/usr/bin/env python

from codecs import open
from pyowm.webapi25.location import Location

"""
Module containing a registry with lookup methods for OWM-provided city IDs
"""

class CityIDRegistry():

    """
    Initialise a registry that can be used to lookup info about cities.

    :param filepath_regex: Python format string that gives the path of the files
           that store the city IDs information.
           Eg: ``folder1/folder2/%02d-%02d.txt``
    :type filepath_regex: str
    :returns: a *CityIDRegistry* instance

    """
    def __init__(self, filepath_regex):
        self._filepath_regex = filepath_regex

    def id_for(self, city_name):
        """
        Returns the long ID corresponding to the provided city name.

        :param city_name: the city name whose ID is looked up
        :type city_name: str
        :returns: a long or ``None`` if the lookup fails

        """
        line = self._lookup_line_by_city_name(city_name)
        return long(line.split(",")[1]) if line is not None else None

    def location_for(self, city_name):
        """
        Returns the *Location* object corresponding to the provided city name.

        :param city_name: the city name you want a *Location* for
        :type city_name: str
        :returns: a *Location* instance or ``None`` if the lookup fails

        """
        line = self._lookup_line_by_city_name(city_name)
        if line is None:
            return None
        tokens = line.split(",")
        return Location(tokens[0], float(tokens[3]), float(tokens[2]),
                        long(tokens[1]), 'NL')

    def _assess_subfile_from(self, city_name):
        c = ord(city_name.lower()[0])
        if c < 97: # not a letter
            raise ValueError('Error: city name must start with a letter')
        elif c in range(97, 103):  # from a to f
            return self._filepath_regex % (97, 102)
        elif c in range(103, 109): # from g to l
            return self._filepath_regex % (103, 108)
            return filename
        elif c in range(109, 115): # from m to r
            return self._filepath_regex % (109, 114)
            return filename
        elif c in range (115, 123): # from s to z
            return self._filepath_regex % (115, 122)
        else:
            raise ValueError('Error: city name must start with a letter')

    def _lookup_line_by_city_name(self, city_name):
        filename = self._assess_subfile_from(city_name)
        with open(filename, "r", "utf-8") as f:
            for line in f:
                if line.startswith(city_name.lower()):
                    return line.strip()
        return None
