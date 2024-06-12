# RTOS 활용
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/d4235b61-7fbb-43fb-b2e8-2e00b19c4d20)

## From a Program to a Process
* Program=instructions+data+metadata(컴파일러가 만듬): 저장장치에 저장되어 실행 가능한 파일
* Process: 실행을 위해 메모리에 올라온 동적인 상태

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/86fa8afa-4f8a-4cf9-9f8e-cb211cf328f5)

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/d95a1d78-6fde-4178-b22d-88d7e3e195a6)

## Thread의 개념
* 프로세스의 자원과 제어에서 제어만 분리한 실행 단위
* 프로세스 하나는 스레드 한 개 이상으로 구성
* 다른 실행 기록(별도 스택 필요)
* 자원, 메모리 등을 공유 가능-> 손상된 데이터나 스레드의 이상 동작 고려
* 같은 프로세스의 스레드들은 동일한 주소 공간 공유
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/8beae790-bda0-438e-bb76-80a77f1a88d0)

# RTOS
## RTOS 개요
### RTOS(Real Time OS) APIs
* Thread: 병렬 작업을 정의하고 제어하는 용도
* Mutex(Mutual Exclusion 상호배제): thread간의 공유 데이터 동시 접근 관리
* Semaphore: 공유하는 자료의 접근을 관리
* Queue: 다른 thread가 시간에 생산한 자료를 다른 thread가 사용할 수 있게 함
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/e91eb488-1123-4d1b-b142-97e7a3d54b69)

* MemoryPool
  * 고정 크기 자료의 메모리 풀을 관리할 수 있는 class
  * 자료를 allocation함
* Mail: Queue와 MemoryPool 기능을 모두 내장한 class
* EventFlags
  * 조건과 사건을 여러 thread에서 공유하게 하는 클래스
  * 하나의 객체는 31개의 flag를 가질 수 있고 ISR에서도 설정 가능
* Event: 사건들을 queuing하여 이후에 처리할 수 있도록 하는 class

# Thread
## Thread
### 주요 용법
* 생성자: 자동 실행을 하지 않는 경우(start() 별도)
생성자1|객체를 생성하지만 자동실행을 하지 않는 경우의 생성자
---|---
Thread(osPriority prior-osPriorityNormal, unit32_t, stk_sz=OS_STACK_SIZE, unit_8t *stack_mem=NULL, const int8_t *name=NULL)
prior|스레드의 실행의 우선순위
stk_sz|스택 크기로서 기본은 4kb
stk_mem|스택 메모리의 포인터
name|스레드의 이름
예제|`Thread t;`

* 생성과 동시에 자동 실행하는 경우: start 함수가 필요 없음
생성자2|객체를 생성하면서 자동실행을 시키는 생성자
---|---
Thread(Callback<void()> task, osPriority pri=osPriorityNormal, unit32_t stk_sz=OS_STACK_SIZE, uint8_t *stk_mem=NULL)
task|실행시키고자 하는 함수 지정
pri|스레드의 우선 순위
stk_sz|스택 크기로서 기본은 4kb
stk_mem|스택 메모리의 포인터
name|스레드의 이름
예제|`Thread t(task);

* 우선순위 관련 상수: 값이 클수록 순위가 높음
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/b3969d09-0a09-46aa-90d2-be8eea042f64)

* 스레드 제어
시작|스레드를 시작시킨다
---|---
osStatus .start(Callback<void()> task)
task|주기적으로 호출될 반환형이 void인 함수의 주소
예제|Thread t; t.start(&task);
osStatus .start(Callback(T *obj, M method))
obj|Thread 객체가 선언된 객체의 주소
method|호출될 멤버 함수의 주소
예제|myClass{thread t;...;t.start(Callback(this, &myclass::task));

## 열거형 osStatus
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/89134ed2-27eb-402a-900b-2ae4b4398ba5)

## Thread
* join(): 메인 스레드를 다른 스레드가 끝날 때까지 대기시킴
종료 대기|다른 스레드가 종료될 때까지 main스레드가 대기한다
---|---
osStatus .join()
반환|함수의 실행 상태를 반환
예제|th.join();

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/92c3ef95-c0cb-4fe9-9442-44132c4ffa60)

* terminate(): thread 강제 종료
강제 종료|thread를 강제 종료시킨다
---|---
osStatus .terminate()
반환|함수의 실행 상태를 반환
예제|`th.terminate();`

* 우선순위 설정
  * .set_priority(osPriority priority): 스레드의 우선순위 설정
  * .get_priority(): 스레드의 우선순위 읽기
 
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/2ca88e9c-9606-420e-9c60-c80f98f4eb52)
```c++
#include "mbed.h"
DigitalOut led1(LED1), led2(D7);
Thread thread;
void led1_thread(){
  led1=!led1;
  wait_us(100000);
}
int main(){
  thread.start(&led1_thread);
  while(true){
    led2!=led2;
    wait_us(500000);
  }
}
```

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/aae34971-c608-4f26-9413-001af5a26b9d)
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/94f380d3-f710-4823-8c25-365c0cf17bfd)

```c++
#include "mbed.h"
DigitalOut led1(LED1), led2(D7);
volitile bool running=true;
void blink(DIgitalOut *led){
  while(running){
    *led!=*led;
    wait_us(20000);
  }
}
int main(){
  thread.start(callback(&blink, &led1);
  led2=1;
  wait_us(5000000);
  running=false;
  thread.join();
  led2=0;
}
```

# Mutex
## Mutex
### 주요 용법
* 뮤텍스는 상호 배제라는 의미로 두 개의 스레드가 하나의 자원을 공유하여 작업하는 경우 두 스레드가 동시에 접근하여 발생하는 문제를 해결하는 역할
* 비유
  * 식당의 화장실 열쇠를 상상하면 됨
  * 열쇠가 하나라 항상 열쇠를 가질 때까지 대기
  * 사용했으면 최대한 빨리 반환
 
* 생성자
생성자|Mutex 객체를 생성한다
---|---
Mutex()
예제|Mutex mu;

* 자료 접근 권한 제어: 접근 권한 획득: blocking
접근 권한 획득|접근 권한을 획득한다.
---|---
osStatus .lock()
반환|성공하면 osOK를 반환
예제|mu.lock()

* 접근 권한 획득 시도
  * 일정 기간 즉 ms동안 획득을 시도한 후 결과 반환 true/false
권한 획득 시도|접근 권한을 획득을 시도한다
---|---
bool .trylock_for(unit_32 t ms)
ms|ms밀리초동안 획득 시도
반환|성공하면 true, 실패하면 false 반환
예제|mu.trylock_for(10);

* 접근 권한 반환: 획득한 mutex를 반환
접근 권한 반납|접근 권한을 반납한다.
---|---
osStatus .unlock()
반환|성공하면 osOK 반환
예제|mu.lock()

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/b1a0f1e7-99ee-4928-8037-9a3cf168c7dc)
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/9bc4c5b3-aecb-4cfe-b9bd-fc33b5451882)

```c++
#include "mbed.h"
Mutex mutex;
Thread thread;
int cnt=0;
DigitalOut led(LED1);
void notify(const char* name, int ct){
  printf("%s: %3d\n\r", name, ct);
}

void thread_plus(const char *args){
  while(true){
    mutex.lock();
    led=!led;
    notify((const char*)args, ++cnt);
    mutex.unlock();
    wait_us(490000);
  }
}

void thread_minus(const char *args){
  while(true){
    mutex.lock();
    notify((const char*)args,--cnt);
    mutex.unlock();
    wait_us(1000000);
  }
}

int main(){
  t2.start(callback(&thread_plus, (const char *)"th2"));
  t3.start(callback(&thread_minus, (const char *)"th3));

  thread_minus((const char *)"th1");
}
```

# Queue
## Queue
### 주요 용법
* 생성자
생성자|Queue 객체를 생성한다
---|---
template<typename T, uint32_t queue_sz> Queue
T|큐에 저장될 메시지의 자료형
queue_sz|큐에 저장될 메시지의 최대 개수
예제|Queue<my_mesage, 100> que;

* 큐에 메시지 넣기(enqueue)
메시지 넣기|큐에 메시지 하나를 넣는다.
---|---
osStatus .put(T *msg, uint32_t millisec=0, uint8_t prio=0)
msg|큐에 저장될 메시지(자료형 T인 메시지의 주소)
millisec|대기의 timeout시간(기본값=0) (대기시간 0: 넣기 시도해보고 곧바로 빠져나온다)
prio|우선순위(기본값=osPriorityNormal)
반환|성공하면 osOK반환
예제|if(que.put(&msg, 0, osPriorityHigh);

* 큐에 메시지 빼기(dequeue)
메시지 읽기|큐로부터 메시지 하나를 읽는다
---|---
osEvent .get(uint32_t millisec=osWaitForever)
millisec|대기시간(기본값이 osWaitForever(메시지를 읽을 때까지 계속 기다리게 하는 설정))
반환|구조체에 메시지가 포함되어 반환
예제|message=que.get();

## osEvent 구조체
* 메시지가 탑재된 구조체
```c++
typedef struct{
  osStatus status;//event 또는 error의 정보 표시
  union{
    uint32_t v;//32bit 정수의 메시지
    void *p;//message 또는 mail의 void 포인터
    int32_t signals;//signal인 경우 플래그
  }value;//event의 값
union{
  osMailQId mail_id;//mail의 경우 id
  osMessageQId message_id;//message의 경우 id
  }def;//event의 정의
}osEvent;
```

## Queue
* 상태확인
  * 큐가 비었는지 확인
큐 empty|큐가 비었는지 확인한다.
---|---
bool.empty()
반환|큐가 비었으면 true 아니면 false
예제|if(que.empty())

  * 큐가 꽉 찼는지 확인
큐 full|큐가 찼는지 확인한다.
---|---
bool.full
반환|큐가 찼으면 true 아니면 false
예제|if(que.full())

![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/f171634e-32ad-41f9-b063-b490e6e57d11)
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/55195250-7fc3-4624-baac-a263ea392065)

```c++
#include "mbed.h"
typedef struct{
  uint32_t xxx, yyy;
  uint32_t counter;
}message_t;
MemoryPool<message_t, 16> mpool;
Queue<message_t, 16> queue;
Thread thread;
void generator(void){
  uint32_t i=0;
  while(true){
    i++;
    i%=101;
    message_t *message=mpool.alloc();
    message->xxx=i*33;
    message->yyy=i*11;
    message->counter=i;
    queue.put(message);
    wait_us(1000000);
  }
}

int main(){
  thread.start(&generator);
  while(true){
    osEvent evt=queue.get();
    if(evt.status==osEventMessage){
      message_t *message=(message_t*)evt.value.p;
      printf("\nxxx: %u\n", message->xxx);
      printf("yyy: %u\n", message->yyy);
      printf("Number of cycles: %u\n", message->counter);
      mpool.free(message);
    }
  }
}
```
![image](https://github.com/qlkdkd/univ-3-1/assets/71871927/f34477d0-6194-4789-8b7f-7b7f7126edc9)

