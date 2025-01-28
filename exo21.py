import statistics

def is_empty(lst):
    return len(lst) == 0

def length(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    return len(lst)

def sum_of_list(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    if is_empty(lst):
        raise ValueError("List cannot be empty.")
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("All elements in the list must be numbers.")
    return sum(lst)

def mean(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    if is_empty(lst):
        raise ValueError("List cannot be empty.")
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("All elements in the list must be numbers.")
    return sum_of_list(lst) / length(lst)

def range_of_list(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    if is_empty(lst):
        raise ValueError("List cannot be empty.")
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("All elements in the list must be numbers.")
    return max(lst) - min(lst)

def median(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    if is_empty(lst):
        raise ValueError("List cannot be empty.")
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("All elements in the list must be numbers.")
    return statistics.median(lst)

def mode(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    if is_empty(lst):
        raise ValueError("List cannot be empty.")
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("All elements in the list must be numbers.")
    try:
        return statistics.mode(lst)
    except statistics.StatisticsError:
        return "No unique mode found."

def variance(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    if is_empty(lst):
        raise ValueError("List cannot be empty.")
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("All elements in the list must be numbers.")
    return statistics.variance(lst)

def standard_deviation(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    if is_empty(lst):
        raise ValueError("List cannot be empty.")
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("All elements in the list must be numbers.")
    return statistics.stdev(lst)

def list_statistics(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list.")
    if is_empty(lst):
        raise ValueError("List cannot be empty.")
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("All elements in the list must be numbers.")
    
    stats = {
        "Length": length(lst),
        "Sum": sum_of_list(lst),
        "Mean": mean(lst),
        "Range": range_of_list(lst),
        "Median": median(lst),
        "Mode": mode(lst),
        "Variance": variance(lst),
        "Standard Deviation": standard_deviation(lst)
    }
    
    return stats

# Test cases
numbers = [1, 2, 3, 4, 5]
print("Statistics for [1, 2, 3, 4, 5]:")
print(list_statistics(numbers))

# Additional test cases
print("\nStatistics for [10, -10, 0, 5]:")
print(list_statistics([10, -10, 0, 5]))

print("\nStatistics for [1.5, 2.5, 3.5]:")
print(list_statistics([1.5, 2.5, 3.5]))

print("\nStatistics for [42]:")
print(list_statistics([42]))

print("\nStatistics for []:")
try:
    print(list_statistics([]))
except ValueError as e:
    print(e)

print("\nStatistics for [1, 1, 2, 2]:")
print(list_statistics([1, 1, 2, 2]))
