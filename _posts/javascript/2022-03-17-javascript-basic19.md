---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 객체지향 - 전역객체
date: 2022-03-17 11:17 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 객체지향 - 전역객체

## 1. 전역객체란?
<br>
<br>
전역객체(Global object)는 특수한 객체다. 모든 객체는 이 전역객체의 프로퍼티다. 
<br>
<br>
func();와 window.func();는 모두 실행이 된다. 모든 전역변수와 함수는 사실 window 객체의 프로퍼티다. 객체를 명시하지 않으면 암시적으로 window의 프로퍼티로 간주된다. 생략이 가능하다는 말이다.

~~~javascript

function func(){
    alert('Hello?');    
}
func();
window.func();

~~~

모든 전역변수와 함수는 window객체의 프로퍼티다. 객체를 명시하지 않으면 암시적으로 window의 프로퍼티로 간주한다. 아래 예제는 전역변수 o에 객체메소드를 지정했다. 그렇기 떄문에 o.func();와 window.o.func();가 모두 실행이 되는걸 알수있다. 

~~~javascript

var o = {'func':function(){
    alert('Hello?');
}}
o.func();
window.o.func();

~~~


---

### 전역객체 API
<br>
<br>
ECMAScript에서는 전역객체의 [API](https://opentutorials.org/course/50/44).를 정의해두었다. 그 외의API는 호스트 환경에서 필요에 따라서 추가로 정의하고 있다. 이를테면 웹브라우저 자바스크립트에서는 alert()이라는 전역객체의 메소드가 존재하지만 node.js에는 존재하지 않는다. 또한 전역객체의 이름도 호스트환경에 따라서 다른데, 웹브라우저에서 전역객체는 window이지만 node.js에서는 global이다. 


