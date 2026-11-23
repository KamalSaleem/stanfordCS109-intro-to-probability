import csv

# load data from files
phone_prior = []
phone_conditional  = []
with open("phone_prior.csv") as file1:
    file1 = csv.reader(file1)
    for i in file1:
        for j in i:
            phone_prior.append(float(j))
with open("phone_conditional.csv") as file1:
    file1 = csv.reader(file1)
    for i in file1:
        for j in i:
            phone_conditional.append(float(j))

P_O = 0
for i in range(len(phone_conditional)):
    P_O += (phone_conditional[i] * phone_prior[i])
print("Using the law to total probability")
print(f"P(o) = {P_O}\t(Sum of P(o|L1)P(L1) + P(o|L2)P(L2) + .... + P(o|Ln)P(Ln))")


phone_postirior = []
for i in range(len(phone_prior)):
    P_Li = (phone_conditional[i] * phone_prior[i]) / P_O
    phone_postirior.append(float(f"{P_Li:.4f}"))

print(f"Our updated probabilities:")
i = 0
while i < len(phone_postirior):
    print(phone_postirior[i], phone_postirior[i+1], phone_postirior[i+2], phone_postirior[i+3])
    i += 4
print(f"Sum of probabilities = {sum(phone_postirior):.4f} (rounding may cause the sum to be slightly off)")