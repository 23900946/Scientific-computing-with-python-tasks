str = "X-DSPAM-Confidence: 0.8475 "
find1 = str.find(":")
print(find1)
find2 = str[find1+2:]
print(find2)
a = float(find2)
print(a)