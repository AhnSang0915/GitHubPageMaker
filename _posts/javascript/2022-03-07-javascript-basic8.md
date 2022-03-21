---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 객체(Object)
date: 2022-03-07 22:32 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---
{% include javascript-table-of-contents.html %}


# JavaScript 객체(Object)

<br>
<br>

---

## 1. 객체의 소개와 문법
<br>
<br>
배열은 연관되어 있는 데이터들을 담아내기 위한 그릇이다. 마찬가지로 객체도 연관된 데이터를 담아내는 것에 있어서 유사하다. 하지만 똑같은 그릇이 있다고 쳤을 때 객체도 그릇에 담아내는 것은 같지만 index의 값으로 숫자나 문자를 쓸 수도 있고, 인덱스로 우리가 원하는 데이터를 지정할 수 있다는 것이 둘의 차이점이라고 할 수 있다. 다른 언어에서는 연관배열(associative array) 또는 맵(map), 딕셔너리(Dictionary)라는 데이터 타입이 객체에 해당한다.
<br>
<br>


### 객체의 생성
<br>
<br>
객체를 만드는 법을 알아보자. 배열은 대괄호로 시작해 대괄호로 끝나지만,객체는 중괄호로 시작해 중괄호로 끝나게 된다. 아래는 데이터값으로 숫자를 썻지만 문자나 다른 데이터를 할당하는 것도 가능하다. 아래 예제에서 ansang은 key(index)가 되고 10은 value(데이터 값)가 된다.

~~~javascript

var grades = {'ansang': 10, 'sanghyun': 6, 'ansanghyun': 80};
            // key : value  key : value  key : value
 
~~~

위의 상태에서 객체를 대표하는 변수를 grades로 지정하고 grades를 호출하면 아래와 같은 값이 나오게 된다.

~~~javascript

grades

odject {ansang: 10, sanghyun: 6, ansanghyun: 80}

~~~

아래는 객체를 만드는 다른 방법이다.

~~~javascript

var grades = {};
grades['ansang'] = 10; //key는 ansang value는 10
grades['sanghyun'] = 6; //key는 sanghyun value는 6
grades['ansanghyun'] = 80; //key는 ansanghyun value는 80

~~~

위에서 객체를 호출하는 방법은 아래와 같다. 아무래도 garade.ansang가 간편하지만, 프로그래밍 적인 기재가 불가능하다 이 경우 garade.'an'+'sang'로 호출하게 되면 SyntaxError가 나오게 된다. 즉 . 뒤의 내용을 프로그래밍 적으로 만들 수 없다. []안에 들어가는 값은 프로그래밍 적으로 생성이 가능하기 때문에 필요에 따라 대괄호 안에 작성하는 게 편리하거나 써야만 하는 상황이 있을 수 있다.

~~~javascript

grades['ansang'] //value 10
garade.ansang //value 10
grades['an'+'sang'] //value 10

~~~

---

## 2.객체와 반복문 for in
<br>
<br>
객체에 저장된 데이터를 기준으로 반복하는 작업을 알아보자. 배열은 저장된 데이터들이 순서를 가지고 있다. 그래서 배열에선 순서 자체가 중요한 정보이다. 하지만 객체엔 순서가 없고, key와 value로 이루어져 있기 때문에 저장된 순서는 없기 때문에 저장된 값이 순서에 따라서 나오지 않을 것 이라는 걸 인지해야 한다.

~~~javascript

var grades = {'ansang' : 10, 'sanghyun' : 6, 'ansanghynu' : 80}
for(key in grandes) {
    document.write("key : "+key+" value : " + grades[key] + "<br />");
}
/*출력
key : ansang value : 10
key : snaghyun value : 6
key : ansanghyun value : 80
*/

~~~
또는 key부분을 변수로 바꿔도 된다. 아래는 var name으로 바꿔보았다.
~~~javascript

var grades = {'ansang' : 10, 'sanghyun' : 6, 'ansanghynu' : 80}
for(var name in grandes) {
    document.write("key : "+name+" value : " + grades[name] + "<br />");
}
/*출력
key : ansang value : 10
key : snaghyun value : 6
key : ansanghyun value : 80
*/

~~~
더 보기 편하게 리스트 형태로 만들어보자. html에서의 ul태그와 li태그를 사용해본다.
~~~html

  <ul>
    <script type="text/javascript">
        var grades = {'ansang': 10, 'sanghyun': 6, 'ansanghynu': 80};
            for(var name in grades) {
            document.write("<li>key : "+name+" value : "+grades[name]+"</li>");
            }    
    </script>
  </ul>

        /* 출력
        -key : ansang value : 10
        -key : snaghyun value : 6
        -key : ansanghyun value : 80
        */
~~~
배열도 for in문으로 사용할수 있다. 배열에선 var name으로 지정한 값이 index가 됨으로 console.log(name)에서 012라는 index가 추출되고 console.log(arr[name])에선 abc라는 데이터가 출력된다. 

~~~javascript

var arr = ['a', 'b', 'c']
for(var name in arr) {
    console.log(name);
}
//출력 
//0
//1
//2
for(var name in arr) {
    console.olg(arr[name]);
}


~~~

---

## 3. 객체 지향 프로그래밍
<br>
<br>
객체 지향 프로그래밍이란 서로 연관되어있는 데이터와 처리형식을 하나의 그릇안에 그룹핑 해놓은 프로그래밍을 객체 지향 프로그래밍 이라한다.
<br>
<br>

객체에 담길 수 있는 값이 무엇지에 대해 알아보자. 아래 예제는 객체 안에 객체와 함수를 담았다. list라는 key 값에 {'ansang' : 10, 'sanghyun' : 8, 'ansanghyun' : 80}라는 value를 넣었고 이 value는 객체이다. show라는 key값에 function(){ alert('Hello World')}; 라는 value를 담았다. javascript에서는 함수도 일종의 값이고 함수도 변수에 저장될 수 있기 때문에 마찬가지로 값으로서의 함수도 객체 안에 저장될 수 있다(고하는데 아직 뭔 소린지 모르겠음).grades에 담긴 

~~~javascript

var grades = {
    'list' : {'ansang' : 10, 'sanghyun' : 8, 'ansanghyun' : 80},
    'show' : function(){
        alert('Hello World');
    }
}
alert(grades['list']['ansang']); //ansang이라는 key가 갖고있는 10이라는 value에 접근
alert(grades['show']); // 함수에 접근
~~~
this라는 키워드를 알아보자. this라는 것은 javascript에서 약속되어있는 변수이다. this 변수는 함수가 속해있는 객체를 가르치는 변수이다. 함수가 소속되어있는 객체를 가르친다는 말이다.아래 예제는 grades라는 객체가 갖고있는 key 값 중 show를 호출해 show 함수가 가진 this변수로 list객체{'ansang' : 10, 'sanghyun' : 8, 'ansanghyun' : 80}를 출력하게 된다.

~~~javascript

var grades = {
    'list' : {'ansang' : 10, 'sanghyun' : 8, 'ansanghyun' : 80},
    'show' : function(){
        alert(this.list);
    }
}
grades['show']();

~~~
이번엔 개발자 도구에서 console.log(name, this.list\[name\]);를 사용해 key와 value를 호출해보자. value를 호출하는 방법은 위에서 배웠듯,  grades\['ansang'\] , garade.ansang 두가지가 있다. for in 문을 사용했기 때문에 list\[name\]을 사용하면 value 값을 불러올 수 있다.

~~~javascript

var grades = {
    'list' : {'ansang' : 10, 'sanghyun' : 8, 'ansanghyun' : 80},
    'show' : function(){
        for(var name in this.list){
            console.log(name, this.list[name]); // ,를 쓰게되면 여러 값을 출력할 수 있다.
        }
    }
}
grades.show();

~~~