# worker A's code
workerA = 30
for i in range(3):
    workerA += 1
print("This is worker A's code: ", workerA)


# worker B's code
workerB = 30
for i in range(3):
    workerB -= 1
print("This is worker B's code: ", workerB)

# edit from the second branch for the third time.

# Notes for git: 
# 1, git rm/mv: directly remove and rename files in stage/index, skipping add step.
# 2, git status -s: brief version of status, showing local and staged status for files.
# 3, unstage/restore a staged file from index/stage (undo add command): git restore --staged fileName.
# 4, discard LOCAL, unstaged changes and return to previous stage: git restore fileName.
# 5, retrieve commited and deleted files by undoing the commit: git restore --source=HEAD~1 fileName

# 6, before everyday pull, stash your code to get to the "clean mode", pull the updates, and apply your code with "git stash pop"

# 7, About branch: 
#       - there is only one active, checked out, HEAD branch.
#       - can only create branch at local repo. Only by publishing it can make remote branches.
#       - create new branch with git branch <branchName>: create banch at current revision/status.
#       - create new branch with git branch <branchName> revisionID: create banch at certain revision/status.
#       - git checkout can be used to change between branches with many other functions. 
#           git switch can also be used to change brances.
#       - git branch -m newBranchName can be used to change the name for current branch. Or you do git branch -m oldName newName.
#           After merging, there will be a editor that asks for some comments on the merge. press i to write/insert. press esc and type ":wq" to exit.

# note from the thrid branch.
