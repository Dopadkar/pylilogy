import random
import math
import statistics  as sts
import numpy as np
import matplotlib.pyplot as plt

def get_row(lenght):
    x = []
    while lenght + 1 > 0:
        if len(x) > 0:
            x.append(x[-1]+(random.random()*2-1))
        else:
            x.append(random.random())
        lenght -= 1
    return x

def draw_logistic(logistic_rows, name= ''):
    import matplotlib.pyplot as plt
    
    l = len(logistic_rows)
    x = range(l)
    plt.plot(x, logistic_rows)
    plt.title('Функция плотности распреления букв в романе "' + name +  '"')
    plt.xlabel('Буквы')
    plt.ylabel('Частота встречаемости')
    plt.show()
    plt.savefig(name + '_распреления букв' + '.png', format='png', transparent=True)

def get_del_row(row, n):
    # функция получает на вход ряд row
    dels_list = []
    row1 = row.copy()
    row2 = row.copy()
    for i in range(n):
        del row1[-1]
        del row2[0]

    l = len(row1)

    del_row = []

    for i in range(l):
        r1 = str(row1[i])
        r2 = str(row2[i])
        r_deff = str(row1[i]-row2[i])
        #print('{:20}-{:20}={:20} '.format(r1,r2,r_deff))
        del_row.append(row1[i]-row2[i])
    
    if len(row1) != len(row2):
        print('Длины рядов не равны')

    return del_row

def get_mean(row):
    return 1.0 * sum(row)/len(row)

def get_difference(numbers):

    mean = get_mean(numbers)
    diff = []

    for num in numbers:
        diff.append(num-mean)
        
    return diff

def calculate_variance(numbers):
    # find the list of differences
    diff = get_difference(numbers)
    # find the squared differences
    s_diff = []
    for d in diff:
        s_diff.append(d**2)
    # Find the variance
    sum_s_diff = sum(s_diff)
    variance = 1.0 * sum_s_diff / len(numbers)
    return variance

def get_std(numbers):
    '''
    Функция принмает на вход ряд чисел row -) стандартное отклонение
    '''
    std = calculate_variance(numbers) ** 0.5
    return std

def get_del_rows(row, n):
    nums = [2 ** x for x in range(1, n)]
    
    del_rows = []
    logistic_rows = []

    for i in nums:
        del_row = get_del_row(row, i)
        # получаем стандартное отклонение для n-ого ряда del
        del_row_std = get_std(del_row)
        print('При n = {} стандартное отклонение равно {}'.format(i,del_row_std))
        del_rows.append(del_row_std)
    
    for x in del_rows:
        logistic_rows.append(math.log2(x))

    return del_row_std, logistic_rows, nums

def get_hurst(logistic_rows):
    import sklearn
    from sklearn.linear_model import LinearRegression
    reg_mod = LinearRegression()
    x=range(len(logistic_rows))
    X = np.array(x)
    l_r = np.array(logistic_rows)
    print(X)
    print(l_r)
    reg_mod.fit(x, l_r)

    y_pred = regr.predict(X)


    # Plot outputs
    plt.scatter(x, logistic_rows,  color='black')
    plt.plot(X, y_pred, color='blue', linewidth=3)

    plt.xticks(())
    plt.yticks(())

    plt.show()
    
    print(reg_mod.coef_)

row = get_row(1000)
#get_del_row(row, 2)

del_rows, logistic_rows, nums =get_del_rows(row, 7)
get_hurst(logistic_rows)

draw_logistic(row)
