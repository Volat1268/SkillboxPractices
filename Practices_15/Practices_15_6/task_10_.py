original_List = [1, 4, 10, 0, 5, -7, -100]

for i in range(len(original_List)):
    for j in range(i, len(original_List)):
        if original_List[j] < original_List[i]:
            original_List[i], original_List[j] = original_List[j], original_List[i]

print(original_List)