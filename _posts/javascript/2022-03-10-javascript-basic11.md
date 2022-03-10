---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 정규표현식
date: 2022-03-10 23:14 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 정규표현식

<br>
<br>
정규표현식(Reguler expression)은 문자열 안에서 어떠한 문자가 있는지 없는지, 그문자를 다른 문자로 치환하는 것들을 도와주는 방법이다. 정보와 관련된 언어에서는 정규표현식이 매우 중요하다. [정규표현식](http://zvon.org/comp/r/tut-Regexp.html#Pages~Contents)의 공부는 양이 많아 따로 해야한다 링크를 통해 공부하고 아래내용을 보는게 좋겠다.

---

## 1. 패턴만들기
<br>
<br>
정규 표현식은 두가지 사용방법으로 이루어진다. 하나는 컴파일(compile) 다른 하나는 실행(execution)이다. 우선 컴파일부터 알아보자. 우리가 문자열을 변수에 담을때 var str = "a"; 의 식으로 하게된다. 마찬가지로 우리가 정규표현식을 만들때 정규표현식 <u>리터럴</u>이라는것을 이용해 만든다.

~~~javascript

//정규표현식 리터럴
var pattern = /a/;

~~~
또하나의 방법은 정규표현식 객체 생성자를 사용하는 방법이다. 두방법 모두 정규표현식 객체를 pattern이라는 변수에 담은것이다. 우리가 찾고자하는 정보를 pattern이라는 변수에 저장을 한것이다.
~~~javascript

var pattern = new RegExp('a');

~~~


---

## 2. RegExp객체의 사용
<br>
<br>
우리가 어떤일을 할때 두가지 방법이 있다. 작업을 할 대상을 선택하고 그리고 그대상에 대하 어떤작업을 할지 정한다. 먼저 해야할 것은 작업할 대상을 찾는것이다. 이작업을 할수 있게 해주는게 정규표현식이다.
<br>
<br>


### 정규표현식 메소드 실행
<br>
<br>
정규표현식을 컴파일해서 객체를 만들었다면 이제 문자열에서 원하는 문자를 찾아내야 한다. 


#### RegExp.exec()
<br>
<br>
문자열 a를 찾고싶다고할때 pattern변수안에 정규표현식 a를 지정하고 RegExp.exec()로 실행을 시킬수 있다.
RegExp는 정규표현식을 의미하고 exec는 실행을 의미한다. 즉, 우리가 지정한 정규표현식을 실행하는데 그실행의 대상을 첫번째 인자로 전달하고, 그정보가 있는지 없는지 찾으려고 하는 정보가 ('abcdef') 이고 이것이 두번째 인자가 된다. 
<br>
<br>

실행결과는 문자열 a를 값으로 하는 배열을 리턴한다.

~~~javascript
var pattern = /a/;
console.log(pattern.exec('abcdef')); // ["a"]
~~~

이번엔 변수에 정규표현식 a.을 담았다. 결과는 ab가되는데 이것은 정규표현식에서 .이 문자 1개를 의미하기 때문이다.

~~~javascript
var pattern = /a./;
console.log(pattern.exec('abcdef')); // ["ab"]
~~~

인자 'bcdef'에는 a가 없기 때문에 null을 리턴한다.

~~~javascript
var pattern = /a/;
console.log(pattern.exec('bcdefg')); // null
~~~

#### RegExp.test()
<br>
<br>
우리가 필요한 정보를 추출해내야 할때 사용한다. 우리가 찾는 어떤 정보가 있는지 없는지를 존재 유무를 테스트 한다.
<br>
<br>
test는 인자 안에 패턴에 해당되는 문자열이 있으면 true, 없으면 false를 리턴한다


~~~javascript
var pattern = /a/;
console.log(pattern.test('abcdef')); // true
cnosole.log(pattern.test('bcdefg')); // false
~~~

---


## 3. String과 정규표현식

###  String.match()
<br>
<br>
RegExp.exec()와 비슷하다.

~~~javascript

var pattern = /a/;
console.log('abcdef'.match(pattern)); // ["a"]
console.log('bcdefg'.match(pattern)); // null

~~~

###  String.replace()
<br>
<br>
String.replace()는 문자열에서 패턴을 검색해서 이를 변경한 후에 변경된 값을 리턴한다.
<br>
<br>
pattern a를 찾아 A로 치환해주었다.

~~~javascript

console.log('abcdef'.replace(pattern, 'A'));  // Abcdef

~~~


---

## 4. 옵션(i, g)
<br>
<br>
정규표현식 패턴을 만들 때 옵션을 설정할수있다. 찾고자하는 값 뒤에 옵션을 넣어주면 되고, 옵션에 따라 검출되는 데이터가 달라진다.

<br>
<br>
i는 대소문자 구분을 없애주는 역할을 한다. 

~~~javascript

var xi = /a/;
console.log("Abcde".match(xi)); // null
var oi = /a/i;
console.log("Abcde".match(oi)); // ["A"];

~~~

g는 문자열에 포함되어 있는 패턴에 해당되는 문자열들을 모두 리턴해준다.

~~~javascript

var xg = /a/;
console.log("abcdea".match(xg)); // ["a"]
var og = /a/g;
console.log("abcdea".match(og)); // ["a","a"]

~~~

두가지 모두 사용도 가능하다.

~~~javascript

var og = /a/ig;
console.log("AabcdAa".match(ig)); // ["A","a","A","a"]

~~~


---


## 5. 캡쳐
<br>
<br>
그룹을 지정하고 지정된 그룹을 가져와 사용하는 기능, 또는 사용할 수 있는 개념을 캡쳐라고 부른다.

~~~javascript

var pattern = /(\w+)\s(\w+)/; // 문자열 공백 문자열
var str = "coding everybody"; //coding$1 everybody$2
var result = str.replace(pattern, "$2, $1"); //$2,(공백)$1로 치환.
console.log(result);
//everybody, coding

~~~

---


## 6. 치환
<br>
<br>
아래 코드는 본문 중의 URL을 링크 html 태그로 교체한다. \b는 단어를 식별한다. ?:로 https를 캡쳐로 지정하지 않고 뒤에 ?로 https, http가 모두 해당되게 했다. 뒤에 //는 escape를 사용해 문자화 시켰고 그뒤의 a-z는 a부터 z까지 0-9 는 0에서 9까지 그리고 그뒤에 주소에 들어갈만한 특수문자들 까지 해당되게 해줬다. 그리고 replace라는 메소드가 실행될때 urlPattern해당되는 텍스트를 찾을때마다 두번째인자로 전달된 함수가 replace라는 메소드 내부로 호출된다. 호출될때 javascript는 호출된 시점에서 검색된 문자열을 첫번째 인자(url)로 전달되게 약속되어있다. 그리고 그 텍스트를 가공을하고 리턴을 해주면 우리가 변경하고싶은 내용으로 변경되게 된다.

~~~javascript

var urlPattern = /\b(?:https?):\/\/[a-z0-9-+&@#\/%?=~_|!:,.;]*/gim;
var content = '생활코딩 : http://opentutorials.org/course/1 입니다. 네이버 : http://naver.com 입니다. ';
var result = content.replace(urlPattern, function(url){
    return '<a href="'+url+'">'+url+'</a>';
});
console.log(result);
//생활코딩 : <a href="http://opentutorials.org/course/1">http://opentutorials.org/course/1</a> 입니다. 네이버 : <a href="http://naver.com">http://naver.com</a> 입니다.

~~~

