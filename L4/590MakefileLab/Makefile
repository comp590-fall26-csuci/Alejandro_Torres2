CC = gcc
CFLAGS = -Wall -Wextra -Iheaders
TARGET = program
SRC = main.c fibonacci.c

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) $(SRC) -o $(TARGET)

clean:
	rm -f $(TARGET)

run: $(TARGET)
	./$(TARGET)
