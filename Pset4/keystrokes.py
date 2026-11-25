from scipy import stats
import math

# read data of a file:
def read_file(filename):
    timeX = []
    letterX = []
    with open(filename) as f:
        for i in f.readlines():
            time, letter = i.split(",")
            timeX.append(float(time))
            letterX.append(letter.strip())

    dataX1 = list(zip(timeX, letterX))
    dataX2 = []
    dataX2.append(dataX1[0])
    # subtract time of the strok from the time of the previous strok
    # since the time given by the data is cumulative time
    for i in range(1, len(dataX1)):
        dataX2.append((dataX1[i][0] - dataX1[i-1][0],dataX1[i][1]))
    return dataX2


dataA = read_file("personKeyTimingA.txt")
dataB = read_file("personKeyTimingB.txt")
dataE = read_file("email.txt")


#########################################
#  a. Estimate 𝐸[𝑋] and 𝐸[𝑌]

# ######## #  E(X) is E(Person A)
Exp_A = [i[0] for i in dataA]
Exp_A = sum(Exp_A) / len(Exp_A)
# print(Exp_A)

# ###### # E(Y) is E(Person B)
Exp_B = [i[0] for i in dataB]
Exp_B = sum(Exp_B) / len(Exp_B)
# print(Exp_B)


# #######  # E(Email)
Exp_E = [i[0] for i in dataE]
Exp_E = sum(Exp_E) / len(Exp_E)
# print(Exp_E)



#########################################
#  b. Estimate 𝐸[𝑋2] and 𝐸[𝑌2]


# # E(X^2) is E(Person A)
Exp_A2 = [i[0] ** 2 for i in dataA]
Exp_A2 = sum(Exp_A2) / len(Exp_A2)
# print(Exp_A2)


# # E(Y^2) is E(Person B)
Exp_B2 = [i[0] ** 2 for i in dataB]
Exp_B2 = sum(Exp_B2) / len(Exp_B2)
# print(Exp_B2)


# # # E(Email^2)
Exp_E2 = [i[0] ** 2 for i in dataE]
Exp_E2 = sum(Exp_E2) / len(Exp_E2)
# print(Exp_E2)



#########################################################
#  c. Use your answers to part (a) and (b) and approximate X and Y as Normals with mean
#  and variance that match their biometric data. Report both distributions.
var_A = Exp_A2 - (Exp_A ** 2)
var_B = Exp_B2 - (Exp_B ** 2)
var_E = Exp_E2 - (Exp_E ** 2)

norm_A = stats.norm(Exp_A, math.sqrt(var_A))
norm_B = stats.norm(Exp_B, math.sqrt(var_B))
norm_E = stats.norm(Exp_E, math.sqrt(var_E))

# print(f"X ~ Normal({Exp_A}, {var_A})")
# print(f"Y ~ Normal({Exp_B}, {var_B})")
# print(f"E ~ Normal({Exp_E}, {var_E})")


#########################################################
# d. Calculate the ratio of the probability that user A wrote the email over the probability
# that user B wrote the email. You don’t need to submit code, but you should include
# the formula that you attempted to calculate and a few sentence description of how your
# code works.

# P(A|E) / P(B|E) = ((P(E|A) * P(A) / P(E))) / ((P(E|B) * P(B) / P(E)))
#  == (P(E|A) * P(A) / (P(E|B) * P(B)) = (f(E|A) * P(A)) / (f(E|B) * P(B))
#  Priors P(A) = P(B) = 0.5

# P(A|E) / P(B|E) = f(E|A) / f(E|B)

f_E_given_A = 1
f_E_given_B = 1
for i in dataE:
    f_E_given_A *= norm_A.pdf(i[0])
    f_E_given_B *= norm_B.pdf(i[0])


ratio_A_over_B = f_E_given_A / f_E_given_B
# print(ratio_A_over_B)


# the result is 0.0085.... which is less than one 
# which tells us the its more likely that persen B is the one who made the keystroks
# P(B|E) > P(A|E)