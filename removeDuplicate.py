def remove_duplicates(strings):
    seen = set()
    result = []
    for string in strings:
        if string not in seen:
            seen.add(string)
            result.append(string)
    return result

# Example usage:
strings = ["Apple", "Banana", "Apple", "Cherry", "Banana"]
unique_strings = remove_duplicates(strings)
print(unique_strings)

