
class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        vector<long long> answer(200005);
        set<int> res ;
        for(int i =0; i< 10 ; i++){
            res.insert(i);
        }
        long long modular  = 1000000007;
        answer[0] = 1;
        for(int i = 0; i < 100005; i++){
            answer[i + zero] %= modular;
            answer[i + zero] += answer[i];
             answer[i + one] %= modular;
           answer[i + one] += answer[i];
        }
        long long sums = 0;
        for(int i = low; i <= high; i++){
            sums = (sums + answer[i])%modular;
        }
        return sums;
    }
};
