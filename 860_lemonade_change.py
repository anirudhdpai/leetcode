def lemonadeChange(bills):
    changeBills = {}
    for i in bills:
        amount = i-5
        if (amount) in changeBills:
            if changeBills[amount]>0:
                changeBills[amount]-=1
            else:

            try:
                changeBills[i] += 1
            except:
                changeBills[i] = 1
        else:
            return False
    return True

def makeChange(coll, toll):
    
# write a function to check if there's change using dictionary 