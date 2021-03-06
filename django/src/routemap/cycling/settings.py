#!/usr/bin/python
# This file is part of the Waymarked Trails Map Project
# Copyright (C) 2011-2012 Sarah Hoffmann
#
# This is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

# common settings for all route maps
from routemap.common.settings import *
from routemap.common.settings import _BASEDIR
try:
    from routemap.common.settings_local import *
except:
    pass # no local settings provided


# Django settings for cycling project.
_ = lambda s : s

ROOT_URLCONF = 'routemap.cycling.urls'

# Project settings
ROUTEMAP_PAGEINFO = {
    # Translators: This is the category of routes for the active map view, will be preceded by site name, such as "Waymarked Trails: ".
    "maptopic" : _("Cycling"),
    "mapdescription" : _("OSM based map with international, national, regional and local cycling routes highlighted."),
    "cssfile" : "cycling_theme.css",
    "bgimage" : "banner_bike.jpg",
    "iconimg" : "map_cycling.ico"
}

ROUTEMAP_MAX_ROUTES_IN_LIST = 30
ROUTEMAP_SOURCE_SYMBOL_PATH = _BASEDIR + '../static/img/symbols'
ROUTEMAP_COMPILED_SYMBOL_PATH = 'cyclingsyms'
ROUTEMAP_UPDATE_TIMESTAMP = _BASEDIR + '/../last_update'

ROUTEMAP_TILE_URL = ROUTEMAP_TILE_BASEURL + '/cycling'

ROUTEMAP_HELPPAGES = {
   'source' : _BASEDIR + 'locale/%s/helppages.yaml',
   "structure" : (("about", "cycling", "osm"),
                  ("rendering", "cyclingroutes", "classification",
                   "labels", "hierarchy",
                     (("hierarchies", "text"),
                      ("hikinglocal", "ukcycle"),
                  )),
                  ("technical", "general", "translation"),
                  ("legal", "copyright", "usage", "disclaimer"),
                  ("acknowledgements", "text"),
                  ("contact", "text")
                 )
}
