#!/usr/bin/python

import curses
import signal, sys

def hackertype(file):
    w = curses.initscr()

    curses.noecho()
    curses.raw()
    curses.cbreak()

    def signal_handler(signal, frame):
        curses.noraw()
        curses.endwin()
        print("OHSHITEXPLODE")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    file = open(file)
    w.leaveok(0)
    while True:
        if w.getch() != -1:
            char = file.read(1)
            sys.stdout.write(char)
            w.move(0, 0)
            if char == '\n':
                sys.stdout.write('\r')
            sys.stdout.flush()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        hackertype(sys.argv[1])
