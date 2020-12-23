ghsync
======

Ghsync is a simple cli tool to synchronize organizations' repositories from GitHub.

Usage
-----

Examples
~~~~~~~~

**Sync all repos from all organizations**

To get a list of all organizations for a user, ghsync will need a GitHub
username:

.. code-block:: bash

   ghsync --token "$TOKEN" --user "$GH_USER" -- ~/backup

**Sync all repos from Acme organization**

To get all repositories of a specific organization, just specify it:

.. code-block:: bash

   ghsync --token "$TOKEN" --org Acme -- ~/backup

**Sync all repos from Foo, Bar and Baz organizations**

To get all repositories of the listed organizations, specify them separated by a
space:

.. code-block:: bash

   ghsync --token "$TOKEN" --org Foo Bar Baz -- ~/backup

License
-------

This project is open source software licensed under the GNU General Public
Licence version 3.  © 2020 Serghei Iakovlev
