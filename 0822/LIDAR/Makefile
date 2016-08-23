
# C++
CC = g++
CFLAGS = -Wall

# Library
LIBS = -lmesasr
LFLAGS = #-L/usr/lib  -I/.

# Target
OBJS = lidar_test.o
TARGET = lidar_test

# プログラム作成
all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS) $(LFLAGS) $(LIBS)

# Clean
clean:
	rm -f *.o
	rm $(TARGET)

