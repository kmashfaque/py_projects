import time


a_z = []
start = time.time()

for letter in string.ascii_lowercase:
    a_z.append(letter)

print(a_z)


def creating_sentence(x):
    sentence = ""
    predicted_sentence = "jemi"
    count = 0

    while sentence != predicted_sentence:
        for i in range(1, len(predicted_sentence)+1):
            sentence += random.choice(a_z)
            print(sentence)
        if sentence == predicted_sentence:
            break
        sentence = ""
        count += 1
    return sentence, count


print(creating_sentence(a_z))
end = time.time()
print(end - start)
