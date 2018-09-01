#include <iostream>
#include <vector>
#include <iomanip>
#include <math.h>
#include <stdio.h>
using namespace std;

double NPV(int t, vector<double> myvec, double irr)
{
    double sum=0;
    for (int i=0;i<=t;++i)
    {
        sum+=(myvec.at(i)/(pow((1+irr),i)));
    }
    return sum;
}

int main()
{
    int devides=0;
    vector <double> myvec;
    double result;
    int t;
    cin >> t;
        double ctf;
        myvec.clear();
        for (int i=0;i<=t;++i)
        {
            cin>>ctf;
            myvec.push_back(ctf);
        }
        double a= -1;
        double b= 2e32;
        while(a<=b && devides<1000000)
        {
            ++devides;
            double mid= (a+b)/2.0;
            result=NPV(t,myvec,mid);
                if (result>=-0.0001 && result <= 0.0001)
                {
                   printf("%.2f",mid);
                   return 0;
                }
                else if(result > 0.0001)
                {
                    a=mid;
                }
                else if(result<-0.0001)
                {
                    b=mid;
                }
        }
    return 0;
}
