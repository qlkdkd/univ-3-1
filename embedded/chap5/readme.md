# C++ Basic

## Why c++
* Mbed OS는 C++ 기반의 소프트웨어 플랫폼과 ARM Cortex-M 펌웨어를 쉽게 프로그램할 수 있는 개발 툴을 포함
* 표준 C++기반의 Mbed 라이브러리를 활용하여 프로그램 진행 가능

### Object&Encapsulation
* 캡슐화
  * 객체(Object)를 싸서 그 내부를 보호하고 볼 수 없게 한다.
  * 객체 내 데이터에 대한 보안, 보호, 접근 제한
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/035a382d-d002-4301-8ffc-adcbc40ce517)

### Object 구성
* 객체의 구성: 상태(변수)와 행동(함수)로 구성
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/02ded1c0-55e3-442e-a84c-8f623d2d9ff0)

### Class & Object
* 클래스(Class)
  * 객체를 만들어내기 위해 정의된 설계도, 틀
  *  멤버 변수와 멤버 함수 선언
* 객체(Object)
  * 객체는 생성될 때 클래스의 모양을 그대로 가지고 탄생
  * 멤버 변수와 멤버 함수로 구성
  * 메모리에 생성, 실체(instance)라고도 부름
  * 하나의 클래스 틀에서 찍어낸 여러 개의 객체 생성 가능
  * 객체들은 상호 별도의 공간에 생성
 
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/6db9d98a-e30a-4dac-b1c7-19386b7024ee)

### Class 생성
* 클래스 작성
  * 멤버 변수와 멤버 함수로 구성
  * 클래스 선언부와 클래스 구현부로 구성
* 클래스 선언부(class declaration)
  * class 키워드를 이용하여 클래스 선언
    * 멤버 변수와 멤버 함수 선언
    * 멤버 변수는 클래스 선언 내에서 초기화할 수 없음
    * 멤버 함수는 원형(prototype) 형태로 선언
  * 멤버에대한 접근 권한 지정
    * private public, protected 중의 하나
    * 디폴트는 private
    * public: 다른 모든 클래스나 객체에서 멤버의 접근이 가능함을 표시
  * 클래스 구현부(class implementation)
    * 클래스에 정의된 모든 멤버 함수 구현

### Class/Object 생성
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/4b89eb7b-9cef-4f6b-b275-a7c2ab38017e)

```c++
#include<iostream>
using namespace std;

//Circle 선언부
class Circle {
public:
	int radious;
	double getArea();
};

//Circle 구현부
double Circle::getArea() {
	return 3.14 * radious * radious;
}

int main() {
	Circle donut;
	donut.radious = 1;//dount객체의 반지름을 1로 설정
	double area = donut.getArea();//도넛 객체의 면적 알아내기
	cout << "donut면적은 " << area << endl;

	Circle pizza;
	pizza.radious = 30;
	area = pizza.getArea();
	cout << "pizza 면적은 " << area << endl;
}
```
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/8eab2e4e-be35-4549-97ad-256be44b1897)

### 생성자
* 객체가 생성되는 시점에서 자동으로 호출되는 멤버함수
* 클래스 이름과 동일한 멤버 함수

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/bd56de80-2370-4e6a-a3cf-d80ad1f2855d)

* 생성자의 목적: 객체가 생성될 때 객체가 필요한 초기화를 위해
  * 멤버 변수 값 초기화, 메모리 할당, 파일 열기, 네트워크 연결 등
* 생성자 이름: 반드시 클래스 이름과 동일
* 생성자는 리턴타입을 선언하지 않는다.
  * 리턴 타입 없음. void타입도 안됨
* 객체 생성 시 오직 한 번만 호출
  * 자동으로 호출됨. 임의로 호출할 수 없음. 각 객체마다 생성자 실행
* 생성자는 중복 가능
  * 생성자는 한 클래스 내에 여러 개 가능
  * 중복된 생성자 중 하나만 실행
* 생성자가 선언되어 있지 않으면 기본 생성자 자동으로 생성
  * 기본 생성자-매개변수 없는 생성자
  * 컴파일러에 의해 자동 생성

### 생성자의 멤버 변수 초기화 방법
```c++
class Point{
  int x, y;
public:
  Point();
  Point(int a, int b)
}
```
1. 생성자 코드에서 멤버 변수 초기화
```c++
Point::Point(){x=0; y=0}
Point::Point(int a, int b){x=a; y=b}
```
2. 생성자 서두에 초기값으로 초기화
```c++
Point::Point(): x(0), y(0){//멤버 변수 x, y를 0으로 초기화
}
Point::Point(int a, int b)//멤버변수 x=a로, y=b로 초기화
  : x(a), y(b){//콜론(:)이하 부분을 밑줄에 써도 됨
}
```
3. 클래스 선언부에서 직접 초기화
```c++
class Point{
  int x=0, y=0;//클래스 선언부에서 x, y를 0으로 직접 초기화
}
```

### 소멸자
* 객체가 소멸되는 시점에서 자동으로 호출되는 함수
  * 오직 한 번만 자동 호출, 임의로 호출할 수 없음
  * 객체 메모리 소멸 직전 호출됨
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/47bb5a7d-0500-4280-9fbd-99888db2c4ef)

* 소멸자의 목적
  * 객체가 사라질 때 마무리 작업을 위함ㄴ
  * 실행 도중 동적으로 할당받은 메모리 해제, 파일 저장 및 닫기, 네트워크 닫기 등
* 소멸자 함수의 이름은 클래스 이름 앞에 \~를 붙인다.
  * 예: `Circle::~Circle(){...}`
* 소멸자는 리턴 타입이 없고, 어떤 값도 리턴하면 안됨
  * 리턴 타입 선언 불가
* 중복 불가능
  * 소멸자는 한 클래스 내에 오직 한 개만 작성 가능
  * 소멸자는 매개 변수 없는 함수
* 소멸자가 선언되어 있지 않으면 기본 소멸자가 자동 생성
  * 컴파일러에 의해 기본 소멸자 코드 생성
  * 컴파일러가 생성한 기본 소멸자: 아무것도 하지 않고 단순 리턴
 
### 접근 지정자
* 캡슐화의 목적
  * 객체 보호, 보안
  * C++에서 객체의 캡슐화 전략
    * 객체의 상태를 나타내는 데이터 멤버(멤버변수)에 대한 보호
    * 중요한 멤버는 다른 클래스나 객체에서 접근할 수 없도록 보호
    * 외부와의 인터페이스를 위해서 일부 멤버는 외부에 접근 허용
* 멤버에 대한 3가지 접근 지정자
  * private(디폴트 접근 지정): 동일한 클래스의 멤버 함수에만 제한함
  * public: 모든 다른 클래스에 허용
  * protected: 클래스 자신과 상속받은 자식 클래스에만 허용
 
``` c++
#include<iostream>
using namespace std;

class Boat {
private:
	double fuel;
public:
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
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/7a0098d4-ecf8-40a5-87fe-7c806e668c8e)

### Call by value VS call by adress
* 인자 전달 방식
  * 값에 의한 호출, call by value
    * 함수가 호출되면 매개변수가 스택에 생성됨
    * 호출하는 코드에서 값을 넘겨줌
    * 호출하는 코드에서 넘어온 값이 매개변수에 복사됨
  * 주호에 의한 호출, call by adress
    * 함수의 매개변수는 포인터 타입
      * 함수가 호출되면 포인터 타입의 매개변수가 스택에 생성됨
    * 호출하는 코드에서는 명시적으로 주소를 넘겨줌
      * 기본 타입 변수나 객체의 경우, 주소 전달
      * 배열의 경우, 배열의 이름
    * 호출하는 코드에서 넘어온 주소 값이 매개 변수에 저장됨
   
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/fb992625-6679-497d-b5ae-ffea7b895b35)
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/257261aa-f032-4c58-a137-3419a3702d8e)
