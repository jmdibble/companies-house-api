import requests

name = "muse"
url_num = "https://4cQ10i70oDMnmWrJKB6QnHNEgU8enNwgw4zNLegU:@api.companieshouse.gov.uk/search?q="+name
print(url_num)
response_company = requests.get(url_num)
print(response_company.json())


