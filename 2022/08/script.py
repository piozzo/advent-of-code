###################################
# --- Day 8: Treetop Tree House ---
###################################

import sys

def treeIsVisibile(i, j):
	tree = forest[i][j];
	if i==0 or i==len(forest):
		return True;

	if j==0 or j==len(forest[0]):
		return True;

	# TOP
	k=0
	while k<i:
		if forest[k][j]>=tree:
			break
		k+=1
	if k==i:
		return True

	# BOTTOM
	k=len(forest)-1
	while k>i:
		if forest[k][j]>=tree:
			break
		k-=1
	if k==i:
		return True

	# LEFT
	k=0
	while k<j:
		if forest[i][k]>=tree:
			break
		k+=1
	if k==j:
		return True

	# RIGHT
	k=len(forest[0])-1
	while k>j:
		if forest[i][k]>=tree:
			break
		k-=1
	if k==j:
		return True

	return False

def scenicScore(i, j):
	tree = forest[i][j]
	distances = []
	# TOP
	viewCount=0
	k=i-1
	while k>=0:
		if forest[k][j] <= tree:
			viewCount+=1
		if forest[k][j] >= tree:
			break
		k-=1
	distances.append(viewCount)
	# BOTTOM
	viewCount=0
	k=i+1
	while k<len(forest):
		if forest[k][j] <= tree:
			viewCount+=1
		if forest[k][j] >= tree:
			break
		k+=1
	distances.append(viewCount)
	# LEFT
	viewCount=0
	k=j-1
	while k>=0:
		if forest[i][k] <= tree:
			viewCount+=1
		if forest[i][k] >= tree:
			break
		k-=1
	distances.append(viewCount)
	# RIGHT
	viewCount=0
	k=j+1
	while k<len(forest[0]):
		if forest[i][k] <= tree:
			viewCount+=1
		if forest[i][k] >= tree:
			break
		k+=1
	distances.append(viewCount)

	score = 1
	for d in distances:
		score*=d

	return score

input = sys.stdin.read().strip().split("\n")
forest = [[c for c in r] for r in input]

visibleTrees = 0
for i in range(len(forest)):
	for j in range(len(forest[i])):
		if treeIsVisibile(i,j):
			visibleTrees+=1
print("Part 1: " + str(visibleTrees))

sScore = 0
for i in range(len(forest)):
	for j in range(len(forest[i])):
		sc = scenicScore(i,j)
		if sc > sScore:
			sScore = sc
print("Part 2: " + str(sScore))
