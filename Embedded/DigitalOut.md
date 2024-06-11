# DigitalOut 클래스
## DigitalOut 생성자
### 주요 용법
* 생성자 함수
  * 반환형이 없고 함수 이름이 클래스 이름 그대로인 아주 특별한 함수
  * 객체 생성시 한번 동작
  * cf.소멸자: 객체 소멸 시 한번 동작
생성자|객체를 생성한다
DigitalOut(PinName pin(int, value))
pin|디지털 출력핀 이름
value|초기 출력값(0/1)

예제
```c++
DigitalOut led(D2);
DigitalOut led(D2, 0);
```

## DigitalOut 읽고 쓰기

write|객체에 할당된 핀에 원하는 값을 출력하는 멤버 함수이다.
void .write(int value)
value|출력값(0/1)

예제
```c++
DigitalOut led(D2);
led.write(1);
```

read|현재 출력되는 값을 읽는다.
int .read()|
return|현재값(0/1)

예제
```c++
DigitalOut led(D2);
printf("led=%d\n", led.read());
```

## DigitalOut 연산자 오버로딩
* 연산자 오버로딩: 형변환 연산자 int()

형변환 연산자 int()|객체가 정수로 변환될 때 동작하며 출력값을 반환한다.
operator int()
return|현재 출력값(0/1)

예제
```c++
DigitalOut led(LED1);
printf("%d", led);
```

* 대입 연산자 = 정수
객체=정수|write함수의 단축형이며 우변이 정수값을 받아 출력한다.
DigitalOut& operator=(int value)
value|원하는 출력값(0/1)

예제
```c++
DigitalOut led(LED1);
led=1;
```

* 대입 연산자 = 객체
객체=객체|우변이 객체일 때 그 출력값을 받아와 좌변 객체에 적용한다.
DigitalOut& operator=(DigitalOut &rhs)
rhs|DigitalOut 객체

예제
```c++
DigitalOut led1(LED1), led2(D3);
led1=led2;
```

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/ce3fa09f-3bfe-4b4b-9329-59ab8befd39e)

```c++
#include "mbed.h"
DigitalOut myled(LED1);
int main(){
  while(1){
    myled=1;
    wait(0.2);
    myled=0;
    wait(1.0);
  }
}
```

## 유용한 wait()함수
wait 관련|프로그램 실행을 지연시킨다.
---|---
wait(float s)|s초동안 대기
wait_ms(int ms)|ms밀리초동안 대기
wait_us(int us)|us마이크로초동안 대기

* 프로세서가 아무 일도 하지 않는 것이기 때문에 고도의 프로그램에서는 효율이 나빠짐

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/a4f32859-eb5e-4bc7-8bee-e35751f37c3c)
```c++
#include "mbed.h"
DigitalOut led(LED1);

int main(){
  srand(time(NULL));
  float v=(float)rand()/RAND_MAX;
  led=(v<0.1f)?1.0;
  wait(0.01);
}
```

## 참고: 정수 자료형 표현: int#_t, uint#_t
* int#_t, uint#_t 자료형
  * 정수 자료형의 바이트 크기 표현이 명확하고 간결함
  * 플랫폼이 바뀌어도 코드에 문제가 없음
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/bb484430-4dbc-4b90-8d87-65aa03a52f8c)

## 참고: DigitalOUt.h 코드
### Mbed의 클래스 코드
* hal/gpio_api.h
  * gpio_init_out
  * gpio_write
  * gpio_read
* 특징
  * HAL의 함수르 Mbed함수가 감쌈(wrap)
* 체크포인트: 연산자 오버로딩
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/26583a3f-64aa-4030-8ad1-e109a2525f95)
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/3456b6a1-cb99-40ad-a5a7-e81bb0f7490c)
