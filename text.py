s="MCMXCVI"

a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,"0":0}
lens = len(s)
print('lens=',lens)
sum = 0
s=s+"0"
print(s)
if lens == 1:
    print(sum + a[s[0]])
for i in range(lens):
    if a[s[i]] < a[s[i+1]] :
        sum = sum - a[s[i]]
        print("sum=", sum)
    else :
        sum=sum+a[s[i]]
        print("esls sum=",sum)
