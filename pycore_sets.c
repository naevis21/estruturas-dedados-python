#include <stdio.h>
#include <stdlib.h>

typedef struct set {
  char **elements;
  int size;
} set_t;

set_t *set_new() {
  set_t *set = malloc(sizeof(set_t));
  set->elements = NULL;
  set->size = 0;
  return set;
}

void set_add(set_t *set, char *element) {
  set->elements = realloc(set->elements, sizeof(char *) * (set->size + 1));
  set->elements[set->size++] = element;
}

void set_remove(set_t *set, char *element) {
  for (int i = 0; i < set->size; i++) {
    if (strcmp(set->elements[i], element) == 0) {
      memmove(set->elements + i, set->elements + i + 1, sizeof(char *) * (set->size - i - 1));
      set->size--;
      return;
    }
  }
}

int set_contains(set_t *set, char *element) {
  for (int i = 0; i < set->size; i++) {
    if (strcmp(set->elements[i], element) == 0) {
      return 1;
    }
  }
  return 0;
}

void set_print(set_t *set) {
  for (int i = 0; i < set->size; i++) {
    printf("%s ", set->elements[i]);
  }
  printf("\n");
}

void set_free(set_t *set) {
  free(set->elements);
  free(set);
}

int main(void) {
  // Cria um conjunto com os nomes das estruturas de dados básicas
  set_t *set1 = set_new();
  set_add(set1, "lista");
  set_add(set1, "tupla");
  set_add(set1, "dicionário");
  set_add(set1, "conjunto");

  // Adiciona um elemento ao conjunto
  set_add(set1, "grafo");

  // Remove um elemento do conjunto
  set_remove(set1, "tupla");

  // Verifica se um elemento existe no conjunto
  if (set_contains(set1, "conjunto")) {
    printf("'conjunto' existe no conjunto: Sim\n");
  } else {
    printf("'conjunto' existe no conjunto: Não\n");
  }

  // Combina dois conjuntos
  set_t *set2 = set_new();
  set_add(set2, "arvore");
  set_add(set2, "hashmap");
  set_t *set3 = set_union(set1, set2);
  set_print(set3);

  // Encontra a interseção de dois conjuntos
  set_t *set4 = set_intersection(set1, set2);
  set_print(set4);

  // Encontra a diferença de dois conjuntos
  set_t *set5 = set_difference(set1, set2);
  set_print(set5);

  // Encontra a diferença simétrica de dois conjuntos
  set_t *set6 = set_symmetric_difference(set1, set2);
  set_print(set6);

  // Libera a memória do conjunto
  set_free(set1);
  set_free(set2);
  set_free(set3);
  set_free(set4);
  set_free(set5);
  set_free(set6);

  return 0;
}
