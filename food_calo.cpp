#include <iostream>
using namespace std;

int main() {

    int w[] = {0,800, 400, 300, 300, 300, 50, 20};
    int calo[] = {0,1501600, 1444000, 1122000, 690000, 237000, 130000, 117800};
    int dp[8][101] = {0};
    
    for(int i = 1; i <=7 ; i ++){
        for(int L = 1 ; L <= 100 ; L ++){
            if(L*10 > w[i]){
                for(int q = 1; L*10 - q*w[i] >=0 ; q++){
                    dp[i][L] = max(dp[i-1][L-q*w[i]/10] + q*calo[i] , dp[i-1][L]);
                }
            }else dp[i][L] = dp[i-1][L];
        }
    }
    cout << dp[7][100] << endl;

}