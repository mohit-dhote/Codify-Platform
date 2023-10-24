#include <iostream>
using namespace std;

class Queue
{
private:
    int size;
    int front;
    int rear;
    int* Q;

public:
    Queue() { front = rear = -1; size = 10; Q = new int[size]; }
    Queue(int size) { front = rear = -1; this->size = size; Q = new int[this->size]; }
    
    void enque(int x);
    int deque();
    void display();
};

void Queue::enque(int x)
{
    if (rear == size - 1)
        cout << "Queue full.";
    else
    {
        rear++;
        Q[rear] = x;
    }
}

int Queue::deque()
{
    int x = -1;
    if (front == rear)
    {
        cout << "Queue is empty"; 
    }

    else
    {
        x = Q[front + 1];
        front++;
    }

    return x;
}   


void Queue::display()
{
    for (int i = front + 1;i <= rear;i++)
        cout << Q[i] << " ";
}



int main()
{
    std::cout << "Queue using class!\n";
    Queue q(5);
    q.enque(10);
    q.enque(6);
    q.enque(9);

    q.display();

    return 0;
}
