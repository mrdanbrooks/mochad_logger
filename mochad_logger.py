#!/usr/bin/env python
#   Copyright 2014 Dan Brooks
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
""" Connects to a Mochad TCP server and logs output to rotating log files. """
import argparse
import ConfigParser
from datetime import datetime
import logging
import logging.handlers
import sys
from twisted.internet import reactor
from twisted.internet.protocol import ReconnectingClientFactory
from twisted.protocols.basic import LineReceiver

# Dont write pyc files
sys.dont_write_bytecode = True

class MochadLogger(LineReceiver):
    """ Receives Messages from Mochad Server and logs the data"""
    delimiter = '\n'

    def __init__(self, logfile, rotate):
        # Attempt to set up the logger with specified log target
        try:
            open(LOG_TARGET, "a").close()
            hdlr = logging.handlers.RotatingFileHandler(logfile, maxBytes=500000, backupCount=rotate)
        except IOError:
            print("Unable to log to %s" % target)
            exit
        self.logger = logging.getLogger("Mochad")
        self.logger.addHandler(hdlr)
        logging.basicConfig(level=logging.DEBUG)

    def get_time_stamp(self):
        return datetime.now().strftime("%m/%d %H:%M:%S")
        
    def connectionMade(self):
        self.logger.info("%s Logging Mochad Server Started!"%self.get_time_stamp())
        self.transport.setTcpKeepAlive(True)

    def lineReceived(self, line):
        self.logger.info(line)

class MochadConnectionManager(ReconnectingClientFactory):
    """ Automagically manages the connection to the host, reconnecting if the
    connection is lost, and backing off the amount of time between tries.
    """

    def __init__(self, protocol):
        self.instance = protocol

    def buildProtocol(self, addr):
        """ Returns the Mochad Logging instance """
#         self.instance = MochadLogger(self)
        return self.instance

    def clientConnectionLost(self, connector, reason):
        print "Lost Connection, Reason:", reason
        ReconnectingClientFactory.clientConnectionLost(self, connector, reason)

    def clientConnectionFailed(self, connector, reason):
        print "Connection Failed. Reason:", reason
        ReconnectingClientFactory.clientConnectionFailed(self, connector, reason)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='mochad_logger', description='A Logging Utility for Mochad')
    parser.add_argument('config', help='logging configuration file')
    args = parser.parse_args(sys.argv[1:])

    config = ConfigParser.SafeConfigParser()
    config.read(args.config)
    HOSTNAME = config.get('MochadServer','host')
    PORT = int(config.get('MochadServer','port'))
    LOG_TARGET = config.get('Logging','logfile')
    ROTATE_NUM = int(config.get('Logging','rotate'))
    print "Connecting to ",HOSTNAME,PORT
    print "Writing logs to ",LOG_TARGET

    mochad_logger = MochadLogger(LOG_TARGET, ROTATE_NUM)
    connection_manager = MochadConnectionManager(mochad_logger)
    reactor.connectTCP(HOSTNAME, PORT, connection_manager)
    reactor.run()
