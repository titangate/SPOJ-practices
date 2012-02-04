#include <cstdio>
const int MAX_DIGIT = 100000;
int main(){
	int c;
	int perm[MAX_DIGIT];
	scanf("%d",&c);
	while (c){
		
		bool amb=true;
		for (int i=0;i<c;i++) {
			scanf("%d",&perm[i]);
		}
		for (int i=0;i<c;i++) {
			if(perm[perm[i]-1]-1!=i){
				amb = false;
			}
		}
		if (amb) printf("ambiguous\n");
		else{printf("not ambiguous\n");}
		scanf("%d",&c);
	}
}