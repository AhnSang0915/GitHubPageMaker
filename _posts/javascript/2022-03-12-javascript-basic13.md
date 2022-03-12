---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 함수지향 - 값으로서의 함수와 콜백
date: 2022-03-12 23:10 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 함수지향 - 값으로서의 함수와 콜백

<br>
<br>


---

## 1. 값으로서의 함수
<br>
<br>
Javascript에서는 함수도 객체이다. 함수를 일단 값이라고 생각하자. 값의 특징은 어떠한 변수에 담을수 있다. var a = "value" a라는 변수에 값으로 value를 넣은것이다. 함수가 일종의 값이라는 것은 함수 역시 어떤 변수에 담을수 있다는 것이다. Javascript의 함수가 다른 언어의 함수와 다른 점은 함수가 값이 될 수 있다는 점이다. 예제를 보자.


~~~javascript
	
function a(){} // var a = function () {}

~~~

위 예제에서 a라고하는 함수를 정의했다. 위처럼 함수를 정의하는 것은 a라고하는 변수에 담겨진 값이라는 것이다. 아래 예제에선 객체에 변수를 담았다. a라는 객체에 b라는 key와 function(){}이란 value를 담은것이다. 이처럼 객체 안에 함수를 담게되면 함수는 값이기 때문에 b는 객체안에서 변수와 같은 역할을 하고있다. 객체안에서 변수의 역할을 하는것을 속성(Property)라고 하고 그 속성에 저장된 값이 함수라면 그함수는 이러한 맥락에선 메소드(method)라고 한다.

~~~javascript

a = {
    b:function(){
    }
};

~~~

또한 함수는 값이기 때문에 다른 함수의 인자로 전달 될수도 있다. increase는 num이라는 매개변수에 +1을해 리턴, decrease는 -1알한 값을 리턴해준다. cal이라는 함수는 func, num이라는 매개변수를 갖고있고 func의 함수에 num이라는 값을 호출하고있다. alert(cal(increase, 1));을 하게되면 cal의 매개변수가 increase, 1이 인자가 된다. 즉, increase라는 함수에 1이라는 인자가 전달되기 때문에 2가된다.

~~~javascript

function cal(func, num){
    return func(num)
}
function increase(num){
    return num+1
}
function decrease(num){
    return num-1
}
alert(cal(increase, 1));
alert(cal(decrease, 1));

~~~



---

## 2. 값으로서의 함수와 콜백 - 함수의 용도2
<br>
<br>
함수는 함수의 리턴 값으로도 사용할 수 있다. 아래 코드를 보자. cal라는 함수를 호출할때 첫번째 인자로 'plus' 라는값을 주면 객체를 담고있는 함수에 'plus'라는 인자가 들어가게 되고 function cal('plus'), return funcs('plus')가 된다. alert(cal('plus') (2, 1))에서 (cal('plus')는 function(left, right){return left + right} 이부분이 되고, alert(cal('plus') (2, 1)) 에서 (2, 1)은 함수를 호출하겠다는 말이고 인자로 2, 1을 전달하겠다는 것이다. 결과는 3이된다.

~~~javascript

function cal(mode){
    var funcs = {
        'plus' : function(left, right){return left + right},
        'minus' : function(left, right){return left - right}
    }
    return funcs[mode];
}
alert(cal('plus')(2,1));
alert(cal('minus')(2,1));

~~~

당연히 배열의 값으로도 사용할 수 있다. process라는 배열을 정의했고 배열안의 요소 3개가 모두 함수이다. for반복문에서  i = 0 일때 process라는 배열의 index 0의 요소의 함수를 호출하고 첫번째 인자로 1을 전달한다. 이후 input의 값은 11이되고 index 다시 반복문으로 돌아와 1의 요소의 함수를 호출하게 된다. 이때 input의 값은 배열의 첫번쨰 요소에서 얻은 11이 된다. 값은 121이 되고 이 값은 다시 input의 값이 된다. 이후배열의 세번째 요소로 121의 값이 전달되고 60.5의 결과가 나온다.

~~~javascript

var process = [
    function(input){ return input + 10;},
    function(input){ return input * input;},
    function(input){ return input / 2;}
];
var input = 1;
for(var i = 0; i < process.length; i++){
    input = process[i](input);
}
alert(input);

~~~


---

## 3. 값으로서의 함수와 콜백 - 콜백이란?
<br>
<br>
콜백은 어떠한 함수가 수신하는 인자가 함수인 경우를 콜백이라고 한다. 
<br>
<br>

### 처리의 위임
<br>
값으로 사용될 수 있는 특성을 이용하면 함수의 인자로 함수로 전달할 수 있다. 값으로 전달된 함수는 호출될 수 있기 때문에 이를 이용하면 함수의 동작을 완전히 바꿀 수 있다. 인자로 전달된 함수 sortNumber의 구현에 따라서 sort의 동작방법이 완전히 바뀌게 된다.
<br>
아래 예제에서 배열의 내용을 정렬하려면 numbers.sort();라는 명령을 내리는 것이다. 여기서 .앞의 numbers는 배열객체가 되고 우리가 아래처럼 \[20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1\]를 작성해 Javascript에 제출을하면 배열객체를 만들어 numbers라고하는 변수에 담아준다. 그리고 배열객체에는 sort라고하는 함수가 정의되어 있기때문에 numbers.sort();를 통해서 배열이 가지고있는 명령어 sort를 호출하게 되는데 여기서 sort는 함수라고 하지않고 객체에 속해있기 때문에 메소드라고 한다. 이러한 numbers객체 또는 sort메소드는 Javascript에서 기본적으로 제공하는 기능이기 때문에 이러한 기능을 내장 객체 내장 메소드, 또는 빌트인 객체 빌트인 메소드라고 한다. 그리고 우리가 만드는 객체나 메소드, 함수같은 것들은 우리가 만드는 것이기 때문에 사용자정의 객체, 사용자정의 메소드 라고한다. 

~~~html

<!DOCTYPE html>
<html>
<head>
<script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
</head>
<body>
<script type="text/javascript">
    var numbers = [20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
    numbers.sort(); 
</script>
</body>
</html>

~~~

위의 코드를 실행하면 배열안의 내용을 정렬해주고 결과는 [1, 10, 2, 20, 3, 4, 5, 6, 7, 8, 9] 가 출력된다. 이유는 숫작의 크기로 비교한게 아니고 문자로 비교를 했기 때문이다. 앞의 숫자가 1인것들이 우선순위를 갖고 나머지를 정렬했기 때문이다. 우리가 원하는 결과를 얻기 위해선 아래의 방법을 이용해야 한다.

~~~html

<!DOCTYPE html>
<html>
<head>
<script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
</head>
<body>
<script type="text/javascript">
    var numbers = [20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
    var sortfunc = function(a, b) {
        console.log(a, b);
        if(a > b) {
            return 1;
        } else if (a>b){
            return -1;
        } else {
            return 0;
        }
    }
    console.log(numbers.sort(sortfunc)); 
</script>
</body>
</html>

~~~

위의 코드를 단순하게 하면 아래처럼 된다. 아래의 함수에서 sortfunc가 콜백함수가 되고 콜백 함수 라는것은 
콜백함수를 수신받는 sort메소드가 sortfunc를 인자로 전달받아 내부적으로 호출하는 것을 통해서 sort함수가 동작하는 기본적인 동작방법을 변경할수 있게 된다. 즉, 값으로서 함수를 사용할수 있기때문에 함수의 동작방법을 값을 전달하는 것을 통해 바꿀수 있는게 콜백 이다. 그리고 콜백이 가능한 것은 Javascript의 함수가 값이기 때문에 가능한 것이다.

~~~html

<!DOCTYPE html>
<html>
<head>
<script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
</head>
<body>
<script type="text/javascript">
    var numbers = [20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
    var sortfunc = function(a, b) {
        return a-b; // 역순 b-a 
    }
    console.log(numbers.sort(sortfunc)); 
</script>
</body>
</html>

~~~

---


## 4. 비동기 콜백과  Ajax
<br>
<br>
예를 들어 우리가 홈페이지를 운영하는데 만명정도의 구독자가 있다고 치자. 우리가 글을쓰면 만명에게 메일이 전송되게 되어있다. 한명에게 메일을 보내는데 1초가 걸리면 만명에게 보내는데에는 만초가 걸리게 된다. 글을 작성하고 이메일을 전송후 작성완료까지 3시간을 기다려야 한다면 이런 서비스를 사용하기는 힘들것이다.이렇게 순서대로 실행하는 것을 동기적 처리라고한다. 그런데 우리가 글작성을하고 이메일을 발송하지 않고 발송 예약후 작성완료를 하게 되면 시간이 훨씬 줄어들게 된다. 그리고 내부적으로 사용자에게 노출되지 않는 프로그램이 작동하면서 이메일 발송예약이 들어와 있는지 아닌지를 확인해 들어와있다면 프로그램이 만명에게 이메일 발송하는 작업을 3시간동안 백그라운드에서 진행하면 될것이다. 이렇게 처리하는 방식을 비동기적인 처리라고한다. 우리는 이 비동기적 처리를 Ajax(Asynchronous javascript and xml) 로 사용할 수 있다.
<br>

우리가 아래와 같은 객체를 만든 파일을 만들었다고 가정하고 예제를 보자.

~~~javascript

{"title":"JavaScript","author":"egoing"}

~~~

생활코딩의 동영상을 보고 이해하는것이 좋겠다...(아직 이해못함.)

~~~javascript

<!DOCTYPE html>
<html>
<head>
<script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
</head>
<body>
<script type="text/javascript">
    $.get('./datasource.json.js', function(result){ //$는 jquery가 제공하는 특수한 객체이다. 여기에 get이라는 메소드를 사용해 json타입 파일을 호출하는 것이다.
        console.log(result);
    }, 'json');
</script>
</body>
</html>

~~~

