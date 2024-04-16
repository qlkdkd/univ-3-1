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
  *   멤버 변수는 클래스 선언 내에서 초기화할 수 없음
  *   멤버 함수는 원형(prototype) 형태로 선언
  * 멤버에대한 접근 권한 지정
  *   private public, protected 중의 하나
  *   디폴트는 private
  *   public: 다른 모든 클래스나 객체에서 멤버의 접근이 가능함을 표시
  * 클래스 구현부(class implementation)
  *   클래스에 정의된 모든 멤버 함수 구현
 
