import requests, time, sys, random, os
from datetime import datetime

def follow(user, token):
    rfollow = requests.post(f'https://api.grustnogram.ru/users/{user}/follow', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36', 'Access-Token': token})
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if rfollow.status_code == 200:
        return f'{current_time} | [+]{token} FOLLOW DONE[+]'
    else:
        return f'{current_time} | [-]{token} FOLLOW ERROR[-]'

def like(post, token):
    rlike = requests.post(f'https://api.grustnogram.ru/posts/{post}/like', headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
        'Access-Token': token
    })
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if rlike.status_code == 200:
        return f'{current_time} | [+]{token} LIKE DONE[+]'
    else:
        return f'{current_time} | [-]{token} LIKE ERROR[-]'

def comment(post, token, commentariy):
    rсomment = requests.post(f'https://api.grustnogram.ru/posts/{post}/comments', headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
        'Access-Token': token
    }, data={
        'comment': str(commentariy)
    })

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if rсomment.status_code == 200:
        return f'{current_time} | [+]{token} COMMENT DONE[+]'
    else:
        return f'{current_time} | [-]{token} COMMENT ERROR[-]\n{rсomment.json()}'

def reports(token, post, type):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    try:
        report = requests.post(f'https://api.grustnogram.ru/posts/{post}/complaint', headers={
            'User-Agent': '',
            'Access-Token': token
        }, data={
            'type': type
        })
        return f'{current_time} | [+]{token} REPORT DONE[+]'
    except Exception as e:
        return f'{current_time} | [-]{token} REPORT ERROR[-]\n{e}'
while True:
    for filename in os.listdir('./'):
        if filename.startswith('token'):
            tokencount = []
            with open(filename, 'r') as token_file:
                for token_line in token_file:
                    tokencount.append(token_line)
                print(f'{filename}: {len(tokencount)} tokens')
    # https://grustnogram.ru/u/grustnogram
    need_tokfile = input('--------------------\nWhich token file i should to use? >')
    choice = input(f'followers/likes/comments/reports >')
    if choice == 'followers':

        url = input('User URL (https://grustnogram.ru/u/....) >')
        with open(need_tokfile, 'r') as tokenlist:
            token_choose_list = []
            for token in tokenlist:
                token_choose_list.append(token[:-1])
            while True:
                print(follow(url, random.choice(token_choose_list)))

    elif choice == 'likes':

        url = input('Post URL (https://grustnogram.ru/p/....) >')
        id_check = requests.get(f'https://api.grustnogram.ru/p/{url[25:]}', headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
        }).json()

        with open(need_tokfile, 'r') as tokenlist:
            token_choose_list = []
            for token in tokenlist:
                token_choose_list.append(token[:-1])
            while True:
                print(like(id_check['data']['id'], random.choice(token_choose_list)))

    elif choice == 'comments':
        for comm_filename in os.listdir('./'):
            if comm_filename.startswith('comments'):
                comments = []
                with open(comm_filename, 'r', encoding='UTF-8') as comm_file:
                    for comm_line in comm_file:
                        comments.append(comm_line[:-1])
                    print(f'-------------------------------\n{comm_filename}: {comments}')

        need_commfile = input('-------------------------------\nWhich comments file i should to use? >')
        #post = int(input(f'Post id >'))

        url = input('Post URL (https://grustnogram.ru/p/....) >')
        id_check = requests.get(f'https://api.grustnogram.ru/p/{url[25:]}', headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
        }).json()

        print(id)
        token_choose_list = []
        with open(need_tokfile, 'r') as tokenlist:
            for token in tokenlist:
                token_choose_list.append(token[:-1])
                use_comments = []
                with open(need_commfile, 'r', encoding='UTF-8') as comments_file:
                    for comm_line in comments_file:
                        use_comments.append(comm_line[:-1])
                print(comment(id_check['data']['id'], random.choice(token_choose_list), random.choice(use_comments)))
    elif choice == 'reports':
        token_choose_list = []
        post = input('Post ID >')
        type = int(input('Reports type:\n1. Содержит недопустимые материалы\n2. Оскорбляет меня\n3. Оскорбляет Российскую Федерацию\n>'))
        with open(need_tokfile, 'r') as tokenlist:
            for token in tokenlist:
                token_choose_list.append(token[:-1])
            while True:
                print(reports(random.choice(token_choose_list), post, type))

    else:
        sys.exit()

# https://api.grustnogram.ru/posts/1107500/
