from time import sleep
import urllib.request
from instagram_private_api import Client
import json

i = 0
shopify_KEY = 'd4608573e15a72d2fa23028c26a9b767'
shopify_PASS = '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'
shopify_NAME = 'Swosh3d'
shopify_URL = 'https://%s:%s@%s.myshopify.com/admin' % (shopify_KEY, shopify_PASS, shopify_NAME)
shopify_ORDERS = shopify_URL+"/api/2021/01/orders.json"
shopify_ORDER_URL = 'https://swosh3d.myshopify.com/admin/api/2021-01/orders.json'

username = 'swoshop'
password = 'kesako69'
instagram = Client(username, password)

def credit(url, username, password):
    p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, url, username, password)
    handler = urllib.request.HTTPBasicAuthHandler(p)
    opener = urllib.request.build_opener(handler)
    urllib.request.install_opener(opener)

def check_orders():
    print("...")
    orders = json.loads(urllib.request.urlopen(shopify_ORDER_URL).read())
    previous_len = len(orders["orders"])
    while True:
        orders = json.loads(urllib.request.urlopen(shopify_ORDER_URL).read())
        sleep(1)
        if len(orders["orders"]) > previous_len: 
            order_title = orders["orders"][0]["line_items"][0]["title"]
            return new_order(True, orders, order_title)
            
def new_order(trlse, orders, title):
    new_bio = "Commandes: %s" % len(orders)
    instagram.edit_profile(first_name="Swosh", biography=new_bio, external_url="https://swosh.ch/", email="info@swosh.ch", phone_number="+41761234567", gender=3)
    print("Nouvelle commande: %s" % title)
    check_orders()


credit(shopify_ORDER_URL, shopify_KEY, shopify_PASS)

check_orders()
