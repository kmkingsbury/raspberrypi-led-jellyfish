#!/usr/bin/python

import os


import time
from time import gmtime, strftime
import threading
#import yaml
import requests, json
import sys, argparse

from pprint import pprint


# Load Config

def mainargs(argv):
  parser = argparse.ArgumentParser(description='Poll Build Server.',
  formatter_class=SmartFormatter
  )
  parser.add_argument('-c', '--config', nargs=1, required=False,
                 help='Config File')
  args = parser.parse_args()
  return args


class SmartFormatter(argparse.HelpFormatter):

    def _split_lines(self, text, width):
        # this is the RawTextHelpFormatter._split_lines
        if text.startswith('R|'):
            return text[2:].splitlines()
        return argparse.HelpFormatter._split_lines(self, text, width)



# Parse Args, handle options
args = mainargs(sys.argv[1:])
configfile = "config.json"
if args.config: configfile = args.config[0]

print "Config: " + configfile

# Load and Parse
with open(configfile) as data_file:
    configdata = json.load(data_file)

pprint(configdata)

print "Site: " + str(configdata['tentacle'][1]['URL'])

# Curl

url = str(configdata['tentacle'][0]['URL'])
headers = {'user-agent': 'my-app/0.0.1', 'Accept': 'application/vnd.travis-ci.2+json'}

r = requests.get(url, headers=headers)
print r.text

resp = r.json()
print "Last Build Status: " + str(resp['repo']['last_build_state'])
if str(resp['repo']['last_build_state']) == '': #null
    print "never built"
elif str(resp['repo']['last_build_state']) == 'passed':
    print "pass"
elif str(resp['repo']['last_build_state']) == 'failed':
    print "fail"
elif str(resp['repo']['last_build_state']) == 'errored': # such as repo doesnt exist
    print "fail"
elif str(resp['repo']['last_build_state']) == 'started':
    print "building"
elif str(resp['repo']['last_build_state']) == 'created': # job queued
    print "building"
elif str(resp['repo']['last_build_state']) == 'canceled': #
    print "build cancled"
else:
    print "unknown: "+str(resp['repo']['last_build_state'])
