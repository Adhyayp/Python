# This is a sample Python script.


def findMissing(numbers):
    nextNumber=numbers[1]
    i:int=0
    while i < len(numbers)-1:
         n=numbers[i]
         if n+1 != numbers[i+1]:
              print(f'Missing number is {n+1}')
         i+=1

findMissing([10,12,14,15,16,18,19,21,22,24])
