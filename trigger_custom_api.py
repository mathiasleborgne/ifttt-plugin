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
url_api = "http://localhost:5555/" if args.local \
    else "http://syllogist.azurewebsites.net/"
full_url_api = url_api + "robot_say"
print "Getting API on:", full_url_api
print send_url(full_url_api)
