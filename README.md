Outline of Case Studies, Labs and Projects for the four verticals of AI.

## Machine Learning

### Labs:
1. Classification of Multivariate Gaussion Distribution using FeedForward Network

### Projects:
1. Automatic Image Classification with Neural Networks and PyBrain

The learnings will be,
- Understanding implementation difference between Classification and Regression
- Data split importance
- Accuracy Calculations

The skills learned will be,
- Reading images with Python
- Converting images to datasets
- Feature extraction in images that will lead to classification

### Case Studies:
1. Back Propagation Algorithm Implementation with Python

## NLP

### Labs:
1. Conditional Frequency Distributions
    - Conditions and Events
    - Counting Words by Genre
    - Plotting and Tabulating Distributions
2. Convert English Text to Pig Latin
    - Definition of Pig Latin Each word of the text is converted as follows: move any consonant (or consonant   cluster) that appears at the start of the word to the end, then append ay, e.g. string → ingstray, idle → idleay. http://en.wikipedia.org/wiki/Pig_Latin
    - Write a function to convert a word to Pig Latin.
    - Write code that converts text, instead of individual words. Extend it further to preserve capitalization, to keep qu together (i.e. so that quiet becomes ietquay), and to detect when y is used as a consonant (e.g. yellow) vs a vowel (e.g. style).
3. Process the Brown Corpus to find answers to the following questions,
    - Which nouns are more common in their plural form, rather than their singular form? (Only consider regular plurals, formed with the -s suffix.)
    - Which word has the greatest number of distinct tags. What are they, and what do they represent?
    - List tags in order of decreasing frequency. What do the 20 most frequent tags represent?
    - Which tags are nouns most commonly found after? What do these tags represent?
4. Write a tag pattern to identify places of work from a set of resumes by building your own grammar.

### Projects:
Analysis of a real world event using Twitter data. This includes graphing with matplotlib.

The various analysis will be,
- Sentiment Classification
- Keyword Extraction
- Frequency Distribution

The feature extractors will be,
- Unigrams + Bigrams
- Frequency Distribution Extraction

Skills learnt will be,
- Data Gathering
- Data Classification
- Data Normalizing
- Graphing
- JSON API Calls and Ratelimiting
- Reading and Storing YAML data

### Case Studies
1. Resume Parser
- Accepts resumes in PDF format
- Must parse the applicants for,
    - Name
    - Birthdate
    - Address
    - Experience in years
    - Categorize skills

## Algorithmic Programming

### Labs:
- Sierpinski Triangle
- Tower of Hanoi
- Exploring a Maze
- Implementing a binary search tree that accepts any input type
- The Knight’s Tour Problem

### Projects:
1. Create rate-limiting tool with Python and Redis
  - Use the Python Redis package, https://pypi.python.org/pypi/redis.
  - Redis will be used to store all the values to be processed.
  - A background job  will read the data from Redis and process them at regular intervals.
  - Background jobs will be managed using the RQ Python package, http://python-rq.org/
  - Create a CLI function that would start these background processes

### Case Studies
1. An Anagram Detection Example using multiple Algorithm Solutions
    - Solution 1: Checking Off
    - Solution 2: Sort and Compare
    - Solution 3: Brute Force
    - Solution 4: Count and Compare
2. Longest Common Sunsequence Algorithm Python Implementation
3. Automatic Text Generation with Hidden Markov Models

## Bayesian Inference

### Labs:
1. Modelling Coin flip patterns using Bayes Rule

### Projects:
1. Ordering Reddit submissions
    - Theory
      - Relook at Law of Large Numbers Relook at Naive Bayes Theorem
      - Relook at Gaussian distribution
    - Introduction to the problem
    - Discussion on factors involved
      - Popularity (Number of upvotes)
      - Difference of upvotes and downvotes
      - Time adjusted (rate of upvotes/downvotes)
      - Ratio of upvotes to total number of votes
    - Understanding how human behavior affects data

### Case Studies
1. Algorithm for human deceit
    - A look at Binomial distribution
    - Example: Cheating Students
