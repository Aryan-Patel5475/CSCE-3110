// Name:		 Aryan Patel
// EUID:      asp0144
// email:     aryanpatel@my.unt.edu
// Professor: Dr Heng Fan
// Date:      12/09/22

#include <iostream>
#include <map>
#include <vector>
#include <list>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

class Graph {
	
	int V;
	vector<list<int> > adj;
	
public:
	Graph(int V);
	void addEdge1(int v, int w);
	void addEdge2(int v, int w);
	void BFS(int s);
	void DFS(int s);
	
	map <int, bool> visited;
	map <int, list<int>> adj2;
};

Graph::Graph(int V) {
	this->V = V;
	adj.resize(V);
}

void Graph::addEdge1(int v, int w) {
	adj[v].push_back(w);
}

void Graph::addEdge2(int v, int w) {
	adj[v].push_back(w);
}

void Graph::BFS(int s) {
	
	vector<bool> visited;
	visited.resize(V, false);
	
	list <int> queue;
	
	visited[s] = true;
	queue.push_back(s);
	
	while (!queue.empty()) {
		s = queue.front();
		cout << s << " ";
		queue.pop_front();
		
		for (auto adjacent:adj[s]) {
			if (!visited[adjacent]) {
				visited[adjacent] = true;
				queue.push_back(adjacent);
			}
		}
	}
}

void Graph::DFS(int s) {
	
	visited[s] = true;
	cout << s << " ";
	
	list <int>::iterator i;
	
	for (i = adj[s].begin(); i != adj[s].end(); ++i) {
		if (!visited[*i]) {
			DFS(*i);
		}
	}
}

int main() {
	
	ifstream file;
	int count = 0;
	file.open("input.txt");
	
	if (file.is_open()) {
		string a;
		while (!file.eof()) {
			getline(file, a);
			count++;
		}
	}
	file.close();
	Graph g(count+1);
	
	file.open("input.txt");
	
	if(file.is_open()) {
		
		int v;
		int w;
		string line;
		while(!file.eof()) {
			getline(file,line);
			stringstream ss(line);
			ss >> v;
			
			while (ss >> w) {
				g.addEdge1(v, w);
				g.addEdge2(v, w);
			}
		}
	}
	
	else {
		cout << "Cannot open file\n";
		return(1);
	}
	
	file.close();
	
	int num;
	
	cout << "Enter a number you want to start breadth first search: ";
	cin >> num;
	
	cout << "BFS: ";
	g.BFS(num);
	cout << endl;
	
	cout << "DFS: ";
	g.DFS(num);
	cout << endl;
	
	return 0;
}
