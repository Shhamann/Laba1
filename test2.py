import time

# for i in range(10):
#     print(i)
#     time.sleep(1)

SET_COLOR = '\x1b[48;5;'
END = '\x1b[0m'
CLEAR = '\033[2H'


def draw_line (offset=0, lenght=1, color=30):
    line = ' ' * lenght
    print(f"{' ' * offset}{SET_COLOR}{color}m{line}{END}")


def draw_romb():
    size = 15
    center = size // 2
    offset = size // 2

    step = 1
    lenght = 1

    # print(size, center, offset)

    colors = [10, 240]

    while True:
        for color in colors:
            for line in range(size):
                draw_line(offset, lenght, color)
                time.sleep(0.02)

                if line < center: 
                    offset  -= step
                    lenght += step*2
                else:
                    offset  += step
                    lenght -= step*2

            print(f"\x1b[{size+2}A")
            print(f"\x1b[{offset}D")

            lenght = 1
            offset = size // 2

            time.sleep(0.5)


if __name__ == "__main__":
    draw_romb()

# if __name__ == "__main__":
    # for i in range (20):
    #     draw_line(lenght=10, offset=i, color=34)
    #     print(f'{CLEAR}')
    #     time.sleep(0.5)