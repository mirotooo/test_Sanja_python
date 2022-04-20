L = int(input("Veuillez saisir le nombre de lignes : "))
C =  int(input("Veuillez saisir le nombre de collonnes : "))
for i in range(1,L+1):
    for j in range(1,C+1):
        if i == 1 or i == L or j == 1 or j == C:
            print("* ",end="")
        else:
            print(" ", end=" ")

    print()
    
# source https://www.youtube.com/watch?v=8ZVdIRTeNwQ&list=RDCMUCs2iRkOaPo7QLRKCtiqczEA&start_radio=1&rv=8ZVdIRTeNwQ&t=0
