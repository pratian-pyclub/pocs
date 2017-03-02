## ACO AI Engine

### Installation
Clone the repo and CD into the ACO folder
```
git clone https://github.com/skcript/aco.git
cd aco
```

## Usage
Enter Python shell and import ACO
```
>> python
>>> from aco import ACO
```

From `./aco/data/members.yml`, choose a MemberID and create and object of ACO
```
>>> aco = ACO(1887)
```

Call `similar()` to get a list of MemberIDs that are similar to given ID
```
>>> aco.similar()
>>> [{2.0: 852}, {0.1092: 4728}, {0.0: 4914}, {0.0: 256}]
```

### Understanding the Output
The output returns an ordered array of dictionaries. Each element is a dictionary!

The key gives the score and the value gives the MemberID.

In the above example, Member #852 has the largest similarity with Member #1887.

### Similarity Calculation Algorithm
1. Normalize both text values by converting to lowercase and removing punctuation.
2. Steam all the words using NLTKs [SnowballStemmer](http://www.nltk.org/howto/stem.html)
3. Create a TFIDF ([term frequency–inverse document frequency](https://en.wikipedia.org/wiki/Tf–idf)) vector
4. Ignore all English stop words like "the", "to", "and" etc.
5. Calculate the cosine all word vectors

### Patient Similarity Algorithm
1. Get Member's CPT and ICD record
2. Calculate similarity of CPT and ICD description against member description
3. Combine and order both CPT and ICD values
4. List top N similar patients
