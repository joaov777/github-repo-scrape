### Github username repository scrape
#### What is this for?
This python script scrapes for repositories of a given github username provided

#### How to use this script?
- Running the script directly
```bash
# I advise creating a virtual environment prior to this
python3 github-repo-scrape.py
```
- Building docker image
```bash
docker build -t github-repo-scrape .
docker run -it --rm github-repo-scrape
```


