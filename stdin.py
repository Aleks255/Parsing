import sys, re
from urllib.request import urlopen


def main():
	text = sys.stdin.readline()
	urls = re.findall(r'(https?://[^\n\s\\]+)', text)
	total = 0
	for URL in urls:
		response = str(urlopen(URL).read().decode('utf-8').split())
		res = len(re.findall(r'(\bgo\W+)', response))
		print(URL, ": ", res)
		total += res
	print("Total: ", total)


if __name__ == '__main__':
	main()