---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 객체지향 - 상속
date: 2022-03-18 18:30 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 객체지향 - 상속

<br>
<br>

---

## 1. 상속(inheritance)이란?
<br>
<br>
우리가 객체라고 하는 것은 하나의 컨테이너고 변수나 메소드가 하나의 객체 안에 상속되어있다. 이런 객체의 특성으로 인해 객체를 그대로 물려받은 새로운 객체를 만들 수 있다. 이 객체는 부모에 해당 되는 객체의 변수의 메소드에 접근할 수 있게 된다. 즉 상속이란 오리지널 객체가 갖고있는 기능을 상속받는 객체가 동일하게 가질 수 있다는 것이다.
<br>
<br>
Person이라고 하는 생성자를 만들었고 그 생성자에 new를 사용해 새로운 객체를 만들었다. 그 객체는 name이라고 하는 프로퍼티와 introduce라고 하는 프로퍼티를 가지고 있고, name의 값은 person에 인자로 전달된 값이 name으로 사용된다. 아래 코드를 실행하면 'My name is ansang'이 출력된다.

~~~javascript

function Person(name){
    this.name = name;
    this.introduce = function(){
        return 'My name is '+this.name; 
    }   
}
var p1 = new Person('ansang');
document.write(p1.introduce()+"<br />");

~~~

아래도 마찬가지로 Person이라고 하는 생성자를 만들었고 그 아래 생성자에 portotype이라고 하는 특수한 프로퍼티에 name이라고 하는 프로퍼티를 준 것이다. 즉 Person이라고 하는 생성자에는 prototype 프로퍼티가 있는데 그 안에 어떤 객체가 들어가있다. 그객체 .name을 하게 되면 어떤 값을 줄 수 있게 되는것이고 그객체 .introduce하고 함수를 할당을 하게 되면 어떤 메소드를 지정할 수 있는 것이다. 

~~~javascript

function Person(name){
    this.name = name;
}
Person.prototype.name=null;
Person.prototype.introduce = function(){
    return 'My name is '+this.name; 
}
var p1 = new Person('ansang');
document.write(p1.introduce()+"<br />");

~~~



---

## 2. 상속의 사용법
<br>
<br>
아래는 우리가 처음에 본 예제에서 Programmer라는 생성자를 추가한 것이다. Programmer라는 생성자를 통해 만든 객체가 Person이라는 생성자를 통해서 만들어진 객체와 동일한 기능성을 갖도록 코드를 작성한 것이다.
new Programmer('ansang');를 통해서 Programmer라는 생성자를 호출했다. name이라는 프로퍼티 값을 ansang으로 지정을 했다. p1.introduce을 사용하려고 하는데 생성자 Programmer에는 introduce라는 메소드가 정의되어 있지 않다. introduce메소드는 Person이라고 하는 생성자에 정의되어 있는데 여기서 Programmer.prototype = new Person();로 Person 생성자의 프로퍼티와 메소드를 가져오게 된다. 우리는 Programmer에서 name의 값을 ansang으로 주었고 Programmer.prototype = new Person();에서 prototype 라는 어떠한 객체의 값이 생성자 Person과 같다고 했기 때문에 name은 ansang이되고 introduce메소드를 사용할 수 있는 것이다.

~~~javascript

function Person(name){
    this.name = name;
}
Person.prototype.name=null;
Person.prototype.introduce = function(){
    return 'My name is '+this.name; 
}
 
function Programmer(name){
    this.name = name;
}
Programmer.prototype = new Person();
 
var p1 = new Programmer('ansang');
document.write(p1.introduce()+"<br />");


~~~

## 3. 기능의 추가
<br>
<br>
상속을 받는 객체를 만들었다면 기능을 추하가는 기능을 알아보자. Person이라고하는 공통의 부모가 있고 Programmer, Designer라는 객체가 person이라는 객체를 상속받는 형식이다. 

~~~javascript

function Person(name){
    this.name = name;
}
Person.prototype.name=null;
Person.prototype.introduce = function(){
    return 'My name is '+this.name; 
}
 
function Programmer(name){
    this.name = name;
}
Programmer.prototype = new Person();
Programmer.prototype.coding = function(){
    return "hello world";
}
function Designer(name){
    this.name = name;
}
Designer.prototype = new Person();
Designer.prototype.design = function(){
    return "beautiful";
}
 
var p1 = new Programmer('ansang');
document.write(p1.introduce()+"<br />");
document.write(p1.coding()+"<br />");

var p2 = new Designer('nibagman');
document.write(p2.introduce()+"<br />");
document.write(p2.design()+"<br />");

~~~

여기서 My name is를 My nickname is로 바꾸면 <br>
My nickname is ansang<br>
hello world<br>
My nickname is nibagman<br>
beautiful<br>
의 값을 출력하게 된다. 이말은 Person이라는 생성자를 상속받은 객체들의 값도 바뀐다는 말이다.

~~~javascript

function Person(name){
    this.name = name;
}
Person.prototype.name=null;
Person.prototype.introduce = function(){
    return 'My nickname is '+this.name; 
}
 
function Programmer(name){
    this.name = name;
}
Programmer.prototype = new Person();
Programmer.prototype.coding = function(){
    return "hello world";
}
function Designer(name){
    this.name = name;
}
Designer.prototype = new Person();
Designer.prototype.design = function(){
    return "beautiful";
}
 
var p1 = new Programmer('ansang');
document.write(p1.introduce()+"<br />");
document.write(p1.coding()+"<br />");

var p2 = new Designer('nibagman');
document.write(p2.introduce()+"<br />");
document.write(p2.design()+"<br />");

~~~


---

## 4. prototype
<br>
<br>
그럼 prototype이란 무엇인가? 한국어로는 원형정도로 번역되는 prototype은 말 그대로 객체의 원형이라고 할 수 있다. 함수는 객체다. 그러므로 생성자로 사용될 함수도 객체다. 객체는 프로퍼티를 가질 수 있는데 prototype이라는 프로퍼티는 그 용도가 약속되어 있는 특수한 프로퍼티다. prototype에 저장된 속성들은 생성자를 통해서 객체가 만들어질 때 그 객체에 연결된  다.
<br>
<br>
생성자는 기본적으로 함수이다. 우리가 이 함 수를 호출할 때 new를 사용하면 생성자가 되는 것이고 그렇게 해서 실행된 결과로 새로운 객체를 만들고 이 객체는 o에 들어가게 된다. 그런데 비어있는 객체를 만드는 것만이 생성자의 역할이라고 한다면 그렇게 효율적이지 못하다. 생성자를 사용하는 이유는 우리가 객체를 생성했을 때 그 객체가 가져야 할 방법이나 프로퍼티 값을 가지고 우리에게 주어지기를 바라기 때문이다. 우리가 어떤 객체를 생성했을 때 객체가 가지고 있어야 하는 방법과 프로퍼티 prototype이라는 프로퍼티에 저장이 되는 것이다. 즉 prototype는 어떠한 객체가 정의가 되어있다는 것이다. 그렇게 하고 new를 이용해 생성자 함수를 생성하게 되면 Javascript는 생성자 함수의 prototype에 저장되어있는 객체를 꺼내서 그것을 돌려보내 주게 된다. 코드를 보자. 우리가 Sub.prototype = new Super(); 라고 하면 생성자 function Super(){} 이 만든 객체 Super.prototype = newUltra(); 이 만든 값이 들어가는 것이고 그리고 생성자 function Super(){}의 값은 Super.prototype = newUltra();로 만들어진 객체가 담긴다는 것이다. 생성자 function Ultra(){}의 값은 Ultra.prototype.ultra Prop = true; 이기 때문에 true가 출력된다. 이러한 개념은 prototype chain 이라고 한다.


~~~javascript

function Ultra(){}
Ultra.prototype.ultraProp = true;
 
function Super(){}
Super.prototype = new Ultra();
 
function Sub(){}
Sub.prototype = new Super();
 
var o = new Sub();
console.log(o.ultraProp);

~~~

---

## 5. prototype chain
<br>
<br>
전에 본 코드를 아래와 같이 바꾸면 1을 출력하게 된다. 그이유는 javascript가 기본적으로 동작할 떄 o라는 객체가 ultraprop라는 값을 가지고 있는지 확인하고 우리가 o.ultraProp = 1;로 지정했기 때문에 1을 출력하게 된다. 

~~~javascript

function Ultra(){}
Ultra.prototype.ultraProp = true;
 
function Super(){}
Super.prototype = new Ultra();
 
function Sub(){}
Sub.prototype = new Super();
 
var o = new Sub();
o.ultraProp = 1;
console.log(o.ultraProp);

~~~

아래의 결과는 2가 된다. 코드를 실행하면 o라는 객체에 ultra Prop기 있는지 확인한다. 우리는 var o = new Sub();로 ultraProp에 대해선 정의한 바가 없다. 그래서 이 객체에 직접 ultraProp가 없다는 걸 확인하고, o라는 객체의 생성자를 알아내고(생성자를 알아내는 방법은 따로 있다.) Sub이라는 생성자의 prototype 객체를 확인해 그 객체의 프로퍼티 중에 ultraProp이 있는지 확인하고 그 값을 가져오게 된다.

~~~javascript

function Ultra(){}
Ultra.prototype.ultraProp = true;
 
function Super(){}
Super.prototype = new Ultra();
 
function Sub(){}
Sub.prototype = new Super();
Sub.prototype.ultraProp = 2;
 
var o = new Sub();
console.log(o.ultraProp);

~~~

아래의 결과는 3이다.

~~~javascript

function Ultra(){}
Ultra.prototype.ultraProp = true;
 
function Super(){}
Super.prototype = new Ultra();
 
function Sub(){}
var s = new Super();
s.ultraProp = 3;
Sub.prototype = s;
 
var o = new Sub();
console.log(o.ultraProp);

~~~

아래의 값은 4이다.

~~~javascript

function Ultra(){}
Ultra.prototype.ultraProp = true;
 
function Super(){}
var t = new Ultra();
t.ultraProp = 4;
Super.prototype = t;
 
function Sub(){}
var s = new Super();
Sub.prototype = s;
 
var o = new Sub();
console.log(o.ultraProp);

~~~

아래의 값은 true다.

~~~javascript

function Ultra(){}
Ultra.prototype.ultraProp = true;
 
function Super(){}
var t = new Ultra();
Super.prototype = t;
 
function Sub(){}
var s = new Super();
Sub.prototype = s;
 
var o = new Sub();
console.log(o.ultraProp);

~~~

주의할점은 어떠한 객체 super를 sub가 상속받고 싶다면 Sub.prototype에는 