#!/usr/bin/env python

# ExaBGP route generator
# Jonathan P. Voss
# 4/1/2022
#

from ipaddress import ip_network

import re
import sys
import time

nexthop    = sys.argv[1]
max_routes = sys.argv[2]

def announce(prefix, nexthop):
  sys.stdout.write('announce route %s next-hop %s\n' % (prefix.with_prefixlen, nexthop))
  sys.stdout.flush()
  time.sleep(0.0005)

def build_generators():
  blocks = []

  for x in range(1, 255):
    blocks.append(ip_network('%d.0.0.0/8' % x).subnets(new_prefix=24))

  return blocks

def main():
  block = list(build_generators())
  supernet = list(block.pop(0))

  for x in range(0, int(max_routes)):
    try:      
      # announce(supernet.pop(0), nexthop)
      net = supernet.pop(0)
    except IndexError:
      supernet = list(block.pop(0))
      net = supernet.pop(0)

    announce(net, nexthop)

  # Prevent looping updates
  while True:
    time.sleep(1)

if __name__ == "__main__":
  main()