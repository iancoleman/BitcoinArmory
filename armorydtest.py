from jsonrpc import ServiceProxy

#curl --user user --data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "getwalletinfo", "params": [] }'  -H 'content-type: text/plain;' http://127.0.0.1:8225/

user = "user"
password = "password"
host = "127.0.0.1"
port = 18225
url = "http://%s:%s@%s:%i" % (user, password, host, port)

access = ServiceProxy(url)

print "Testing rpc at %s" % url
print

print "getinfo()"
print access.getinfo()
print

print "getwalletinfo()"
print access.getwalletinfo()
print

