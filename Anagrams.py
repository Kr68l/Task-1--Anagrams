from string import punctuation, digits

def reversed_text(text):
    lst = []
    qw = set.union(set(punctuation), set(digits))

    for word in text.split(' '):
        sort = [i for i in word if i not in qw]

        for i in word:
            if i not in qw: 
                lst.append(sort.pop())
            else:
                lst.append(i)
              
        lst.append(' ')

    return ''.join(lst[:len(lst)-1])


if __name__ == '__main__':
    cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        (" ", " "), 
    ]

    for text, expected_output in cases:
        assert reversed_text(text) == expected_output

    print(reversed_text(input("Please enter the text: ")))