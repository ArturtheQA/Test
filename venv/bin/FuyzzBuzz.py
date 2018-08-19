

i=1
a=1000000
FuzzNumber=5
BuzzNumber=3
FuzbuzzNumber=FuzzNumber*BuzzNumber
while i<a:
    if i%FuzbuzzNumber==0:
        print("FuzzBuzz")
    elif i%BuzzNumber==0:
        print("Buzz")
    elif i%FuzzNumber==0:
        print("Fuzz")
    else:
        print(i)
    i=i+1