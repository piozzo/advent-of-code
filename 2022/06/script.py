####################################
# --- Day 6: Tuning Trouble ---
####################################
import sys

def findMessageMarker(data, distinctChars):
	buffer = [x for x in data[0:(distinctChars-1)]]
	i = distinctChars-1
	stopIndex = len(data)
	while i < stopIndex:
		if len(set(buffer)) == len(buffer) and data[i] not in buffer:
			return i+1
		else:
			buffer.pop(0)
			buffer.append(data[i])
			i+=1
	return -1


codice = sys.stdin.read().strip()
p1 = findMessageMarker(codice, 4)
print("Part 1: " + (str(p1) if p1 != -1 else "NotFound"))
p2 = findMessageMarker(codice, 14)
print("Part 2: " + (str(p2) if p2 != -1 else "NotFound"))
