# PWM 출력 프로그래밍

## PWM이란?
### PWM(Pulse Width Modulation): 펄스폭 변조
* 일정한 주기의 펄스에서 펄스의폭을 변경하여
  * 정보 전달: RC 서보모터
  * 근사 아날로그 출력(파워제어): 모터 제어, 히터 제어, 조명 제어
 
## 정보 전달용 PWM
* PWM은 일정 주기 간격으로 나타나는 펄스의 폭(On-duty)으로 정보를 전달
* 예: 다음과 같은 파형으로 10, 17, 18 순서로 정보 전달

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/fc956443-4d31-4506-abfa-3f4ce0ef7bbe)

## 근사 아날로그 출력용 PWM
### 근사 아날로그 출력의 원리
* 주기를 매우 짧게 하여 아날로그 전압 신호를 근사적으로 발생
* 고가의 DAC와 아날로그 회로 없이 스위칭 소자를 활용
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/b1df8fe5-b54e-4b1b-b01d-9cf3f788268b)

* 주기를 매우 짧게 하여 아날로그 전압 신호를 근사적으로 발생
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/09e8ddfd-0262-4242-9aee-c0b20f9bb6a2)

### PwmOut 클래스
* 주요 용법: 생성자
생성자|PwmOut 객체를 생성한다
---|---
PwmOut(PinName pin)
pin|PWM 출력 핀 이름

예제
```c++
PwmOut rc(D2);
```

* 주기설정: 시간 단위에 따라 period, period_ms, period_us
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/bfe3d5ed-fb4b-4852-a6e0-e87c02872352)

* 쓰기 함수
쓰기 함수 write|PWM 출려값을 0.0과 1.0 사이의 수로 지정한다
---|---
void .writd(float value)
value|float형의 PWM출력값(0.0~1.0)

예제
```c++
PwmOut pwm(D2);
pwm.write(0.5);
```

* 펄스폭 지정 함수: 시간 단위에 따라 pulsewidth, pulsewidth_ms, pulsewidth_us
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/65d07e5c-48fe-498e-a60d-bf3e189dcca4)

* 읽기 함수
읽기함수 read|현재 출력되고 있는 값을 읽어 반환한다.
---|---
float .read()
return|PWM핀의 현재 출력값을 float형으로 반환(0.0~1.0)

예제
```c++
PwmOut pwm(D2);
float v=pwm.read();
```

* 연산자 오버로딩: 대입 연산자 = (float)
대입 연산자 =|우변의 float값을 출력으로 지정한다.
---|---
PwmOut& =(float value)
value|원하는 PWM출력값(0.0~1.0)

예제
```c++
PwmOut pwm(D2);
pwm=0.5;
```

* 형변환 연산자 float()
형변환 연산자 float()|객체를 float로 형변환하면 현재 출력을 반환한다.
---|---
operator float()
return|현재 출력되고 있는 PWM핀의 값(0.0~1.0)

예제
```c++
PwmOut pwm(D2);
float v=pwm;
```

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/337c530f-de94-45bd-a74b-85df663e779d)
```c++
#include "mbed.h"
PwmOut pwm(D7);

int main(){
  int count=0;
  pwm.period_us(25);
  while(1){
    pwm=count/100.;
    count++;
    count%=101;'
    wait(0.1);
  }
}
```
