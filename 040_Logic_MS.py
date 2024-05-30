def merge_sort(arr):
    if len(arr) > 1:
        # Encuentra el punto medio del array
        mid = len(arr) // 2

        # Divide el array en dos mitades
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Llama recursivamente a merge_sort en cada mitad
        merge_sort(left_half)
        merge_sort(right_half)

        # Inicializa los índices para iterar sobre las dos mitades y el array principal
        i = j = k = 0

        # Copia los datos en arr de forma ordenada
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Verifica si quedan elementos en left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Verifica si quedan elementos en right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Ejemplo de uso
arr = [12, 11, 13, 5, 6, 7]
print("Array original:", arr)
merge_sort(arr)
print("Array ordenado:", arr)
