'''
Easier solution:

https://github.com/MitkoVtori/SoftUni-Fundamentals-September-2022/blob/main/(F)%20Lists%20Advanced/More%20Exercise/05.%20Dots.py?fbclid=IwZXh0bgNhZW0CMTAAAR2PTaviozNNx6pWJ_hCYS3QYcgeJDZiX-iFPOYagzB9DB_IWbPZBET8aQc_aem_LpezNSR-vnP2v8jYYmz99w

Softuni Forum:

https://softuni.bg/forum/41325/python-fundamentals-list-advanced-more-exercise-05-dots
'''

def localize_dot(a):
    """Locate the first dot ('.') in the grid."""
    for b, c in enumerate(a):
        for e, f in enumerate(c):
            if f == '.':
                return [b, e]
    return None  # No dot found


def check_sides(a, b):
    """Check the availability of movement in all four directions."""
    U, D, L, R = True, True, True, True
    rows, cols = len(a), len(a[0])

    # Up
    if b[0] > 0:  # Ensure within bounds
        if a[b[0] - 1][b[1]] in ['-', 'x', '–']:
            U = False
    else:
        U = False

    # Down
    if b[0] < rows - 1:  # Ensure within bounds
        if a[b[0] + 1][b[1]] in ['-', 'x', '–']:
            D = False
    else:
        D = False

    # Left
    if b[1] > 0:  # Ensure within bounds
        if a[b[0]][b[1] - 1] in ['-', 'x', '–']:
            L = False
    else:
        L = False

    # Right
    if b[1] < cols - 1:  # Ensure within bounds
        if a[b[0]][b[1] + 1] in ['-', 'x', '–']:
            R = False
    else:
        R = False

    a[b[0]][b[1]] = 'x'  # Mark as visited
    z = [x for x, y in enumerate((U, D, L, R)) if y]
    return z, a


def cont(a, b):
    """Determine new positions based on available directions."""
    e = []
    for i in b:
        if i == 0:
            e.append([a[0] - 1, a[1]])  # Up
        elif i == 1:
            e.append([a[0] + 1, a[1]])  # Down
        elif i == 2:
            e.append([a[0], a[1] - 1])  # Left
        elif i == 3:
            e.append([a[0], a[1] + 1])  # Right
    return e


def check_sides_two(a, b):
    """Check the sides for multiple positions."""
    d = []
    for i in b:
        c, a = check_sides(a, i)
        d.append(c)
    return d, a


def zipidi(a, b, c):
    """Process and update the grid for multiple positions."""
    e = []
    f = []
    d = list(zip(a, b))

    for i in d:
        for x in i[1]:
            if x == 0:
                e.append([i[0][0] - 1, i[0][1]])  # Up
            elif x == 1:
                e.append([i[0][0] + 1, i[0][1]])  # Down
            elif x == 2:
                e.append([i[0][0], i[0][1] - 1])  # Left
            elif x == 3:
                e.append([i[0][0], i[0][1] + 1])  # Right

    for i in e:
        # Ensure valid indices and prevent duplicates
        if (
            i not in f
            and 0 <= i[0] < len(c)
            and 0 <= i[1] < len(c[0])
            and c[i[0]][i[1]] == '.'
        ):
            f.append(i)
            c[i[0]][i[1]] = 'x'  # Mark as visited

    return f, c


if __name__ == '__main__':
    a = int(input())
    b = [input().split() for _ in range(a)]
    m = []  # To store the sizes of connected components
    c = localize_dot(b)  # Locate the first dot

    while c:
        z = 1
        d, e = check_sides(b, c)  # Check available sides for the initial position
        f = cont(c, d)  # Get new positions
        z += len(f)

        g, h = check_sides_two(e, f)  # Check sides for the new positions
        i, j = zipidi(f, g, h)  # Update the grid and find new positions
        z += len(i)

        while len(i) != 0:
            g, h = check_sides_two(j, i)
            i, j = zipidi(i, g, h)
            z += len(i)

        m.append(z)
        c = localize_dot(j)  # Locate the next dot

    print(max(m)) if m else print(0)
