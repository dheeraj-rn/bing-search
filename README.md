# Bing Search Cli

## Dependencies  

Requires `Python3+` and `pip`

## Installing

### Source
```sh
$ git clone https://github.com/dheeraj-rn/BingSearchCli.git
$ cd BingSearchCli
$ sudo python3 setup.py install
```

## Usage
### Options
```sh
$ bingsearchcli --help
usage: bingsearchcli [-h] [-w OUTFILE] [-l LIMIT] query

Bing Search Cli

positional arguments:
  query                 Your search query.

optional arguments:
  -h, --help            show this help message and exit
  -w OUTFILE, --outfile OUTFILE
                        Write to the specified output file instead of standard
                        output.
  -l LIMIT, --limit LIMIT
                        Limit the Number of pages to check.
```

### Basic Usage
```sh
$ bingsearchcli "linux"           #outputs search results to terminal screen
```

### Write search results to file
```sh
$ bingsearchcli "linux" -w output.txt         #Writes search results to output.txt
$ bingsearchcli "linux" --outfile output.txt
```

### Limit number of pages to check on bing search
```sh
$ bingsearchcli "linux" -l 2           #outputs search results in first 2 pages in bing search
$ bingsearchcli "linux" --limit 2
```

## Contribute

Found an issue? Post it in the [issue tracker](https://github.com/dheeraj-rn/BingSearchCli/issues). <br> 
Want to add another awesome feature? [Fork](https://github.com/dheeraj-rn/BingSearchCli/fork) this repository and add your feature, then send a pull request.

## License
The MIT License (MIT)