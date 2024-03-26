import random
import time
operators_list=["+","-","*"]
no_of_problems=int(input("enter the number of problems you want to solve : "))

input("press enter to start the game")
print("*******************************************************")
start_game=time.time()
for i in range(no_of_problems):
    operand1 = random.randint(1, 10)
    operand2 = random.randint(1, 10)
    operator = random.choice(operators_list)
    expr=str(operand1)+" "+operator+" "+str(operand2)

    ans=eval(expr)
    while True:
        user_answer = int(input("Problem #" + str(i + 1)+" :" + expr + " = "))
        if user_answer==ans:
            break
end_game=time.time()
total_time=round(end_game-start_game,3)
print("the total time taken to solve",no_of_problems,"problem(s) is:",total_time)








