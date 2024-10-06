def isGoodString(s):
        for i in range(len(s)-1):
            if not (s[i]=='a' and s[i+1]=='z' or s[i]=='z' and s[i+1]=='a'):
                if abs(ord(s[i])-ord(s[i+1]))==1:
                    continue
                else:
                    print("NO")
        print("YES")
  s=input("Enter a string!!! ")
  isGoodString(s)
