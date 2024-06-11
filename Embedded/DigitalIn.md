# DigitalIN 클래스
## 생성자
생성자|DigitalIn객체를 생성한다
---|---
DigitalIn(PinName pin, PinMode pull)
pin|디지털 핀 이름
pull|입력 핀의 pull 회로 지정
|pullUp, pullDown, pullNone
예제|DigitalIn sw(D2, pullUp)

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/a033d798-f800-4774-b39a-944deafd9eb7)

## 입력모드 설정
* 입력모드 설정: 생성자에서 지정하지 않거나 변경하는 경우
입력 모드|내부 풀업 관련 입력 회로를 선택적으로 활성화한다
void .mode(PinMode pull)
pull|입력 핀의 pull회로 지정. PullUp, PullDown, PullNone중 하나를 선택

예제
```c++
DigitalIn switch(D2);
switch.mode(PullDown);
```

## DigitalIn클래스: 읽기
읽기 함수 read|입력 핀의 현재 상태 값을 읽는다
int .read()
return|입력 핀의 현재 값(0/1)

예제
```c++
DigitalIn sw(D2);
int a=sw.read();
```

* 형변환 연산자 int(): 연산자 오버로딩
연산자 int()|형변환 int()연산자의 오버로딩이며 현재 상태 값을 반환한다.
operator int()
return|입력 핀의 현재 값(0/1)

예제
```c++
DigitalIn but(D2);
DigitalOut led(LED1);
led=but;
```
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/fd0470e5-50dd-42aa-8d32-22e862a84989)
```c++
#include "mbed.h"
DigitalOut led(LED1);

DigitalIn but(BUTTON1);
int main(){
  while(1){
    led!=but;
  }
}
```

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/a9b00ef9-f96f-4ad2-be2e-2d7d9bd25d3e)

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/f1a0bd17-e801-491c-b27d-a5085a16b6f2)

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/4afe8db3-7603-4f91-8173-9b724d0a1a3a)

![Uploading image.png…]()
