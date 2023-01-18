# ETF scraper
> Scrapes ETF (Exchange Traded Fund) Listed on Borsa Italiana and output to excel files..


## Installation

OS X & Linux:

```sh
git clone https://github.com/Fabio82/etf-scraper.git
cd etf-scraper
pipenv sync

```

## Usage example

It is very simple:
```sh 
pipenv run python scrap.py
pipenv run python excel-maker.py
```


the program will generate one excel with all the etf and an excel with the dividend of those etf that have dividends.

## Meta

Fabio82 – [@fabio8ne](https://twitter.com/fabio8ne)

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/fabio82/etf-scraper](https://github.com/fabio82/etf-scraper)

## Contributing

1. Fork it (<https://github.com/fabio82/etf-scraper>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
