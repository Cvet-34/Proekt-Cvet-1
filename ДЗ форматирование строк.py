
# %
team1_num = 'Мастер кода'
uchact = 5
print('В коменде %s, участyников %s' % (team1_num, uchact))
team2_num = 'Волшебники данных'
uchact1 = 6
print('В коменде %s, участyников %s' % (team2_num, uchact1))

# format
score_1 = 40
score_2 = 42
team_time = 18015.2
print('Команда {} решила задачи в колличестве {}'.format('Волшебники данных', score_2))
team1_time = 428.93
print('Команда {} решила в среднем задачу за {} {}'.format('Волшебники данных', team1_time, 'c'))

print('Команда {} решила задачи в колличестве {}'.format('Мастера кода', score_1))
team2_time = 450.38
print('Команда {} решила в среднем задачу за {} {}'.format('Мастера кода', team2_time, 'c'))

#f строка
score_1 = 40
score_2 = 42
challenge_result = 'Волшебники данных'
print(f'{40 < 42} По колличесту решенных задач Победила команда, {challenge_result}')

tasks_total = 82
time_avg = 350.4
print(f'Решено за период соревнований: {tasks_total}')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print('Победа команды Мастер кода!')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print('Победа команды Волшебники данных!')
else:
    print('Ничья')





