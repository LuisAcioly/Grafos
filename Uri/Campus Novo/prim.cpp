#include <iostream>
#define INFINITO 1000000
using namespace std;

int MinimoPrim(int *grafo , int nVertices, int origem , bool *passou){
	int minimo = INFINITO;
    int vertice = 0;
    
    for (int i = 0; i < nVertices; i++){
		if(grafo[i] < minimo and passou[i] == false){
            minimo = grafo[i];
            vertice = i;
		}
	}
    return vertice;
}

int main(){
	
	int nArestas , nVertices;
	
	cin >> nVertices >> nArestas;
	int grafo[nVertices][nVertices];
	bool passou[nVertices];
	
	for (int i = 0; i < nVertices; i++){
		passou[i] = false;
	}
	
	
	for (int i = 0; i < nVertices; i++){
		for (int d = 0; d < nVertices; d++)
		{
			 grafo[i][d] = INFINITO;
		}

	}
	
	int a , b,c;
    for (int i = 0; i < nArestas; i++){
		cin >> a >> b >> c;
		grafo[a-1][b-1] = c;
		grafo[b-1][a-1] = c;
		}
	
	int origem = 0;
	int aux_passou=0;
	
	passou[origem] = true;
	int soma = 0;
    int nmr_vertices = nVertices;

    while(nmr_vertices !=0){
        int u = MinimoPrim(grafo[origem],nVertices,origem,passou);
        if (passou[u] == false){ 
            passou[u] = true;
            aux_passou +=1;
            soma += grafo[origem][u];
		}
        origem = u;
        nmr_vertices = nmr_vertices - 1;
	}

		if(aux_passou == nVertices-1){
			cout << soma << endl;
		}else {
			cout << "impossivel" << endl;
		}

   return 0;
}
