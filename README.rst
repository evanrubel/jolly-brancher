==============
jolly_brancher
==============


A sweet branch creation tool


Description
===========

A longer description of your project goes here...


Installation
============
```
pip install --user jolly-brancher
```

Installation For Development
============
```
ahonnecke@contranym:~/src/jolly_brancher$ python3 -m site | grep USER_SITE
USER_SITE: '/home/ahonnecke/.local/lib/python3.8/site-packages' (exists)
ENABLE_USER_SITE: True
```
Note the USER_SITE packages path, that is passed in to the prefix

```
ahonnecke@contranym:~/src/jolly_brancher$ pip install --prefix=/home/ahonnecke/.local/lib/python3.8/site-packages --force-reinstall -e .
Obtaining file:///home/ahonnecke/src/jolly_brancher
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
    Preparing wheel metadata ... done
Installing collected packages: jolly-brancher
  Attempting uninstall: jolly-brancher
    Found existing installation: jolly-brancher 0.0.post1.dev3+g8723568.d20210709
    Can't uninstall 'jolly-brancher'. No files were found to uninstall.
  Running setup.py develop for jolly-brancher
Successfully installed jolly-brancher
```

Invocation
==========
```
ahonnecke@contranym:~/src/jolly_brancher$ fibonacci
usage: fibonacci [-h] [--version] [-v] [-vv] INT
fibonacci: error: the following arguments are required: INT
```

```
ahonnecke@contranym:~/src/jolly_brancher$ fibonacci 5
The 5-th Fibonacci number is 5
```

This package requires a configuration .ini file. Upon invocation, you will be prompted for your Atlassian login email, the base Atlassian URL for your organization, your API token (which can be generated [here](https://id.atlassian.com/manage-profile/security/api-tokens)), and the path to the root directory for your repositories. Please see `example.ini` for reference.

.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.0.2. For details and usage
information on PyScaffold see https://pyscaffold.org/.
