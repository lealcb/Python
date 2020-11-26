# import itertools
# numbers = [216.17, 13.59, 26.59, 52.80, 14.27, 5.67, 72.28, 7.37, 20.00, 3.00, 45.81, 2.00, 62.93, 49.63, 18.14, 41.23, 7.97, 85.90, 36.46, 115.41, 72.85, 27.14, 16.82, 9.72, 20.00, 16.49, 53.90, 17.26, 65.86, 49.43, 8.24, 10.31, 13.32, 16.84, 49.06, 36.72, 94.13, 25.55, 40.23, 15.98, 18.70, 20.83, 13.34, 12.75, 37.82, 386.50, 67.64, 12.61, 38.95, 19.13, 19.99, 9.25, 37.75, 19.99, 29.90, 2.00, 27.96, 8.00, 16.34, 34.73, 71.76, 26.43, 13.45, 17.30, 14.20, 31.72, 22.58]
# result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) == 146.64]
# print (result)

def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print("sum(%s)=%s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n])


if __name__ == "__main__":
    subset_sum([216.17, 13.59, 26.59, 52.80, 14.27, 5.67, 72.28, 7.37, 20.00, 3.00, 45.81, 2.00, 62.93, 49.63, 18.14, 41.23, 7.97, 85.90, 36.46, 115.41, 72.85, 27.14, 16.82, 9.72, 20.00, 16.49, 53.90, 17.26, 65.86, 49.43, 8.24, 10.31, 13.32, 16.84, 49.06, 36.72, 94.13, 25.55, 40.23, 15.98, 18.70, 20.83, 13.34, 12.75, 37.82, 386.50, 67.64, 12.61, 38.95, 19.13, 19.99, 9.25, 37.75, 19.99, 29.90, 2.00, 27.96, 8.00, 16.34, 34.73, 71.76, 26.43, 13.45, 17.30, 14.20, 31.72, 22.58], 146.64)

    # Outputs:
    # sum([3, 8, 4])=15
    # sum([3, 5, 7])=15
    # sum([8, 7])=15
    # sum([5, 10])=15