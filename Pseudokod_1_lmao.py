Födelsemånad = input("Födelsemånad?")
print(Födelsemånad)

KronorMånad = 1250
MånadÅr = 10
År = 3

HalvtBidrag = KronorMånad/2

Sum = KronorMånad*MånadÅr*År

HalvtBidrag = HalvtBidrag * År

if Födelsemånad == "juli":
    Sum = Sum - HalvtBidrag
    print("Du får", Sum, "kr i studiebidrag på tre år")

elif Födelsemånad == "augusti":
    Sum = Sum - HalvtBidrag
    print("Du får", Sum, "kr i studiebidrag på tre år")

elif Födelsemånad == "september":
    Sum = Sum - HalvtBidrag
    print("Du får", Sum, "kr i studiebidrag på tre år")
else:
    print("Du får", Sum, "kr i studiebidrag på tre år")