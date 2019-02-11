prompt = ''' 
1. Task1
2. Task2
3. Quit
'''
num = 0
while num != 3 :
    print(prompt)
    num = int(input("Choose Task Number : "))
    if( num != 3 ) :
        print("Do Some Task.")

print("Task is over")