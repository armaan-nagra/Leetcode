class Solution {
public:
    int getSum(int a, int b) {
        while (b != 0){
            int noCarry = a ^ b;
            int carry = (a & b) << 1;
            a = noCarry;
            b = carry;
        }
        return a;
    }
};