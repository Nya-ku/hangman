import random
def hangman():
    word_list = ["hinatazaka", "ひなたざか", "日向坂"]
    word = random.choice(word_list)
    wrong = 0
    stages = ["",
                "__________        ",
                "|                 ",
                "|         |       ",
                "|         O       ",
                "|        /|\     ",
                "|        / \     ",
                "|                 "
                ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages))
        print('あなたの負け！正解は{}'.format(word))

#mission_word = ["hinatazaka", "ひなたざか", "日向坂"]
hangman()
