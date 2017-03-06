# -*- coding: utf-8 -*-
import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

# PROBABILITY MASS FUNCTION: A probability mass function (pmf)
# is a function that gives the probability that a discrete random variable
# is exactly equal to some value.

# PROBABILITY DISTRIBUTION FUNCTION: The probability of occurrence of different
# possible outcomes in an experiment.
# For instance, if the random variable X is used to denote the outcome of a
# coin toss ('the experiment'), then the probability distribution of X
# would take the value 0.5 for X=Heads and 0.5 for X=Tails.

# ==============================================================================

# The beta distribution is a
# family of continuous probability distributions
# defined on the interval [0, 1]

# It is parametrized by two positive shape parameters
# denoted by a and β
# that appear as exponents of the random variable
# and control the shape of the distribution.

# https://en.wikipedia.org/wiki/File:Beta_distribution_pdf.svg

# The beta distribution has been applied to model the behavior of random variables
# limited to intervals of finite length in a wide variety of disciplines.

# The beta distribution can be used in Bayesian analysis to describe
# initial knowledge concerning probability of success.

# In Bayesian inference, the beta distribution is the prior probability distribution
# for the Bernoulli, binomial, negative binomial and geometric distributions.
dist = stats.beta

# ==============================================================================
# n_trials = [0, 1]
n_trials = [0, 1, 2, 3, 4, 5, 8, 15, 50, 500]

# The Bernoulli distribution is the probability distribution of a random variable
# which takes the value 1 with probability p and
# the value 0 with probability q = 1 − p
# It can be used to represent a coin toss where 1 and 0 would represent
# "head" and "tail" (or vice versa), respectively.

# 0.5 => probability of heads occuring (the prior probability)
data = stats.bernoulli.rvs(0.5, size=500)

# ==============================================================================

x = np.linspace(0, 1, 100)

# For the already prepared, I'm using Binomial's conj. prior.
for k, N in enumerate(n_trials):
    sx = plt.subplot(len(n_trials)/2, 2, k+1)
    plt.xlabel("$p$, probability of heads") if k in [0, len(n_trials)-1] else None
    plt.setp(sx.get_yticklabels(), visible=False)

    # The number of heads that occurred in N trials
    heads = data[:N].sum()
    y = dist.pdf(x, 1 + heads, 1 + N - heads)

    plt.plot(x, y, label="observe %d tosses,\n %d heads" % (N, heads))
    plt.fill_between(x, 0, y, color="#348ABD", alpha=0.4)
    plt.vlines(0.5, 0, 4, color="k", linestyles="--", lw=1)

    leg = plt.legend()
    leg.get_frame().set_alpha(0.4)
    plt.autoscale(tight=True)

plt.suptitle("Bayesian updating of posterior probabilities",
             y=1.02,
             fontsize=10)

plt.tight_layout()
plt.show()

# The posterior probabilities are represented by the curves, and our uncertainty
# is proportional to the width of the curve. As the plot above shows, as we start
# to observe data our posterior probabilities start to shift and move around.
# Eventually, as we observe more and more data (coin-flips), our probabilities
# will tighten closer and closer around the true value of p=0.5 (marked by a dashed line).
