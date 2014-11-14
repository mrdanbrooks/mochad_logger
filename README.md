mochad_logger
=============

A logging daemon for mochad.

Installation
------------
Clone the git repository

```bash
$ git clone https://github.com/mrdanbrooks/mochad_logger.git
```

The module `mochad_logger` can be used by itself from this directory, or you can install it. 
Installation requires setuptools. In ubuntu you can install setuptools using 

```bash
$ sudo apt-get install python-setuptools
```

Then you can install mochad_logger using

```bash
$ sudo python setup.py install
```

**Note:** This does not install mochad itself. For information about installing mochad see https://github.com/njh/mochad.



Usage
-----

Make sure Mochad is already started. The logger can then be started by running

```bash
$ mochad_logger mochad_logger.conf
```


Configuration File
------------------
A configuration file is required to run the logger. An example is given below

```
[MochadServer]
host: localhost
port: 1099

[Logging]
RotationPeriod: 5
logfile: ./mochad.log
```
