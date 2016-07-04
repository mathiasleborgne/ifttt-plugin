
import urllib
import urllib2

secret_key="ndiOkN5RH40vmI-AgK5rx717BpSL2i9vXjw6gsNtB-8"
# string=$IFS
# IFS='=&'
# param=($QUERY_STRING)
# param_0, param_1 = param
# IFS=$string

def send_url(url):
    req = urllib2.Request(url)
    handle = urllib2.urlopen(req)
    return handle.read()

def trigger_event(trigger_name, data_dict):
    additional_data = "?" + urllib.urlencode(data_dict)
    return send_url("https://maker.ifttt.com/trigger/{trigger}/with/key/{secret_key}{additional_data}"\
         .format(secret_key=secret_key, trigger=trigger_name,
                 additional_data=additional_data))

data_dict = {"value1": "Stuuuff"}
trigger_name = "robot_heard_word"
print trigger_event(trigger_name, data_dict)

param_0, param_1 = "param_0", "param_1"
"""
Content-type: text/html

<html>
    <head><title>Maker Channel</title></head>
    <body>
        <p>{param_0} = {param_1}</p>
    </body>
</html>
""".format(param_0=param_0, param_1=param_1)