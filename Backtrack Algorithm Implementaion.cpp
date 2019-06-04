#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
using namespace std;

class node
{
public:
    vector<int> leftlist;
    vector<int> rightlist;
    node* left;
    node* right;
    vector <int> jump;
    int id;
};



int sum(vector <int> alist)
{
    int FirstSum = 0;
    for(auto i : alist)
    {
        FirstSum += i;
    }
    return FirstSum;
};

vector <int> MyInitialList(4);
float mean;
vector <node*> leaves;
int counter = 1;
void MyMain(node* base)
{
    ++counter;
    cout<<"Left node number: "<<counter<<endl;
    node *left = new node;
    left->id = counter;
    int i;
    int j;
    int sth;
    for (j=0; j<base->rightlist.size(); ++j)
    {
        sth = base->rightlist.at(j);
        cout<<" checking for what to pick up: " << sth<< endl;
        for (i=0; i<base->jump.size(); ++i)
        {
            if (sth == base->jump.at(i))
            {
                break;
            }
        }
        if (i ==base->jump.size())
        {
            cout<<"picked up: "<< sth<<endl;
            break;
        }
    }
    left->jump.push_back(sth);
    left->jump.insert(left->jump.end(), base->jump.begin(), base->jump.end());
    left->leftlist.push_back(sth);
    left->leftlist.insert(left->leftlist.end(), base->leftlist.begin(), base->leftlist.end());
    base->jump.push_back(sth);
    left->rightlist = base->rightlist;
    vector<int>::iterator position = std::find(left->rightlist.begin(), left->rightlist.end(), sth);
    left->rightlist.erase(position);
    base->left = left;
    if (sum(left->leftlist) < mean && left->jump.size() != MyInitialList.size())
    {
        MyMain(left);
    }
    else
    {
        leaves.push_back(left);
    }
    node *right = new node;
    ++counter;
    right->id = counter;
    cout<<"Right node number: "<<counter<<endl;
    right->leftlist = base->leftlist;
    right->rightlist = base->rightlist;
    right->jump = base->jump;
    base->right = right;
    cout<<" jump size: "<<right->jump.size()<<endl;
    cout<<"jump list: ";
    for (int m =0; m<right->jump.size();++m)
    {
        cout<<right->jump.at(m)<<"  ";
    }
    cout<<endl;
    cout<<"Base jump list: ";
    for (int m =0; m<base->jump.size();++m)
    {
        cout<<base->jump.at(m)<<"  ";
    }
    cout<<endl;
    if (right->jump.size() != MyInitialList.size())
    {
        MyMain(right);
    }
}


int main()
{
    MyInitialList.at(0) = 10;
    MyInitialList.at(1) = 20;
    MyInitialList.at(2) = 30;
    MyInitialList.at(3) = 40;

    mean = sum(MyInitialList)/2;
    cout<<"mean"<<mean<<endl;
    node* base = new node;
    base->rightlist = MyInitialList;
    base->id = 1;
    MyMain(base);
    cout<<leaves.size()<<endl;
    vector<pair<int, node*>> FinalAnswer;
    for (int y  =0; y<leaves.size(); ++y)
    {
        pair<int, node*> leaf;
        leaf = make_pair(abs(sum(leaves.at(y)->leftlist) - sum(leaves.at(y)->rightlist)),leaves.at(y));
        FinalAnswer.push_back(leaf);
    }
    sort(FinalAnswer.begin(), FinalAnswer.end());
    for (int y  =0; y<leaves.size(); ++y)
    {
        cout<<"***item number "<<y<<"***"<<endl;
        cout<<"Objective Value: "<< FinalAnswer.at(y).first <<endl;
    }

    for (int u =0; u<3; ++u)
    {
        node* temp = new node;
        temp =FinalAnswer.at(u).second;
        cout<<"item num: "<< u<<endl<< "  leftlist: ";
        for (int o=0; o<temp->leftlist.size(); ++o)
        {
            cout<<temp->leftlist.at(o)<< "  ";
        }
        cout<<endl;
        cout<<" rightlist: ";
        for (int o=0; o<temp->rightlist.size(); ++o)
        {
            cout<<temp->rightlist.at(o)<< "  ";
        }
        cout<<endl;
    }
    return 0;
}
