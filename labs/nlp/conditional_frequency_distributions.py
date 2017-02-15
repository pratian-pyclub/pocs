# make sure to install Python's NumPy and Matplotlib packages
from nltk.book import *
from nltk.corpus import brown
from nltk.corpus import udhr

def dispersion_plot():
    # Corpus Used: Inaugural Address Corpus

    # dispersion plots are used to determine the location of a word in the text
    # it shows how many words from the beginning it appears

    # Each stripe represents an instance of a word,
    # and each row represents the entire text.

    text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
    # output: 'dispersion_plot.png'

def frequency_distribution():
    # Corpus Used: Moby Dick by Herman Melville 1851

    # to create a frequency distribution from words in text1
    fdist1 = FreqDist(text1)

    # to display the most common 50 words
    print fdist1.most_common(50)

    # to print frequency of the word 'whale'
    print fdist1['whale']

def counting_words_by_genre():
    # Corpus Used: Brown

    # A frequency distribution counts observable events, such as the
    # appearance of words in a text.
    # A conditional frequency distribution needs to pair
    # each event with a condition.
    # So instead of processing a sequence of words, we have to process a
    # sequence of pairs.

    cfd = nltk.ConditionalFreqDist(
            (genre, word)
            for genre in brown.categories()
            for word in brown.words(categories=genre))

    # Let's break this down, and look at just two genres, news and romance
    # For each genre, we loop over every word in the genre,
    # producing pairs consisting of the genre and the word
    genre_word = [(genre, word)
                    for genre in ['news', 'romance']
                    for word in brown.words(categories=genre)]

    # We can now use this list of pairs to create a ConditionalFreqDist,
    # and save it in a variable cfd. As usual, we can type the name of the
    # variable to inspect it, and verify it has two conditions
    cfd = nltk.ConditionalFreqDist(genre_word)
    print cfd.conditions()

    # Let's access the two conditions, and satisfy ourselves that each is
    # just a frequency distribution
    print(cfd['news'])
    print(cfd['romance'])

def plotting_and_tabulating_distributions():
    # The last of these corpora, udhr, contains the
    # Universal Declaration of Human Rights in over 300 languages.

    # The fileids for this corpus include information about the character
    # encoding used in the file, such as UTF8 or Latin1.

    # Let's use a conditional frequency distribution to examine the differences
    # in word lengths for a selection of languages included in the udhr corpus.
    languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut',
        'Hungarian_Magyar', 'Ibibio_Efik']
    cfd = nltk.ConditionalFreqDist(
           (lang, len(word))
           for lang in languages
           for word in udhr.words(lang + '-Latin1'))

    cfd.plot(cumulative=True)
    # output: plotting.png

    cfd.tabulate(conditions=['English', 'German_Deutsch'],
        samples=range(10), cumulative=True)
        # Output
        #                   0    1    2    3    4    5    6    7    8    9
        # English           0  185  525  883  997 1166 1283 1440 1558 1638
        # German_Deutsch    0  171  263  614  717  894 1013 1110 1213 1275
