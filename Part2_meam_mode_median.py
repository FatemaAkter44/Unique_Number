directory = [9, 11, 22, 34, 17, 22, 34, 22, 40]
length = len(directory)
get_sum = sum(directory)
mean = get_sum / length
print("Mean value of the the directory is: ", "{0:.2f}".format(mean))
# print("Mean value of the the directory is: " + str(mean))

directory.sort()
if length % 2 == 0:
    median1 = directory[length // 2]
    median2 = directory[length // 2 - 1]
    median = (median1 + median2) / 2
else:
    median = directory[length // 2]
print("Median of the Directory is: " + str(median))

from collections import Counter

data = Counter(directory)
get_mude = dict(data)
mode = [k for k, v in get_mude.items() if v == max(list(data.values()))]
if len(mode) == length:
    get_mode = "No mode found"
else:
    get_mode: str = "Mode of the directory is: " + ', '.join(map(str, mode))

print(get_mode)
