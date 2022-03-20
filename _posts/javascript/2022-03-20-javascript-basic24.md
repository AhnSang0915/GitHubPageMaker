---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 객체지향 - 데이터타입
date: 2022-03-20 14:10 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 객체지향-테이터 타입

## 1. 원시 데이터 타입과 객체
<br>
<br>
데이터 타입은 크게 2가지로 구분할 수 있다. 원시 데이터 타입과 객체 데이터 타입이다. 원식 데이터 타입은 기본데이터 타입이라고도 하고 객체 데이터 타입은 참조 데이터 타입이라고도 한다. 객체가 아닌 데이터 타입을 원시 테이터 타입이라고 하고 아래와같다.

- 숫자
- 문자열
- boolean(true/false)
- null
- nudefined

위 항목의 데이터 타입을 원시 데이터 타입 이라고 하고 이외의 모든 데이터 타입을 객체 데이터 타입이라고 한다.


---

## 2. 래퍼 객체
<br>
<br>
위와 같은 데이터 타입을 분류하는게 중요한것은 아니고 개발자 입장에서 이러한것이 효용을 갖기 위해서는 원시데이터 타입과 객체가 서로 다르게 동작할 때에 효용이 있는것 이다.
<br>
<br>
아래 코드는 문자열을 변수에 담았다. 문자열의 길이와 문자열의 첫번째 값을 출력한다. 객체가 아닌것은 원시데이터 타입이다. 문자열은 원시데이터 타입인데 아래 console.log를보면 객체처럼 동작하고 있다. 이 .의 정식 명칭은 Object access operator이고 객체접근 연산자 라는 뜻이다. 이 .을썻다는것은 .앞에있는 것이 객체라는 것을 의미한다. 객체이기 때문에 length프로퍼티와 charAt(0)메소드가 존재하는것이다. 이말은 str에 담겨있는 무엇인가가 객체이고 문자열은 객체라는 것이다. Javascript에서 문자열이 원시데이터가 맞긴한데 그문자열을 우리가 제어하기 위해서, 여기서는 문자열의 길이와 첫번째 값을 구하기 위해서는 원시데이터 타입인 문자열이 마치 객체인 것 처럼 동작 해야지만 이런 작업을 할 수 있다. 그런 이유로 인해서 Javascript에서 문자열과 같은 원시데이터 타입은 그것을 객체로서 사용할때 그것을 임시로 객체데이터 타입으로 만들어준다. 우리가 str.length를 할때 그순간에 내부적으로 str = new String('coding'); 이라고하는 객체를 생성해 str변수에 담아준것과 같은 작업이 1행과 2행 사이에 생긴다고 보면 된다.   
 
~~~javascript

var str = 'coding';
console.log(str.length);        // 6
console.log(str.charAt(0));     // "C"

~~~

'coding'이라는 문자열을 str변수에 담았고 str.prop로 prop라는 프로퍼티를 지정했다. 거기에 'everybody'라는 텍스트를 넣었다. console.log(str.prop);로 출력을 하려고하면 undefined가 출력된다. 이말은 우리가 우리가 str.prop = 'everybody'를통해 문자열을 객체화 시킨후 그 다음행으로 문제없이 넘어갈 수 있게 되는데 이순간엔 객체가 만들어졌지만 끝난후에 그 객체를 제거하고 원래의 원시 데이터 타입으로 변경했기 때문에 prop라는 값이 존재하지 않는것이다. 

~~~javascript

var str = 'coding';
str.prop = 'everybody';
console.log(str.prop);      // undefined

~~~

원시 데이터 타입은 객체처럼 사용하려고 할때 자동으로 만들어지는 객체를 래퍼객체(Wrapper Object)라고 한다. 원시 데이터 타입이 있을 때 그 원시 데이터 타입을 감싸주는 객체가 만들어져 객체화 시켜주는게 래퍼객체이다. 

- 숫자 (Number)
- 문자열 (String)
- boolean(true/false) (Boolean)
- null X
- nudefined X

null과 nudefined은 래퍼객체가 존재하지 않는다. 객체화 시키려고 하면 타입에러가 발생할 것이다.