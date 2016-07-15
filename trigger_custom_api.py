import urllib2

def send_url(url):
    req = urllib2.Request(url)
    handle = urllib2.urlopen(req)
    return handle.read()

# print send_url("http://127.0.0.1:5000/")
# print send_url("http://10.0.164.222:9090/")
print send_url("http://syllogist.azurewebsites.net/articles")
