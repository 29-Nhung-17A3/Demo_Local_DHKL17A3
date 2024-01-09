def process_string(s, s_sub, s_find, s_replace):
    s = s.strip()
    s = s.capitalize()
    print(f"Modified String (after removing leading/trailing whitespaces and capitalizing): {s}")
    count_s_sub = s.count(s_sub)
    print(f"The substring '{s_sub}' appears {count_s_sub} times in '{s}'")
    modified_string = s.replace(s_find, s_replace)
    print(f"String after replacing '{s_find}' with '{s_replace}': {modified_string}")
s = input("Enter the original string (s): ")
s_sub = input("Enter the substring to count (s_sub): ")
s_find = input("Enter the substring to find (s_find): ")
s_replace = input("Enter the replacement string (s_replace): ")
process_string(s, s_sub, s_find, s_replace)