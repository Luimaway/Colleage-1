def ssort0(s):
	if s!=[]:
		smallest = min(s)
		s.remove(smallest)
		return [smallest]+ssort0(s)
	else:
		return[]

print(ssort0([3,4,6,5]))