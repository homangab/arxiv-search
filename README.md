# Searching arxiv for papers based on topic and timestamp



## Installation

- Python3.6
- [pandas](https://pandas.pydata.org)
- [numpy](https://numpy.org/)
- [urllib](https://docs.python.org/2/library/urllib.html)


## Description
This script is based on the Arxiv API and is a quick way to scrape arxiv for papers based on topics (like Model-based RL) and a timestamp beyond which to search. The resulting URLs for pdfs along with their first upload timestamps are staored in a csv file.



## Steps

Run `python arxiv_by_topic.py <keywords> --time=<time>` to obtain a csv file `arxiv.csv` of URLs for all papers with the specified keywords in the abstract and first upload timestamp beond the time specified. 

For example, to search for all papers with keywords `model` and `reinforcement` in the abstract with a first upload timestamp beyond Jan 1, 2019, use the following command `python arxiv_by_topic.py model reinforcement --time='2019-01-01'`









