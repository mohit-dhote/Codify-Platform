import random

if __name__ == "__main__":
    s1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']
    s2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    s3 = ['1','2','3','4','5','6','7','8','9','0']
    s4 = ['!','@','#','$','%','^','&','*','(',')','_','+','{','}','|','[',']','"',';','<','>','?','/',',']

    passLen = int(input("Enter Your password lenght: "))
    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    a =0
    print("Choose any one of the 5 passwords given below!")
    print("")
    while a<5:
        random.shuffle(s)
        print("\t","".join(s[0:passLen]))
        a=a+1
