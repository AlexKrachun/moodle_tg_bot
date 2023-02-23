from random import randint

topic_path = {
    '/кубические': 'cube',
    '/показательные': 'exponential',
    '/иррациональные': 'irrational',
    '/логарифмические': 'logarithmic',
}

kind_path = {
    '/уравнения': 'equations',
    '/неравенства': 'inequalities',
    '/выражения': 'expressions',
}


def create_task_file(data):
    topic = data['topic']
    kind = data['kind']
    amount = int(data['amount'][1:])
    path = f'./db/{topic_path[topic]}/{topic_path[topic]}_{kind_path[kind]}.txt'
    bd_file = open(path, encoding='utf-8')
    bd = [i for i in bd_file.read().split('\n\n')]
    bd_file.close()


    ind = randint(0, len(bd) - amount)
    tasks = bd[ind:ind + amount]

    output = open('task_file.txt', 'w', encoding='utf-8')
    for i in range(len(tasks)):
        a = tasks[i].split('::')
        a[1] = f' Вопрос {i + 1} \n'
        print('::' + '::'.join(a[1:]), end='\n\n', file=output)













