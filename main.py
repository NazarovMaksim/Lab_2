import re
def generate_code(template, language):

    # cортировка массива слиянием
    match = re.match(r"Отсортировать массив \[(.+)\] алгоритмом слияния", template)
    if match:
        array = match.group(1)
        if language == 'Python':
            return ("def merge_sort(arr):\n"
                    "    if len(arr) > 1:\n"
                    "        mid = len(arr) // 2\n"
                    "        left_half = arr[:mid]\n"
                    "        right_half = arr[mid:]\n"
                    "        merge_sort(left_half)\n"
                    "        merge_sort(right_half)\n"
                    "        i = j = k = 0\n"
                    "        while i < len(left_half) and j < len(right_half):\n"
                    "            if left_half[i] < right_half[j]:\n"
                    "                arr[k] = left_half[i]\n"
                    "                i += 1\n"
                    "            else:\n"
                    "                arr[k] = right_half[j]\n"
                    "                j += 1\n"
                    "            k += 1\n"
                    "        while i < len(left_half):\n"
                    "            arr[k] = left_half[i]\n"
                    "            i += 1\n"
                    "            k += 1\n"
                    "        while j < len(right_half):\n"
                    "            arr[k] = right_half[j]\n"
                    "            j += 1\n"
                    "            k += 1\n"
                    "arr = [" + array + "]\n"
                    "merge_sort(arr)\n"
                    "print(arr)")
        elif language == 'JavaScript':
            return ("function mergeSort(arr) {\n"
                    "    if (arr.length <= 1) {\n"
                    "        return arr;\n"
                    "    }\n"
                    "    const mid = Math.floor(arr.length / 2);\n"
                    "    const left = mergeSort(arr.slice(0, mid));\n"
                    "    const right = mergeSort(arr.slice(mid));\n"
                    "    return merge(left, right);\n"
                    "}\n"
                    "function merge(left, right) {\n"
                    "    let result = [], i = 0, j = 0;\n"
                    "    while (i < left.length && j < right.length) {\n"
                    "        if (left[i] < right[j]) {\n"
                    "            result.push(left[i]);\n"
                    "            i++;\n"
                    "        } else {\n"
                    "            result.push(right[j]);\n"
                    "            j++;\n"
                    "        }\n"
                    "    }\n"
                    "    return result.concat(left.slice(i)).concat(right.slice(j));\n"
                    "}\n"
                    "const arr = [" + array + "];\n"
                    "console.log(mergeSort(arr));")

    # нахождение максимума и минимума в матрице
    match = re.match(r"Найти максимум и минимум в матрице \[(.+)\]", template)
    if match:
        matrix = match.group(1)
        if language == 'Python':
            return ("matrix = [" + matrix + "]\n"
                    "flat_matrix = [item for row in matrix for item in row]\n"
                    "print(f'Max: {max(flat_matrix)}, Min: {min(flat_matrix)}')")
        elif language == 'JavaScript':
            return ("const matrix = [" + matrix + "];\n"
                    "const flatMatrix = matrix.flat();\n"
                    "console.log(`Max: ${Math.max(...flatMatrix)}, Min: ${Math.min(...flatMatrix)}`);")

    # транспонирование матрицы
    match = re.match(r"Транспонировать матрицу \[(.+)\]", template)
    if match:
        matrix = match.group(1)
        if language == 'Python':
            return ("matrix = [" + matrix + "]\n"
                    "transposed = list(map(list, zip(*matrix)))\n"
                    "print(transposed)")
        elif language == 'JavaScript':
            return ("const matrix = [" + matrix + "];\n"
                    "const transposed = matrix[0].map((_, colIndex) => matrix.map(row => row[colIndex]));\n"
                    "console.log(transposed);")

    return "Шаблон не распознан. Попробуйте другой запрос."


examples = [
    ("Отсортировать массив [3, 5, 1, 8, 2] алгоритмом слияния", "Python"),
    ("Отсортировать массив [10, 7, 2, 1, 5] алгоритмом слияния", "JavaScript"),
    ("Найти максимум и минимум в матрице [[1, 2], [3, 4]]", "Python"),
    ("Найти максимум и минимум в матрице [[9, 5], [7, 1]]", "JavaScript"),
    ("Транспонировать матрицу [[1, 2, 3], [4, 5, 6], [7, 8, 9]]", "Python"),
    ("Транспонировать матрицу [[1, 4, 7], [2, 5, 8], [3, 6, 9]]", "JavaScript")
]

for template, language in examples:
    print(f"\nШаблон: {template}\nЯзык: {language}\nСгенерированный код:")
    print(generate_code(template, language))
