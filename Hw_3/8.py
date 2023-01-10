"""
    Витущкин Денис
    N человек, пронумерованных числами от 1 до N, стоят в кругу. Они начинают играть в считалку на выбывание, 
где каждый K-й по счёту человек выбывает из круга, после чего счёт продолжается со следующего за ним человека.
"""

n = 8
k = 3

players = [i for i in range(1,n+1)]

curr_counter = 0
while len(players) >1:
    out = (k + curr_counter - 1) % len(players)
    curr_counter = out
    print("Выбывает ", players[out])
    players.pop(out)
    print("Остались ",players)
    if out == len(players):
        cur_counter = 0
    
print(players[0])


