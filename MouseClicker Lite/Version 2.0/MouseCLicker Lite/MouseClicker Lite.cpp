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
	long c;
	long long b; 
	system("title MouseClicker LITE V2");
	cout << "Version 2.0(Lite) Made by 12sdj" << endl;
	cout << endl;
	
	cout << "���и�������:" << endl;
	cout << "1.0(2022.5.2)" << endl;
	cout << "2.0(2022.5.8)" << endl;
	
	cout << "-------------------------" << endl;
	cout << "˵����" << endl;
	cout << "�ð汾Ϊ�й���½�������ع��汾���������ĺ��ײ�����" << endl;
	cout << endl;
	cout << "�ð汾�����У�" << endl;
	cout << "1.ԭ���������" << endl;
	cout << "2.���ȥ���ֹ���" << endl;
	cout << "3.�����ܵ����ߵ�����" << endl;
	cout << "-------------------------" << endl;
	cout << "�ð汾���п�Դ��Ŀ��Э��" << endl;
	cout << "��Ŀ��ַ:https://github.com/12sdj/MouseClicker-by-12sdj" << endl;
	cout << "MIT License: Copyright (c) 2022 12sdj" << endl;
	cout << "������ʹ�����������ҵ��;���޸ġ����䡢˽��ʹ��" << endl;
	cout << endl;
	
	cout << "<4������������>" << endl;
	Sleep(3950);
	system("cls");

	system("color 03");

	cout << "�����Զ���CPS: ";
	cin >> b;
	cout << endl;
	c = 1000/b;
	system("cls");
	cout << "<�ѽ����������ݣ���ȴ�>" << endl;
	Sleep(2000);
	system("cls");
	cout << "<��������>" << endl;
	cout << "CPS:" << b << endl;
	

	while (1) {
		mouse_event(MOUSEEVENTF_LEFTDOWN, 500, 500, 0, 0);
		mouse_event(MOUSEEVENTF_LEFTUP, 500, 500, 0, 0);
		Sleep(c); 
		}
	}

