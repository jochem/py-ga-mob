===================================================
PYGA: Python Google Analytics - Data Collection API
===================================================
.. image:: https://secure.travis-ci.org/kra3/py-ga-mob.png?branch=master
   :alt: Build Status
   :target: http://travis-ci.org/kra3/py-ga-mob
.. image:: https://img.shields.io/pypi/v/pyga.svg
   :target: https://crate.io/packages/pyga
.. image:: https://coveralls.io/repos/github/kra3/py-ga-mob/badge.svg?branch=master
   :target: https://coveralls.io/github/kra3/py-ga-mob?branch=master


pyga is an implementation of Google Analytics (ga.js) in Python;so that it can be used at server side.
This project only helps you with Data Collection part of Google Analytics.
ie., You can consider this as a replacement for ga.js at client side.

Google Provides Android SDK,iOS SDK + Flash SDK.
And left everybody else with a single page documentation about GIF request parameters.
Also with a basic sample of server side implementation in quite a few languages (perl, php, jsp).

PS: Google moved away from ga.js to analytics.js; a new operating standard for Google Analytics named "universal analytics".
Soon ga.js will be deprecated. I'm planning to have a pyga equivalent to the new standard. Read more here at
https://developers.google.com/analytics/devguides/collection/upgrade/#upgrade-guides
https://developers.google.com/analytics/devguides/collection/protocol/v1/#getting-started

* PyPi Package Page: http://pypi.python.org/pypi/pyga
* Main Repository: https://github.com/kra3/py-ga-mob
* Documentation: http://readthedocs.org/docs/pyga-python-google-analytics-data-collection-api/en/latest/#


Use Cases
--------------

1. You want to track data from server side
2. You're developing a mobile site and have to support devices w/o JS support


Supported Features
----------------------

* Page View
* E-Commerce
* Social Interaction
* Custom Variables
* Events
* Campaigns

  not yet

* Ad-Words
* Search Engine



To know more about mobile-tracking see:
https://developers.google.com/analytics/devguides/collection/other/mobileWebsites


Example
-------------------
::

     from pyga.requests import Tracker, Page, Session, Visitor

     tracker = Tracker('MO-XXXXX-X', 'yourdomain.com')
     visitor = Visitor()
     visitor.ip_address = '194.54.176.12'
     session = Session()
     page = Page('/path')
     tracker.track_pageview(page, session, visitor)




`PHP version <https://github.com/thomasbachem/php-ga>`_

Thanks to: `Expicient Inc <http://www.expicient.com>`_


And for you fans out there, we even have `mountain bikes named pyga <http://www.pygaindustries.com/bikes.html>`_ ;)
