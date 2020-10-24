lowerBound = int(input("Enter the lower bound of the F value : "))
upperBound = int(input("Enter the upper bound of the F value : "))
gap = int(input("Enter the gap you want between conversions"))

values = []
def convertFtoC(F):
    C = (F - 32) *(5/9)
    return C
    



for value in range(lowerBound,upperBound,gap):
    values.append(convertFtoC(value))

print(*values,sep='\t')
