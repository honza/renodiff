===============================
renodiff
===============================


.. image:: https://img.shields.io/pypi/v/renodiff.svg
        :target: https://pypi.python.org/pypi/renodiff

.. image:: https://img.shields.io/travis/honza/renodiff.svg
        :target: https://travis-ci.org/honza/renodiff

.. image:: https://readthedocs.org/projects/renodiff/badge/?version=latest
        :target: https://renodiff.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/honza/renodiff/shield.svg
     :target: https://pyup.io/repos/github/honza/renodiff/
     :alt: Updates


renodiff is a tool for converting a git commit diff to a `reno`_ release note.

.. _reno: https://docs.openstack.org/developer/reno/ 


Installation
------------

::

    pip install renodiff

Usage
-----

::

    git show | renodiff

License
-------

GNU General Public License v3

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

