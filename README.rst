############
s3-parse-url
############

.. image:: https://img.shields.io/pypi/pyversions/s3-parse-url
  :alt: PyPI - Python Version

.. image:: https://img.shields.io/pypi/v/s3-parse-url
  :alt: PyPI

.. image:: https://img.shields.io/pypi/l/s3-parse-url
 :alt: PyPI - License


.. image:: https://coveralls.io/repos/github/marazmiki/s3-parse-url/badge.svg?branch=master
 :target: https://coveralls.io/github/marazmiki/s3-parse-url?branch=master

.. image:: https://img.shields.io/codacy/grade/80c1a1af099848ddb5cc86221723f8d5
  :alt: Codacy grade

-----

Parses S3 credentials from the given string and returns it in comfortable
format to pass to popular clients like boto3.

About
=====

This is a small utility to parse locations of buckets of S3-compatible
storage (and, of course, the original Amazon's S3 itself) given in the URL form
like ``s3://bucket/``.

It could be useful in our epoch of the 12-factor applications when it's a
good practice to store credentials inside of environment variables.

Also, these days, there are some notable S3-compatible storage services:

* `Selectel <https://>`_

* `MinIO <https://min.io>`_ `(a self-hosted solution extremely handy for testing)`

And dozens of others.

With ``s3-parse-url``, you can use any one of these services with no doubts about
configuration endpoints. For example, you can connect to your Selectel storage
with ``boto3`` just using ``selectel://my-bucket`` DSN.

That's an example, what it was all about:

.. code:: python

    from s3_parse_url import s3_parse_url
    from s3_parse_url.ext.clients import get_boto3_client

    dsn = "s3://AKIA***OO:XP***@my-bucket/?region=us-east-2"

    # It's a completely ready boto3 client instance to work with Selectel
    s3_client = get_boto3_client(dsn)

Of course, in the code above we worked with Selectel (have you ever heard
about it?). You can work this way with any S3 compatible storage. If you
prefer unknown storage, you can easily create a plugin to add support for
your favorite service. Or, if you are a pervert, you can use a universal ``S3://``
scheme, but in this case, you should manage endpoints by yourself:

.. code:: python

    from s3_parse_url.ext.clients import get_boto3_client

    # Also should work
    dsn = "s3://my-minio-user:my-minio-pass@minio.example.com:9000/?region=us-east-1"

    # A ready client to work with a minio instance
    s3_client = get_boto3_client(dsn)


Supported providers
===================

Currently we have support for these storages

* Amazon S3
* Selectel
* Yandex
* Mail.ru
* MinIO

But you can easily add your own one.

License
=======

This project is licensed under the terms of the MIT license.

