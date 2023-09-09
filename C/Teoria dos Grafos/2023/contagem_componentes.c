#include <stdio.h>
#include <stdlib.h>

int qtd_global[10001];

typedef struct vertice
{
    int visitado;
    struct lista *lista_adj;
} vertice;

typedef struct lista
{
    int qtd;
    struct registro *inicio;
} lista;

typedef struct registro
{
    int valor;
    struct registro *prox;
} registro;

void mostrar_lista(lista *l);
int incluir_ordenado_lista(lista *l, int x);
registro *aloca_registro();
lista *aloca_lista();
int carrega_grafo(vertice *vertices, char *nome_do_arquivo);
void push(vertice *v, int x);
void mostrar_lista_dos_vertices(vertice *v, int tam);
void dfs(vertice * vertices , int x);

int main(int *argc, char *argv[])
{
    int cc=0;
    vertice *vertices;
    int qtd_vertices, qtd_arestas;

    //printf(" Parametro recebido: %s", argv[1]); //argv[1] é o nome do arquivo que vai ser lido (parada estranha que o professor fez)

    vertices = (vertice *)calloc(10000, sizeof(vertice));

    printf("\nDigite a quantidade de Vertices e Arestas:\n");
    scanf("%d %d", &qtd_vertices, &qtd_arestas);


    for(int i=1;i<=qtd_arestas;i++)
    {
        int a, b;
        printf("\n A: %d B: %d", a, b);

        push(&vertices[a], b);
        push(&vertices[b], a);
        
    }

    for(int i=1;i<=qtd_vertices;i++)
    {
        if (vertices[i].visitado ==0)
        {
            cc++;
            
            dfs(vertices,i);
        }
    }


    printf("\n Quantidade de Componentes Conectados: %d",cc);

    // printf("\n Chamando DFS: "); // (aqui ele tirou a chamada do DFS, se descomentar vai fazer a mesma coisa que dfs)
    // dfs(vertices,1);

    printf("\n");
    return 0;
}

void push(vertice *v, int x)
{
    if (v->lista_adj == NULL){
        v->lista_adj = aloca_lista();
    }
    incluir_ordenado_lista(v->lista_adj, x);
}

lista *aloca_lista()
{
    lista *novo;
    novo = (lista *)calloc(1, sizeof(lista));
    return novo;
}

registro *aloca_registro()
{
    registro *novo;
    novo = (registro *)calloc(1, sizeof(registro));
    return novo;
}

int incluir_ordenado_lista(lista *l, int x)
{
    if (l == NULL)
        return 0;

    registro *novo, *aux = NULL, *ant = NULL;
    novo = aloca_registro();
    novo->valor = x;

    if (l->inicio == NULL)
    {
        l->inicio = novo;
    }
    else
    {
        int inserido = 0;
        aux = l->inicio;
        while (aux != NULL && !inserido)
        {

            if (aux->valor == novo->valor)
            {
                return 0;
            }

            if (aux->valor < novo->valor)
            {
                ant = aux;
                aux = aux->prox;
            }
            else
            {
                if (ant == NULL)
                    l->inicio = novo;
                else
                    ant->prox = novo;

                novo->prox = aux;
                inserido = 1;
            }
        }
        if (!inserido)
        {
            ant->prox = novo;
            inserido = 1;
        }
    }
    l->qtd++;
    return 1;
}

void mostrar_lista_dos_vertices(vertice *v, int tam)
{
    int i;

    for (i = 0; i < tam; i++)
    {
        if (v[i].lista_adj != NULL)
        {
            printf("\n Lista de Adjacencias do no : %d", i);
            mostrar_lista(v[i].lista_adj);
        }
    }
}

void mostrar_lista(lista *l)
{
    registro *aux;

    if (l == NULL)
    {
        printf("\n Lista nula");
        return;
    }

    if (l->inicio == NULL)
    {
        printf("\n Lista vazia");
        return;
    }

    aux = l->inicio;
    while (aux != NULL)
    {
        printf("\n -> %d", aux->valor);
        aux = aux->prox;
    }
}


void dfs(vertice * vertices , int x)
{
    registro * aux;
    vertices[x].visitado=1;
    printf(" %d",x);

    if (vertices[x].lista_adj==NULL)
        return;
        
    aux = vertices[x].lista_adj->inicio;

    while(aux!=NULL)
    {
        if (vertices[aux->valor].visitado==0)
        {
            dfs(vertices,aux->valor); 
        }
        aux = aux->prox;
    }

}