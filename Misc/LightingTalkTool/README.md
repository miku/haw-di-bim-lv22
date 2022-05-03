# Lightning Talk: jq 

> Martin Czygan, 2022-05-03, 08:30 CEST

# Motivation: JSON

* [JSON](https://en.wikipedia.org/wiki/JSON) is one of the most popular data formats on the web

This is how it looks:

```json
{
  "name": "Martin Czygan",
  "favorite_number": 42,
  "hobbies": [
    "programming",
    "reading",
    "🚲"
  ]
}
```

It is mostly mappings (keys and values) and lists. 

# The web is full of JSON

If some institution or entity wants to publish more than lists, they may use JSON.

From [TikTok](https://www.tiktok.com/node/share/discover) to
[DNB](https://hub.culturegraph.org/entityfacts/118540238), everyone is using
JSON.

These are sometimes called Web APIs - web application programming interfaces,
because JSON is easy for a machine to consume.

# Consuming JSON

* `jq` allows to pretty print JSON and perform operations on it
* useful to inspect and filter data
* it has a mini-language for expressing what you want to do (need to learn this first 😔)

```shell
$ curl https://api.coindesk.com/v1/bpi/currentprice.json > price.json

$ jq . price.json
{
  "time": {
    "updated": "May 3, 2022 05:46:00 UTC",
    "updatedISO": "2022-05-03T05:46:00+00:00",
    "updateduk": "May 3, 2022 at 06:46 BST"
  },
  "disclaimer": "This data was produced from ....",
  "chartName": "Bitcoin",
  "bpi": {
    "USD": {
      "code": "USD",
      "symbol": "&#36;",
      "rate": "38,486.5267",
      "description": "United States Dollar",
      "rate_float": 38486.5267
    },
    "GBP": {
      "code": "GBP",
      "symbol": "&pound;",
      "rate": "30,757.2390",
      "description": "British Pound Sterling",
      "rate_float": 30757.239
    },
    "EUR": {
      "code": "EUR",
      "symbol": "&euro;",
      "rate": "36,646.9477",
      "description": "Euro",
      "rate_float": 36646.9477
    }
  }
}

$ jq .bpi.EUR.rate_float price.json
36646.9477
```

It allows to flatten JSON, which is sometimes useful, too:

```shell
$ jq -rc '.bpi|to_entries[]| [.key, .value.rate_float] | @tsv' price.json
USD     38486.5267
GBP     30757.239
EUR     36646.9477
```

## Random internet user

> jq is a cool tool

-- https://wclarke.net/posts/2018-06-08--jq-is-a-cool-tool.html
