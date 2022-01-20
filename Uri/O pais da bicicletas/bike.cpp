#include <iostream>
#include <list>

using namespace std;

class aresta{
    friend class vertice;
    private:
       vertice* vDestino;
       int peso;
    public:
        aresta(vertice v,int num);
        int getPeso();
};

aresta::aresta(vertice v, int num){
    vDestino = &v;
    peso = num;
}

int aresta::getPeso(){
    return peso;
}

class vertice{
    friend class aresta;
    private:
        int valor;
        list<aresta> vizinhos;
        bool visitado;
    public:
        vertice(int num);
        void addVizinho(aresta V);
        void setTrue();
};

vertice::vertice(int num){
    valor = num;
    visitado = false;
}

void vertice::addVizinho(aresta V){
    vizinhos.push_front(V);
}

int main (){


    return 0;
}