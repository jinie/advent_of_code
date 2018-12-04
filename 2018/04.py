import re
from collections import namedtuple, defaultdict
from datetime import datetime,timedelta

Entry = namedtuple('Entry','timestamp,action')
entries = list()

with open('04_input.txt','rt') as f:
	lines = f.readlines()

pat = re.compile('\[(.*)\]\s*(.*)')
for l in lines:
	match = pat.match(l)
	ts = datetime.strptime(match.group(1),'%Y-%m-%d %H:%M')
	entries.append(Entry(ts, match.group(2)))

entries.sort(key=lambda entry: entry.timestamp)

def timedelta_minutes(td):
	return (td.seconds//60)%60

guard_on_duty = None
timer = timedelta(0)
sleepbegin = None

schedule = defaultdict(list)
guard_list = defaultdict(list)

def most_asleep_minute(guard, schedule):
	most_asleep = defaultdict(int)
	for m,gl in schedule.items():
		if guard not in gl:
			continue
		most_asleep[m]+=gl.count(guard)

	high = 0
	highm = 0
	for m,c in most_asleep.items():
		if c > high:
			high = c
			highm = m
	#print(high,highm)
	return (namedtuple('MostAsleep','count, minute')(high, highm))

def most_asleep_guard(schedule, minute):
	return {g:schedule[minute].count(g) for g in schedule[minute]}

for e in entries:
	if e.action.startswith('Guard #'):
		match = re.match('Guard\s*#(\d*)\s*(.*)',e.action)
		if match.group(2).startswith('begins'):
			guard_on_duty = match.group(1)

	elif e.action.startswith('falls asleep'):
		sleepbegin = e.timestamp
	elif e.action.startswith('wakes up'):
		duration = e.timestamp - sleepbegin
		for i in range((duration.seconds//60)%60):
			schedule[(sleepbegin+timedelta(minutes=i)).minute].append(guard_on_duty)
		guard_list[guard_on_duty].append(duration)

high = timedelta(0)
highg = 0

for g,s in guard_list.items():
	sleeptime = sum(s,timedelta())
	if sleeptime > high:
		high = sleeptime
		highg=g

res = most_asleep_minute(highg,schedule)
print("Part 1 : {} ({}) {} = {}".format(highg, res, res.minute, int(highg)*int(res.minute)))

highg = 0
highc = 0
highm = -1
for i in range(60):
	for g,c in most_asleep_guard(schedule,i).items():
		if c > highc:
			highc = c
			highg = g
			highm = i
print("Part 2 : {} ({}) {} = {}".format(highg, highc, highm, int(highg) * int(highm)))

