import urllib.request
#comment
value = input('Enter your base : ')
content = urllib.request.urlopen("https://api.exchangeratesapi.io/latest?base=" + value)
for line in content:
    kaxamb = line.decode('utf-8')
    varung = kaxamb.replace(',', '\n')
    print(varung)



