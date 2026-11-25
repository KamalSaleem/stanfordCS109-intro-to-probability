from numpy.random import rand
from scipy import stats
import math


def bern(p):
    if rand() < p:
        return 1
    return 0

def gauss(mean, var):
    norm = stats.norm(mean, math.sqrt(var))
    return norm.rvs()


####################################################################
# a. What is the probability that a person with the flu has a fever greater than 103? You must
# give a numerical answer for full credit

# P(TEMP > 103 | F = 1) = 1 - P(TEMP < 103 | F = 1)
# since F = 1, T ~ N(101, 4)
# = 1 - phi((103-101) / 2)

Prob_T_lessthan103_given_F = 1 - stats.norm(101, 2).cdf(103)
print(Prob_T_lessthan103_given_F)



######################################################################
# b. For this simple model, we can calculate exact probabilities. What is the probability that
# someone has a flu given they have a temperature of 100?

# P(F|T = 100) = ((P(T=100 | F) * P(F)) / (P(T=100)))
# using law of total probability:
# P(F | T = 100) = ((P(T=100 | F) * P(F)) / ((P(T=100 | F) * P(F) + (P(T=100 | F') * P(F'))

# P(F) = 0.01, P(F') = 1 - 0.01 = 0.99
# P(F | T = 100) = ((f(T=100 | F) * P(F)) / ((f(T=100 | F) * P(F) + (f(T=100 | F') * P(F'))

prob_f = 0.01
prob_not_f = 1 - prob_f

prob_T_given_f = stats.norm(101, 2).pdf(100)
prob_T_given_not_f = stats.norm(98, 2).pdf(100)

prob_f_given_T = (prob_T_given_f * prob_f) / ((prob_T_given_f * prob_f) + (prob_T_given_not_f * prob_not_f))
print(prob_f_given_T)


# c. Write pseudocode to calculate the probability that someone has a flu given a fever of 100. 
# Use Cheeky Rejection Sampling with 𝑁 = 10000 samples. Use the functions:
# Method Description
# bern(p) Returns a random sample from a Bernoulli
# gauss(𝜇, 𝜎^2) Returns a random sample from a Normal


def get_samples():
    samples = []
    for i in range(10000):
        flu = bern(0.01)
        if flu == 1:
            temp = gauss(101, 4)
        else:
            temp = gauss(98, 4)

        samples.append([temp, flu])

    return samples

# P(F | T=100) = count(F, T = 100) / count(T = 100)
samples = get_samples()

count_joint = 0
count_denom = 0

for i in samples:
    if abs(i[0] - 100) <= 0.1:
        count_denom += 1
        if i[1] == 1:
            count_joint += 1

prob_f_given_T_with_RS = count_joint / count_denom
print(prob_f_given_T_with_RS)


##############################################
# d. What is the probability that out of 10,000 iterations of Cheeky Rejection Sampling for
# our model, there are < 20 samples that have a temperature within 0.1 degrees of 100
# degrees? Use an approximation to compute a numerical answer.

# lamda = n * p = 10000 * P(99.9 <= T <= 100.1)
# P(99.9 <= T <= 100.1) = P(99.9 <= T <= 100.1 | F)*P(F) + P(99.9 <= T <= 100.1 | F')*P(F')

Prob_T_within_tenth_given_F = (stats.norm(101, 2).cdf(100.1) - stats.norm(101, 2).cdf(99.9)) * prob_f
Prob_T_within_tenth_given_not_F = (stats.norm(98, 2).cdf(100.1) - stats.norm(98, 2).cdf(99.9)) * prob_not_f

Prob_T_within_tenth = Prob_T_within_tenth_given_F + Prob_T_within_tenth_given_not_F

l = 10000 * Prob_T_within_tenth

prob_less_than_20 = stats.poisson(l).cdf(19)
print(prob_less_than_20)