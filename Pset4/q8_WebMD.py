from numpy.random import rand



# running this funtion will cause a typeError beause other functions return None
def bern(p):
    if rand() < p:
        return 1
    return 0

# this function is provided to us as the question claims
def probFlu(s, e):
    pass

# this function is provided to us as the question claims
def probCold(s, e):
    pass

# this function is provided to us as the question claims
def probSymptom(i, f, c):
    pass

def get_samples():
    samples = []

    for j in range(100000):
        stress = bern(0.5)
        Exposure = bern(0.1)
        
        flu = bern(probFlu(stress, Exposure))
        cold = bern(probCold(stress, Exposure))

        i = 2
        xi = bern(probSymptom(i, flu, cold))
        # i can be any value from 1 to 10
        # but for the required question we will set it to 2

        samples.append([stress, Exposure, flu, cold, xi])

    return samples


def prob_flu():
    samples = get_samples()
    # count where Flu = 1 , Exposure = 1 , X2 = 1
    count_joint = 0
    # count where Exposure = 1 , X2 = 1
    count_denom = 0

    for i in samples:
        if i[1] == 1 and i[-1] == 1:
            count_denom += 1
            if i[2] == 1:
                count_joint += 1

    return count_joint / count_denom



prob_of_flu_given_Exp_and_X2 = prob_flu()
print(prob_of_flu_given_Exp_and_X2)