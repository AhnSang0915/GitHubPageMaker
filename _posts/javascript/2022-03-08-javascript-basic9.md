---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 모듈
date: 2022-03-08 23:58 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---
{% include javascript-table-of-contents.html %}


# JavaScript 모듈

<br>
<br>

---

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
모듈을 로드하는 방법은 호스트 환경에 따라서 달라진다. Node.js에서는 아래와 같은 방법으로 모듈을 로드한다.

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
<br>
<br>
라이브러리는 자주 사용되는 로직을 재사용되기 편리하도록 잘 정리한 일련의 코드들의 집힘을 의미한다고 할 수 있다. 오픈 소스를 통해 만들어진 수많은 라이브러리가 있기 때문에 우리가 만들고자 하는 프로그래밍의 핵심적인 부분이 아니라면 공개되어있는 좋은 라이브러리를 선택하고 잘 사용하는 것은 프로그래밍의 핵심이라고 할 수 있다. Javascript로 웹 브라우저를 제어하는 방법은 기본적으로 웹 브라우저가 제공하는 기능, Javascript가 제공하는 기능을 이용해 모든 것을 다 할 수 있다. 다르게 말하면 웹 브라우저와 Javascript가 제공하지 않는 기능은 전혀 사용할 수 없다. 왜냐하면, 브라우저가 허용하는 기능만을 쓸 수 있기 때문이다. 브라우저의 기능이 너무 다양하고 파편화되어 있기 때문에 라이브러리를 사용한다. 라이브러리는 어떤 목적을 정해놓고 목적을 쉽게 달성할 수 있게 만들어놓은 프로그래밍의 집합이기 때문이다. 우리가 사용해볼 라이브러리는 query다.


---


## 5. 라이브러리 사용하기
<br>
<br>
jQuery를 이용한 예제와 사용방법을 알아볼 것이다. 하지만 jQuery에 대한 공부를 하는것 보다 어떻게 사용하는지에 대한 예제 이기 때문에 jQuery강의를 보고 공부를 해야한다. 아래 코드list에있는 empty를 한번에 coding paratice gym으로 바꾸는 예제이다. 아래의 상태에서

~~~html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <ul id="list">
        <li>empty</li>
        <li>empty</li>
        <li>empty</li>
        <li>empty</li>
    </ul>
</body>
</html>

~~~

아래 예제 처럼 변경해준다. 아래 jQuery를 사용한 3줄의 코드로 작업을 수행하게 되었다.

~~~html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script type="text/javascript" src="./jquery.js" ></script>
</head>
<body>
    <ul id="list">
        <li>empty</li>
        <li>empty</li>
        <li>empty</li>
        <li>empty</li>
    </ul>
    <input type="button" value="execute" id="execute_btn"/>
    <script type="text/javascript">
        $('#execute_btn').click(function(){
            $('#list li').text('coding practice gym');
        });
    </script>
</body>
</html>

~~~

하지만 jQuery를 사용하지 않으면 아래 예제처럼 쉽지않은 프로그래밍을 해야한다.

~~~html

<!DOCTYPE html>
<html>
<body>
    <ul id="list">
        <li>empty</li>
        <li>empty</li>
        <li>empty</li>
        <li>empty</li>
    </ul>
    <input id="execute_btn" type="button" value="execute" />
    <script type="text/javascript">
    function addEvent(target, eventType,eventHandler, useCapture) {
        if (target.addEventListener) { // W3C DOM
            target.addEventListener(eventType,eventHandler,useCapture?useCapture:false);
        } else if (target.attachEvent) {  // IE DOM
            var r = target.attachEvent("on"+eventType, eventHandler);
        }
    }
    function clickHandler(event) {
        var nav = document.getElementById('list');
        for(var i = 0; i < nav.childNodes.length; i++) {
            var child = nav.childNodes[i];
            if(child.nodeType==3)
                continue;
            child.innerText = 'Coding everybody';
        }
    }
    addEvent(document.getElementById('execute_btn'), 'click', clickHandler);
    </script>
</body>
</html>

~~~

이번 강의에선 라이브러리가 중요하다는 것을 알아야 한다. 세세하게 어떻게 하는지 알려고 하는 것보단 라이브러리의 장점과 편의성에 초점을 맞추고 이후 나오는 내용에서 자세히 알아볼 시간이 있을 것이다.