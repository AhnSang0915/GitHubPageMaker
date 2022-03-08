---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 모듈
date: 2022-03-08 19:32 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 모듈

<br>
<br>
<br>

## 1. 모듈이란?
<br>
<br>
프로그램은 작고 단순한 것에서 크고 복잡한 것으로 진화한다. 이과정에 필요한 것은 코드의 재활용성, 유지보수의 편의성등이 있다. 어떤 프로그램을 구성하고 있는 수만은 로직들을 재사용 할 수 있는 단위로 조각조각 나누어 구획화를 시켜 별도의 모듈이라는 형태로 떼어내 이것을 또다른 프로그램의 부품으로 사용하는 기법, 그런 부품들을 모듈이라 하고 이러한 기법을 모듈화 라고 한다. 아래는 모듈화를 통해 얻을 수 있는 효과이다.<br>

- 자주 사용되는 코드를 별도의 파일로 만들어서 필요할 때마다 재활용할 수 있다.
- 코드를 개선하면 이를 사용하고 있는 모든 애플리케이션의 동작이 개선된다.
- 코드 수정 시에 필요한 로직을 빠르게 찾을 수 있다.
- 필요한 로직만을 로드해서 메모리의 낭비를 줄일 수 있다.
- 한번 다운로드된 모듈은 웹브라우저에 의해서 저장되기 때문에 동일한 로직을 로드 할 때 시간과 네트워크 트래픽을 절약 할 수 있다. (브라우저에서만 해당)

<br>
Javascript에서는 모듈이라는 개념이 분명하게 존재하지 않는다. Javascript에서는 모듈이라는 기능 자체를 제공하지 않는다. 구동 환경(호스트 환경)에 따라서 Javascript로직 구성을 모듈형식으로 구성해 사용한다.
<br>


## 2.모듈화
<br>
<br>
모듈화를 알기 전에 모듈이 없다는 가정을 해보자. 그리고 funcion함수가 엄청 복잡하다고 가정하고, 함수 호출도 여러번하며 html파일이 아래 welcome이라는 함수를 여러 html에서 호출한다고 생각해보자. 그렇다면 welcome이라는 함수를 해당 페이지에 두는것은 덩치가 엄청 커질것이다. 이런경우 내가 필요한 코드와 그렇지 않은 코드를 분류하는게 힘들어 질 것이다. welcome이라는 함수를 별도의 파일로 빼고 그 별도의 파일을 읽어 오는것을 통해 welcome이라는 함수를 사용할 수 있다면 복잡한 코드가 한줄로 바뀔 수 있다.

~~~html

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
</head>
<body>
    <script>
        function welcome(){
            return 'Hello world'
        }
        alert(welcome());
    </script>
</body>
</html>

~~~

아래 예제에서 별도의 파일로 js를 불러오는 형식을 알아보자. 아래 내용을 코드를 에디터를 활용해 실행해보자. greeting.js 라는 파일에 위 예제에서 사용한 function함수를 저장하고 불러오는 형식이다.
\<script type="text/javascript" src="greeting.js"\>\</script\> 그다음 welcom함수를 호출하면 greeting.js파일에서 불러오게 된다. 다른 html파일에서도 마찬가지로 위 코드로 불러와 함수를 사용할 수 있다.


~~~html

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <script type="text/javascript" src="greeting.js"></script>
</head>
<body>
    <script>
        alert(welcome());
    </script>
</body>
</html>


~~~


---

## 3.node.js의 모듈화
<br>
<br>
모듈을 로드하는 방법은 호스트 환경에 따라서 달라진다. Node.js에서는 아래와 같은 방법으로 모듈을 로드한다..

~~~javascript

var PI = Math.PI;
  
exports.area = function (r) {
return PI * r * r;
};
  
exports.circumference = function (r) {
return 2 * PI * r;
};

~~~

~~~javascript

var circle = require('./node.circle.js');
console.log( 'The area of a circle of radius 4 is '
           + circle.area(4));

~~~

---

## 4.라이브러리