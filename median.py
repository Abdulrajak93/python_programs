data = list(map(int, (input().split())))
datadup = sorted(data)
mid = len(datadup)//2
if len(datadup)%2 == 0:
    print(f"The median in {(datadup[mid]+datadup[mid-1])//2}")
else:
    print(f"The median is {datadup[mid]}")