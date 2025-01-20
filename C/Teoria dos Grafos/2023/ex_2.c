#include <stdio.h>
#include <stdlib.h>

typedef struct vertice{
    int visitado;
    int distancia;
    struct lista *lista_adj;
}vertice;

typedef struct fila{
    int tam;
    struct registro *inicio;
    struct registro *fim;
}fila;

typedef struct lista{
    int qtd;
    struct registro *inicio;
}lista;

typedef struct registro{
    int valor;
    struct registro *proximo;
}registro;

int bfs(vertice *v, int raiz, int qtd_vertices);
fila *aloca_Fila();
lista *aloca_Lista();
registro *aloca_Registro();
int incluir_lista(lista *l, int x);
void push(vertice *v, int valor);
void push_FilaBFS(fila *f, int x);
int pop_FilaBFS(fila *f);

int main(){
    
    int qtd_vertices;
    int qtd_arestas;
    int i;
    int a,b;
    int qtd_casos=0;
    vertice *vertices;

    scanf("%d", &qtd_casos);

    while(qtd_casos--){
        scanf("%d %d", &qtd_vertices, &qtd_arestas);
        vertices= (vertice *)calloc(10001, sizeof(vertice));

        for(i=0; i< qtd_arestas; i++){
            scanf("%d %d", &a, &b);
            push(&vertices[a], b);
            push(&vertices[b], a);
        }

        printf("%d \n" , bfs(vertices, 1, qtd_vertices));
    }
    return 0;
}

fila *aloca_Fila(){
    fila *novo;
    novo = (fila *)calloc(1, sizeof(fila));
    return novo;
}

lista *aloca_Lista(){
    lista *novo;
    novo = (lista *)calloc(1, sizeof(lista));
    return novo;
}

registro *aloca_Registro(){
    registro *novo;
    novo = (registro *)calloc(1,sizeof(registro));
    return novo;
}

int incluir_lista(lista *l, int x){

    registro *novo= aloca_Registro();
    novo->valor= x;
    novo->proximo=NULL;

    if(l->inicio==NULL){
        l->inicio=novo;
        l->qtd++;
        return 0;
    }

    registro *aux= l->inicio;

    while(aux->proximo!= NULL){
        aux= aux->proximo;
    }

    aux->proximo=novo;
    l->qtd++;
    return 1;
}

void push(vertice *v, int valor){

    if(v->lista_adj==NULL){
        v->lista_adj= aloca_Lista();
    }
    incluir_lista(v->lista_adj, valor);
}

int pop_FilaBFS(fila *f){

    int aux;
    aux= f->inicio->valor;
    f->inicio=f->inicio->proximo;
    f->tam--;

    return aux;
}

void push_FilaBFS(fila *f, int x){

    registro *novo= aloca_Registro();
    novo->valor= x;

    if(f->inicio==NULL){

        f->inicio=novo;
        f->fim=novo;
        f->tam++;
        return;
    }

    f->fim->proximo= novo;
    f->fim= novo;
    f->tam++;

}


int bfs(vertice *v, int raiz, int qtd_vertices){

    fila *f= aloca_Fila();

    int atual;
    registro *aux;

    for(int i=0; i<qtd_vertices; i++){
        v[i].visitado =0;
        v[i].distancia=-1;
    }

    push_FilaBFS(f, raiz);
    v[raiz].visitado=1;
    v[raiz].distancia=0;

    while(f->tam>0){

        atual= pop_FilaBFS(f);
        aux= v[atual].lista_adj->inicio;

        while(aux!= NULL){
            if(v[aux->valor].visitado==0){
                v[aux->valor].visitado=1;
                push_FilaBFS(f,aux->valor);
                v[aux->valor].distancia= v[atual].distancia + 1;
            }
            aux=aux->proximo;
        }

    }
    return v[qtd_vertices].distancia;
}
