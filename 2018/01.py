with open('01_input.txt','rt') as f:
    lines = f.readlines()
lines = [int(l.strip()) for l in lines]
freq = 0

for l in lines:
    freq = freq + l
print(freq)

freq = 0
freqs = set()
found = False
while not found:
    for l in lines:
        freqs.add(freq)
        freq = freq + l
        if freq in freqs:
            print('repeated frequency',freq)
            found = True
            break
