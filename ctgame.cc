#include <cstdio>
#include <algorithm>
using namespace std;
int grid[1000][1000][1000];
int solve(){
	int h,w;
	char c;
	int m=0;
	scanf("%d %d",&h,&w);
	for (int i=0;i<h;i++){
		for (int j=0;j<w;){
			
			for (int k=0;k<h;k++) grid[j][i][k]=0;
			scanf("%c",&c);
			if (c == 'R' || c=='F') {
				if (c == 'R'){
					grid[j][i][0]=0;
				}
				else {
					grid[j][i][0]=1;
					if (j>0 and i>0) {
						int k=0;
						while (grid[j][i-1][k]){
							grid[j][i][k]=grid[j-1][i][k]+1;
							k++;
						}
						grid[j][i][k]=grid[j-1][i][k]+1;
						m=max(m,(k+1)*grid[j][i][k]);
					}
				}
				j++;
			}
		}
	}
	return m;
}
int main(){
	int c;
	scanf("%d",&c);
	for (int i=0;i<c;i++) printf("%d\n",solve()*3);
	return 0;
}