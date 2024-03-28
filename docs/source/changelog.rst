Changelog
#########

0.4.x
=====


0.4.0
-----

Released 2024-03-28

* Just removed Python 3.7 support
* Updated development stuff (github action versions, deps, etc)

0.3.x
=====


0.3.2
-----

Released 2024-03-28

* Tested support for python ``3.11`` and ``3.12``

0.3.1
-----

Released 2022-06-06

* Fixed the issue when a secret key contains special chars (fixed by urlquoting). The solution authored by `@nikell28 <https://github.com/nikell28>`_ from the refused `PR <https://github.com/marazmiki/s3-parse-url/pull/2>`_
* Filled ``docs/source/authors.rst`` a bit :)

0.3.0
-----

Released 2022-01-06

A technical minor release to check if it will be automatically delivered to PyPI.

0.2.x
=====

0.2.1
-----

Released 2022-01-06

* Fixed a misspell in README that caused a fail while publishing the package
* Fine tuned the ``.github/workflows/pypi.yml``

0.2.0
-----

* Prettified the project metadata inside ``pyproject.toml`` to make pypi release more sexy
* A new action to automatic publish the package on PYPI
* ce32a12 2022-01-06 | Decorate our readme with badges [Mikhail Porokhovnichenko]

0.1.x
=====

0.1.0
-----

The initial release issued 2021-10-05

* Basic functionality: parse schemes
* Ability to add custom scheme l
* Support scheme of some popular s3-compatible storages:

  * Amazon AWS S3 (of course, ``s3://``)
  * Selectel Storage (``selectel://``)
  * Mail.Ru Cloud (``mailru://``, ``mailru+hot://`` and ``mailru+ice://``: first two ones for the standard storage, the last one for "cold" storage)
  * Yandex Cloud (``yandex://``)

* Ability to add an arbitrary scheme: wanna ``linode://``? Or ``digitalocean://``? Fill free to add
