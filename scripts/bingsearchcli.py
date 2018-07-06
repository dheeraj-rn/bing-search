#!/usr/bin/env python3
import urllib.parse
import requests
import argparse
import re, sys


def output(outfile, output_list):
	file_var = open(outfile,'w')
	no_of_links = len(output_list)
	for i in range(no_of_links):
		file_var.write(output_list[i])
		file_var.write('\n')


def search(query, outfile, limit):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0', 'Referer': 'https://www.bing.com/'}
	session = requests.Session()
	end_of_search = 'No results found for <strong>' + query + '</strong>'
	enc_query = urllib.parse.quote(query)
	output_list = []
	if_limit = False
	sw_next = True
	response = ''
	next = 1

	if limit :
		limit = (limit - 1) * 10 + 1
		if_limit = True

	try:
		while end_of_search not in response and sw_next == True:
			search_url = 'https://www.bing.com/search?q=' + enc_query + '&go=Submit&qs=n&pq=' + enc_query + '&first=' + str(next) + '&FORM=PERE'
			response = session.get(search_url, headers=headers)
			hrefs = re.findall('<h2><a href="\S+', response.text)

			for href in hrefs:
				temp = href.replace('<h2><a href="http://', 'http://').replace('<h2><a href="', '')
				url = temp.replace('"', '').replace('amp;', '')
				if not outfile:
					print(url)
				else:
					output_list.append(url)

			if if_limit:
				if next < limit and re.findall('Next\S+', response.text):
					sw_next = True
				else:
					sw_next = False
			elif re.findall('Next\S+', response.text):
				sw_next = True
			else:
				sw_next = False
			next = next + 10

		if outfile:
			output(outfile, output_list)

	except Exception:
		print('Connection Error')


def main():
	description = 'Bing Search Cli'
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument('query', type=str, help='Your search query.')
	parser.add_argument('-w', '--outfile', type=str, help='Write to the specified output file instead of standard output.')
	parser.add_argument('-l', '--limit', type=int, help='Limit the Number of pages to check.')
	args = parser.parse_args()
	print('Searching for:', args.query, '\n')
	query = args.query
	outfile = args.outfile
	limit = args.limit
	search(query, outfile, limit)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('Exiting..')
		sys.exit()
