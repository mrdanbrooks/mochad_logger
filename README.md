mochad_logger
=============

A logging daemon for mochad.


Installation
------------
Download the debian installer from [github](https://github.com/mrdanbrooks/mochad_logger/releases/download/0.0.2/mochad-logger.deb)

Install the package using the following commands

```bash
$ sudo dpkg -i --force-depends mochad-logger.deb
$ sudo apt-get -f install
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
