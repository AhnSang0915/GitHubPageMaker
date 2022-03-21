---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 객체지향 - 생성자와 new
date: 2022-03-16 18:17 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---
{% include javascript-table-of-contents.html %}


# JavaScript 객체지향 - 생성자와 new

<br>
<br>

---

## 1.자바스트립트의 객체지향
<br>
<br>
Javascript는 어떠한 객체지향 언어와도 같지않다. Javascript만의 독특한 성질을 갖고있고, Javascript의 계열에 속하는 언어들은 prototype-based programming이라 부른다. Javascript도 여기에 속해있는 언어다. 전통적인 함수형 언어의 특성을 그대로 갖고있는게 아니고 객체지향언어가 갖고있는 문법을 비슷하게 사용하면서 사실은 함수형언어의 특성을 갖고있다. 객체지향 프로그래밍을 간단하게 이야기하면 서로 연관되어있는 변수와 메소드를 하나의 객체라고하는 그릇에 넣는것이다. 그리고 서로 연관되어있지 않은 것들은 별도의 객체에다 분리를 시켜놓는 것이 객체지향 프로그래밍의 기본적인 형태라고 할 수 있다. 연관되어 있는 로직들을 객체화 시키게되면 각각의 로직들은 하나하나가 독립된 프로그램처럼 독립성을 갖게된다. 독립성을 갖게된다는것은 여러 완제품의 부품으로 사용될 수 있다는 것이다. 우리가 객체지향 프로그래밍으로 도달하고자하는 목표는 좋은 부품을 만드는 것이라고 할 수 있겠다. 

---

## 2. 객체 생성
<br>
<br>
객체를 만들어 보자. {}를 사용하면 비어있는 객체를 만드는 것이고, oject라는 이름의 object를 만드는 것이다. 비어있는 상자라고 생각하자.  person.name 이라고하면 object라는 그릇에 name이라는 변수를 담은것이다. 그변수의 내용은 문자열 'ansang'이 되는것이다. 그런데 우리는 객체에 담겨있는 변수를 변수라고 하지않고 프로퍼티(property)라고 부를것이다. 그리고 우리는 또다른 프로퍼티로 person.introduc 를 넣었다. 프로퍼티 안에 함수를 담게되면 우리는 메소드라고 부르기로했다. 객체 내의 변수를 프로퍼티(property) 함수를 메소드(method)라고 부른다는 것이다. 아래 예제를 실행을 시키면 함수가 실행이 되는데 
'My name is '+this.name 의 this는 함수가 속해있는 객체, person이 담고있는 객체를 의미하는 것이다. person이 담고이있는 객체는 person.name = 'egoing'으로 this.name은 'ansang'을 의미하게 된다. 그런데 아래 코드는 객체를 만들었는데 객체안에 들어갈 여러 프로퍼티가 객체와 분리가 되어있다. 그렇다보니 그 과정에서 중간에 다른 코드가 끼어든다거나 여러가지 이유로 인해서 객체를 정의하는 부분이 집중도가 떨어질 수 있다. 

~~~javascript

var person = {} //비어있는 객체 
person.name = 'ansang';
person.introduce = function(){
    return 'My name is '+this.name; 
}
document.write(person.introduce());

~~~

위와같은 문제를 방지하는 것이 우리가 직접 객체를 시작하고 닫는 기호 사이에 프로퍼티와 메소드를 직접 정의해 주는것이다.

~~~javascript

var person = {
    'name' : 'ansang',
    'introduce' : function(){
        return 'My name is '+this.name;
    }
}
document.write(person.introduce());

~~~

만약에 person이라는 객체를 여러개 만들어서 여러사람에대한 정보를 담을수 있는 person객체를 만든다고 하면 아래처럼 만들면 될까? 
~~~javascript

var person1 = {
    'name' : 'ansang',
    'introduce' : function(){
        return 'My name is '+this.name;
    }
}
var person2 = {
    'name' : 'ansanghyun',
    'introduce' : function(){
        return 'My name is '+this.name;
    }


~~~
1,2로 두개의 객체를 만들었다. 문제는 name을 정의하는 부분과 introduce메소드 부분이 중복되어있다. name은 각각의 데이터가 다르기때문에 완전한 중복이라고는 보기힘들지만 메소드 부분은 완벽히 같은 내용으로 중복되어있다. 이것들이 같은 취지의 객체라고 한다면 그 객체가 가지고있는 메소드를 찾아서 똑같이 바꿔줘야하는 이슈가 생긴다. 이것은 프로그래머들이 혐오하는 중복이 발생한 것이다. 중복이 있다는것은 가독성이 떨어지고 코드의 양이 많아져 유지보수가 힘들어진다는 것이다. 이문제를 해결할 수 있는 방법은 중복을 제거하는 것이고 그방법은 생성자,new라는 것이다.

---

## 3.생성자와 new
<br>
<br>

### 생성자
<br>
<br>
생성자(constructor)는 객체를 만드는 역할을 하는 함수다. 자바스크립트에서 함수는 재사용 가능한 로직의 묶음이 아니라 객체를 만드는 창조자라고 할 수 있다.<br>
아래는 개발자 도구에서 실행한 코드이다. new를 붙이고 함수를 호출하게 되면 함수는 그냥 함수라고 하지 않고 생성자라고 부른다. 이생성자는 객체의 생성자이고 비어있는 객체를 만들어 p에 반환한다. 그래서 p에는 
person {}의 비어있는 객체가 만들어졌다.


~~~javascript

function person () {} //함수를 만들었다. 함수는 어떠한 값도 담고있지 않다.
undefined
var p0 = person(); //함수에 변수를 지정했다.
undefined
p0                  //p0의 값이 없다고 나온다.
undefined
var p = new person(); // new를 추가하고 실행하면 아래와같은 객체가 만들어진게 보인다. 
undefined
p
person {} // var p = {} 과 같다고 볼수있다. (완전히 같진 않지만 지금 단계에서는.)

~~~

자바스크립트에서는 원시타입(숫자, 불린값, null과 undefined)를 제외한 모든 값이 객체이다.객체를 생성하는 방법에는 2가지가 있는데 객체리터럴과 생성자로 객체를 만들 수 있는데 아래 예제는 객체 리터럴{}로 객체를 생성한 것과 같은 방법이라고 할 수 있다.

~~~javascript

function Person(){}
var p = new Person();
p.name = 'egoing';
p.introduce = function(){
    return 'My name is '+this.name; 
}
document.write(p.introduce());

~~~

아래 예제는 객체리터럴로 객체를 생성해 introduce 메소드 부분이 중복된 상황이다. 

~~~javascript

function Person(){}
var p1 = new Person();
p1.name = 'egoing';
p1.introduce = function(){
    return 'My name is '+this.name; 
}
document.write(p1.introduce()+"<br />");
 
var p2 = new Person();
p2.name = 'leezche';
p2.introduce = function(){
    return 'My name is '+this.name; 
}
document.write(p2.introduce());

~~~

위의 중복된 상황을 해결하기 위해 new를 사용해 생성자를 사용해 코드를 바꾸었다. 생성자함수( new 연산자와 함께 호출하여 객체(인스턴스)를 생성하는 함수를 말한다. 생성자 함수에 의해 생성된 객체를 인스턴스(instance)라 한다.) 코드를 통해서 알 수 있듯이 생성자 함수는 일반함수와 구분하기 위해서 첫글자를 대문자로 표시한다. Person이라는 함수를 작성했고 var p1 = new Person 함수의 앞에 new를 배치해 Person이라는 함수는 생성자가 된것이다. 인자로 'ansang'을 배치해 그값은 name에 들어간다 그리고 name은 this.name = 'ansang' 이된다. 즉 이객체의 프로퍼티의 값이 ansang이 된것이다. 그리고 현재 객체의 introduce라고하는 프로퍼티에 함수를 정의해 메소드를 만들었다. 생성자 함수가 다실행된 후에 p1에 담겨지게 된다. p1,p2에 new Person('ansang');, new Person('sanghyun'); 를통해 생성자에 전달해 introduce라는 부분이 간단해졌다. 우리가 Person이라는 생성자가 만들어 놓은 빈 객체가 가져야할 프로퍼티와 메소드를 생성자 함수안에 기술하는것으로 인해서 그객체가 가지고있 정보와 객체가 할수 있는 일,이러한 것들을 이렇게 세팅해 주고 있는데 이런것들을 초기화 라고하고 줄여서init또는 initialize라고 한다. 즉 중요한 점은 생성자를 통해 객체를 초기화를 했다는 것이다.

~~~javascript

function Person(name){
    this.name = name; 
    this.introduce = function(){
        return 'My name is '+this.name; 
    }   
}
var p1 = new Person('ansang');
document.write(p1.introduce()+"<br />");
 
var p2 = new Person('sanghyun');
document.write(p2.introduce());

~~~