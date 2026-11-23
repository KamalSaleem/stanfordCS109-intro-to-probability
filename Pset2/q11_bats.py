import csv

with open("bats.csv") as file:
    file = csv.reader(file)
    S = 0

    N_T = 0
    N_G1 = 0
    N_G2 = 0
    N_G3 = 0
    N_G4 = 0
    N_G5 = 0

    N_T_G1 = 0
    N_T_G2 = 0
    N_T_G3 = 0
    N_T_G4 = 0
    N_T_G5 = 0
    for i, j in enumerate(file):
        G1, G2, G3, G4, G5, T = j
        S += 1
        if G1 == "True":
            N_G1 += 1
        if G2 == "True" :
            N_G2 += 1
        if G3 == "True":
            N_G3 += 1
        if G4 == "True":
            N_G4 += 1
        if G5 == "True":
            N_G5 += 1
        if T == "True":
            N_T += 1
        if G1 == "True" and T == "True":
            N_T_G1 += 1
        if G2 == "True" and T == "True":
            N_T_G2 += 1
        if G3 == "True" and T == "True":
            N_T_G3 += 1
        if G4 == "True" and T == "True":
            N_T_G4 += 1
        if G5 == "True" and T == "True":
            N_T_G5 += 1

    P_G1 = N_G1 / S
    P_G2 = N_G2 / S
    P_G3 = N_G3 / S
    P_G4 = N_G4 / S
    P_G5 = N_G5 / S
    P_T = N_T / S
    print(f"P(T) = {P_T:.4f}\nP(G1) = {P_G1:.4f}\nP(G2) = {P_G2:.4f}\nP(G3) = {P_G3:.4f}\nP(G4) = {P_G4:.4f}\nP(G5) = {P_G5:.4f}")
    P_T_G1 = N_T_G1 / N_G1
    P_T_G2 = N_T_G2 / N_G2
    P_T_G3 = N_T_G3 / N_G3
    P_T_G4 = N_T_G4 / N_G4
    P_T_G5 = N_T_G5 / N_G5
    print(f"\nP(T|G1) = {P_T_G1:.4f}\nP(T|G2) = {P_T_G2:.4f}\nP(T|G3) = {P_T_G3:.4f}\nP(T|G4) = {P_T_G4:.4f}\nP(T|G5) = {P_T_G5:.4f}")
    print(f"T looks to be heavely dependent on G5 and since the probabilaty changed from 0.3 to 0.9 in the preseance of gene G5\ngenge G3 also chnges the prpbabilty to 0.58 which means its a strong factor the illnes (not as strong as G5)" \
    f"gene G4 is slightly change the probabilty to 0.37, genes G1,G2 only changed the probabilty be a small fraction {abs((P_T-P_T_G1)/P_T) * 100:.3f} % ")
    print("the presence of gene G5 looks to have the bats go sick from the illness\nas the probabilty of having the illnes increases alot when gene G5 is present\nSame with gene G3 but less in effect form G5")