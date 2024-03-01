#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        temp = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(temp)))
        print("\t- content: {}".format(temp))
        print("\t- utf8 content: {}".format(temp.decode()))
