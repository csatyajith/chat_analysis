import operator

chat_text = open("dir", "r", encoding="utf8", errors="ignore")  # Replace with the location of your chat file

person_names = ["Name1", "Name2"]  # Replace with the names of people in the exported chat file
encoded_names = list()
message_frequency_counter = dict()
personal_msg_freq = dict()
for person_name in person_names:
    encoded_names.append(" - " + person_name + ": ")
person_count = dict()
message_length_total = dict()
for person_name in person_names:
    person_count[person_name] = 0
    personal_msg_freq[person_name] = dict()
    message_length_total[person_name] = 0
for line in chat_text:
    for location in range(len(line)):
        for i in range(len(encoded_names)):
            person = encoded_names[i]
            person_name = person_names[i]
            end_loc = location + (len(person)) if location + (len(person)) < len(line) else len(line)
            validation_string = line[location: end_loc]
            message = []
            if validation_string == person:
                person_count[person_name] += 1
                message = line[end_loc: -1]
                message_length_total[person_name] += len(message)
                words = message.split(" ")
                for word in words:
                    if word in ["<Media", "omitted>"]:
                        continue
                    if word not in message_frequency_counter.keys():
                        message_frequency_counter[word] = 0
                    message_frequency_counter[word] += 1
                    if word not in personal_msg_freq[person_name].keys():
                        personal_msg_freq[person_name][word] = 0
                    personal_msg_freq[person_name][word] += 1

total_messages = sum(list(person_count.values()))
sorted_message_freq = sorted_x = sorted(message_frequency_counter.items(), key=operator.itemgetter(1), reverse=True)
print("Total messages in the conversation: ", total_messages)
print("Total messages sent per person in this conversation: ", person_count)
print("100 most common words used in this conversation: ", sorted_message_freq[0:100])
sorted_personal_freq = dict()
for freq_name in personal_msg_freq.keys():
    sorted_personal_freq[freq_name] = sorted(personal_msg_freq[freq_name].items(), key=operator.itemgetter(1),
                                             reverse=True)
    print(freq_name + "'s 50 most common words: ", sorted_personal_freq[freq_name][0:50])

for person_name in person_names:
    print(person_name, "'s average message length", message_length_total[person_name] / person_count[person_name])
chat_text.close()
