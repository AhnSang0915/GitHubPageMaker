---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 객체지향-Object
date: 2022-03-19 23:10 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 객체지향-Object

## 1. Object란?
<br>
<br>
Object객체는 객체의 가장 기본적인 형태를 가지고 있는 객체이다. 다시 말해서 아무것도 상속받지 않는 순수한 객체다. Javascript에서는 값을 지정하는 기본적인 단위로 Object를 사용한다. 
<br>
<br>

~~~javascript

var grades = {'egoing': 10, 'k8805': 6, 'sorialgi': 80};

~~~

우리는 이전에 property에대해 배울 때 Ultra, Super, Sub라는 생성자 예제를 통해 상속에대해 알아보았다. Sub는 Super를 Super는 Ultra를 상속받았다. Ultra는 최상위에 있는것처럼 보이지만 암시적으로는 사실 Object라는 객체에 상속되어 있는것이다. Object라는 객체의 프로퍼티는 모든 객체가 갖고있는 프로퍼티가 되는것이다. 즉 Object의 prototype은 모든객체가 사용할 수 있는 prototype이 된다는 것이다. 우리가 모든 객체가 가지고 있었으면 하는 기능이 있다면 Object의 prototype에 우리가 직접 기능을 추가하는 것을 통해서 모든객체가 그기능을 갖게 할 수 있다는 것이다.


---

## 2. Object API사용법
<br>
<br>
Object.keys는 배열이 어떠한 인덱스값을 가지고 있는지 배열로 리턴하는 메소드이다. 따라서 첫번째 결과는 Object.keys(arr)['0', '1', '2'] 이된다. toString은 문자열을 리턴해준다고 생각하자. 중요한 것은 Object.keys()와 Object.prototype.toString()에서 prototype이 있고 없고의 차이가 뭔지 알아야한다. prototype이 있는 것은 어떠한 객체를 만든다. 그리고 그객체를 담고있는 식별자. toString이라고 한다. 그런데 prototype이 없는 Object.keys같은 경우에는 Object.keys(arr)처럼 어떠한 인자를 받아서 처리한다. 이러한 차이는 Object라고 하는 것이 생성자 함수인 것이다. 함수는 javascript에서 객체이기 때문에 프로퍼티를 가질수 있다. 그래서 Object.keys가 가능한 것이고 이렇게 정의되었을 것이다 Object.keys = function(){}. toString의 경우는 prototype의 프로퍼티이다. 즉 Object.prototype.toString = function(){} 로 정의되어 있다. 어떠한 메소드가 new Object를 실행을 시키는 순간에 어떠한 객체를 만들고 그객체는 prototype이라고 하는 특수한 프로퍼티에 저장되어있는 객체를 원형으로 하는 객체가 생성이 되는것이다. 그렇게 생성된 객체는 toString이라는 메소드를 사용할 수 있기 때문에 메소드로서 사용하게 되는것이다.

~~~javascript

//Object.keys()
var arr = ["a", "b", "c"];
console.log('Object.keys(arr)',Object.keys(arr));

//Object.prototype.toString()
var o = new Object();
console.log('o.toString()',o.toString());

var a = new Array(1,2,3);
console.log('a.toString()'),a.toString());


~~~

---

## 3. Object 확장
<br>
<br>
우리가 필요한 기능을 모든 객체에서 사용 가능한 Object를 만드는 방법을 알아보자.
<br>
<br>
아래 배열과 객체에서 contain.(인자)메소드로 어떤 인자를 전달하게되면 인자가 해당 되는 값이 그 객체나 배열에 있다면 true 없다면 false를 리턴하게하는 코드를 만들어 보았다. 모든 객체의 부모는 Object이기 때문에 Object라고 적어주고, o와a모두 객체이다. 객체에 어떤 기능, 메소드를 갖도록 추가하고 싶다면 prototype이라고하는 프로퍼티안의 객체를 변경하면 된다. for in문으로 배열과 객체를 차례로 나열하여 값을 확인하는 코드를 작성했다. 아래 코드에서 메소드 안의 this는 그 메소드가 소속되어있는 객체를 의미한다. name에는 각각의 객체에대한 키값이 담기게 된다. 현재 열거되고 있는 value값을 가져오려면 this[name]으로 가져오고 그값과 neddle을 비교하여 두 값이 일치하면 true를 리턴한다. 마지막 value까지 나열했는데 일치하는 값이 없다면 false를 리턴한다.



~~~javascript

Object.prototype.contain = function(neddle) {
    for(var name in this){
        if(this[name] === neddle){
            return true;
        }
    }
    return false;
}
var o = {'name' : 'ansang', 'city' : 'suwon'}
console.log(o.contain('ansang'));
var a = ['ansang', 'sang', 'hyun'];
console.log(a.contain('sang'));

~~~


---

## 4. Object 확장의 위험
<br>
<br>
확장의 위험성에 대해 알아보자. 확장을 함으로써 모든 객체에 영향을 주기때문에 주의해야한다.
<br>
<br>
크롬 개발자 도구에서 아래 코드를입력후 for(var name in o){console.log(o[name]);}을 출력한 결과를 보자. 함수까지 출력된 상황이다. 이유는 contain이 포함되었기 때문이다. 개발자 도구에서 다시 코드를 작성해보자. for(var name in o){console.log(name)}의 결과는 name, city, contian이다.for(var name in a){console.log(name)}의 실행결과 역시 0,1,2,contain이다. 

~~~javascript

Object.prototype.contain = function(neddle) {
    for(var name in this){
        if(this[name] === neddle){
            return true;
        }
    }
    return false;
}
var o = {'name' : 'ansang', 'city' : 'suwon'}
console.log(o.contain('ansang'));
var a = ['ansang', 'sang', 'hyun'];
console.log(a.contain('sang'));

// 개발자 도구에서 for(var name in o){console.log(name)}을 출력한 결과
for(var name in o){
    console.log(o[name]);}
VM693:2 ansang
VM693:2 suwon
VM693:2 ƒ (neddle) {
    for(var name in this){
        if(this[name] === neddle){
            return true;
        }
    }
    return false;
}
// 개발자 도구에서 for(var name in a){console.log(name);}을 출력한 결과

1
2
contain

~~~

부모로 부터 contain이라는 프로퍼티까지 상속받았기 때문에 위와같은 결과가 나오는 것이다. 그렇다면 이런 문제를 해결할수 있는 메소드를 알아보자. a.hasOwnProperty(name)는 실행되는 객체가 인자로 전달된 값을 자신의 프로퍼티로 가지고 있는지 확인할 수 있는 메소드이다. contain은 부모로부터 상속받은 프로퍼티이기 때문에 어떠한 프로퍼티의 이름이 그객체의 직접적으로 정의되어있는지 확인하는 기능인 hasOwnProperty로 구별할 수 있다.


~~~javascript

Object.prototype.contain = function(neddle) {
    for(var name in this){
        if(this[name] === neddle){
            return true;
        }
    }
    return false;
}
var o = {'name' : 'ansang', 'city' : 'suwon'}
var a = ['ansang', 'sang', 'hyun'];

for(var name in o){
    if(o.hasOwnProperty(name)){
        console.log(name)
    }
}
//name, city
for(var name in a){
    if(a.hasOwnProperty(name)){
        console.log(name)
    }
}
//0,1,2
~~~


## 5. prototype vs __proto__
<br>
<br>
이번엔 prototype과 \__proto__의 관계를 알아보자. 그전에 함수란 무엇인가를 확인해 보면. 함수는 javascript에서는 객체이다. function Person(){}는 var Person = new Function();으로 표현할수 있다. javascript에서 함수는 객체이기 때문에 프로퍼티를 가질 수 있다. 
<br>
<br>
아래와 같은 함수를정의하면 객체이기 때문에 함수에 해당되는 Person이라고하는 객체가 생성되고 Person의 prototype이라는 객체가 하나 더 생긴다. 두개의 객체는 서로 연관되어 있기 때문에 Person이라고하는 객체는 내부적으로 prototype이라는 프로퍼티가 생기고 그 프로퍼티는 Person의 prototype객체를 의미한다. 그래서  Pserson.prototype이라 함은 Person의 prototype객체를 의미한다. Person의 prototype객체도 자신이 Person의 소속인것을 표시하기 위해서 어딘가에 기록해야한다. 그러기 위해서 Person의 prototype객체 안에 constructor라고하는 프로퍼티를 만들고 이 프로퍼티는 Person을 가르키게 된다. 서로간의 상호참조를 하고있는 것이다. Person은 prototype프로퍼티를 통해서 Person의 prototype객체를 가르키고 Person의 prototype객체는 constructor프로퍼티를 통해서 Person객체를 가르킨다는 것이다. 그다음person.prototype.sum = function(){} 를정의하게 되면 Person의 prototype객체에 sum이라는 함수가 없기때문에 생성하고 함수를 정의한다. var kim=new Person('kim',10,20) 이렇게 객체를 생성하면 kim이라고하는 객체가 생성되고 kim이라는 객체 안에 프로퍼티 값으로 name,first,second 그리고 \__proto__가 생성이 된다. kim객체의 __proto\__ 프로퍼티는 Person의 prototype객체를 의미한다. 그렇다면 Person.prototype을통해서 Person의 prototype객체에 접근할 수 있고, kim.__proto__를 통해서도 접근 할 수 있다. var lee = new Person('lee',10,10)를 통해서도 같은 접근을 할 수 있다. console.log(kim.name)을하면 name이라는 프로퍼티가 있는지를 확인하고 그값을 출력할 것이다. 만약 name이라는 값이 없다면 \__proto__가 가르키는 객체에 name이 있는지 다시 찾아본다. kim.sum()을 하게 되면 kim이라는 객체에는 sum이라는 메소드가 없다. 그렇다면 javascript는 __proto__가 가르키는 Person의 prototype객체에 sum이 있는지 찾는다. 이런식으로 prototype이 동작하는 것이다.

![프로토타입 설명](https://media.vlpt.us/images/turtle601/post/93a9e49b-c4a0-428a-825b-b73adca66227/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-08-30%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%209.29.11.png)

~~~javascript

function Person(name, first, second){
    this.name = name;
    this.first = first;
    this.second = second;
}

person.prototype.sum = function(){}

var kim = new Person('kim',10,20)
var lee = new Person('lee',10,10)

console.log(kim.name)
kim.sum()
~~~