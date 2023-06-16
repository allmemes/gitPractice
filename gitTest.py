# worker A's code
workerA = 1000000
for i in range(3):
    workerA += 1
print("This is worker A's code: ", workerA)


# worker B's code
workerB = 30
for i in range(3):
    workerB -= 1
print("This is worker B's code: ", workerB)

# edit from the second branch, again.

# Notes for git: 
# 1, git rm/mv: directly remove and rename files in stage/index, skipping add step.
# 2, git status -s: brief version of status, showing local and staged status for files.
# 3, unstage/restore files from index/stage (undo add command): git restore --staged fileName.
# 4, reset LOCAL changes to previous stage: git restore fileName.
# 5, retrieve commited and deleted files by undoing the commit: git restore --source=HEAD~1 fileName
# 6, 