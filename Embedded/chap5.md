# C++ basic
## Object & Encapsulation
### 캡슐화
* 객체(Object)를 싸서 그 내부를 보호하고 볼 수 없게 한다.
* 객체 내 데이터에 대한 보안, 보호, 접근 제한

## Object 구성
### 객체의 구성
* 상태(변수)와 행동(함수)로 구성

## Class & Object
### 클래스
* 객체를 만들어내기 위해 정의된 설계도, 틀
* 클래스는 객체가 아님. 실체도 아님
* 멤버 변수와 멤버 함수 선언
### 객체
* 객체는 생성될 때 클래스의 모양을 그대로 가지고 탄생
* 멤버 변수와 멤버 함수로 구성
* 메모리에 생성, 실체(instance)라고도 부름
* 하나의 클래스 틀에서 찍어낸 여러 개의 객체 생성 가능
* 객체들은 상호 별도의 공간에 생성

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/d5e4b092-02cd-479e-af9a-88ad674df464)

## 클래스 생성
### 클래스 작성
* 멤버 변수와 멤버 함수로 구성
* 클래스 선언부와 클래스 구현부로 구성

### 클래스 선언부(class declaration)
* class 키워드를 이용하여 클래스 선언
* 멤버 변수와 멤버 함수 선언
  * 멤버 변수는 클래스 선언 내에서 초기화할 수 없음
  * 멤버 함수는 원형(prototype)형태로 선언
* 멤버에 대한 접근 권한 지정
  * private, public, protected중의 하나
  * 디폴트는 private
  * public: 다른 모든 클래스나 객체에서 멤버의 접근이 가능함을 표시

### 클래스 구현부(class implementation)
* 클래스에 정의된 모든 멤버함수 구현

## Class/Object 생성
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/1512b29f-fed5-477f-9984-b8f5ba3545a6)

```c++
#include <iostream>
using namespace std;

class Circle{
  //Circle 선언부
  int radius;
  double getArea();
};
//Circle 구현부
double Circle::getArea(){
  return 3.14*radius*radius;
}

int main(){
  Circle donut;//객체 donut 생성
  donut.radius=1;//donut의 멤버변수 접근
  double area=donut.getArea();//donut의 멤버함수 호출
  cout<<"donut면적은"<<area<<endl;
  ...
}
```
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/bd9a9898-d00a-4b0c-b7ab-96ac6bcf6692)


## 생성자
### 생성자(constructor)
* 객체가 생성되는 시점에서 자동으로 호출되는 멤버 함수
* 클래스 이름과 동일한 멤버 함수

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/e959b0bd-5975-4b6d-9e56-cfac4fc07416)

* 생성자의 목적
  * 객체가 생성될 때 객체가 필요한 초기화를 위해
    * 멤버 변수 값 초기화, 메모리 할당, 파일 열기, 네트워크 연결 등
* 생성자 이름: 반드시 클래스 이름과 동일
* 생성자는 리턴 타입을 선언하지 않는다.: 리턴 타입 없음. void타입도 안됨
* 객체 생성 시 오직 한 번만 호출: 자동으로 호출됨. 임의로 호출할 수 없음. 각 객체마다 생성자 실행
* 생성자는 중복 가능
  * 생성자는 한 클래스 내에 여러개 가능
  * 중복된 생성자 중 하나만 실행
* 생성자가 선언되어 있지 않으면 기본 생성자 자동으로 생성
  * 기본 생성자-매개변수 없는 생성자
  * 컴파일러에 의해 자동 생성
## 생성자의 멤버 변수 초기화 방법
```c++
class Point{
  int x, y;
public:
  Point();
  Point(int a, int b);
};

//1. 생성자 코드에서 멤버 변수 초기화
Point::Point(){x=0; y=0;}
Point::Point(int a, int b){x=a; y=b}

//2. 생성자 서두에 초기값으로 초기화
Point::Point(): x(0), y(0){}//멤버 변수 x, y를 0으로 초기화
Point::Point(int a, int b): x(a), y(b)//멤버 변수 x=a로, y=b로 초기화. 콜론 이하 부분을 밑줄에 써도 됨

//3. 클래스 선언부에서 직접 초기화
class Point{
  int x=0, y=0;//클래스 선언부에서 x, y를 0으로 직접 초기화
public:...
};
```

## 소멸자
### 소멸자
* 객체가 소멸되는 시점에서 자동으로 호출되는 함수
  * 오직 한 번만 자동 호출, 임의로 호출할 수 없음
  * 객체 메모리 소멸 직전 호출됨
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/fd16d37e-5178-4672-ab0d-78e7fd0c83e0)
* 소멸자의 목적
  * 객체가 사라질 때 마무리 작업을 위함
  * 실행 도중 동적으로 할당받은 메모리 해제, 파일 저장 및 닫기, 네트워크 닫기 등
* 소멸자 함수의 이름은 클래스 이름 앞에 \~를 붙인다.
  * 예: Circle::~Circle(){...}
* 소멸자는 리턴 타입이 없고, 어떤 값도 리턴하면 안됨
  * 리턴 타입 선언 불가
* 중복 불가능
  * 소멸자는 한 클래스 내에 오직 한 개만 작성 가능
  * 소멸자는 매개변수 없는 함수
* 소멸자가 선언되어 있지 않으면 기본 소멸자가 자동 생성
  * 컴파일러에 의해 기본 소멸자 코드
  * 컴파일러가 생성한 기본 소멸자: 아무것도 하지 않고 단순 리턴
 
## 접근 지정자
### 캡술화의 목적
* 객체 보호, 보안
* C++에서 객체의 캡슐화 전략
  * 객체의 상태를 나타내는 데이터 멤버(멤버 변수)에 대한 보호
  * 중요한 멤버는 다른 클래스나 객체에서 접근할 수 없도록 보호
  * 외부와의 인터페이스를 위해서 일부 멤버는 외부에 접근 허용
 
### 멤버에 대한 3가지 접근 지정자
* private(디폴트 접근 지정)
  * 동일한 클래스의 멤버 함수에만 제한함
* public: 모든 다른 클래스에 허용
* proteted: 클래스 자신과 상속받은 자식 클래스에만 허용

```C++
#include<iostream>
using namespace std;

class Boat {
public:
	double fuel;
	void Move() {
		if (fuel > 0) {
			/*....*/
		}
	}

	void Fueling(double j) {
		fuel += j;
	}
};

int main() {
	Boat Jerry;

	Jerry.Fueling(100);
	Jerry.Move();

	Jerry.fuel += 100;//error!
	return 0;
}
```

## Call by value Vs Call by address
### 인자 전달 방식
* 값에 의한 호출, call by value
  * 함수가 호출되면 매개변수가 스택에 생성됨
  * 호출하는 코드에서 값을 넘겨줌
  * 호출하는 코드에서 넘어온 값이 매개변수에 복사됨
* 주소에 의한 호출, call by adress
  * 함수의 매개변수는 포인터 타입: 함수가 호출되면 포인터 타입의 매개 변수가 스택에 생성됨
  * 호출하는 코드에서는 명시적으로 주소를 넘겨줌
    * 기본 타입 변수나 객체의 경우, 주소 전달
    * 배열의 경우 배열의 이름
  * 호출하는 코드에서 넘어온 주소 값이 매개 변수에 저장됨
 
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/78987c8b-6322-4e2e-85ca-2daf83c7d877)
## call by value
```c++
#include<iostream>
using namespace std;

class Circle {
private:
	int radius;
public:
	Circle();
	Circle(int r);
	~Circle();
	double getArea() { return 3.14 * radius; };
	int getRadius() { return radius; };
	void setRadius(int radius) { this->radius = radius; };
};

Circle::Circle() {
	radius = 1;
	cout << "생성자 실행 radius= " << radius << endl;
}

Circle::Circle(int radius) {
	this->radius = radius;
	cout << "생성자 실행 radius= " << radius << endl;
}

Circle::~Circle() {
	cout << "소멸자 실행 radius= " << radius << endl;
}

void increase(Circle c) {
	int r = c.getRadius();
	c.setRadius(r + 1);
}

int main() {
	Circle waffle(30);
	increase(waffle);
	cout << waffle.getRadius() << endl;
}
```
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/99c4a2a9-85dd-4585-a0cb-12def19707cc)

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/13c408ab-cad4-4d6c-9b66-7fea7ef94b2c)

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/8f91e2af-5499-4c5a-8e42-fcc8038735f6)

## Reference
### 참조
* 참조란 가리킨다는 뜻으로 이미 존재하는 객체나 변수에 대한 별명
* 참조 활용
  * 참조 변수
  * 참조에 의한 호출
  * 참조 리턴
 
### 참조 변수 선언
* 참조자 &의 도입
* 이미 존재하는 변수에 대한 다른 이름(별명)을 선언
  * 참조 변수는 이름만 생기며
  * 참조 변수에 새로운 공간을 할당하지 않는다.
  * 초기화로 지정된 기존 변수를 공유한다.
```c++
int n=2;
int &refn=n;//참조 변수 refn 선언. refn은 n에 대한 별명

Circle cirlce;
Circle &refc=circle;//참조변수 refc 선언. refc는 circle에 대한 별명
```
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/a638d817-d6eb-4fd7-8fc8-6fc9d62077ab)

## 객체에 대한 참조
```c++
#include<iostream>
using namespace std;

class Circle {
	int radius;
public:
	Circle() { radius = 1; }
	Circle(int radius) { this->radius = radius; }
	void setRadius(int radius) { this->radius = radius; }
	double getArea() { return 3.14 * radius * radius; }
};

int main() {
	Circle circle;
	Circle& refc = circle;
	refc.setRadius(10);
	cout << refc.getArea() << " " << circle.getArea();
}
```

## Call by Reference
* 참조를 가장 많이 활용하는 사례
* call by reference라고 부름
* 함수 형식
  * 함수의 매개 변수를 참조 타입으로 선언
    * 참조 매개변수라고 부름
      * 참조 매개변수는 실인자 변수를 참조함
    * 참조매개변수의 이름만 생기고 공간이 생기지 않음
    * 참조 매개변수는 실인자 변수 공간 공유
    * 참조 매개변수에 대한 조작은 실인자 변수 조작 효과

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/1d45530c-6fc9-4dfc-b18a-085e466e8240)

## 참조에 의한 호출로 객체에 참조 전달
```c++
#include<iostream>
using namespace std;

class Circle {
private:
	int radius;
public:
	Circle();
	Circle(int r);
	~Circle();
	double getArea() { return 3.14 * radius * radius; }
	int getRadius() { return radius; }
	void setRadius(int radius) { this->radius = radius; }
};

Circle::Circle() {
	radius = 1;
	cout << "생성자 실행 radius= " << radius << endl;
}

Circle::Circle(int radius) {
	this->radius = radius;
	cout << "생성자 실행 radius= " << radius << endl;
}

Circle::~Circle() {
	cout << "소멸자 실행 radius= " << radius << endl;
}


void increaseCircle(Circle &c){
	int r = c.getRadius();
	c.setRadius(r + 1);
}


int main() {
	Circle waffle(30);
	increaseCircle(waffle);
	cout << waffle.getRadius() << endl;
}
```

## 참조 리턴
### C언어의 함수 리턴
* 함수는 반드시 값만 리턴
  * 기본 타입 값
  * 포인터 값
* C++의 함수 리턴
  * 함수는 값 외에 참조 리턴 가능
    * 변수 등과 같이 현존하는 공간에 대한 참조 리턴
      * 변수의 값을 리턴하는 것이 아님
     
## 값을 리턴 VS 참조를 리턴
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/67002ec7-0f86-41c0-bb02-9b80f444e16c)

## 참조 리턴 예
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/6242b83c-8154-4545-8491-d78448c530c6)

## 변환 연산자
```c++
#include<iostream>
using namespace std;

class Distance {
private:
	int kilometer, meter;

public:
	Distance() : kilometer(0), meter(0) {}
	Distance(int newDist) {
		kilometer = newDist / 1000;
		meter = newDist % 1000;
	}
	operator int() {
		return kilometer * 1000 + meter;
	}
	void PrintDistance() {
		cout << "Distance is " << kilometer << "km " << meter << "m/n";
	}
};

int main() {
	Distance d(2030);
	int nDist = d;
	cout << "Value is " << nDist << endl;

	return 0;
}
```
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/82625164-1b5f-4d3c-b329-271be72ad659)

## 변환 연산자
```c++
operator int(){
  return read();
}

int a=led1;
```

## 산술 연산자 재정의 Example
```c++
class Power{
  int kick;
  int punch;
public:
  this->kick=kick;
  this->punch=punch;
}
```

## + 연산자
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/dfdebc31-3ceb-4f9e-9f18-3fc98aeed01a)

```c++
#include<iostream>
using namespace std;

class Power {
	int kick;
	int punch;
public:
	Power(int kick = 0, int punch = 0) {
		this->kick = kick; this->punch = punch;
	}
	void show();
	Power operator+ (Power op2);
};

void Power::show() {
	cout << "kick=" << kick << ", " << "punch=" << punch << endl;
}

Power Power::operator+(Power op2) {
	Power tmp;
	tmp.kick = this->kick + op2.kick;
	tmp.punch = this->punch + op2.punch;
	return tmp;
}

int main() {
	Power a(3, 5), b(4, 6), c;
	c = a + b;
	a.show();
	b.show();
	c.show();
}
```

```c++
#define _CRT_SECURE_NO_WARNINGS
#include<string.h>
#include<iostream>
using namespace std;

class Employee {
public:
	int number;
	char* name;
	long pay;
	Employee();
	~Employee();
	Employee& operator=(Employee& obj);
};

Employee::Employee() {
	name = new char[80];
}

Employee::~Employee() {
	delete[] name;
}

Employee& Employee:: operator=(Employee& obj) {
	this->number = obj.number;
	this->pay = obj.pay;
	strcpy(this->name, obj.name);

	return *this;
}

int main() {
	Employee hansung_in, someone;

	hansung_in.number = 1234;
	strcpy(hansung_in.name, "송경주");
	hansung_in.pay = 24000000;

	someone = hansung_in;

	cout << "someone: " << someone.name << "\n";

	strcpy(someone.name, "김나연");
	cout << "someone: " << someone.name << "\n";

	cout << "hansung_in: " << hansung_in.name << "\n";

	return 0;
}
```
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/c515186b-2a04-49d7-80fe-adeff32916a2)

## Template
### 템플릿
* 함수나 클래스를 일반화하는 C++ 도구
* template 키워드로 함수나 클래스 선언
  * 변수나 매개변수의 타입만 다르고, 코드 부분이 동일한 함수를 일반화시킴
* 제네릭 타입-일반화를 위한 데이터 타입

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/42f046c6-bb05-43b5-a1f3-82d549227c9e)

## Template Example
```c++
#include<iostream>
using namespace std;

class Circle {
	int radius;
public:
	Circle(int radius = 1) { this->radius = radius; }
	int getRadius() { return radius; }
};

template <class T>
void myswap(T& a, T& b) {
	T tmp;
	tmp = a;
	a = b;
	b = tmp;
}

int main() {
	int a = 4, b = 5;
	myswap(a, b);
	cout << "a=" << a <<", "<< "b=" << b << endl;

	double c = 0.3, d = 12.5;
	myswap(c, d);
	cout << "c=" << c << ", " << "d=" << d << endl;

	Circle donut(5), pizza(20);
	myswap(donut, pizza);
	cout << "donut 반지름: " << donut.getRadius() << ", ";
	cout << "pizza 반지름: " << pizza.getRadius() << endl;
}
```
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/c21c8818-1d58-4188-a079-f1ae5fd39ad7)

## class Template을 사용한 Stack 구현
```c++
#include<iostream>
using namespace std;

template <class T>
class MyStack {
	int tos;
	T data[100];
public:
	MyStack();
	void push(T element);
	T pop();
};

template <class T>
MyStack<T>::MyStack() {
	tos = -1;
}

template<class T>
void MyStack<T>::push(T element) {
	if (tos == 99) {
		cout << "stack full";
		return;
	}
	tos++;
	data[tos] = element;
}

template <class T>
T MyStack<T>::pop() {
	T retData;
	if (tos == -1) {
		cout << "stack empty";
		return 0;
	}
	retData = data[tos--];
	return retData;
}

int main() {
	MyStack<int> iStack;
	iStack.push(3);
	cout << iStack.pop() << endl;

	MyStack<double> dStack;
	dStack.push(3.5);
	cout << dStack.pop() << endl;

	MyStack<char>* p = new MyStack<char>();
	p->push('a');
	cout << p->pop() << endl;
	delete p;
}
```
