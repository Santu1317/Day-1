n=float(input())
f=input("Enter the currency:")
if f=="Euro":
    print(n*0.0147)
elif f=="British Pound":
    print(n*0.0100)
elif f=="Australian Dollar":
    print(n*0.02140)
elif f=="Canadian Dollar":
    print(n*0.02027)
else:
    print(-1)
