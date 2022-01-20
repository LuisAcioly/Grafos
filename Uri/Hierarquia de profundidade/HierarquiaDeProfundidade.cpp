// Grafos - Hierarquia De Profundidade (Exercício 1 da Lista Avaliativa REO1)

#include <iostream>
#include <list>
#include <stack> // Pilha auxiliar para usar na DFS

using namespace std;

class Grafo{
	int V; // Número de vértices
	list<int>* vertices; // Ponteiro para um array contendo as listas de adjancências
	
	public:
		Grafo(int V);
		~Grafo();
		void adicionarAresta(int v1, int v2); // Adiciona uma aresta no grafo
		void dfs(int v); // Faz uma DFS a partir de um vértice
};

Grafo::Grafo(int V){
	this -> V = V; // Atribui o número de vértices
	vertices = new list<int>[V]; // Cria as listas
}

Grafo::~Grafo(){
	for(int i = 0; i < V; i++)
		vertices[i].clear();
		
	delete[] vertices;
}

void Grafo::adicionarAresta(int v1, int v2){
	vertices[v1].push_back(v2); // Adiciona vértice v2 à lista de vértices adjacentes de v1
}

void Grafo::dfs(int v){
	stack<int> pilha;
	bool visitados[V]; // Vetor de visitados
	bool raiz = true;
	int profundidade = 1;
	
	// Marcar todos como não visitados
	for(int i = 0; i < V; i++)
		visitados[i] = false;
		
	while(true){
		if(!visitados[v]){
			visitados[v] = true; // Marca como visitado
			pilha.push(v); // Insere "v" na pilha
		}
		else{
			//cout << v << "-" << proximo vertice << endl;
		}
		
		bool found = false;
		list<int>::iterator it; // Vértice corrente, para iteração em lista
		
		// Busca por um vizinho não visitado
		for(it = vertices[v].begin(); it != vertices[v].end(); it++){
			if(!visitados[*it]){
				cout << v << "-" << *it << " pathR(G," << *it << ")" << endl;
				found = true;
				break;
			}
		}
		
		if(found){
			v = *it; // Atualize o 'v' com o vértice que se liga a v
			raiz = false;
		}
		else{
			// Se todos os vizinhos estão visitados ou não existem vizinhos
			// Remove da pilha
			pilha.pop();
			
			bool allFound = true;
			for(int i = 0; i < V; i++){
				if(!visitados[i])
					allFound = false;
			}
			
			if(!pilha.empty())
				v = pilha.top();
			else if(pilha.empty() && !allFound){
				for(int i = 0; i < V; i++){
					if(!visitados[i]){
						v = i;
						break;
					}
				}
			}
			else if(pilha.empty() && allFound){ 
				// Se a pilha ficar vazia, então terminou a busca
				cout << "Stack vazia!" << endl;
				break; 
			}
		}
	}
}

int main(){
	
	int N; // Quantidade de casos
	int V; // Quantidade de vértices
	int E; // Quantidade de arestas
	cin >> N;

	int v1, v2;
	for(int i = 0; i < N; i++){ // N casos
		cout << "Caso " << (i + 1) << ":" << endl;
		cin >> V >> E;
		Grafo grafo(V);
		for(int j = 0; j < E; j++){ // E arestas
			cin >> v1 >> v2;
			grafo.adicionarAresta(v1, v2);
		}
		
		grafo.dfs(0);
	}
	
	return 0;
}
