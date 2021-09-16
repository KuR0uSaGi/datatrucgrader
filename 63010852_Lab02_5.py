class TorKham:
    def __init__(self):
        self.words = []
    
    def restart(self):
        self.words.clear()
        return "game restarted"

    def play(self,word):
        if word[0] == "P" :
            if len(self.words)>1 and self.words[len(self.words)-2][len(self.words[len(self.words)-2])-2:len(self.words[len(self.words)-2])].lower() != self.words[len(self.words)-1][len(self.words[len(self.words)-1])-2:len(self.words[len(self.words)-1])].lower() :
                return "game over"
            else:
                self.words.append(word[1])
                return self.words   
            

            
    def peek(self):
        return self.words[-1]
    

torkham = TorKham()

print("*** TorKham HanSaa ***")

oldW = '0'

S = input("Enter Input : ").split(',')
for i in range(len(S)):
    S[i]=S[i].split(" ")
for j in range(len(S)):
    
    if S[j][0] == "R":
        oldW = 0
        print(torkham.restart())
    elif S[j][0] == "P":
        print('\'{}\''.format(S[j][1]),end=" -> ")
        print(str(torkham.play(S[j])))
       
    elif S[j][0] == "X":
        break
    else:
        print("\'{}\'".format(" ".join(S[j]))+" is Invalid Input !!!")
        break
