#!/usr/bin/env python
import sys,httplib,random
from md5 import md5

def main(*args):
  if len(args) < 1: raise ValueError("Should provide database to load")
  random.seed()
  for spl in range(1000002,9999999,30000):
    print 'Loading between %s and %s' % (spl, spl+30000)
    c = httplib.HTTPConnection("127.0.0.1",5984)
    docs = '{"docs":[%s]}' % ','.join(map(lambda ID: randomResult(ID), range(spl,spl+30000,3)))
    c.request("POST",'/%s/_bulk_docs' % args[0], docs, {"Content-Type": "application/json"})
    r = c.getresponse()

def randomResult(ID):
  q1t = random.randint(0,50)
  q2t = random.randint(0,50)
  v1t = random.randint(0,50)
  v2t = random.randint(0,50)
  return  """{
      "_id": "%s",
      "name": "%s",
      "passwd": "%s",
      "t": {
        "q1": %d,
        "q2": %d,
        "v1": %d,
        "v2": %d
      },
      "f": {
        "q1": %d,
        "q2": %d,
        "v1": %d,
        "v2": %d
      },
      "q": {
        "s": %f,
        "r": %d
      },
      "v": {
        "s": %f,
        "r": %d
      },
      "ew": {
        "s": %f,
        "r": %d
      }
    }""".strip().replace('\n','').replace('  ','') % (
      ID,
      name_generator(),
      md5(str(ID)).hexdigest(),
      q1t, q2t, v1t, v2t,
      50 - q1t, 50 - q2t, 50 - v1t, 50 - v2t,
      random.uniform(100, 0), 0,
      random.uniform(100, 0), 0,
      random.uniform(100, 0), 0,
    )


def name_generator():
  first = ["John","George","Amy","Olive","Jack","Kate","Paul"]
  last = ["Hammer","Drill","Cutter","Knife"]
  randomNumber1 = random.randrange(0,len(first))
  randomNumber2 = random.randrange(0,len(last))
  return first[randomNumber1] + " " + last[randomNumber2]
 
if __name__ == "__main__":
  main(*sys.argv[1:])

# vim: set ts=2 sw=2 et:
