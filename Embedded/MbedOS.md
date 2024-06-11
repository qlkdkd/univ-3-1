# Mbed 시작하기
## Mbed의 출현
* IOT의 바람이 시작되던 2009년에 32비트 ARM COrtex-M플랫폼을 위한 Mbed OS를 발표
* Mbed OS는 C++기반의 소프트웨어 플랫폼과 ARM Cortex-M 펌웨어를 쉽게 프로그램할 수 있는 개발 툴을 포함함
* 데모 보드를 가지면 별도의 프로그램 장비 구입이나 개발환경 구출에 시간을 쓸 필요 없이 웹브라우저와 USB 케이블로만으로도 간단한 예제 프로그램을 시작 가능

## Mbed의 혁신적인 점
* 개발 난이도 측면
  * 개발 환경 구축이 매우 신속
  * 표준 C++ 기반의 Mbed 라이브러리를 활용하여 프로그램을 진행 가능
  * 복잡한 레지스터 수준의 고려가 필요가 없음
  * Mbed API 전반에 일관성이 존재하여 몇몇 기능에 대한 API를 이해하면 나머지는 비교적 무난하게 학습 가능
* 성능적 측면
  * 8bit 수준의 가격으로 32비트의 고성능 시스템을 구축 가능
  * Mbed는 원래 IoT를 지향하여 출발하였기 때문에 Ethernet, USB, Bluetoot, CAN등의 다양한 연결성에 대한 라이브러리 지원
  * RTOS의 실시간 프로그래밍의 라이브러리 지원
 
## Mbed의 전망
* 미래의 전망
  * 광범위한 일반 MCU의 기능은 물론 IoT 시대에 필요한 다양한 연결성을 지원하여 미래지향적
  * 추세적으로 MCU관련 산업에서 32비트 ARM 프로세서가 대세로 자리를 잡았기에 이를 따라가기 위하여 꼭 배워야할 도구

## Mbed란?
### 개요
* Cortex-M 마이크로컨트롤러 프로그램용 OS
  * 온라인 소프트웨어 개발 툴 + USB 메모리와 전원
  * 2009년 처음 개발
* 장점
  * 사용하기 편리, 회로를 모르더라도 개발 가능, 별도의 다운로드 장비 불필요
  * 온라인의 방대한 라이브러리 공유
  * 고성능 ARM 코어의 다양한 기능 수용
    * Ethernet, USBHost, USBDevice, SPI, I2C, CAN, AnalogIn, PWMOut, AnalogOut
* 단점
  * 레지스터 레벨의 디버깅 안됨
 
## 지원 장치
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/8cf140e4-2e36-4717-a40e-4b5f355a03d5)

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/0d8580f2-466b-4299-ab3e-c9e0f1ba3698)

# Nucleo 보드
## Nucleo-F411RE Kit
### 특징
*STM32F411RET6 프로세서 사용
  * ARM 32bit Cortex M4 CPU with FPU
  * Clock: Max. 100MHz
  * VDD from 1.7V to 3.6V
  * 512KB Flash & 128KB SRAM
  * GPIO(50)with external interrupt capability
  * 12bit ADC with 16 channels
  * RTC and Timers(8)
  * I2C(3) USART(3), and SPI(5)
  * USB OTG Full Speed
  * SDIO(Secure Digital IO: for SD/MMC/eMMC)

## STM32F411RET6 프로세서 블록도
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/3c847a36-2439-4d1a-9b7d-69a02930937b)

## Nucleo-F411RE kit
### 특징
* 외부 연결용 핀 헤더
  * 아두이노 우노 Revision 3 핀 헤더
  * STMicroelectronics의 Morpho extension 핀 헤더
* 보드에  ST-LINK/V2-1 디버거/프로그래머 포함
* 다양한 전원 공급
  * USB
  * 외부 전원
* 사용자 LED(LD2)
* 2개의 푸시 버튼: USER 버튼 and RESET 버튼
* USB를 통한 3가지 기능
  * Virtual Com port 제공
  * Drag and Drop 프로그래밍이 가능한 Mass storage(USB Disk dirve)
  * 디버거 포트
* Mbed-OS 지원

### Nucleo 보드의 명명법
* Nucleo-TxxxRY
  * Txxx: STM32 MCU 타입
  * R: 헤더 핀 수
    * k: 32pins, R: 64pins, Z: 144pins
  * Y: code size
    * 4: 16kb, 6: 32kb, 8: 64kb, b: 128k, c: 256kb
    * e: 512k, G fo

## Nucleo 보드 종류
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/973005e7-8f78-4168-8273-a35201704516)
* 보드 외형

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/72f0fb75-6ed1-4573-8f50-e122b259dd7c)
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/95550c76-ee60-4474-9563-6b8d316ab4fe)
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/0d4c99f8-76bc-4335-b3a2-43e2e7fcdf42)
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/1563181c-2ba7-4018-8250-21f0f90e6bb5)

## Nucleo-F411RE kit
* LED LD3
  * 전원 LED
  * 충분한 전류 공급될 때 켜짐(max: 300mA)
* USB 전원
  * JP5: 1~2 Short
  * JP1 OFF: 300mA max(default)
  * JP1 ON: 100mA max
* VIN or EV5
  * JP5: 2~3 short
* VINL CN6~8 or CN7~24, 7~12V
  * input current: (7V: max 800mA, 7V~9V: 450mA, 9V~12V 250mA)
* E5V: CN7~6, 4.75V~5.25V, max: 500mA

