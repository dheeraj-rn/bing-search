# Bing Search [![Last commit](https://img.shields.io/github/last-commit/dheeraj-rn/bing-search.svg)](https://github.com/dheeraj-rn/bing-search/commits/master) [![License](https://img.shields.io/github/license/dheeraj-rn/bing-search.svg)](https://github.com/dheeraj-rn/bing-search/blob/master/LICENSE.md)
Python command line application to search queries and dorks on [bing.com](https://www.bing.com/) and return urls in the search results
## Dependencies  

Requires `Python3+` and `pip`

## Installing

### Source
```sh
$ git clone https://github.com/dheeraj-rn/bing-search.git
$ cd bing-search
$ sudo python3 setup.py install
```

## Usage
### Options
```sh
$ bing --help
usage: bing [-h] [-w OUTFILE] [-l LIMIT] query

Bing Search

positional arguments:
  query                 Your search query.

optional arguments:
  -h, --help            show this help message and exit
  -w OUTFILE, --outfile OUTFILE
                        Write to the specified output file instead of standard
                        output.
  -l LIMIT, --limit LIMIT
                        Limit the Number of pages to check.
  -x PROXY, --proxy PROXY
                        Proxy to be used. Format:
                        [PROTOCOL://][USER:PASSWORD@]HOST[:PORT]                      
```

### Basic Usage
```sh
$ bing "linux"           #outputs search results to terminal screen
```

### Search Dork Query
```sh
$ bing "index.php?id="   #outputs search results to terminal screen
```

### Write search results to file
```sh
$ bing "linux" -w output.txt         #Writes search results to output.txt
$ bing "linux" --outfile output.txt
```

### Limit number of pages to check on bing search
```sh
$ bing "linux" -l 2           #outputs search results in first 2 pages in bing search
$ bing "linux" --limit 2
```

## Contribute

Found an issue? Post it in the [issue tracker](https://github.com/dheeraj-rn/bing-search/issues). <br> 
Want to add another awesome feature? [Fork](https://github.com/dheeraj-rn/bing-search/fork) this repository and add your feature, then send a pull request.

## License
The MIT License (MIT)