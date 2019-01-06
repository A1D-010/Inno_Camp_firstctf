import requests


d = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def calcstr(a):
    ans = list()
    for i in range(2, len(a)-1, +1):
        ans.append(str(d[a[i]]))
    ans.append(str(a[len(a)-1]))
    sans = ""
    for i in range(len(ans)):
        sans += str(ans[i])
    return sans


link: str = 'http://81.23.10.193/task/'
response = str(requests.get("http://81.23.10.193/task/6522869.html").text).split()
next = link + calcstr(response)
while True:
    response = str(requests.get(next).text).split()
    print(response)
    next = link + calcstr(response)
