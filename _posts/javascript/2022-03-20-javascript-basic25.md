---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 객체지향 - 참조
date: 2022-03-20 14:10 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 객체지향 - 참조

<br>
<br>

---

## 1. 복제란?
<br>
<br>
바로 이러한 특징이 소프트웨어를 기존의 산업과 구분하는 가장 큰 특징일 것이다. 프로그래밍에서 복제가 무엇인가를 살펴보자.
<br>
<br>
아래 코드의 결과는 1이다. 2행에서 var b = a; 3행에서 b = 2;기떄문에 2가 아닌가 생각할 수 있지만 그렇지 않다. a와 b는 각각다른 데이터를 갖고있기 때문에 a의 값에는 영향을 주지 않는다. 두 변수는 연결되어 있지 않은 별도의 데이터이다.

~~~javascript

var a = 1;
var b = a;
b = 2;
console.log(a); //1

~~~

![복제](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/532/2226.png)

---

## 2. 참조
<br>
<br>
객체는 어떻게 동작하는지 알아보자. b = a;라고 했고 b에는 {'id':1};이런 값이 들어가게 될것이다. 그상태 에서 b.id로 b의 id값을 2로바꿨다. 그리고 a의 id값을 체크하면 값이 2가된다. 이말은 b의 프로퍼티 값을 변경하면 a의 프로퍼티 값이 변경 된다는 것이다. 

~~~javascript

var a = {'id':1}; //a라는 변수에 di가 1인 객체를 지정
var b = a;
b.id = 2;
console.log(a.id);  // 2

~~~

아래의 예제는 1을 출력한다. b = {'id' : 2};로 새로운 객체를만들어 변수b에 할당을 한것이다. 그렇기 때문에 b라는 변수는 더이상 {'id':1};를 의미하지 않고 새롭게 만들어진 {'id' : 2};를 의미하게 되는 것이다.

~~~javascript

var a = {'id':1}; 
var b = a;
b = {'id' : 2};  //객체를 생성한것이다.
console.log(a.id); //1

//사실상 아래의 코드와 같다.

var a = 1;
var b = a;
b = 2;
console.log(a); //1


~~~

변수에 담겨진 값이 객체인경우 b = a;라고 했을때 b와 a는 똑같은 객체를 바라보게된다. 하지만 데이터가 원시 데이터 타입인 경우 b = a;라고하면 이순간에 a에 담겨있던 값이 복제되어 새로만들어지고 그값이 b에 담겨지게 되는것이다. 즉 참조건 복제건 상관없이, 원시데이터이건 객체건 상관없이 새로운 데이터를 만들어서 그것을 변수에 할당하면 새로운 데이터의 값을 바라보게 되지만 지만 객체는 b = a; 라고 했을 때 객체는 똑같은 객체를 각각의 변수들이 바라보게 되는것이고 원시데이터에서 b = a;라고 했을땐 a가 바라보던 값을 b가 만들어졌을땐 복제한 별개의 값을 바라보게 되는것이다. 


![참조](https://s3.ap-northeast-2.amazonaws.com/opentutorials-user-file/module/532/2227.png)

---

## 3. 함수와 참조
<br>
<br>
그럼 일종의 변수할당이라고 할 수 있는 메소드의 매개변수는 어떻게 동작하는가를 살펴보자. 조금 복잡하므로 꼼꼼하게 살펴봐야 한다. 예제를 보자.
<br>
<br>
다음은 원시 데이터 타입을 인자로 넘겼을 때의 동작 모습이다. a에 1이라는 값이 담겨있다. 그리고 함수를 정의했는데 매개변수(parameter)인 b의값을 2로 바꾸고있다. 그리고 함수를 호출할때 a를 전달했다. 이말은 b = a;라는 것과 같다. a=1인상태이고 b=a;, 그리고 b=2; 인것이다. 여기서 a=1이고 함수가 b = a;라는 의미이기 때문에 복제와 같다. a=1의 값이 함수 b에 들어가지만 함수내의 b=2;로 b=2가되고 개별의 데이터인 a는 그대로 1이되게 된다.

~~~javascript

var a = 1;
function func(b){ // b = a; 라는것이다.
    b = 2;
}
func(a);
console.log(a);

~~~

이번에는 변수에 담긴 값이 객체이다. a = {'id':1};이고 위 함수와 마찬가지로 b = a;를 의미하고 a는 객체이기 때문에 b와 a는 똑같은 객체를 바라보고 있는 상황이지만 b = {'id':2};가 새로운 객체를 만들었고 b에 새로운 객체를 할당했기 때문에 b는 {'id':2};를 바라보고 있다. 그렇기 때문에 b와 a가 같은 객체를 바라보지 않게 되는것이다. 따라서 결과는 1이다.

~~~javascript

var a = {'id':1};
function func(b){
    b = {'id':2};
}
func(a);
console.log(a.id);  // 1

~~~

아래는 결과가 다르다. 아래도 마찬가지로 b = a;를 함수로 나타내고 있지만 b.id = 2;로 b와a는 데이터가 객체이기 때문에 같은 객체를 바라보고 있다. b.id = 2;로 a의 값도 바뀌기 때문에 결과는 2가된다.

~~~javascript

var a = {'id':1};
function func(b){
    b.id = 2;
}
func(a);
console.log(a.id);  // 2

~~~