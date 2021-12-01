with open('2020/input05.txt') as f:
    data = [l.strip() for l in f.readlines()]

rpos = lambda pos,begin, end: (begin, begin+(end-begin)//2) if (pos=='F' or pos=='L') else (begin + 1 + (end-begin)//2,end)
rotseat = lambda row,col: row * 8 + col

def boarding_to_seat(boarding):
    begin,end=0,127
    for i in range(7): (begin,end) = rpos(boarding[i],begin,end)
    row = begin if boarding[6] =='F' else end
    
    begin,end=0,7
    for i in range(7,9): (begin,end) = rpos(boarding[i],begin,end)
    column = begin if boarding[9] == 'L' else end
    
    return (row, column)

def missing_seats(seat_list):
    missing = set(((r,c) for r in range(128) for c in range(8))) - set(seat_list)
    seatids = [rotseat(r[0],r[1]) for r in seat_list]
    return list((mis for mis in (rotseat(r[0],r[1]) for r in missing) if mis not in seatids and mis-1 in seatids and mis+1 in seatids))

seats=[boarding_to_seat(b) for b in data]
print(f'Part1: {max((rotseat(s[0],s[1]) for s in seats))}')
missing = missing_seats(seats)
print(f'Part2: {missing}')