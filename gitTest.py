# worker A's code
workerA = 0
for i in range(3):
    workerA += 1
print("This is worker A's code: ", workerA)


# worker B's code
workerB = 0
for i in range(3):
    workerB -= 1
print("This is worker B's code: ", workerB)