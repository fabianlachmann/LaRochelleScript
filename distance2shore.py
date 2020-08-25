import requests
#IDK why tf no works

lat = "56.95415"
lon = "-7.492229"
key = "b19d3b66-0ac1-4ccc-b1dc-d8ba54be4610"

url1 = "https://api.kbgeo.com/coastal-distance/v2/coord?lat=<"+lat+">&lng=<"+lon+">"

url = "https://api.kbgeo.com/coastal-distance/v2/coord?lat=<56.954153>&lng=<-7.492229>"

headers1 = {"kb-auth-token: "+key}

headers = {"kb-auth-token: b19d3b66-0ac1-4ccc-b1dc-d8ba54be4610"}
r = requests.get(url, auth=headers)

response = r.json()

print(response)