# Baseline solution used for just generating the answer file
import sys


def solve(dictionary, needle):
    sorted_needle = sorted(needle)
    ans = []
    for word in dictionary:
        if sorted(word) == sorted_needle:
            ans.append(word)
    return ans


with open("dictionaries/1.txt", "r", encoding="iso-8859-4") as f:
    dictionary = list(map(lambda x: x.strip(), f.readlines()))

with open("testwords/testwords.txt", 'r', encoding="iso-8859-4") as f:
    testwords = list(map(lambda x: x.strip(), f.readlines()))


if __name__ == '__main__':
    out = []
    for testword in testwords:
        ans = solve(dictionary, testword)
        # print(ans[0])
        out.append(testword + ":" + ",".join(ans) + "\n")
    print(out)
    with open("testwords/answers.txt", "w", encoding="iso-8859-4") as f:
        f.writelines(out)

        # print(testword)
