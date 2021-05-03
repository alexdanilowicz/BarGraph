# BarGraph 🍻

> Get your user data with the Untappd API and run fancy stats on it.

## Local Development 📊

We use a simple Python script to hit the Untappd API. We use R to make graphs and run stats.

### Getting Untappd API Secrets

To run the Python script, you'll need an Untappd `CLIENT_ID` and `CLIENT_SECRET`. Put those in the `.env` file in the root of project, like so:

```
echo "CLIENT_ID=123" >> .env
echo "CLIENT_SECRET=456" >> .env
```

You'll need to apply for an [Untappd API key](https://untappd.com/api/docs).

You'll also need to put USERNAMES in the `.env` file as a list, like so:

```
echo "USERNAMES=alexdannylow,andrewbogo" >> .env
```

The users cannot be private on Untappd.

For a single username, you can exclude the comma:

```
"USERNAMES=alexdannylow"
```

### Running the Python Script

To create the outfile.csv, you'll need to run the Python script to hit the Untappd API.

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

Note that we ignore `.csv` via our `.gitignore`.

### R

#### First time?

Install [Docker Desktop](https://docs.docker.com/desktop/) for your system.

Then, pull the Docker image from Docker Hub:

`docker pull aboghoss/bargraph`

#### Then

```
docker run -it \
  -v <DATA_DIRECTORY>:/data \
  -v <OUTPUT_DIRECTORY>:/out_dir \
   aboghoss/bargraph \
   -d /data/<FILENAME> \
   -o /out_dir
   -n <OUTFILE_NAME>
   -a <ANONYMIZE>
```
`-d`: string name of your data file
`-o`: string name of directory to write to
`-n`: string name of the report that will be created
`-a`: `0` to keep usernames, `1` to anonymize data

The `-v` arguments mount directories to the container allowing them to read and write in those directories. If the directory you want to write to is the same as the one containing your data remove line 94 and edit line 97 to be `-o /data`.

## Deploying 🚀

In our case, the output index.html file in the `site` directory is deployed via [surge](https://surge.sh/) to [http://a-few-beers-later.surge.sh/](http://a-few-beers-later.surge.sh/)

```
surge ./site a-few-beers-later.surge.sh
```
