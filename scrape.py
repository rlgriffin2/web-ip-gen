import requests
import re
import ipaddress
def scrape():
    data = requests.get('https://rlgriffin2.github.io/web-ip-gen/')
    refined = ""

    for c in data.text:
        if c.isdigit() or c =='.':
            refined += c

#ip = ipaddress.ip_address(refined)
    try:
        ip = ipaddress.ip_address(refined)
        print(ip)
        return ip
    except:
        print("That is not a valid ip")
        print(refined)
        return 0

if __name__ == '__main__':
    scrape()
