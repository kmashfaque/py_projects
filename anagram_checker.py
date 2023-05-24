def anagram_solution(s1, s2):
    a_list = list(s2)
    still_ok = True
    pos_1 = 0

    while pos_1 < len(s1) and still_ok:
        pos_2 = 0
        found = False

        while pos_2 < len(a_list) and not found:

            if s1[pos_1] == a_list[pos_2]:
                found = True
            else:
                pos_2 = pos_2+1

        if found:
            a_list[pos_2] = None
        else:
            still_ok = False

        pos_1 = pos_1+1

    return still_ok


print(anagram_solution("apple", "pleapeap"))


def anagram_solution(s1, s2):

    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord("a")
        c1[pos] = c1[pos]+1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord("a")
        c2[pos] = c2[pos]+1

    j = 0
    still_ok = True

    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j+1
        else:
            still_ok = False

    return still_ok


print(anagram_solution("apple", "pleapeap"))
