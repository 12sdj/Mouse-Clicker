#include <windows.h>
#include <iostream>
#include <conio.h>
#include <stdlib.h>
#include <time.h>
#include <cstdio>
using namespace std;

int main()
{
	int a;

	cout << "version:1.2(Update 02 2022.1.25) Made by 12sdj" << endl;

	cout << "���� �����ַ� �Կ�ʼ��Ĭ��CPS15)" << endl;

	cout << "��ע�⣺Ŀǰû���κ��趨�ķ�����ֹ������ر�" << endl;
	system("title ����������1.2");
	cout << "input: ";
	cin >> a;
	cout << "Beginning!" << endl;
	while (1) {
		
		for (int i = 1; i <= 50; i++) {
			mouse_event(MOUSEEVENTF_LEFTDOWN, 500, 500, 0, 0);
			mouse_event(MOUSEEVENTF_LEFTUP, 500, 500, 0, 0);
			Sleep(50);
		}
			
		
		

	}

}

