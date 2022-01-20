/*
 * Disciplina : Algoritimo em Grafos
 * Professor : Mayron C. O. Moreira
 * Universidade Federal de Lavras
 * 
 * Problema Pais das Bicicletas , o objetivo do exercicio e determinar
 * entre o menor caminho de um ponto a outro , a altidude maxima encontrada 
 * 
 * Usado na resolucao do problema o algoritimo de dijkstra com algumas modificacoes
 * para se adaptar ao problema proposto
 * 
 * @author Walisson Mendes Ferreira 10A
 * @author Luis Wagner Acioly Bastos 10A
 * 
 * 
 * */

#include <iostream>
#include <vector>
#include <set>
#define INF 0x3f3f3f3f //Infinito representado no C++
using namespace std;
typedef vector<vector<pair<int, int> > > graph; // Lista de adjacencia do grafo


// Verifica se o custo e maior que o vertice de origem
//ele o maior valor encontrado entre vertice de U e o custo da aresta
int max (int a, int b){ 
  if (a == INF)
    return b;
  if (b == INF)
    return a;
  return a > b ? a : b;
}

int dijkstra (graph &g, int n, int x, int y){

  set<pair<int, int>> s; // Definindo set de par de elementos e chamando eles de S do grafo
  vector<int> vertice(n, INF); // Peso em cada vertice;
  
  
  vertice[x] = INF;
  s.insert(make_pair(0, x)); // adiciono o peso 0 no vertice inicial
 
  
  if (x == y) // caso seja 0 0
    return 0;
  
  while (!s.empty()){
    auto p = *s.begin(); // pego o par contendo o vertice inicial
    s.erase(s.begin()); //apago esse valor da lista 
    int u = p.second; // atribuo o segundo valor do meu primeiro par ,como o ponto de inicio,
	//porque o primeiro valor do par e o custo da aresta
    
    if (u == y) break; // verificacao para ver se o vertice que estou é o fim
    
    for (auto it : g[u]){ // loop que faz o calculo do menor caminho para todos os vertices adjacentes de U
      int v = it.second;// vertice que esta na lista de Adjacencia de U
      int cost = it.first;// custo da aresta de u -> v
      
      if (vertice[v] > max(vertice[u], cost)){ //verifica se o vertice Adjacente tem distancia maior
        vertice[v] = min(vertice[v], max(vertice[u], cost)); //verifica se a distancia de U a V e menor que a que esta
        //atribuido a ele , se for altera, do contrario mantem o mesmo valor
        s.insert(make_pair(vertice[v], v)); //adiciono a lista S , o custo e o vertice a qual foi explorado
      }
    }
  }
  
  return vertice[y]; //retorno o valor do vertice passado como destino da main
}
 


int main (){
  
  int instancia = 1;
  
  while (true){

    int n, m;
    cin >> n >> m;
    if (n == 0 and m == 0){
		 break;
	 }
    
    graph g(n); //Lista de adjacencia sendo feita usando par de valores
    
    //Parte da insercao de dados
    for (int i=0; i<m; i++){
      int a, b, c;
      cin >> a >> b >> c; // Valores digitados de vertice e peso
      a--;
      b--;
      
      g[a].push_back (make_pair (c, b)); // cria a lista de adjacencia
      g[b].push_back (make_pair (c, a));// adiciona na lista de ambos os vertices  
    }
    
   
    //Parte do Caminho
    cout << "Instancia " << instancia++ << endl;
    
    int k; // Numero de testes para um Grafo G
    cin >> k;
    for (int i=0; i<k; i++){
      int u, v;
      cin >> u >> v; // Inicio e fim
      cout << dijkstra(g, n, u-1, v-1) << endl;
    }
    cout << endl;
    
   
  }


  return 0;
}
