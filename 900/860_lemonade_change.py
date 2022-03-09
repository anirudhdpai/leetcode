def lemonadeChange(bills):
    changeBills = {}
    for i in bills:
        amount = i-5
        if (amount) in changeBills:
            if changeBills[amount]>0:
                changeBills[amount]-=1
            else:
                pass
            try:
                changeBills[i] += 1
            except:
                changeBills[i] = 1
        else:
            return False
    return True

def makeChange(bank, toll):
    if toll in bank:
        if bank[toll]>0:
            bank[toll] -= 1
    else:
        for i in bank:
            if toll==0:
                break
            if bank[i]>0 and i<toll:
                bank[i] -= 1
                toll -= i
# complete this 

# write a function to check if there's change using dictionary 