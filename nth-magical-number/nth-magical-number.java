class Solution {
    public int nthMagicalNumber(int n, int a, int b) {
        int mod=(int)1e9+7;
        long l=1,r=(long)1e18;
        while(l<r){
            long mid=l+((r-l)>>1);
            long count=mid/a+mid/b-mid/minMul(a,b);
            if(count>n){r=mid-1;}
            else if(count<n){l=mid+1;}
            else{r=mid;}
        }
        return (int)(l%mod);
    }
    public int minMul(int a,int b){
        if(a>=b){
            int d=a*b;
            while(a%b>0){
                int c=a%b;
                a=b;
                b=c;
            }
            return d/b;
        }
        return minMul(b,a);
    }
}