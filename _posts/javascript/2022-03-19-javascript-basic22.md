---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 객체지향-표준 내장객체의 확장
date: 2022-03-19 17:25 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 객체지향-표준 내장객체의 확장

<br>
<br>

---

## 1. 표준 내장 객체란?
<br>
<br>
표준 내장 객체(Standard Built-in Object)는 자바스크립트가 기본적으로 가지고 있는 객체들을 의미한다. 내장 객체가 중요한 이유는 프로그래밍을 하는데 기본적으로 필요한 도구들이기 때문에다. 결국 프그래밍이라는 것은 언어와 호스트 환경에 제공하는 기능들을 통해서 새로운 소프트웨어를 만들어내는 것이기 때문에 내장 객체에 대한 이해는 프로그래밍의 기본이라고 할 수 있다. 
<br>
<br>
자바스크립트의 표준 내장객체는 아래와 같다.
<br>

- Object
- Function
- Array
- String
- Boolean
- Number
- Math
- Date
- RegExp




---

## 2. 배열의 확장 1
<br>
<br>
내장객체에 우리가 원하는 기능을 추가하는 방법을 알아보자. 아래 예제는 도시이름이 랜덤하게 값으로 반환되는 코드이다. Math.random함수는 0에서 1사이의 난수(난수란 무작위로 만들어진 수열을 가리킨다. 여기서 무작위란 다음에 나올 수를 절대 예측할 수 없다는 것을 뜻한다.)를 반환하는 함수이다.arr.length * Math.random()은 소수값이 포함되어 있기 때문에 index값을 불러올 수 없다. 그렇기 때문에 Math가 가진 API중에 Math.floor을 사용해 정수로 만들어 줘야한다. Math.floor는 소수점을 없애주는 역할을 한다. 예를들어 0.1은 0, 5.2는 5로 바꿔주는 역할을 한다. 그렇게 하고 우리가 랜덤하게 배열의 인덱스값을 배열에 전달할 수 있게 return arr[index];}를 해준다. 

~~~javascript

var arr = new Array('seoul','new york','ladarkh','pusan', 'Tsukuba');
function getRandomValueFromArray(arr){
    var index = Math.floor(arr.length * Math.random());
    return arr[index];
}
console.log(getRandomValueFromArray(arr))

~~~

## 3. 배열의 확장 2
<br>
<br>
이번엔 Array생성자를 확장해서 모든 배열이 그 배열이 갖고있는 값 중에 어떤 특정한 값을 랜덤하게 획득할 수 있는 기능을 모든 배열의 객체가 획득할 수 있도록 코드를 변경해 보자.  new Array로 새로운 배열을 만들어 낼때 Array.prototype.random = function() { }라는 생성자 함수가 실행이 될것이다. 그생성자가 가지고있는 prototype이라는 프로퍼티 안에 있는 객체가 만들어지는 그 객체의 원형이 되기 떄문에 random이라는 것을 추가한는 것을 통해서 배열객체가 만들어지는 원형, 배열객체의 원형에 random이라는 메소드를 추가하게 되는것이다. 프로토타입을 추가하는걸 통해서 배열 생성자를 통해서 만들어진 객체가 random이라는 메소드를 가지고 있다. random이라는 메소드 안에서 this는 배열객체 자체를 의미한다.

~~~javascript

/*
var arr = new Array('seoul','new york','ladarkh','pusan', 'Tsukuba');
function getRandomValueFromArray(arr){
    var index = Math.floor(arr.length * Math.random());
    return arr[index];
}
console.log(getRandomValueFromArray(arr))
*/

Array.prototype.random = function() { //배열을 만들기 위한 생성자함수
    var index = Math.floor(this.length * Math.random());
    return this[index];
}
var arr = new Array('seoul','new york','ladarkh','pusan', 'Tsukuba');
console.log(arr.random());

~~~