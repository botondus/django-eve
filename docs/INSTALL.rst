================
django-eve Setup
================

Some knowledge of Django and common practices are assumed. If you have any
questions about the installation process, make sure you see the *Support*
section of ``eve_db/README.rst`` for help.

-----------------------
Installing Dependencies
-----------------------

After downloading and extracting django-eve, you'll want install all of
the dependencies. We recommend using the ``pip`` command. If you don't
have this, or think you may not, run the following::

    easy_install pip

Next, direct ``pip`` to your ``requirements.txt`` file. If your current
directory is eve_db, this will be done something like this::

    pip install -r docs/requirements.txt
    
After this point, you're ready to start importing the CCP data dump.

------------------
Importing CCP Data
------------------

In order to import the CCP data, you will first need to download the SQLite
dumps from: 

    http://eve.no-ip.de/inc100/inc100-sqlite3-v2.db.bz2

Download and extract the DB file and place it the same directory as your
settings.py file. You will then want to rename it to ccp_dump.db. You are then 
ready to run the importers. This is generally done like this::

    python manage.py syncdb
    python manage.py migrate
    python manage.py eve_import_ccp_dump
    
Note that this will take a very long time to run, possibly over an hour. You
should only have to do this once, though.

-----------------
What do I do now?
-----------------

By this point, you should have a fully functioning foundational project. You
have all of CCP's data dump imported into Django models. Take it from here,
it's your decision.
