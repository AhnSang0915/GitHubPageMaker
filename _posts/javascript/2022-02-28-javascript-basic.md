---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 기본 
date: 2022-02-28 21:34 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 기본 

<br>
<br>
<br>

## 1. 주석 (Comment)
<br>
<br>

주석은 JavaScript Code외의 우리가 쓰는 문자로 사용되는 내용을 말한다.<br>
코드 내용에대한 부연설명이나 함수에 대한 기능을 작성할수 있고 불필요한 코드의 실행을 막을수 있다.<br>

---

### **JavaScript주석의 코드 사용 방법**

<br>
<br>

한줄 주석의 경우 - // 내용<br>
여러 줄의 경우 - /* 내용 */ 로 사용한다

~~~javascript
// 한줄 주석 사용시

/* 
    여러줄 
    주석 
    사용시
*/
~~~
<br>
<br>
## 2. 줄바꿈과 여백
<br>
<br>

JavaScript의 경우 명령이 끝났다는걸 알려주기 위해 ;를 표시해준다 <br>
줄바꿈을 할 경우엔 JavaScript에서 자동으로 명령이 끝났다고 판단하지만 한줄에 여러 명령을 쓸 경우가 있어 명령어 뒤엔 ;를 붙여주는게 좋다.
<br>
<br>

---

~~~javascript
    <script type="text/javascript">
        var a = 1; //;을 안넣어도 줄이 바뀌면 명령이 끝났다고 인식한다
        alert(a);
    </script>
~~~
<br>
위 코드에서 ;기호를 없애도 줄바꿈을 했기 때문에 명령이 끝났다고 인식할 것 이다.
하지만
<br>
~~~javascript
    <script type="text/javascript">
        var a = 1; alert(a); //;가 없다면 var a = 1alert(a) 가 될것이다.
        
    </script>
~~~

<br>
이런 경우엔 ;가 없다면 하나의 명령이 될 것이다.( var 뒤 띄어쓰기를 해야 하고 =양쪽엔 하지 않아도 된다.)
<br>  
그리고 코드를 썼는데 코드가 다닥다닥 붙어 있다면 코드를 보기 힘들 것이다.<br>
<u> 가독성이 좋지 않다는 말이다. </u>  
Tap키를 명령어와 함수 사이에 적절히 사용해 좀 더 보기 좋게 하는 게 좋을 것이다.


