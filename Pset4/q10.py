from numpy.random import rand
from scipy import stats
import math


################################################
# a. Say you try the first drug on 7 patients. It cures 5 patients and has no effect on 2. 
# What is your belief about the drug’s probability of success, 𝜃1? Your answer should be a Beta.

# prior 𝜃1 ~ Beta(1,1)
# postrior 𝜃1 ~ Beta (1 + 5, 1 + 2) = Beta(6,3)



##################################################
# Methods

# V = sampleBeta(a, b)
# Returns a real number value in the range [0, 1] with probability
# defined by a PDF of a Beta with parameters 𝑎 and 𝑏.

# R = giveDrug(i)
# Gives drug 𝑖 to the next patient. Returns a True if the drug was
# successful in curing the patient or False if it was not. Throws an
# error if 𝑖 ∉ {1, 2}.

# I = argmax(list)
# Returns the index of the largest value in the list.

# b. Write pseudocode to administer either of the two drugs to 100 patients using Thompson’s
# Sampling Algorithm. Use functions from the table above. Your code should execute
# giveDrug 100 times

# this function is provided to us as the question claims
# but is simply enough to be written by ourselfs
def sampleBeta(a, b):
    return stats.beta(a, b).rvs()

# this function is provided to us as the question claims
def giveDrug(i):
    pass

# this function is provided to us as the question claims
# but is simply enough to be written by ourselfs
def argmax(list: list):
    return list.index(max(list))


def Thompson_Sampling():
    a1 = 1
    b1 = 1
    a2 = 1
    b2 = 1
    for _ in range(100):
        i = 1 if sampleBeta(a1, b1) > sampleBeta(a2, b2) else 2
        test = giveDrug(i)

        if i == 1:
            if test:
                a1 += 1
            else:
                b1 += 1
        else:
            if test:
                a2 += 1
            else:
                b2 += 1

    return stats.beta(a1, b1), stats.beta(a2, b2)

sampled_betas = Thompson_Sampling()



#######################################################
# c. After running Thomspons’ Algorithm 20 times, you end up with the following Beta
# distributions:
# 𝜃1 ∼ Beta(3, 4),
# 𝜃2 ∼ Beta(13, 4)
# What is the probability that 𝜃2 > 𝜃1? You may provide an approximate answer. Explain
# briefly how you obtained your answer.
𝜃1 = stats.beta(3, 4)
𝜃2 = stats.beta(13, 4)

b1 = 0
b2 = 0
for i in range(10000):
    if 𝜃2.rvs() > 𝜃1.rvs():
        b1 += 1
    else:
        b2 += 1

prob_𝜃2_over_𝜃1 = b1 / (i + 1)
print(prob_θ2_over_θ1)

# exlaination:
# sample a ton and see how much times 𝜃2 > 𝜃1 
# and with more test the probability will converge
# to the true probability