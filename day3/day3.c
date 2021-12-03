#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 256
#define LINES 2048

void part_one() {
    FILE *f = fopen("input.txt", "r");

    char buffer[BUFFER_SIZE];
    int gamma_rate[BUFFER_SIZE];
    int epsilon_rate[BUFFER_SIZE];
    memset(gamma_rate, 0, sizeof(int) * BUFFER_SIZE);

    fscanf(f, "%s", buffer);
    int length = strlen(buffer);
    do {
        for (int i = 0; i < length; i++) {
            gamma_rate[i] += buffer[i] == '1' ? 1 : -1;
        }
    } while (fscanf(f, "%s", buffer) == 1);

    int epsilon = 0;
    int gamma = 0;

    for (int i = 0; i < length; i++) {
        if (gamma_rate[i] > 0) {
            gamma |= (1 << (length - i - 1));
        } else {
            epsilon |= (1 << (length - i - 1));
        }
    }
    printf("%d\n", epsilon * gamma);

    fclose(f);
}

int is_only_number_left(int *numbers, int lines) {
    int o = 0;
    for (int i = 0; i < lines; i++) {
        if (numbers[i]) {
            o++;
        }
    }
    return o == 1;
}

int binary_to_decimal(char *bin, int length) {
    int num = 0;
    for (int i = 0; i < length; i++) {
        if (bin[i] == '1') {
            num |= (1 << (length - i - 1));
        }
    }
    return num;
}

void part_two() {
    FILE *f = fopen("input.txt", "r");

    char *buffers = malloc(sizeof(char) * BUFFER_SIZE * LINES);
    int lines = 0;
    fscanf(f, "%s", buffers);
    int length = strlen(buffers);
    lines++;

    for (; fscanf(f, "%s", buffers + lines * BUFFER_SIZE) == 1; lines++)
        ;

    int *oxygens = malloc(sizeof(int) * lines);
    int *carbons = malloc(sizeof(int) * lines);
    memset(oxygens, 1, sizeof(int) * lines);
    memset(carbons, 1, sizeof(int) * lines);

    for (int i = 0; i < length; i++) {
        int o_occurrence = 0;
        int c_occurrence = 0;
        for (int j = 0; j < lines; j++) {
            int res = buffers[i + j * BUFFER_SIZE] == '1' ? 1 : -1;
            if (oxygens[j]) {
                o_occurrence += res;
            }
            if (carbons[j]) {
                c_occurrence += res;
            }
        }

        int is_single_carbon = is_only_number_left(carbons, lines);
        int is_single_oxygen = is_only_number_left(oxygens, lines);

        for (int j = 0; j < lines; j++) {
            if (!is_single_carbon) {
                if (c_occurrence >= 0) {
                    // 0 is the least common value, keep that and remove 1s
                    if (buffers[i + j * BUFFER_SIZE] == '1') {
                        carbons[j] = 0;
                    }

                } else {
                    // 1 is the least common value, keep that and remove 0s
                    if (buffers[i + j * BUFFER_SIZE] == '0') {
                        carbons[j] = 0;
                    }
                }
            }

            if (!is_single_oxygen) {
                if (o_occurrence >= 0) {
                    // 1 is the most common value, removes the 0s
                    if (buffers[i + j * BUFFER_SIZE] == '0') {
                        oxygens[j] = 0;
                    }
                } else {
                    // 0 is the most common value, removes the 1s
                    if (buffers[i + j * BUFFER_SIZE] == '1') {
                        oxygens[j] = 0;
                    }
                }
            }
        }
    }

    int oxygen_val = 0;
    int carbon_val = 0;
    for (int i = 0; i < lines; i++) {
        if (oxygens[i]) {
            oxygen_val = binary_to_decimal(buffers + i * BUFFER_SIZE, length);
        }
        if (carbons[i]) {
            carbon_val = binary_to_decimal(buffers + i * BUFFER_SIZE, length);
        }
    }

    printf("%d\n", oxygen_val * carbon_val);

    free(buffers);
    free(oxygens);
    free(carbons);

    fclose(f);
}

int main(void) {
    // part_one();
    part_two();
    return 0;
}