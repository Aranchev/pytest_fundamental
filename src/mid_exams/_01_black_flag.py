
if __name__ == '__main__':
    a = int(input()) # days of plunder
    b = int(input()) # daily plunder
    c = float(input()) # expected plunder
    plunder = 0

    for i in range(1, a + 1):
        plunder += b
        if i % 3 == 0:
            plunder += b / 2
        if i % 5 == 0:
            plunder -= plunder * 0.3
    if plunder >= c:
        print(f'Ahoy! {plunder:.2f} plunder gained.')
    else:
        print(f'Collected only {plunder/c * 100:.2f}% of the plunder.')

    '''
    How do you figure what percentage one number is of another?
    Consider two numbers 30 and 45. Let us calculate what percentage is 30 out of 45. For this, we divide the part (30) by the whole (45) and multiply the result by 100. This gives 30/45 × 100 = 66.67%
    '''


