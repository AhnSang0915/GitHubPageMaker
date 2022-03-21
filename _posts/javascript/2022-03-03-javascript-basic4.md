---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 조건문
date: 2022-03-03 22:00 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---
{% include javascript-table-of-contents.html %}


# JavaScript 조건문

<br>
<br>

---

## 1. 조건문이란?
<br>
<br>
조건문(Conditional statement)은 if로 시작한다.if뒤에는 반드시 true나 false로 두개의 값중에 하나가 온다. 그뒤 중괄호안에 조건이 들어오게 된다.
<br>
<br>
아래의 예제는 true를 출력할것이다. if뒤가로에 true가 오게되면 중괄호 안의 내용이 실행된다.

~~~javascript

if(true){
    alert('result : true');

~~~

이번엔 아무것도 출력하지 않는다. if뒤에 false가오면 중괄호 안의 내용을 실행하지 않는다.

~~~javascript

if(false){
    alert('result : true');

~~~

12345를 출력 할것이다.

~~~javascript

if(true){
    alert(1);
    alert(2);
    alert(3);
    alert(4);
}
alert(5);

~~~

5만 출력한다. false기 때문에 중괄호 안의 내용은 실행하지 않는다.

~~~javascript

if(false){
    alert(1);
    alert(2);
    alert(3);
    alert(4);
}
alert(5);

~~~


---

## 2. else, else if
<br>
<br>
if만으로는 조건문을 사용하는데에 제약이 있다. else와 else if는 더 다양하게 조건문을 응용할 수 있게 해준다.

<br>

### else

<br>
<br>

if뒤 true가 있다면 중괄호 안의 내용이 실행이 되고, else는 실행이 되지 않는다. 만약에 참 이라면 if중괄호가 실행후 else는 무시하고 결과는 1이된다.

~~~javascript

if(true){
    alert(1);
} else {
    alert(2);
}

~~~

if뒤에 false가 있다면 중괄호 안의 내용이 실행이 안되고, 만약에 거짓이라면 else가 실행이 된고 결과는 2다.

~~~javascript

if(false){
    alert(1);
} else {
    alert(2);
}

~~~

### else if 

<br>
<br>
아래 코드에 대한 해석을 해보자. 1번에서 if뒤의 false로 2번alert(1)이 실행되지 않고 다음으로 넘어간다. 3번코드 else에선 1번에서 if가 false기 때문에 실행이 되고 else뒤의 if가 true이기 때문에 2라는 값이 출력된다. 4번이 실행 되었기 때문에 5와 7의 else가 실행될수 없다. 그대로 2만 출력 할 것이다.


~~~javascript

if(false){       //1
    alert(1);    //2
} else if(true){ //3
    alert(2);    //4
} else if(true){ //5
    alert(3);    //6
} else {         //7
    alert(4);    //8
}

~~~

아래 코드도 해석해보면 3이 출력된다는 걸 알 수 있다.

~~~javascript

if(false){
    alert(1);
} else if(false){
    alert(2);
} else if(true){
    alert(3);
} else {
    alert(4);
}

~~~

아래 코드도 해석해보면 4가 출력된다는 걸 알 수 있다.

~~~javascript

if(false){
    alert(1);
} else if(false){
    alert(2);
} else if(false){
    alert(3);
} else {
    alert(4);
}
~~~

---

## 3. 조건문의 응용
<br>
<br>

### 변수와 비교연산자
~~~javascript

if(true) {
    alert(1);
}

~~~
위와 같은 코드는 javascript에서 쓸일이 없다. 무조건 1이 출력이 되기 때문이다. 조건문과 변수가 만나 상황에 따라 가변적인 요소가 되어야 조건문이라 할수 있다. prompt라는 구문을 사용해야 하는데 prompt는 사용자가 입력한 값을 가져와서 변수의 값으로 대입해준다. 예제를 통해 더 알아보자.
<br>

<br>
~~~html

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
</head>
<body>
    <script>
        id = prompt('아이디를 입력해주세요.') //prompt를 통해 사용자가 입력한 값을 id라는 변수에 적용
        if(id=='Ahnsang'){
            alert('아이디가 일치 합니다.')
        } else {
            alert('아이디가 일치하지 않습니다.')
        }
    </script>
</body>
</html>

~~~


<br>

위의 예제를 응용해 아이디와 비밀번호 모두 사용하게 해보자. 아이디가 일치하면 비밀번호를 물어볼 필요가 없다. id 변수에 입력한 값이 if id의 조건문에서 아이디가 일치한다면 if password에서 prompt를 통해 비밀번호를 요구한다. 그렇게 되면 입력한 비밀번호가 password라는 변수에 담겨서 입력 값과 111111라는 password와 일치하면 로그인 하셨습니다. 다르다면 비밀번호가 다릅니다라는 메세지가 나오게 된다.

<br>

~~~html

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
</head>
<body>
    <script>
        id = prompt('아이디를 입력해주세요.');
        if(id=='Ahnsang'){
            password = prompt('비밀번호를 입력해주세요.');
            if(password==='111111'){
                alert('로그인 했습니다.');
            } else {
                alert('비밀번호를 확인해 주세요.');
            }
        } else {
            alert('아이디를 확인해 주세요.');
        }
    </script>
</body>
</html>

~~~

---

## 4. 논리 연산자
<br>
<br>

논리 연산자는 조건문을 더 간결하고 다양하게 사용할수 있다.
<br>

### &&
<br>
&&는 좌항과 우항이 모두 참(true)일때 참이된다. 아래 예제에선 1이라는 값이 출력된다. 이러한 연산자를 and연산자라고 한다. 

~~~javascript

if(true && true){
    alert(1);
}
if(true && false){
    alert(2);
}
if(false && true){
    alert(3);
}
if(false && false){
    alert(4);
}

~~~

아래 예제에선 논리연산자 중 and연산자를 활용한 것 이다. 두 변수를 동시에 호출하기 위해 id와 password를 prompt로 호출해주고 && 연산자로 둘의 값이 모두 참일때만 '인증했습니다.'라는 메세지를 출력 하게되고 하나라도 다르다면 '인증에 실패 했습니다.' 라는 값을 출력하게 된다. and연산자는 2개 이상도 사용할 수 있다.

~~~html

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
</head>
<body>
    <script>
        id = prompt('아이디를 입력해주세요.');
        password = prompt('비밀번호를 입력해주세요.');
        if(id=='Ahnsang' && password=='111111'){
            alert('인증 했습니다.');
        } else {
            alert('인증에 실패 했습니다.');
        }
    </script>
</body>
</html>

~~~

### ||
<br>
<br>
||는 ||의 좌우항 하나라도 참이라면 참이 되고 둘다 거짓일때 거짓이 되는 연산자 이다. 예제는 1, 2, 3이 출력되고 ||는 or연산자 라고 한다.
<br>

~~~javascript
if(true || true){
    alert(1);
}
if(true || false){
    alert(2);
}
if(false || true){
    alert(3);
}
if(false || false){ //둘다 false기 때문에 false
    alert(4);
}
~~~
아래 예제는 Ahnsang, Ahnsang1, Ahnsang2 값중 하나라도 변수값에 들어오면 '인증 했습니다.'라는 값을 출력하게 될것이다.
~~~javascript
id = prompt('아이디를 입력해주세요.');
if(id==='Ahnsang' || id==='Ahsang1' || id==='Ahnsang2'){
    alert('인증 했습니다.');
} else {
    alert('인증에 실패 했습니다.');
}
~~~
다음예제는 or와 and를 사용하는 방법이다.id 비교를 할 때 괄호를 사용한 것은 사칙 연산을 할 때 괄호부터 계산하는 것과 같은 원리다. 세개의 id중 하나라도 맞고 password가 111111이면 로그인 했습니다 라는 값이 출력된다.

~~~javascript
id = prompt('아이디를 입력해 주세요')
password = prompt('비밀번호를 입력해 주세요.')
if(id === 'Ahnsang' || id === 'Ahnsang1' || id === 'Ahnsang2' && password = '111111') {
    alert('로그인 했습니다.')
}   else {
    alert('로그인 실패 했습니다.')
}

~~~

### !
<br>
<br>
!는 부정의 의미로 true나 false 앞에 !를 붙이면 값을 역전시킨다. not 연산자 라고 부른다. 아래 에제에서 !를 사용하면 어떻게 되는지 확인하자. 값은 4이다.

~~~javascript
if(!true && !true){ //false false 이기 때문에 &&연산자 에선 실행되지 않는다.
    alert(1);
}
if(!false && !true){ //true false &&는 둘다 참이어야 실행한다.
    alert(2);
}
if(!true && !false){ //true false &&는 둘다 참이어야 실행한다.
    alert(3);
}
if(!false && !false){ //true true기 때문에 실행한다.
    alert(4);
}
~~~

### 5.boolean의 대체제
<br>
<br>

### 0과 1
<br>
<br>
조건문에 사용될 수 있는 데이터 형이 꼭 불린만 되는 것은 아니다. 관습적인 이유로 0는 false 0이 아닌 값은 true로 간주된다. 아래의 예제는 2를 출력한다.

~~~javascript
if(0){
    alert(1)
}
if(1){
    alert(2)
}
~~~

### 그외의 false로 간주되는 데이터

~~~javascript
if(!''){
    alert('빈 문자열')
}
if(!undefined){
    alert('undefined');
}
var a;
if(!a){
    alert('값이 할당되지 않은 변수'); 
}
if(!null){
    alert('null');
}
if(!NaN){
    alert('NaN');
}
~~~