==============
jolly_brancher
==============


Add a short description here!


Description
===========

A longer description of your project goes here...


Installation
============
```
ahonnecke@contranym:~/src/jolly_brancher$ sudo pip install -e .
Obtaining file:///home/ahonnecke/src/jolly_brancher
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
    Preparing wheel metadata ... done
Installing collected packages: jolly-brancher
  Attempting uninstall: jolly-brancher
    Found existing installation: jolly-brancher 0.0.post1.dev1+g12a84b8.d20210708
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

.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.0.2. For details and usage
information on PyScaffold see https://pyscaffold.org/.
