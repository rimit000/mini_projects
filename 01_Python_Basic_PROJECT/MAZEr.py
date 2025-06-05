## 시간 측정 라이브러리
import time

## 맵(스테이지)
map=['⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛',
    '⬛⬜⬜⬛🟩⬜⬛⬜⬜⬜⬜⬜⬜⬜🟦⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜🟦⬛',
    '⬛⬜⬜⬛🟦⬜⬛⬜⬜🟩⬜⬜⬜⬛⬛⬜⬜⬜⬛⬜🟩⬜⬜⬜⬜⬜⬜⬜🟩⬜⬜⬛',
    '⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬛⬛⬜⬜⬜⬛⬛🟩⬜⬜⬜⬜⬜🟩⬛',
    '⬛⬜⬜⬛⬜⬜⬛⬜⬜⬛⬛⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬛⬛⬛⬛',
    '⬛⬜⬜⬛⬜⬜🟦⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜🟦⬜⬜⬜⬜⬜⬛🟦⬜⬜⬜⬜⬜⬛',
    '⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬛⬜⬜🟩⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬛⬛⬛🟩⬜⬜⬜⬛',
    '⬛⬜⬜⬜⬜⬛⬛⬜⬜🟦⬛⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜⬛⬛🟩⬜🟦⬛⬜⬜⬜✨⬛',
    '⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛']

## 0. 메인화면
def main_screen():
    print()
    print(' ⬜⬛🟩🟦')
    print('      🟩🟦  M A Z E R  ⬜⬛')
    print('                       ⬜⬛🟩🟦')
    print()
    print('- - - - - - - M E N U - - - - - - -')
    print()
    print(' 1 . S T A R T')
    print(' 2 . R A N K I N G')
    print(' 3 . D E S C R I P T I O N')
    print()

## 이름 검증 및 변환
def name_check(name):
    name=name.upper().strip() # 대문자 변환 및 공백 제거
    if not name.isalpha(): # 이름이 알파벳이 아닐 때
        return None # None 반환
    if len(name)<3:
        name=name.ljust(3,'O')
    elif len(name)>3:
        name=name[:3]
    return name

## 1-1. 이름 설정 화면
def start_game():
    print()
    print(' ⬜⬛🟩🟦')
    print('      🟩🟦  M A Z E R  ⬜⬛')
    print('                       ⬜⬛🟩🟦')
    print()
    print()
    print('     N A M E ')
    print()
    print('                  ( E X : ABC )')
    print()
    print()
    while True: # 올바른거 입력할 때까지 무한 반복
        name=input("N A M E : ")
        valid_name=name_check(name) # 입력 검증 및 보정
        if valid_name: # 유효한 이름이면
            print(f'✨ Y O U R  N A M E ✨ : {valid_name}')
            character_choiced=character()
            print(f'✨ W E L C O M E ! ✨  {valid_name} {character_choiced}')
            before_start()
            play(valid_name, character_choiced)
            break # 루프 종료
        else:
            print(f'T R Y   A G A I N (EX : ABC)')

## 1-2. 캐릭터 설정 화면
def character():
    while True:
        print()
        print(' ⬜⬛🟩🟦')
        print('      🟩🟦  M A Z E R  ⬜⬛')
        print('                       ⬜⬛🟩🟦')
        print()
        print()
        print('  C H A R A C T E R : ')
        print()
        print('                1🙃   2😡   3😈')
        print('                4👽   5🤖   6💩')
        print('                7🐣   8🐧   9🐍')
        choice=input(" C H A R A C T E R : ")
        if choice in ['1','2','3','4','5','6','7','8','9']:
            characters={'1': '🙃', '2': '😡', '3': '😈',
                        '4': '👽', '5': '🤖', '6': '💩',
                        '7': '🐣', '8': '🐧', '9': '🐍'}
            character_choiced=characters[choice]
            return character_choiced
        else:
            print(" T R Y   A G A I N (1 ~ 9)")

## 1-3. (게임 시작 전)조작 설명
def before_start():
    while True:
        print()
        print(f' ⬜⬛🟩🟦')
        print(f'      🟩🟦  M A Z E R  ⬜⬛')
        print(f'                       ⬜⬛🟩🟦')
        print()
        print(f'        W              UP')
        print(f'     A  S  D    LEFT  DOWN  RIGHT')
        print()
        print(f'              GAME START? [Y/N]')
        print()
        print()
        choice=input(" G A M E   S T A R T ? : ")
        if choice.lower() == 'y':
            return True
        elif choice.lower()=='n':
            return False

## 맵(스테이지) 설정
def mazer(maze, move, character_choiced):
    for y, row in enumerate(maze): 
        for x, cell in enumerate(row):
            if (y,x)==move:
                print(f'{character_choiced}', end="")
            else:
                print(cell, end="")
        print()

## 이동키 설정
def mover(move, direction, maze):
    y,x=move
    if direction=="w" and maze[y-1][x]!="⬛":  # 세로 좌표 y를 1 감소시켜 위로 이동
        y-=1
    elif direction=='s'and maze[y+1][x]!="⬛":
        y+=1
    elif direction=='a'and maze[y][x-1]!="⬛":
        x-=1
    elif direction=='d'and maze[y][x+1]!="⬛":
        x+=1
    elif direction=="ww" and maze[y-2][x]!="⬛":
        y-=2
    elif direction=='ss'and maze[y+2][x]!="⬛":
        y+=2
    elif direction=='aa'and maze[y][x-2]!="⬛":
        x-=2
    elif direction=='dd'and maze[y][x+2]!="⬛":
        x+=2
    return y,x

## 1-4. 게임 실행
def play(name,character):
    total_score=0 # 총 점수
    maze=[list(row) for row in map] # 맵 복사
    move=(1,1) # 플레이어 시작 위치
    bonus_score=0 # 보너스 점수 초기화
    start_time=time.time() # 스테이지 시작 시간
    
    while True: # 남은 시간 계산
        elapsed_time=time.time()-start_time
        remaining_time=max(0,50-elapsed_time)

        mazer(maze, move, character) # 미로 출력
        print(f"⌛ T I M E   L E F T : {remaining_time : .2f} S  |  🔥 B O N U S   P O I N T : {bonus_score}\n")
        movement=input(' M O V E : ').lower()
            
        if movement in ['w','s','a','d','ww','ss','aa','dd']: # 이동 처리
            move=mover(move,movement,maze)
                
            if maze[move[0]][move[1]]=="✨": # 도착지 도달
                time_score=max(2,int(remaining_time*200)) # 시간 점수 계산
                total_score+=time_score+bonus_score
                
                if game_summary(total_score, time_score, bonus_score):
                    return

            elif maze[move[0]][move[1]]=="🟩":    # 보너스 블럭 처리
                bonus_score+=500
                maze[move[0]][move[1]]="⬜"
            elif maze[move[0]][move[1]]=="🟦":
                bonus_score+=1000
                maze[move[0]][move[1]]="⬜"

## 1-5. (게임 종료 후)점수 표시 화면
def game_summary(total_score, time_score, bonus_score):
    while True:
        print()
        print(f'      🟩🟦  M A Z E R  ⬜⬛')
        print(f'')
        print(f'       🎉 S T A G E  C L E A R 🎉')
        print()
        print(f" T I   M E    S C O R E : {time_score}")
        print(f" B O N U S    S C O R E : {bonus_score}")
        print()
        print(f" T O T A L    S C O R E : {total_score}")
        print()
        print("                      QUIT? [Y]")
        choice=input("Q U I T : ").lower()
        if choice.lower() == 'y':
            return True  # 메인 화면으로 이동

## 2. 랭킹 화면(미구현)
def ranking():
    while True:
        print()
        print("      🟩🟦  M A Z E R  ⬜⬛")
        print("             R A N K I N G ")
        print()
        print(" - - - 1. NDR 👽  15321")
        print(" - - - 2. RIM 🐧  13582")
        print(" - - - 3. IOO 🤖  11732")
        print(" - - - 4. RIM 💩   9254")
        print(" - - - 5. lEE 😈   7796")
        print("                  QUIT? [Y]")
        print()
        choice=input(" Q U I T ? : ")
        if choice.lower() == 'y':
            return

## 3. 게임 설명 화면
def description():
    while True:
        print()
        print("      🟩🟦  M A Z E R  ⬜⬛")
        print()
        print(" STAGE - 01 ~ 05, STAGE TIME LIMIT : 50 SEC ")
        print(" TIME POINT - 0.01 SEC : -2 POINT")
        print("    EX) 10 SEC : 8000P, 20 SEC : 6000P")
        print(" BONUS POINT - GREEN BLOCK 🟩 : 500P")
        print("               BLUE BLOCK  🟦 : 1000P")
        print(" DEVELOPED BY NOH DONGRIM")
        print(" VERSION : 1.0.0")
        print("                         QUIT? [Y]")
        choice=input(" Q U I T ? : ")
        if choice.lower() == 'y':
            return

## 메인화면 실행
while True:
    main_screen()
    choice=input("M A N U : ")
    if choice == '1':
        start_game()
    elif choice == '2':
        ranking()
    elif choice == '3':
        description()
    else:
        print(" T R Y   A G A I N  ")