from dotenv import load_dotenv
import os
import requests
load_dotenv()
import json

API_URL=os.getenv("shopify_product_url")
url=API_URL+'?limit=250'
products=[]
headers={'Content-Type': 'application/json'}
r=requests.get(url,headers=headers)
products.append(r.json()['products'])

header_link=r.headers['Link']
header_link_arr=header_link.split(',')
print(header_link_arr)

while not(header_link.find('rel="next"')==-1):
    # if(len(header_link_arr)==2):
    #     print(header_link_arr[0])
    #     print(header_link_arr[1])
    #     break
    
    # print(page_rel)
    if(len(header_link_arr)==2):
        page_rel=header_link_arr[1]        
        page_rel=page_rel[page_rel.find('&')+1:]
    else:
        page_rel=header_link_arr[0]
        page_rel=page_rel[page_rel.find('&')+1:]
    
    next_page_rel=page_rel[page_rel.find('=')+1:page_rel.find('>')]
    
    url=API_URL+'?limit=250&page_info='+next_page_rel
    r=requests.get(url,headers=headers)
    products.append(r.json()['products'])

    header_link=r.headers['Link']
    header_link_arr=header_link.split(',')
    
    print(header_link_arr)


# if not(page_rel.find('rel="next"')==-1):
#     next_page_rel=page_rel[page_rel.find('=')+1:page_rel.find('>')]
#     print(next_page_rel)

with open('products.json', 'w') as fout:
    json.dump(products , fout)