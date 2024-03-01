#!/usr/bin/python3
"""
POST request to the passed URL with the email as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
	def main(argv):
		"""
		Sends a POST request to the passed URL with the email as a parameter,
		and displays the body of the response (decoded in utf-8)
		"""
		values = {'email': argv[2]}
		url = argv[1]
		r = requests.post(url, data=values)
		print(r.text)
