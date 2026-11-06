CC = gcc
CFLAGS = -Wall -Wextra -std=c11 -I590MakefileLab/headers

all: program

program:
	$(CC) $(CFLAGS) -o program 590MakefileLab/main.c 590MakefileLab/fibonacci.c

run: program
	./program

clean:
	rm -f program
