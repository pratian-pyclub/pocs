# Movrec
Movie recommender based on IMDB user behaviour. This dataset has ratings given by 943 users over 1682 movies with 5 being the largest rating and 0 being no rating.

Movrec uses a Collaborative Filtering (CF) to determine similar movies based on item-item and user-item models. What this means is,

- **Item-Item Collaborative Filtering**: “Users who liked this movie also liked …”
- **User-Item Collaborative Filtering**: “Users who are similar to you also liked these movies …”

The system does not do chain recommendations. Meaning all similar movies are found using a feed forward network. If Movie A recommendation is Movie B, it does not entail Movie B to have a recommendation as Movie A.

## Pre Requisite Packages
1. os [Default]
2. pickle : `pip install pickle`
3. pandas : `pip install pandas`
4. numpy : `pip install numpy`
5. scikit-learn : `pip install scikit-learn`

## Installation
1. Clone this repo
2. Cd into "movrec"
3. Install the package using,
```
python setup.py install
```

## Shell Access
Open Python shell and type in,

```
from movrec import Movrec
m = Movrec()

> Populating...
> 943 users
> 1682 movies
> Sparsity: 6.30%
```

## Command Line Access
In order to use `movrec` over the terminal, you must first save your model. Command line access only allows read access, the model can not be trained via CMD.
#### Show Similar Movies
To show movies which are similar to a said movie, simply pass in the movie_id to,
```
movrec similar_movies -id 1
```
This will return all the movies that the users of said movie have watched most frequently.

To display the similar movies based upon similar user behavious, simply pass in the movie_id to,
```
movrec similar_movies_via_user_behaviour -id 1
```
This will return all movies that users with similar watch patterns have seen.

## Usage
### Learn
To teach your CF model, simply type in,
```
m.learn()
```
Now your model has been taught and is ready to make predictions.

### Show Similar Movies
To show movies which are similar to a said movie, simply pass in the movie_id to,
```
m.similar_movies(1)
```
This will return all the movies that the users of said movie have watched most frequently.

To display the similar movies based upon similar user behavious, simply pass in the movie_id to,
```
m.similar_movies_via_user_behaviour(1)
```
This will return all movies that users with similar watch patterns have seen.

### Save and Load
You can also save and load your progress. If you decide to save your model, there is no need to teach your model again the next time. Simply call upload the `load` function to reload your progress.
```
m.save()
m.load()
```

### Meta
To display the meta of the data, simply type in,
```
m.meta()
> 943 users
> 1682 movies
> Sparsity: 6.30%
```
This dataset has ratings given by 943 users over 1682 movies with 5 being the largest rating and 0 being no rating.
Sparsity is a measure of data quality. If almost every user has rated on every movie, sparsity will be lower.

### Movies
The dataset stores only movie IDs. To display a list of movies with it's ID and NAME, simply type in,
```
m.movies()
```

### Movie Name
The dataset stores only movie IDs. To display the name of the movie_id, simply pass in the movie_id to this function,
```
m.movie_name(1)
> 'Toy Story (1995)    01-Jan-1995\nName: id, dtype: object'
```
