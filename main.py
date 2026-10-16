import numpy as np

# Task 1
arr = np.random.randint(0, 101, size=10)


print("Масив до сортування:", arr)


min_val = np.min(arr)
max_val = np.max(arr)
mean_val = np.mean(arr)

print(f"Мінімальне значення: {min_val}")
print(f"Максимальне значення: {max_val}")
print(f"Середнє значення: {mean_val}")


sorted_arr = np.sort(arr)


print("Масив після сортування:", sorted_arr)


print("=" * 40)
print("ЗАВДАННЯ 2")
print("=" * 40)


arr_2d = np.random.randint(1, 51, size=(4, 4))


print("Двовимірний масив 4x4:")
print(arr_2d)


row_sums = np.sum(arr_2d, axis=1)
col_sums = np.sum(arr_2d, axis=0)


total_mean = np.mean(arr_2d)


print(f"\nСуми за рядками: {row_sums}")
print(f"Суми за стовпчиками: {col_sums}")
print(f"Загальне середнє значення масиву: {total_mean:.2f}")


print("\n" + "=" * 40)
print("ЗАВДАННЯ 3")
print("=" * 40)


arr_3x5 = np.arange(15).reshape(3, 5)


print("Вихідний масив 3х5:")
print(arr_3x5)


transposed_arr = arr_3x5.T
print("\nТранспонований масив:")
print(transposed_arr)


reshaped_arr = np.arange(15).reshape(5, 3)
print("\nМасив після reshape (5х3):")
print(reshaped_arr)