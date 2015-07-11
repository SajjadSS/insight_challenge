# Insight Coding Challenge
Solution to the coding challenge for insight data engineering fellowship. All the codes are written using Python
programming language. Python needs to be installed before running the program.
  
## What does the code do?
  
In this program a text file containing several tweets is processed to answer the following questions. Each tweet is stored 
in a seperate line in the text file.  

1. Calculate the total number of times each word has been tweeted.  
2. Calculate the median number of unique words per tweet, and update this median as tweets come in.  
  

## Directories and files  
  
**"src"** contains two Python files.    
- "words_tweeted.py" finds answer to question 1.  
- "median_tweet.py" finds answer to question 2.  
  
**"tweet_input"** contains the input text file "tweets.txt".   
  
**"tweet_output"** contains the output files.  
- "ft1.txt" is the output of "words_tweeted.py". It contains all words and number of times each has been repeated.  
- "ft2.txt" is the output of "tweet_output.py". It contains the medians.   
   
**"Run.sh"** is the shell script of the whole program.  

## How to run the program?
  
In order to run the program you just need to open the shell script "Run.sh" in Terminal (command for windows). Results are "ft1.txt" 
and "ft2.txt" stored in the "tweet_output" folder.


