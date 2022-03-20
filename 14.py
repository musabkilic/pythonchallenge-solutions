import xmlrpc.client
s = xmlrpc.client.ServerProxy(
    "http://www.pythonchallenge.com/pc/phonebook.php")
print(s.phone("Bert"))
