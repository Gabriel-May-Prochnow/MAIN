#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

//Gabriel May Prochnow -2122082032


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


typedef struct {
    int x, y, w;
} Aresta;


void djkstra(int grafo[100 + 1][100 + 1], int distancia[100 + 1], int N);
const char* rabito(int N, int M, Aresta arestas[2000], int K, int P, int pos[2000]);
int menor(const void *a, const void *b);
///?///////////////////////////////////////////

int main() {

    int valor;
    scanf("%d", &valor);

    for (int t = 0; t < valor; t++) {
        
        int N, M;
        scanf("%d %d", &N, &M);

        Aresta arestas[2000];
        for (int i = 0; i < M; i++) {
            scanf("%d %d %d", &arestas[i].x, &arestas[i].y, &arestas[i].w);
        }

        int K, P;
        scanf("%d %d", &K, &P);

        int pos[2000];
        for (int i = 0; i < K; i++) {
            scanf("%d", &pos[i]);
        }

        const char* resultado = rabito(N, M, arestas, K, P, pos);
        printf("%s\n", resultado);

    }

    return 0;
}

///////////////////////////////////////////////
void djkstra(int grafo[100 + 1][100 + 1], int distancia[100 + 1], int N) {

    int visitado[100 + 1] = {0};

    for (int i = 1; i <= N; i++) {

        distancia[i] = INT_MAX;

    }

    distancia[1] = 0;

    for (int j = 0; j < N - 1; j++) {
        int minDistance = INT_MAX, index;

        for (int y = 1; y <= N; y++) {

            if (!visitado[y] && distancia[y] <= minDistance) {

                minDistance = distancia[y];
                index = y;

            }

        }

        visitado[index] = 1;

        for (int y = 1; y <= N; y++) {

            if (!visitado[y] && grafo[index][y] && distancia[index] != INT_MAX && distancia[index] + grafo[index][y] < distancia[y]) {

                distancia[y] = distancia[index] + grafo[index][y];

            }
            
        }
    }
}

const char* rabito(int N, int M, Aresta arestas[2000], int K, int P, int pos[2000]) {

    int grafo[100 + 1][100 + 1] = {{0}};

    for (int i = 0; i < M; i++) {

        grafo[arestas[i].x][arestas[i].y] = arestas[i].w;
        grafo[arestas[i].y][arestas[i].x] = arestas[i].w;

    }

    int distancia[100 + 1];
    djkstra(grafo, distancia, N);

    
    qsort(pos, K, sizeof(int), menor);

    for (int i = 0; i < K; i += P) {

        int osso[P];
        for (int j = 0; j < P && i + j < K; j++) {

            osso[j] = pos[i + j];

        }

        for (int j = 0; j < P && i + j < K; j++) {

            if (distancia[osso[j]] <= P + j) {
                return "yes";
            }

        }
    }

    return "No";
}

int menor(const void *a, const void *b) {

    return (*(int *)a - *(int *)b);

}
