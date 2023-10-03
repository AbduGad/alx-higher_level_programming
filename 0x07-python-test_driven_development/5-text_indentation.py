#!/usr/bin/python3
def text_indentation(text):
	if not isinstance(text, str):
		raise TypeError("text must be a string")
	c = 0
	while c < len(text):
		if text[c] in ".?:":
			print(text[c], end = "\n\n")
			c += 1
		else:
			print(text[c], end = '')
		c += 1
	print()
