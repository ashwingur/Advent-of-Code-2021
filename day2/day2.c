#include <stdio.h>
#include <string.h>

int main(void) {
    FILE *f = fopen("input.txt", "r");
    int horizontal = 0;
    int depth = 0;
    char buffer[256];
    int aim = 0;
    int num;
    while (fscanf(f, "%s %d", buffer, &num) == 2) {
        if (strcmp(buffer, "forward") == 0) {
            horizontal += num;
            depth += aim * num;
        } else if (strcmp(buffer, "up") == 0) {
            aim -= num;
        } else {
            aim += num;
        }
    }
    printf("%d\n", depth * horizontal);
    fclose(f);

    return 0;
}