# User Defined Function
def is_found(latter, statement):  # () stands for the parameters list
    """ Returns wither the letter is found within the given statement.

    :param latter, string, the latter to search for
    :param statement, string, the statement to search inside

    :return True or False, boolean, whither the latter is found or not
    """
    if latter in statement:
        return True
    return False


# Don't leave any executable statement directly on the line

# 152 =  8
def summ_digits(num):
    num = str(num)
    summ = 0
    for i in num:
        summ += int(i)
    return summ


if __name__ == "__main__":
    print(is_found('z', "This is a python string"))
    print(summ_digits(562))

# problem-solving
# general solution - can handle almost all use case with minimum code changes - considerable performance
# optimal solution - specific for a use case - highest performance


for i in range(5):
    for j in range(5):
        if i > j:
            print('*', end='')
        else:
            print(" ", end='')
    print()

for i in range(5):
    print("*" * i)
