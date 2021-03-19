# BarGraph 🍻

> Get your user data with the Untappd API and run fancy stats on it

## Deploying

The output index.html file in the `site` directory is deployed via [surge](https://surge.sh/) to [http://untappd-report.surge.sh/](http://untappd-report.surge.sh/)

## Local Development

We use a simple Python script to hit the Untappd API. We use R to make graphs and run stats.

### Getting Untappd API Secrets

To run the Python script, you'll need an Untappd `CLIENT_ID` and `CLIENT_SECRET`. Put those in the `.env` file in the root of project, like so:

```
echo "CLIENT_ID=123" >> .env
echo "CLIENT_SECRET=456" >> .env
```

Apply for an [Untappd API key](https://untappd.com/api/docs)s.

You'll also want to put USERNAMES in thw `.env` file as a list, like so:

```
echo "USERNAMES=alexdannylow,andrewbogo" >> .env
```

### Running the Python Script

#### First time?

Create virutal env:

`python3 -m venv venv`

In the future, we would like to dockerize this.

#### Then:

`source venv/bin/activate`

`pip3 install -r requirements.txt`

Once everything is installed, you can run the script.

```
python3 main.py --help
usage: main.py [-h] [--force] [--outfile OUTFILE]
               [--number-of-unique-beers NUMBER_OF_UNIQUE_BEERS]

Hit the Untappd API for user data 🍻.

optional arguments:
  -h, --help            show this help message and exit
  --force               Actually make a request. Used so you don't blow
                        through your Untappd API limit. (default: False)
  --outfile OUTFILE     Name of outfile. Should match filename in R script.
                        (default: data.csv)
  --number-of-unique-beers NUMBER_OF_UNIQUE_BEERS
                        How many unique beers for each user? (default: 49)
```

Example usage:

```
python3 main.py --force --outfile "allBeers.csv" --number-of-unique-beers 49
```

### R

TODO
