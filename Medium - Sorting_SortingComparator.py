# Enter your code here. Read input from STDIN. Print output to STDOUT
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
          
    def comparator(a, b): 
        if a.score < b.score:
            return 1
        elif a.score > b.score:
            return -1
        else:
            len_a = len(a.name)
            len_b = len(b.name)
            
            if len_a < len_b:
                for i in range(len_a):
                    if a.name[i] < b.name[i]:
                        return -1
                    elif a.name[i] > b.name[i]:
                        return 1
                return -1
            elif len_b < len_a:
                for i in range(len_b):
                    if b.name[i] < a.name[i]:
                        return 1
                    elif b.name[i] > a.name[i]:
                        return -1
                return 1
            else:
                for i in range(len_a):
                    if a.name[i] < b.name[i]:
                        return -1
                    elif a.name[i] > b.name[i]:
                        return 1
                return 0







# Enter your code here. Read input from STDIN. Print output to STDOUT
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
          
    def comparator(a, b):
        if b.score > a.score:
            return 1
        elif b.score < a.score:
            return -1
        else:
            len_a = len(a.name)
            len_b = len(b.name)
            if len_a < len_b:
                for i in range(len_a):
                    if a.name[i] < b.name[i]:
                        return -1
                return 1
            elif len_b < len_a:
                for i in range(len_b):
                    if b.name[i] < a.name[i]:
                        return -1
                return 1
            else:
                for i in range(len_a):
                    if a.name[i] < b.name[i]:
                        return -1
                    elif a.name[i] > b.name[i]:
                        return 1
                return 0



ba 9                        
cb 9
aab 8
ab 8
ab 8
b 8
cbb 8
ccb 8
bb 7
b 6
bca 6
ccc 4
b 3
b 3
bb 3
bb 3
bb 2
bbb 2
a 1
bba 0




    def comparator(a, b): 
        if a.score < b.score:
            return 1
        elif a.score > b.score:
            return -1
        else:
            len_a = len(a.name)
            len_b = len(b.name)
            
            if len_a < len_b:
                if a.name[0] <= b.name[0]:
                    return -1
                else:
                    return 1
            elif len_a > len_b:
                if a.name[0] > b.name[0]:
                    return 1
                else:
                    return -1
            else:
                for i in range(len_a):
                    if a.name[i] < b.name[i]:
                        return -1
                    elif a.name[i] > b.name[i]:
                        return 1
                return 0
                    