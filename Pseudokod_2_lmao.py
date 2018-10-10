Betyg = [4, 1, 3, 3]
Billig = [12500, 3423, 9500, 8560]
Tid = [12, 14, 12, 8]
Billigast = min(Billig) 
Snabbast = min(Tid)
Högstbetyg = max(Betyg)
if Billigast == 12500: 
    print("SAS är Billigast")  
elif Billigast == 3423: 
    print("ryanair är Billigast")
elif Billigast == 9500:
    print("grönt flyg är Billigast")
else: print("flygfort är Billigast")

if Snabbast == 12:
    print("SAS, grönt flyg är Snabbast")
elif Snabbast == 14:
    print ("ryanair är snabbas")
else:
    print ("flyg fort är Snabbast")

if Högstbetyg == 4:
    print("SAS har högst betyg")
elif Högstbetyg == 1:
    print ("ryanair har högst betyg")
else:
    print ("Grönt flyg, flyg fort har högst betyg")
