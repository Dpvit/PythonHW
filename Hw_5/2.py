"""
    Витушкин Денис
    Ханойские башни 
"""

def tower_of_hanoi(numbers, start, auxiliary, end):  
    if(numbers == 1):  
        print('1',start,end)
        return
    tower_of_hanoi(numbers - 1, start, end, auxiliary)
    print(numbers,start,end)
    tower_of_hanoi(numbers - 1, auxiliary, start, end)

  
tower_of_hanoi(3, 'A', 'B', 'C')