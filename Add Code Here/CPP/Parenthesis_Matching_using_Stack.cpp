#include <iostream>
#include<cstring>
using namespace std;

class Node {
public:
    char data;
    Node* next;
};

class Stack {
private:
    Node* top;
public:
    Stack();
    ~Stack();
    void push(char x);
    char pop();
    char peek(int index);
    int isEmpty();
    int isFull();
    char stackTop();
};

Stack::Stack() {
    top = NULL;
}

Stack::~Stack() {
    Node* p = top;
    while (top) {
        top = top->next;
        delete p;
        p = top;
    }
}

void Stack::push(char x) {
    Node* t = new Node;
    if (t == nullptr) {
        cout << "Stack Overflow!" << endl;
    }
    else {
        t->data = x;
        t->next = top;
        top = t;
    }
}

char Stack::pop() {
    Node* p;
    char x = -1;
    if (top == nullptr) {
        cout << "Stack Underflow!" << endl;
    }
    else {
        p = top;
        x = p->data;
        top = top->next;
        delete p;
    }
    return x;
}

int Stack::isFull() {
    Node* t = new Node;
    int r = t ? 1 : 0;
    delete t;
    return r;
}

int Stack::isEmpty() {
    return top ? 0 : 1;
}

char Stack::stackTop() {
    if (top) {
        return top->data;
    }
    return -1;
}

char Stack::peek(int index) {
    if (isEmpty()) {
        return -1;
    }
    else {
        Node* p = top;

        for (int i = 0; p != nullptr && i < index - 1; i++) {
            p = p->next;
        }

        if (p != nullptr) {
            return p->data;
        }
        else {
            return -1;
        }
    }
}

bool isBalanced(char* exp) {
    Stack st;

    for (int i = 0; i < strlen(exp); i++) {
        char ch = exp[i];
        if (ch == '(' || ch == '[' || ch == '{') {
            st.push(ch);
        }
        else {
            if (st.isEmpty()) {
                return false;
            }
            char top = st.stackTop();
            if ((ch == ')' && top == '(') ||
                (ch == ']' && top == '[') ||
                (ch == '}' && top == '{')) {
                st.pop();
            }
            else {
                return false;
            }
        }
    }
    return st.isEmpty();
}


int main() {

    char E[] = "([]{(a+b)*(c-d)})";
    cout << isBalanced(E) << endl;

    char F[] = "((a+b)*(c-d)))";
    cout << isBalanced(F) << endl;

    char G[] = "(((a+b)*(c-d))";
    cout << isBalanced(G) << endl;

    return 0;

}
 
