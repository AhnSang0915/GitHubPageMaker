---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 배열
date: 2022-03-06 10:39 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 배열

<br>
<br>
<br>

## 1. 배열의 문법
<br>
<br>

### 배열
<br>
<br>
배열(array)이란 연관된 데이터를 모아서 통으로 관리하기 위해 사용하는 데이터의 형식이다. 변수는 하나의 데이터를 저장하기 위한 것이라면 배열은 여러 개의 데이터를 하나의 변수에 저장하기 위해 사용한다. <br>
아래 코드는 name이라는 변수에 'Ahnsang'이라는 데이터를 할당한 것이다.

~~~javascript

var name = 'Ahnsang'
alert(name);

~~~

### 배열의 생성
<br>
<br>
위에선 변수에 하나의 데이터를 할당 했다. 이제 배열로 여러개의 데이터를 변수에 할당하는 방법을 공부해 보자.<br>
여러개의 데이터를 할당 하려면 변수명 = 뒤에 [] 대괄호를 사용해 여러개의 데이터를 작성할 수 있다.

~~~javascript

var member = ['Ahnsang', 'SangHyun', 'AhnSangHyun']

~~~

이 각각의 데이터를 요소,또는 원소(Element)라고 부르고 이제 이 원소들을 호출할것이다. 요소는 순서대로 0,1,2의 고유한 값,식별자를 가지게 된다. 색인 이라고도 하고 index라고도한다.

~~~javascript

var member = ['Ahnsang', 'SangHyun', 'AhnSangHyun']
alert(member[0]);
alert(member[1]);
alert(member[2]);

~~~
코드를 실행하면 차례대로 'Ahnsang', 'SangHyun', 'AhnSangHyun' 세개의 데이터를 차례로 경고창에 출력해준다.


---

## 2. 배열의 효용성
<br>
<br>
배열이 없다면 변수에 하나의 데이터만 할당할수 있기 때문에 불편할 것이다. 아래의 예제를 보자.
함수는 여러개의 입력값을 받을 수 있지만, 하나의 출력만 할 수 있다.

~~~javascript

function get_member1(){
    return 'Ahnsang';
}
document.write(get_member1());
 
function get_member2(){
    return 'SangHyun';
}
document.write(get_member2());
 
 
function get_member3(){
    return 'AhnSangHyun';
}

~~~

위 코드처럼 배열을 사용하지 않으면 각각의 회원정보를 반환하는 함수로 표한해야한다. 배열을 사용해 코드를 만들어 보자. return 안에 배열을 사용해 각각의 색인으로 원하는 정보를 호출할 수 있다.

~~~javascript

function get_members() {
    return ['Ahnsang', 'SangHyun', 'AhnSangHyun']
}
var members = get_members();
document.write(members[0]);
document.write(members[1]);
document.write(members[2]);

~~~

---

## 3. 배열의 사용 - 배열과 반복문
<br>
<br>
우리가 배열을 사용해 index값을 호출할때 그 값을 일일히 기억해서 호출한다는것은 불가능하다. 배열이 몇백 몇천개가 사용될수도 있기 때문이다. 그렇기 때문에 배열이란 결국 배열에 담겨있는 값을 하나하나 꺼내서 그꺼내진 값을 가공하는게 배열의 핵심적인 요소라고 할수있다.

<br>
<br>
아래 예제에서 출력값을 대문자로 출력하려고 .toUpperCase();라는 javascript내장함수를 사용해 출력했다.
'AHNSANG','SANGHYUN','AHNSANGHYUN'을 출력하게 될것이다.

~~~javascript

function get_members() {
    return ['Ahnsang', 'SangHyun', 'AhnSangHyun']
}
var members = get_members();
document.write(members[0].toUpperCase()+"<br />");
document.write(members[1].toUpperCase()+"<br />");
document.write(members[2].toUpperCase()+"<br />");

~~~
위 예제 처럼 우리가 직접 손으로 배열을 호출을 하기엔 무리가 있다. 이때 사용할 수 있는 방법이 배열과 반복문을 결합하는 것이다. 그전에 한가지 예제를 더 보자. 아래 예제는 배열의 값이 몇개인지 나타내 주는 함수이다. 경고창 내용은 3을 출력하게 된다.
~~~javascript

var a = ['Ahnsang', 'SangHyun', 'AhnSangHyun']
alert (a.length);
~~~
이제 배열과 반복문을 결합한 예제를 보자. i란변수를 지정하고 시작은 0에서 1씩 증가해 2로 끝나게 된다. 이렇게 나온 0, 1, 2는 index 값으로 사용하고, members[index값]에 i의 값이 어가게 되어 차례로 출력할 수 있게 된다.'AHNSANG','SANGHYUN','AHNSANGHYUN'을 출력하게 될것이다.

~~~javascript

function get_members() {
    return ['Ahnsang', 'SangHyun', 'AhnSangHyun']
}
var members = get_members();
for(var i = 0; i < 3; i++) {
    document.write(members[i].toUpperCase()+"<br />");
}

~~~

그런데 여기서 배열의 갯수가 늘어난다면 우리는 반복문의 조건을 수정해야한다. 이것도 함수를 사용해 더 편리하게 만들어 보면, 우리는 members라는 변수에 get_members라는 함수를 호출했다. 그 함수안에 return의 배열이 들어있기 때문에 members.length함수를 사용하면 배열안의 요소의 갯수를 호출해 사용할 수 있다.

~~~javascript

function get_members() {
    return ['Ahnsang', 'SangHyun', 'AhnSangHyun']
}
var members = get_members();
for(var i = 0; i < members.length; i++) {
    document.write(members[i].toUpperCase()+"<br />");
}

~~~

---

## 4. 배열의 제어
<br>
<br>
배열은 복수의 데이터를 효율적으로 관리, 전달하기 위한 목적으로 고안된 데이터 타입이다. 따라서 데이터의 추가/수정/삭제와 같은 일을 편리하게 할 수 있도록 돕는 다양한 기능을 가지고 있다. 몇가지 중요한 기능들만 살펴보자.
<br>
<br>

### 배열의 조작 - 추가 push
<br>
<br>
배열의 끝에 원소를 추가하는 방법을 알아보자. push는 인자로 전달된 값을 배열에 추가하는 javascript 내장함수 이다. 아래 코드를 실행하면 "f"가 추가된 배열이 출력된다.

~~~javascript

var li = ['a', 'b', 'c', 'd', 'e'];
li.push('f');
alert(li);

~~~
아래의 함수와 위의 함수는 같다.
~~~javascript

function numbering() {
    var i = 0;
    while(1 < 10) {
        document.write(i);
        i += i;
    }
}

~~~

아래 함수는 이름을 정하지도 않고 변수도 붙이지 않았다. 함수를 정의하고 함수를 괄호로 묶었다. 그다음에 호출할때 사용하는 기호 ();로 호출하게 되면 정의와 호출을 하나의 문장으로 같이하는 함수로 <u>익명함수</u>라고 한다. 일회 성으로 호출할때 이런 함수를 사용한다.

~~~javascript

(function(){
    i = 0;
    while(i < 10){
        document.write(i);
        i += 1;
    }   
}) ();

~~~

### 배열의 추가 concat
<br>
<br>
concat(concatenate)은 복수의 원소를 배열에 추가하는 방법이다. 추가한 출력은 ['a', 'b', 'c', 'd', 'e','f', 'g'] 가된다.

~~~javascript

var li = ['a', 'b', 'c', 'd', 'e'];
li = li.concat(['f', 'g']);
alert(li);

~~~

### 배열의 추가 unshift
<br>
<br>
unshift는 배열의 시작점에 원소를 추가하는 방법이다. 출력은 ['z','a', 'b', 'c', 'd', 'e'] 가되고 index도 0~5로 변경된다.

~~~javascript

var li = ['a', 'b', 'c', 'd', 'e'];
li.unshift('z');
alert(li);

~~~

### 배열의 추가 splice
<br>
<br>
splice는 배열의 특정구간을 추출하거나, 특정구간에 특정 배열을 추가하는 방법이다. 문법은 아래와 같고,

~~~javascript

array.splice(index, howmany, element1, ...., elementN);

~~~
아래 표를 보면서 이해해보자.

|인자명|데이터형|필수/옵션|설명|
|:---|---:|:---:|
|index|number|필수|배열에 추가할 특정 배열의 위치를 가르키는 index|
|howmany|number|필수|index에서부터 제거될 원소들의 수. index부터 index+howmany에 <br>해당하는 원소들은 삭제된다. 이 값이 0이면 어떠한 원소도 삭제되지<br> 않는다.|
|element1,...,elementN|number|옵션|index와 index+howmany 사이에 추가될 값|

아래와 같이 splice를 이용해 배열에 'x','y'를 추가하는 코드가 있다. splice뒤에 오는 1은 [a,b,c] 배열에서 'b'를 가르키고 0은 'b'를 제거하지 않고 index 1번 위치에 'x','y'를 추가하겠다는 말이다.
이러면 배열은 ['a','x','y','b','c'] 가된다.

~~~javascript

var a = ['a','b','c']
a.splice(1,0,['x','y'])

~~~

이번엔 기존 배열을 삭제하고 추가하는 예제를 보자. index 1번자리에 있는 'b'의 자리에서 2개의 원소를 삭제하고 ['x','y']를 순서대로 넣어주겠다는 말이다. 변경된 배열은 ['a' , 'x', 'y']가 된다.

~~~javascript

var a = ['a','b','c']
a.splice(1,2,['x','y'])

~~~

몇가지 예제를 더보자.

~~~javascript

var numbers = [1,2,3,4,5,6,7,8,9,10];
alert(numbers.splice(2)); //2번 index를 포함 이후의 모든 요소를 제거한다.
alert(numbers); // [1,2]
 
var numbers = [1,2,3,4,5,6,7,8,9,10];
alert(numbers.splice(2, 4)); // array, [3,4,5,6]
 
var numbers = [1,2,3,4,5,6,7,8,9,10];
alert(numbers.splice(2, 4, 'three', 'four', 'five', 'six')); // array, [3,4,5,6]
alert(numbers); // array, [1,2,three,four,five,six,7,8,9,10]

~~~

---


## 5. 배열의 조작 - 제거, 정렬
<br>
<br>

### 제거 shift
<br>
<br>
shift는 배열의 첫번째 원소를 제거하는 방법이다. index 0번에 위치한 원소를 제거하고 나머지 값들을 한칸씩 앞으로 당겨온다. 만약 배열의 length가 0이면 undefined을 리턴한다. 아래 예제의 결과는 b, c, d, e다.

~~~javascript

var li = ['a', 'b', 'c', 'd', 'e'];
li.shift();
alert(li);

~~~

### 제거 pop
<br>
<br>
pop은 배열의 마지막 원소를 제거하는 방법이다. 마지막 index에 위치한 원소를 제거하고 마찬가지로 빈 배열이라면 undefined을 리턴한다.

~~~javascript

var li = ['a', 'b', 'c', 'd', 'e'];
li.pop();
alert(li);

~~~

### 정렬 sort
<br>
<br>
배열을 이용하는 중요한 이유중 하나가 정렬이다. sort는 배열의 정렬을 하고싶을때 사용한다.

~~~javascript

var li = ['c', 'e', 'a', 'b', 'd'];
li.sort();
alert(li);

~~~

하지만 만약 배열이 ['1', '10', '6'] 인경우엔 정렬이 1, 10, 6이 된다. 데이터를 문자로 보기때문에 앞에 1이 온 10을더 작다고 보는것이다. 이것을 올바르게 정렬하려면 아래와 같은 예제를 사용한다.

~~~javascript

function sortNumber(a,b){
    return a-b; //역순을 구한다면 b-a를 활용한다.
}
var numbers = [20, 10, 9,8,7,6,5,4,3,2,1];
alert(numbers.sort(sortNumber)); // array, [1,2,3,4,5,6,7,8,9,10,20]

~~~

위 함수 a-b; 부분을 이해하려 찾아보았다. 정확하게 javascript에서 어떤 알고리즘으로 작동하는지 모르지만 이런 식으로 작동할 것이라는 글을 보게 되었다.<br>
만약 5,4,6,1,3,2 라는 배열이 있다고 가정하자.<br>
a-b에서 양수면 위치를 바꾸고 음수면 유지한다.<br>
5-4는 양수로 위치를바꾼다.<br>
4,5,6,1,3,2<br>
4-6은 음수로 유지.<br>
4,5,6,1,3,2<br>
4-1은 양수로 변경.<br>
1,5,6,4,3,2<br>
1-3,1-2도 음수로 자리를 유지하고 index0번위치에 1이 오게된다.<br>
이제 1,5,6,4,3,2에서 두번째 자리를 찾는다.<br>
5-6은 음수로 유지.<br>
1,5,6,4,3,2<br>
5-4는 양수로 변경.<br>
1,4,6,5,3,2<br>
4-3은 양수로 변경.<br>
1,3,6,5,4,2<br>
3-2는 양수로 변경.<br>
1,2,6,5,4,3 두번째 자리를 찾았다.<br>
....<br>
...<br>
이런 식으로 반복해서 찾는다는 글을 봤는데 맞는진 모르겠지만 이렇게 이해하면 좋을 것 같다.
<br>
<br>

### 정렬 reverse
<br>
<br>
reverse는 역순으로 정렬하고 싶을때 사용한다.

~~~javascript

var li = ['c', 'e', 'a', 'b', 'd'];
li.reverse();
alert(li);

~~~