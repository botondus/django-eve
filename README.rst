==========
django-eve
==========

django-eve is an effort to provide a solid foundation for developers to build
EVE-Online related sites from. Features include importing data from the CCP 
dump, as well as modules for querying the EVE API to update more dynamic 
things like alliances, corporations, etc.

The software is all written in `Python`_, and utilizes the 
excellent `Django`_ web development framework.

Source: https://github.com/gtaylor/django-eve

.. _Django: http://djangoproject.com
.. _Python: http://python.org

--------------------
django-eve ecosystem
--------------------

This particular Google Code project (django-eve) is merely a template and a 
hub for the django-eve effort. This project is merely a suggested project 
layout to start from with the necessary settings in settings.py. A number of 
sub-projects provide the actual functionality. You may find them listed below:

* `django-eve-db`_ - Django models and importers for the CCP data dump. This 
  lets you worry less about SQL, and more about getting your project out of 
  the door.
* `django-eve-proxy`_ - An EVE data API proxy/cache application. This is useful 
  for when you want to query the API but don't want to deal with cache recycle 
  times yourself. `django-eve-api`_ may also be set up like a traditional EVE data 
  API proxy service if you require it for Javascript or third party usage. 
  Note that this app performs no parsing of the results from the API, see 
  `django-eve-api`_ for that.
* `django-eve-api`_ - A set of Django models meant to make querying the 
  EVE data API trivial. All parsing of the data returned by the API is handled, 
  as are cache recycle times via `django-eve-proxy`_.
  
.. _django-eve-db: http://code.google.com/p/django-eve-db/
.. _django-eve-proxy: http://code.google.com/p/django-eve-proxy/
.. _django-eve-api: http://code.google.com/p/django-eve-api/
  
---------------
Getting Started
---------------

The easiest way to get started developing EVE software with django-eve is to 
follow the installation instructions. This will get you running quickly 
and easily.

-----------
Development
-----------

This software and all related projects are primarily developed by 
Blackman Industries, a software consulting and development EVE Corporation. 
Please consider sending ISK if this software has saved you time or 
benefited you.

-------
Support
-------

For support, you may either file an issue in our issue tracker, or send a 
message to our `mailing list`_.

.. _mailing list: http://groups.google.com/group/django-eve