#include <stdio.h>
#include <stdlib.h>

// Rabito and Rayito are playing a nice game. They start with a weighted bidirectional connected graph (all weights are positive) and a set of K bones placed on some of the vertices.

// They start taking turns with Rabito playing first. The game consists of moving the bones through the graph towards the vertex 1. 
// On a turn one the players takes a subset of at least 1 and at most P of the bones (that have not reached the vertex 1) 
// and moves these bones through one or more of the edges of the graph (the bones moves are independent of each other) 
// subject to this condition: he may use a particular edge for a bone if it makes that bone eventually reach the vertex 1 using the least possible amount of time 
// (it takes A units of time to move a bone through and edge of weight A) and if the edge makes this bone eventually reach the vertex 1 using the largest amount of edges.

// There's a huge bone waiting for the winner of the game, 
// so your task is to decide which of the two dogs will triumph on this game and have a nice meal 
// (assuming both of the dogs play with an optimal strategy). The loser of the game is, of course, the dog that cannot make a move.

// Input:
// The first line contains a single integer T (T <= 100) the number of test cases. The description of T test cases follows. 
// A test case begins with a line containing two integers N, M (1 <= N <= 100, 1 <= M <= 2000) 
// denoting the number of vertices and edges of the graph, then follow M lines each with three integers u, v, w (1 <= u, v <= N) (0 < w <= 1000000) 
// representing the vertices of the i-th edges and its weight. Then a line with two integers K (0 < K <= 1000) and P (0 < P) 
// denoting the number of bones initially placed on the graph and the parameter P as described in the problem statement. 
// Finally a single line containing K integers describing the initial positions of the K bones.

// Output
// Output T lines, one for each test case. If Rabito has a strategy that will guarantee his victory output "Yes", otherwise output "No".

int count = 1;

typedef struct elemento {
    int vertice;
    int origem;
    int distancia;
} elemento;

int qtd_global[10001];
int count_min_heap = 0;
elemento heap[10000];

typedef struct vertice {
    int visitado;
    int distancia;
    struct lista *lista_adj;
    int in;
    int lower;
} vertice;

typedef struct lista {
    int qtd;
    struct registro *inicio;
} lista;

typedef struct registro {
    int valor;
    int peso;
    struct registro *prox;
} registro;

int min(int x, int y);
void mostrar_lista(lista *l);
int incluir_ordenado_lista(lista *l, int x, int peso);
registro *aloca_registro();
lista *aloca_lista();
int carrega_grafo(vertice *vertices, char *nome_do_arquivo);
void push(vertice *v, int x, int peso);
void mostrar_lista_dos_vertices(vertice *v, int tam);
void dfs(vertice *vertices, int x, int pai);
elemento pop();
int push_fila(elemento x);
void desce_minimo(int indice);
void subir_minimo(int indice);
int define_pai(int indice);
int define_filho_direita(int indice);
int define_filho_esquerda(int indice);
int empty();
void djikstra(vertice *vertices, int raiz);
void inicializar_distancias(vertice *vertices);

int main() {
    vertice *vertices;
    int qtd_vertices, i;
    vertices = (vertice *)calloc(10001, sizeof(vertice));
    qtd_vertices = carrega_grafo(vertices, "D:/DOCUMENTOS/FACULDADE/Git/MAIN/C/Teoria dos Grafos/2023/djkstra.txt");
    if (qtd_vertices) {
        printf("\n Grafo carregado com sucesso qtd vertices: %d", qtd_vertices);
        mostrar_lista_dos_vertices(vertices, 10001);
    } else
        printf("\n Problema no carregamento do grafo");

    printf("\nDigite qual a raiz a ser usada:\n");
    int raizGrafo=0;
    scanf("%d", &raizGrafo);
    djikstra(vertices, raizGrafo);//vertices e raiz

    for (i = 1; i <= qtd_vertices; i++) {
        printf("\n Distancia do vertice %d para a raiz = %d", i, vertices[i].distancia);
    }

    printf("\n");
    return 0;
}

void inicializar_distancias(vertice *vertices) {
    int i;

    for (i = 0; i < 10001; i++) {
        vertices[i].distancia = 9999;
    }
}

void djikstra(vertice *vertices, int raiz) {
    int corrente, distancia_atual;
    elemento elemento_aux;
    registro *aux;

    inicializar_distancias(vertices);

    vertices[raiz].distancia = 0;
    elemento_aux.distancia = 0;
    elemento_aux.vertice = raiz;
    elemento_aux.origem = raiz;
    push_fila(elemento_aux);

    while (!empty()) {
        elemento_aux = pop();
        corrente = elemento_aux.vertice;
        distancia_atual = elemento_aux.distancia;

        if (vertices[corrente].lista_adj == NULL) {
            printf("\n Vertice em componente desconetado");
            return;
        }

        aux = vertices[corrente].lista_adj->inicio;
        while (aux != NULL) {
            if (distancia_atual + aux->peso < vertices[aux->valor].distancia) {
                vertices[aux->valor].distancia = distancia_atual + aux->peso;
                elemento_aux.distancia = vertices[aux->valor].distancia;
                elemento_aux.vertice = aux->valor;
                elemento_aux.origem = corrente;
                push_fila(elemento_aux);
            }
            aux = aux->prox;
        }
    }
}

int carrega_grafo(vertice *vertices, char *nome_do_arquivo) {
    FILE *arq;
    arq = fopen(nome_do_arquivo, "r");
    int a, b, c;
    int qtd_vertices = 0;

    int i;

    for (i = 0; i < 10001; i++) {
        qtd_global[i] = 0;
    }

    if (arq == NULL) {
        printf("\n Arquivo nao localizado");
        return 0;
    }

    while (fscanf(arq, "%d;%d;%d\n", &a, &b, &c) != EOF) {
        printf("\n A: %d B: %d", a, b);

        if (qtd_global[a] == 0)
            qtd_vertices++;
        qtd_global[a] = 1;

        if (qtd_global[b] == 0)
            qtd_vertices++;
        qtd_global[b] = 1;

        push(&vertices[a], b, c);
        push(&vertices[b], a, c);
    }

    return qtd_vertices;
}

void push(vertice *v, int x, int peso) {
    if (v->lista_adj == NULL)
        v->lista_adj = aloca_lista();
    incluir_ordenado_lista(v->lista_adj, x, peso);
}

lista *aloca_lista() {
    lista *novo;
    novo = (lista *)calloc(1, sizeof(lista));
    return novo;
}

registro *aloca_registro() {
    registro *novo;
    novo = (registro *)calloc(1, sizeof(registro));
    return novo;
}

int incluir_ordenado_lista(lista *l, int x, int peso) {
    if (l == NULL)
        return 0;

    registro *novo, *aux = NULL, *ant = NULL;
    novo = aloca_registro();
    novo->valor = x;
    novo->peso = peso;

    if (l->inicio == NULL) {
        l->inicio = novo;
    } else {
        int inserido = 0;
        aux = l->inicio;
        while (aux != NULL && !inserido) {
            if (aux->valor == novo->valor) {
                return 0;
            }

            if (aux->valor < novo->valor) {
                ant = aux;
                aux = aux->prox;
            } else {
                if (ant == NULL)
                    l->inicio = novo;
                else
                    ant->prox = novo;

                novo->prox = aux;
                inserido = 1;
            }
        }
        if (!inserido) {
            ant->prox = novo;
            inserido = 1;
        }
    }
    l->qtd++;
    return 1;
}

void mostrar_lista_dos_vertices(vertice *v, int tam) {
    int i;

    for (i = 0; i < tam; i++) {
        if (v[i].lista_adj != NULL) {
            printf("\n Lista de Adjacencias do no : %d", i);
            mostrar_lista(v[i].lista_adj);
        }
    }
}

void mostrar_lista(lista *l) {
    registro *aux;

    if (l == NULL) {
        printf("\n Lista nula");
        return;
    }

    if (l->inicio == NULL) {
        printf("\n Lista vazia");
        return;
    }

    aux = l->inicio;
    while (aux != NULL) {
        printf("\n -> %d", aux->valor);
        aux = aux->prox;
    }
}

void dfs(vertice *vertices, int x, int pai) {
    registro *aux;
    vertices[x].visitado = 1;
    vertices[x].in = count;
    vertices[x].lower = count;
    count++;

    if (vertices[x].lista_adj == NULL)
        return;

    aux = vertices[x].lista_adj->inicio;

    while (aux != NULL) {
        if (aux->valor != pai) {
            if (vertices[aux->valor].visitado == 1) {
                vertices[x].lower = min(vertices[x].lower, vertices[aux->valor].in);
            } else {
                dfs(vertices, aux->valor, x);

                if (vertices[aux->valor].lower > vertices[x].in) {
                    printf("\n PONTE entre %d e %d", x, aux->valor);
                }

                vertices[x].lower = min(vertices[x].lower, vertices[aux->valor].lower);
            }
        }
        aux = aux->prox;
    }
}

int min(int x, int y) {
    return x < y ? x : y;
}

int define_filho_esquerda(int indice) {
    return indice * 2;
}

int define_filho_direita(int indice) {
    return (indice * 2) + 1;
}

int define_pai(int indice) {
    return indice / 2;
}

void subir_minimo(int indice) {
    elemento aux;

    if (indice <= 1)
        return;

    int pai = define_pai(indice);

    if (heap[indice].distancia < heap[pai].distancia) {
        aux = heap[indice];
        heap[indice] = heap[pai];
        heap[pai] = aux;
        subir_minimo(pai);
    }
}

void desce_minimo(int indice) {
    if (indice * 2 > count_min_heap)
        return;

    int esquerda = define_filho_esquerda(indice);
    int direita = define_filho_direita(indice);

    int menor = indice;

    if (esquerda <= count_min_heap && heap[esquerda].distancia < heap[menor].distancia) {
        menor = esquerda;
    }

    if (direita <= count_min_heap && heap[direita].distancia < heap[menor].distancia) {
        menor = direita;
    }

    if (menor == indice)
        return;

    elemento aux;

    aux = heap[indice];
    heap[indice] = heap[menor];
    heap[menor] = aux;
    desce_minimo(menor);
}

int push_fila(elemento x) {
    count_min_heap++;
    heap[count_min_heap] = x;
    subir_minimo(count_min_heap);
}

elemento pop() {
    elemento retorno;
    if (count_min_heap == 0) {
        retorno.distancia = -1;
        retorno.vertice = -1;
        return retorno;
    }

    retorno = heap[1];
    heap[1] = heap[count_min_heap];
    count_min_heap--;
    desce_minimo(1);
    return retorno;
}

int empty() {
    if (count_min_heap == 0)
        return 1;
    else
        return 0;
}
