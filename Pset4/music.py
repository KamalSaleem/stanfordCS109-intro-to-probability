import csv

############ reading data ################
comp = {}
with open("music.csv", "r") as file:
    file = csv.DictReader(file)
    for i in file.fieldnames:
        comp[i] = []

    for i in file.reader:
        for j, field in enumerate(file.fieldnames):    
            comp[field].append(i[j])




################## a.
folk_count = [0,0,0,0,0]
total = 0
for i in comp["Folk"]:
    total += 1
    folk_count[int(i)-1] += 1


# P(Xfolk = 5) = count(folk = 5) / total
folk_prob_x_is_5 = folk_count[4] / total 
# print(f"{folk_prob_x_is_5:.5f}")



################# b.
# P(Xfolk = x) = count(folk = x) / total
folk_prob_x_is_x = [i / total for i in folk_count] 
# print(folk_prob_x_is_x)



################## c. What is 𝐸[𝑅Musical] = wieghted avrage = (1*count(1) + 2*count(2) + .... ) / total  

Musical_count = [0,0,0,0,0]
total = 0
for i in comp["Musical"]:
    total += 1
    Musical_count[int(i)-1] += 1

Exp_musical = 0
for i in range(len(Musical_count)):
    Exp_musical += (i+1) * Musical_count[i]

Exp_musical = Exp_musical / total
# print(f"{Exp_musical:.5f}")





################## d. What is 𝑃(𝑅Folk = 5|𝑅Musical = 5) = count(folk = 5, musical = 5) / SUMx [count(folk = x, musical = 5)]

count_folk5_given_musical5 = 0
count_folkx_given_musical5 = 0
for i in zip(comp["Folk"], comp["Musical"]):
    if int(i[1]) == 5:
        if int(i[0]) == 5:
            count_folk5_given_musical5 += 1
        count_folkx_given_musical5 += 1

prob_folk5_given_musical5 = count_folk5_given_musical5 / count_folkx_given_musical5
# print(f"{prob_folk5_given_musical5:.5f}")





################## e. What is 𝑃(𝑅Folk = 𝑥|𝑅Musical = 5) = P(1|5) , P(2|5) , ... , P(5|5) 
############# = [count(1|5), ... , count(5|5)] / count(x,5) (each count to be divides sepretly)

folkx_given_musical5_count = [0,0,0,0,0]
musical5_count = 0
for i in zip(comp["Folk"], comp["Musical"]):
    if int(i[1]) == 5:
        musical5_count += 1
        folkx_given_musical5_count[int(i[0])-1] += 1


prob_folkx_given_musical5 = [i/musical5_count for i in folkx_given_musical5_count]
# print(f"{prob_folkx_given_musical5}")





############ f. What is the covariance of 𝑅Opera and 𝑅Punk?

# ecpected value of ROpera:
opera_count = [0,0,0,0,0]
total = 0
for i in comp["Opera"]:
    total += 1
    opera_count[int(i)-1] += 1

Exp_Opera = 0
for i in range(len(opera_count)):
    Exp_Opera += (i+1) * opera_count[i]

Exp_Opera = Exp_Opera / total
# print(Exp_Opera)


# ecpected value of Punk:
punk_count = [0,0,0,0,0]
total = 0
for i in comp["Punk"]:
    total += 1
    punk_count[int(i)-1] += 1

Exp_punk = 0
for i in range(len(punk_count)):
    Exp_punk += (i+1) * punk_count[i]

Exp_punk = Exp_punk / total
# print(Exp_punk)


# ecpected value of opera*Punk:
opera_punk = []
for i in zip(comp["Opera"], comp["Punk"]):
    opera_punk.append(int(i[0]) * int(i[1]))

min_value = min(opera_punk)
max_value = max(opera_punk)


opera_punk_count = [0] * max_value
total = 0
for i in opera_punk:
    total += 1
    opera_punk_count[int(i)-1] += 1 


Exp_opera_punk = 0
for i in range(len(opera_punk_count)):
    Exp_opera_punk += (i+1) * opera_punk_count[i]

Exp_opera_punk = Exp_opera_punk / total



# covariance = E(opera*punk) - E(opera)*E(punk):
cov = Exp_opera_punk - (Exp_Opera*Exp_punk)
# print(cov)