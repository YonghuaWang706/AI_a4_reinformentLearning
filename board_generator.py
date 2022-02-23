import random


def generate_board(x, y, file_name):
    with open(file_name, 'w') as file:
        for i in range(x):
            if i != 0:
                file.write('\n')
            for j in range(y):
                int_to_write = 0
                probability = random.uniform(0, 1)
                if probability < 0.05:
                    int_to_write = random.randint(-10, 10)
                if j < y - 1:
                    file.write(str(int_to_write) + "\t")
                else:
                    file.write(str(int_to_write))


if __name__ == "__main__":
    generate_board(11, 6, 'testBoard.txt')
