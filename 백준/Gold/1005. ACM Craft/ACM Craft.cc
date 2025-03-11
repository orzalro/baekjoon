#include <iostream>
#include <vector>

using namespace std;
int cal(int);
vector<vector<int>> v;
vector<int> D;
vector<int> R;

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, K, W, A = 0;
		cin >> N >> K;
		
		D.clear();
		D.resize(N);
		for (int j = 0; j < N; j++) {
			cin >> D[j];
		}

		v.clear();
		v.resize(N + 1);
		for (int j = 0; j < K; j++) {
			int x, y;
			cin >> x >> y;
			v[y].emplace_back(x);
		}
		
		cin >> W;
		R.clear();
		R.assign(N + 1, -1);
		A = cal(W);
		
		cout << A << endl;
	}
	
}

int cal(int W) {
	if (!v[W].empty()) {
		if (R[W] != -1) {
			return R[W];
		}
		if (v[W].front() == v[W].back()) {
			R[W]= D[W - 1] + cal(v[W].front());
			return R[W];
		}
		else {
			int i = 0;
			int MAX;
			MAX = cal(v[W].at(i));
			while (v[W].at(i) != v[W].back()) {
				i++;
				int j;
				j = cal(v[W].at(i));
				if (MAX < j) {
					MAX = j;
				}
			}
			R[W] = D[W - 1] + MAX;
			return R[W];
		}
	}
	else {
		return D[W - 1];
	}
}