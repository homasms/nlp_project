"# nlp_project" 

this is a project to analyse Maulana Rumi's poems and compare two books of his names Masnavi and Divan-e Shams.
we are using NLP tools and methods for analysis.
python selenium library is used for gathering data from ganjoor.net website.

to gather data you should run crawling.py.
to run whole code run it without argument,
to gather Masnavi, run crawling.py with -m argument,
to gather Divan-e Shams, run crawling.py with -s argument.

to break words:
run without argument: run whole code
run with -m argument: break Masnavi to its words
run with -s argument: break Divan-e Shams to its words

to do statistics:
run without argument: run whole code
run with -b argument: number of units
run with -w argument: number of words
run with -u argument: number of unique words in each dataset
run with -c argument: number of common words
run with -r argument: 10 most used words in each dataset
run with -rnf argument: 10 words chosen by rnf from each dataset
run with -tf argument: 10 words chosen by tf-idf from each dataset
run with -hist argument: plot word-count for 100 words in each dataset
