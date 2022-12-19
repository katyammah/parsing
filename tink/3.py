count, time = map(int, input().split())
i = map(int, input().split())
number = int(input())

people = list(i)
lastperson = people[-1]
firstperson = people[0]
importantperson = people[number - 1]
dif1 = importantperson - firstperson
dif2 = lastperson - importantperson
dif3 = lastperson - firstperson

if time < dif1:
    stairs = dif3
    if dif1 <= dif2:
        stairs = dif1 + dif3
    else:
        stairs = dif2 + dif3
else:
    stairs = dif3

print(stairs)
