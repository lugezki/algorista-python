def spiral_traverse(matrix):
    """
    Takes a matrix and returns an array after performing a spiral traversal.
    """
    if len(matrix) <= 0:
        return []

    result = []
    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = cols - 1
    top = 0
    bottom = rows - 1

    while left <= right and top <= bottom:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left -1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

