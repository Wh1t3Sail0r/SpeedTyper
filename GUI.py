import pygame_textinput
import pygame
import time as t
import numpy as np
pygame.init()

FONT = pygame.font.SysFont('Comic Sans', 25)

test = 'The quick brown fox jumped over the lazy dog'

textinput = pygame_textinput.TextInput()

screen = pygame.display.set_mode((1080, 600))

clock = pygame.time.Clock()

count = 0

# data_file = open('data.txt', 'w+')


def get_stats(text_input, word, start):
    end = t.time()
    # print(end - start)
    # print(text_input.get_text())
    count = get_accuracy(text_input.get_text(), test)
    acc = str(str(round(float(1 - (count / (len(test)))) * 100, 2)))
    # print(acc)
    time_taken = (str(round(end-start, 2)) + ' seconds')
    wpm = (str(round(60 * 9/(end-start))) + ' wpm')
    return [acc, time_taken, wpm]


def get_accuracy(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros((size_x, size_y))
    for x in range(size_x):
        matrix[x, 0] = x
    for y in range(size_y):
        matrix[0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x - 1] == seq2[y - 1]:
                matrix[x, y] = matrix[x - 1, y - 1]

            else:
                matrix[x, y] = min(matrix[x - 1, y], matrix[x - 1, y - 1], matrix[x, y - 1]) + 1

    # print(matrix)
    return matrix[size_x - 1, size_y - 1]


def new_window():
    while True:
        screen.fill((128, 128, 128))
        rect = pygame.Rect((150, 150), (780, 40))
        rect = pygame.draw.rect(screen, (255, 255, 255), rect)
        pygame.display.update()
        break


def main(screen, test, clock, textinput, FONT):
    start = 0
    bool_start = False
    x = 0

    run = True
    while run:
        clock.tick(30)
        screen.fill((128, 128, 128))
        rect = pygame.Rect((150, 150), (780, 40))
        rect = pygame.draw.rect(screen, (255, 255, 255), rect)

        text = FONT.render(test, 1, (0, 0, 0))
        screen.blit(text, (540-(text.get_rect().width/2), 100))

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    start = t.time()

        screen.blit(textinput.get_surface(), (160, 158))
        if textinput.update(events):
            break

        pygame.display.update()
    get_stats(textinput, test, start)
    data = get_stats(textinput, test, start)
    print(data)
    data_file = open('data.txt', 'w')
    data_file.write((' ' + data[0]) + (' ' + data[1]) + (' ' + data[2]))


    while run:
        clock.tick(30)
        screen.fill((128, 128, 128))
        rect = pygame.Rect((150, 150), (780, 40))
        rect = pygame.draw.rect(screen, (255, 255, 255), rect)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        screen.blit(textinput.get_surface(), (160, 158))
        text = FONT.render(('Accuracy: ' + data[0] + '% accurate'), 1, (0, 0, 0))
        screen.blit(text, (10, 20))
        text = FONT.render(('Time: ' + data[1]), 1, (0, 0, 0))
        screen.blit(text, (250, 20))
        text = FONT.render(('Words per Minute: ' + data[2]), 1, (0, 0, 0))
        screen.blit(text, (450, 20))

        rect = pygame.Rect((450, 450), (180, 80))
        rect = pygame.draw.rect(screen, (255, 255, 255), rect)
        text = FONT.render(('Restart'), 1, (0, 0, 0))
        screen.blit(text, (540-(text.get_rect().width/2), 490-(text.get_rect().height/2)))

        for event in events:
            if rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONUP:
                    pygame.quit()
                    pygame.init()
                    textinput.clear_text()
                    f = pygame.font.SysFont('Comic Sans', 25)
                    ti = 'The quick brown fox jumped over the lazy dog'
                    te = pygame_textinput.TextInput()
                    s = pygame.display.set_mode((1080, 600))
                    c = pygame.time.Clock()
                    main(s, ti, c, te, f)

        pygame.display.update()


main(screen, test, clock, textinput, FONT)
