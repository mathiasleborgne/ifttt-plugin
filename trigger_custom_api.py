import urllib2

import argparse

parser = argparse.ArgumentParser(description="Check server stuff")
parser.add_argument("--local", action="store_true",
                         help="Check API on local server")
args = parser.parse_args()


def send_url(url):
    req = urllib2.Request(url)
    handle = urllib2.urlopen(req)
    return handle.read()

# print send_url("http://127.0.0.1:5000/")
# print send_url("http://10.0.164.222:9090/")
if args.local:
    print send_url("http://localhost:5555/articles")
else:
    print send_url("http://syllogist.azurewebsites.net/articles")
