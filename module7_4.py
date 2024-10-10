def competition(team1_num, team2_num, score_1, score_2, team1_time, team2_time, tasks_total, time_avg):
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'

    return print('В команде Мастера кода участнтков: %s! \n' % team1_num,
                 'И того сегодня в командах участников: %s, %s!\n' % (team1_num, team2_num),
                 'Команда Волшебники данных решила задач: {}!\n'.format(score_2),
                 'Волшебники данных решили задачи за {}!\n'.format(team1_time),
                 f'Команды решили {score_1} и {score_2} задач.\n',
                 f'Результат битвы: {result}\n',
                 f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')


competition(team1_num=5, team2_num=6, score_1=40, score_2=42, team1_time=1552.512, team2_time=2153.31451,
            tasks_total=82, time_avg=45.2)
