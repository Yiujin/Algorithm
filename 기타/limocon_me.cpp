#include <iostream>
using namespace std;
int n, m;
int tmp;
int check = 0;

void f(int x) {
	if (x == 0) return;

	if (x >= 10) {
		check++;
		f(x-10);
	}
	else {
		if (x >= 5) {
			check++;
			f(x - 5);
		}
		else
		{
			check++;
			f(x - 1);
		}
	}
}

int main()
{
	cin >> n >> m;
	int tmp = abs(m - n);
	f(tmp);
	cout << check << endl;
	return 0;
}