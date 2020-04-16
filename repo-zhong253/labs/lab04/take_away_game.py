import random
remain = 21
def choose_test(choose):
    while choose not in [1,2,3]:
        print("oops, you must choose 1,2 or 3...")
        choose = int(input("%d objects remain, choose 1,2 or 3: " % remain))
    return choose

# Main
q = input('Would you like to go first (y/n)?')
if q == 'y':
    while True:
        choose = int(input("%d objects remain, choose 1,2 or 3: " % remain))
        choose_test(choose)
        remain = remain - choose
        if remain in [1,2,3]:
            print("I win!")
            break
        op_choose = random.randint(1,3)
        print(remain, "objects remain, I'll take ", op_choose)
        remain = remain - op_choose
        if remain in [1,2,3]:
            print("You win!")
            break
else:
    while True:
        op_choose = random.randint(1,3)
        print(remain, "objects remain, I'll take ", op_choose)
        remain = remain - op_choose
        if remain in [1,2,3]:
            print("You win!")
            break
        choose = int(input("%d objects remain, choose 1,2 or 3: " % remain))
        choose_test(choose)
        remain = remain - choose
        if remain in [1,2,3]:
            print("I win!")
            break
