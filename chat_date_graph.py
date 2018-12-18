import datetime

import matplotlib.pyplot as plt
import numpy as np

chat_text = open("dir", "r", encoding="utf8", errors="ignore")  # Replace with the location of your chat file

person_names = ["Name1", "Name2"]  # Replace with the names of people in the exported chat file

encoded_names = list()
for person_name in person_names:
    encoded_names.append(" - " + person_name + ": ")

day_based_frequency = dict()

for line in chat_text:
    try:
        processed_day = datetime.datetime(day=int(line[0:2]), month=int(line[3:5]), year=int(line[6:10]),
                                          hour=int(line[12:14]), minute=int(line[15:17]))
    except BaseException:
        continue
    day = str(processed_day.month) + " / " + str(processed_day.year)
    if day not in day_based_frequency.keys():
        day_based_frequency[day] = dict()
        for person_name in person_names:
            day_based_frequency[day][person_name] = 0
    for person_id in range(len(person_names)):
        person_name = person_names[person_id]
        if encoded_names[person_id] in line:
            day_based_frequency[day][person_name] += 1

N = len(list(day_based_frequency.keys()))
person_1 = list()
person_2 = list()
day_set = list()
for day in day_based_frequency:
    day_set.append(day)
    person_1.append(day_based_frequency[day][person_names[0]])
    person_2.append(day_based_frequency[day][person_names[1]])
ind = np.arange(N)  # the x locations for the groups
width = 0.2  # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind - 0.2, person_1, width)
p2 = plt.bar(ind, person_2, width)

plt.ylabel('Messages')
plt.title('Dates')
plt.xticks(ind, list(day_based_frequency.keys()), rotation=90)
plt.yticks(np.arange(0, 401, 20))
plt.legend((p1[0], p2[0]), (person_names[0], person_names[1]))
plt.figure(figsize=(20, 20))
plt.show()

print(day_based_frequency)
