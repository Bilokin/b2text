======
b2text
======


.. image:: https://img.shields.io/pypi/v/b2text.svg
        :target: https://pypi.python.org/pypi/b2text

.. image:: https://img.shields.io/travis/bilokin/b2text.svg
        :target: https://travis-ci.com/bilokin/b2text

.. image:: https://readthedocs.org/projects/b2text/badge/?version=latest
        :target: https://b2text.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Package to convert basf2 steering to text.


* Free software: MIT license

Usage
-----

Append ``b2text.`` in front of all basf2 imports like so:

.. code-block:: python

  import b2text.basf2 as b2
  import b2text.modularAnalysis as ma
  import b2text.stdCharged as sc

and then run the script to get description text in LaTeX. 

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
