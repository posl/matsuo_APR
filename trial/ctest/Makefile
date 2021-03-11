CC = gcc
CFLAGS = -std=c99
TARGET = fib

$(TARGET): src/main.c
    $(CC) $(CFLAGS) $^ -o $(@)

test: $(TARGET)
    @./fib > output.txt
    @if diff output.txt test/answer.txt > /dev/null; then echo "test: OK"; else echo "test: NG"; exit 1; fi

clean:
    rm -f output.txt $(TARGET)