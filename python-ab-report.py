#!/usr/bin/env python

from subprocess import run,PIPE
from collections import namedtuple
from terminaltables import AsciiTable

class report(object):
  class entry(object):
    class statistic(object):
      min = 0
      mean = 0
      sd = 0
      median = 0
      max = 0
    class percentiles(object):
      _50 = 0
      _66 = 0
      _75 = 0
      _80 = 0
      _90 = 0
      _95 = 0
      _98 = 0
      _99 = 0
      _100 = 0
    class requests(object):
      complete = 0
      failed = 0
      non_2xx = 0
      keepAlive = 0
    class server(object):
      serverSoftware = ""
      serverHostname = ""
      sslTlsProtocol = ""
      serverPort = 0
      serverTempKey = ""
      tlsServerName = ""
    class functions(object):
      def serverSoftware(self, line):
        pass
      def serverHostname(self, line):
        pass
      def serverPort(self, line):
        pass
      def sslTlsProtocol(self, line):
        pass
      def serverTempKey(self, line):
        pass
      def tlsServerName(self, line):
        pass
      def documentPath(self, line):
        pass
      def documentLength(self, line):
        pass
      def concurrencyLevel(self, line):
        pass
      def timeTakenForTests(self, line):
        pass
      def completeRequests(self, line):
        pass
      def failedRequests(self, line):
        pass
      def non_2xxResponses(self, line):
        pass
      def keepAliveRequests(self, line):
        pass
      def totalTransferred(self, line):
        pass
      def htmlTransferred(self, line):
        pass
      def requestsPerSecond(self, line):
        pass
      def timePerRequest(self, line):
        pass
      def timePerRequestMean(self, line):
        pass
      def transferRate(self, line):
        pass
      def connect(self, line):
        pass
      def processing(self, line):
        pass
      def waiting(self, line):
        pass
      def total(self, line):
        pass
      def get50(self, line):
        pass
      def get66(self, line):
        pass
      def get75(self, line):
        pass
      def get80(self, line):
        pass
      def get90(self, line):
        pass
      def get95(self, line):
        pass
      def get98(self, line):
        pass
      def get99(self, line):
        pass
      def get100(self, line):
        pass

    documentPath = ""
    documentLength = 0

    concurrencyLevel = 0
    timeTakenForTests = 0
    totalTransferred = 0
    htmlTransferred = 0
    requestsPerSecond = 0
    timePerRequest = 0
    timePerRequestMean = 0
    transferRate = 0

    request = requests()
    connect = statistic()
    processing = statistic()
    waiting = statistic()
    total = statistic()
    percentile = percentiles()

    function = functions()

  commands = [
    "ab -k -f TLS1.2 -c 5 -t 5 -q https://en.wikipedia.org/wiki/Main_Page",
    "ab -k -f TLS1.2 -c 5 -t 5 -q https://en.wikipedia.org/wiki/Transmission_Control_Protocol"
  ]

  def __init__(self):
    self.process()

  def process(self):
    for command in self.commands:
      result = run(command.split(' '), stdout=PIPE)
      for line in result.stdout.splitlines():
        print(line)
        #FUNCTIONS

if __name__ == '__main__':
    report()

'''
b'Server Software:        Dreamlab'
b'Server Hostname:        www.onet.pl'
b'Server Port:            443'
b'SSL/TLS Protocol:       TLSv1.2,ECDHE-RSA-AES128-GCM-SHA256,2048,128'
b'Server Temp Key:        ECDH P-256 256 bits'
b'TLS Server Name:        www.onet.pl'
b''
b'Document Path:          /'
b'Document Length:        705505 bytes'
b''
b'Concurrency Level:      5'
b'Time taken for tests:   10.006 seconds'
b'Complete requests:      257'
b'Failed requests:        0'
b'Keep-Alive requests:    257'
b'Total transferred:      181479265 bytes'
b'HTML transferred:       181314785 bytes'
b'Requests per second:    25.68 [#/sec] (mean)'
b'Time per request:       194.675 [ms] (mean)'
b'Time per request:       38.935 [ms] (mean, across all concurrent requests)'
b'Transfer rate:          17711.40 [Kbytes/sec] received'
b''
b'Connection Times (ms)'
b'              min  mean[+/-sd] median   max'
b'Connect:        0    2  13.5      0     104'
b'Processing:    57  190 138.6    153    1242'
b'Waiting:       19  103  30.1    104     156'
b'Total:         57  192 145.6    153    1343'
b''
b'Percentage of the requests served within a certain time (ms)'
b'  50%    153'
b'  66%    182'
b'  75%    189'
b'  80%    210'
b'  90%    302'
b'  95%    372'
b'  98%    551'
b'  99%    905'
b' 100%   1343 (longest request)'
'''
