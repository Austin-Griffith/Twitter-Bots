#!/usr/bin/env python

from secrets import *
import urllib2
import base64
import zlib
import threading
from threading import Lock
import json
import sys
import ssl
import pdb
# Tune CHUNKSIZE as needed.  The CHUNKSIZE is the size of compressed data read
# For high volume streams, use large chuck sizes, for low volume streams, decrease
# CHUNKSIZE.  Minimum practical is about 1K.

CHUNKSIZE = 4*1024
GNIPKEEPALIVE = 30  # seconds
NEWLINE = '\r\n'


HEADERS = { 'Accept': 'application/json',
            'Connection': 'Keep-Alive',
            'Accept-Encoding' : 'gzip',
            'Authorization' : 'Basic %s' % base64.encodestring('%s:%s' % (UN, PWD)).replace('\n', '')  }

print(repr(HEADERS['Authorization']))

print_lock = Lock()
err_lock = Lock()

class procEntry(threading.Thread):
    def __init__(self, buf):
        self.buf = buf
        threading.Thread.__init__(self)

    def run(self):
        for rec in [x.strip() for x in self.buf.split(NEWLINE) if x.strip() <> '']:
            try:
                jrec = json.loads(rec.strip())
                tmp = json.dumps(jrec)
                with print_lock:
                    print(tmp)
                    #append to text file
                    # with open('data.txt', 'a') as f:
                    #     print(tmp, file=f)
            except ValueError, e:
                with err_lock:
                    sys.stderr.write("Error processing JSON: %s (%s)\n"%(str(e), rec))

def getStream():
    req = urllib2.Request(URL, headers=HEADERS)
    response = urllib2.urlopen(req, timeout=(1+GNIPKEEPALIVE))
    decompressor = zlib.decompressobj(16+zlib.MAX_WBITS)
    remainder = ''
    while True:
        tmp = decompressor.decompress(response.read(CHUNKSIZE))
        if tmp == '':
            return

        pdb.set_trace()
        [records, remainder] = ''.join([remainder, tmp]).rsplit(NEWLINE,1)
        procEntry(records).start()

if __name__ == "__main__":
# Note: this automatically reconnects to the stream upon being disconnected
    while True:
        try:
            getStream()
            with err_lock:
                sys.stderr.write("Forced disconnect: %s\n"%(str(e)))
        except ssl.SSLError, e:
            with err_lock:
                sys.stderr.write("Connection failed: %s\n"%(str(e)))
