if __name__ == '__main__':
    N = int(input())
    number = []
    for i in range(0,N):
        s = input().split()
        if(s[0]=="insert"):
            number.insert(int(s[1]),int(s[2]))
        elif(s[0]=="print") :
            print(number)
        elif(s[0]=="remove"):
            number.remove(int(s[1]))
        elif(s[0]=="append"):
            number.append(int(s[1]))
        elif(s[0]=="sort"):
            number.sort()
        elif(s[0]=="pop"):
            number.pop()
        elif(s[0]=="reverse"):
            number.reverse()