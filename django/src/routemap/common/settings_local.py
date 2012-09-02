# -*- coding: utf-8 -*-
# Local settings for route.is

DEBUG = True

ADMINS = (
    ('Guttorm Flatabø', 'gfl@vestforsk.no'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'norway',                      # Or path to database file if using sqlite3.
        'USER': 'osm',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS' : {
            'autocommit' : True
        },
    }
}

TIME_ZONE = 'Etc/UTC'

ROUTEMAP_TILE_BASEURL = 'http://kunnskapkryssergrenser.no/tiles'

# ELEVATION_PROFILE_DEM  = _BASEDIR + '../static/elevationdem/hoyde_900913.tif'
# ELEVATION_PROFILE_TMP_DIR =  _BASEDIR + '../tmp'
# ELEVATION_PROFILE_ERROR_IMG =  _BASEDIR + '../static/img/noelevationprofile.gif'
