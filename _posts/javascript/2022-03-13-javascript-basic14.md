---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 함수지향 - 클로저
date: 2022-03-13 22:10 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 함수지향 - 클로저

<br>
<br>
클로저(closure)는 내부함수가 외부함수의 맥락(context)에 접근할 수 있는 것을 가르킨다. 클로저는 자바스크립트를 이용한 고난이도의 테크닉을 구사하는데 필수적인 개념으로 활용된다.  
<br>
<br>

## 1. 내부함수, 외부함수
<br>
<br>

### 내부함수
<br>
<br>
아래 코드는 함수안에 또다른 함수를 선언한 것이다. 함수 outter은 외부함수가 되고 inner함수는 내부함수가 된다. inner함수는 var inner = fuction {} 과 같게된다. 

~~~javascript
	
function outter(){
    function inner(){
        var title = 'coding everybody'; 
        alert(title);
    }
    inner();
}
outter();

~~~

아래 코드는 outter란 외부함수에 var title = 'coding everyday'; 라는 지역변수를 만들었다. 그리고 내부함수로 inner을 만들었는데, 이때 이 내부함수 inner에 title이라는 변수를 사용하려고 하는데 이때 inner라는 함수에 지역변수가 존재하지 않는다면 Javascript는 이 inner라는 내부함수를 포함하고 있는 외부함수에서 title이라고하는 변수를 찾게된다. 즉, 내부함수에서 외부함수의 지역변수에 접근할 수 있다.이러한 것을 클로저(closure)라고 한다.

~~~javascript

function outter(){
    var title = 'coding everybody';  
    function inner(){        
        alert(title);
    }
    inner();
}
outter();
~~~



---

## 2. 클로저란?
<br>
<br>
클로저(closure)는 내부함수와 밀접한 관계를 가지고 있는 주제다. 내부함수는 외부함수의 지역변수에 접근 할 수 있는데 외부함수의 실행이 끝나서 외부함수가 소멸된 이후에도 내부함수가 외부함수의 변수에 접근 할 수 있다. 이러한 메커니즘을 클로저라고 한다. 
<br>
<br>
아래 예제는 이전의 예제를 조금 변형한 것이다. 내부함수inner를 outter함수내에서 호출하는 것이 아니라 반환하도록 했다. 함수 outter는 내부함수 inner를 반환하고 생을 마감했다. 즉, 함수 outter는 실행된 이후 실행이 종료되어 함수 ouuter의 변수 title또한 더이상 유효하지 않게되어 변수 title에 접근할수 없어 보인다. 그러나 아래 코드의 실행 결과는 경고창으로 coding everybody를 출력할 것이다. 이처럼 자신을 포함하고 있는 외부함수보다 내부함수가 더 오래 유지되는 경우, 외부함수 밖에서 내부함수가 호출되더라도 외부함수의 지역 변수에 접근할 수 있는데 이러한 함수를 클로저(closure)라고 부른다.


~~~javascript

function outter(){
    var title = 'coding everybody';  
    return function(){        
        alert(title);
    }
}
var inner = outter();
inner();

~~~

 즉, 클로저는 반환된 내부함수가 자신이 선언됐을 때의 환경(Lexical environment)인 스코프를 기억하여 자신이 선언됐을 때의 환경(스코프) 밖에서 호출되어도 그 환경(스코프)에 접근할 수 있는 함수를 말한다. 이를 조금 더 간단히 말하면 클로저는 자신이 생성될 때의 환경(Lexical environment)을 기억하는 함수다라고 말할 수 있겠다.


---

## 3. Private variable
<br>
<br>
소프트웨어가 커지는 과정에서 어떠한 정보가 있을때 그 정보를 아무나 수정하는것을 방지하는 것을 Private variable이라 한다. 소프트웨어가 커지면 여러사람이 코드를 작성하게 된다. 그안에는 과거의 자기자신과 미래의 자기자신이 포함되게된다. 그런경우 많은 데이터가 소프트웨어 안에 존재하게 되는데 그 데이터가 누구나 고칠수있는 데이터가 된다는것은 그데이터가 망가질 가능성이 크다는 것이다. 그런 것을 방지하기 위해 접근하는 방법을 클로저를 사용하여 데이터를 가져오고 수정하는 것을 안전하게 하는것이다.
<br>
<br>
아래는 factory_movie라는 외부함수가 get_title, set_title이라는 두 메소드에 함수를 지정한 객체를 담고있다. 이때 get_title, set_title은 내부 함수가 된다. get_title메소드를 호출하면 title이라는 값을 리턴하는데 그 title의 값은 factory_movie함수에 첫번째 인자이다. 첫번째 매개변수가 title이고 이 매개변수는 함수안에서 지역변수로 사용이 된다. 그렇기 때문에 factory_movie(title)은 지역변수이고 지역변수는 내부함수에서 접근이 가능하기 때문에 get_title을 호출하면 factory_movie의 첫번째 매개변수인 title이 값이 되기때문에 factory_movie함수의 (title)에 전달된 값을 리턴해준다. 그리고 set_title메소드는 첫번째 인자로 _title을 갖고 그리고 _title이라는 값은 다시 title이되고 그값은 내부변수를 의미하기때문에 factory_movie의 (title)을 변경하게 된다. 그다음 ghost와 matix라는 변수에 리턴값을 담았다. alert(ghost.get_title()); 는 'Ghost in the shell'을 출력하고, alert(matrix.get_title());는 'Matrix'를 출력한다. 이말은 ghost와 matix가 같은 객체를 담고 있지만 그 객체가 담고있는 get_title이라는 메소드가 접근하는 title이라고하는 외부변수에 담겨있는 값은 서로 다르다는 것이다. ghost.set_title('공각기동대');는 ghost라는 변수 안에 set_title이라는 메소드를 호출하고 '공각기동대' 를 인자로 사용하겠다는 말이다. '공각기동대는' _title이되고 _title은 title이 되기 때문에 이 타이틀의 값은 factory_movie함수의 지역변수를 바꾸게 된다. alert(ghost.get_title());를 호출하게 되면 '공각기동대'를 출력하고, alert(matrix.get_title());를 호출하면 'Matrix'를 실행하게 된다. 즉, 우리가 factory_moviex통해 두개의 ghost와 matix변수를 만들었고, 그두개의 변수는 자신들이 실행된 그 시점에서의 외부함수의 지역변수에 접근할 수있었고 그지역변수의 값은 유지되고 있기때문에 ghost라는 함수에 set_title을 통해서 그내용을 '공각기동대'로 바꾼다 라는것은 ghost가 접근할수있는 title의 값만을 바꾸는것이지 matrix라는 변수가 접근할수 있는 title의 값에는 어떠한 영향도 미치지 않는다는 것이다.

~~~javascript

function factory_movie(title){
    return {
        get_title : function (){
            return title;
        },
        set_title : function(_title){
            title = _title
        }
    }
}
ghost = factory_movie('Ghost in the shell');
matrix = factory_movie('Matrix');
 
alert(ghost.get_title());
alert(matrix.get_title());
 
ghost.set_title('공각기동대');
 
alert(ghost.get_title());
alert(matrix.get_title());


~~~

이코드의 진짜 효용은 private variable이라는 것이다.  ghost와 matix변수에 객체를 담았다. 이객체의 get_title, set_title은 언제든지 접근할 수 있는 메소드이다. 누구나 접근할수 있다는 것이다. get_title, set_title이 내부적으로 사용하고 이있는 변수는 title이다. 이title은 외부 함수의 지역변수인 title이다.이지역변수인 title은 factory_movie라는 함수가 어떠한 값을 리턴했을때 factory_movie함수 자체는 실행이 끝났기 때문에 그지역변수인 title은 factory_movie의 내부함수인 get_title, set_title을 통해서만 접근할 수 있는 변수가 되는것이다. 즉, 우리가 title이라는 변수 값을 private variable로 만들고 그값을 수정할때는 set_titl을 통해서만 수정할 수 있고, 그변수의 값을 가져올때는 get_title를 통해서만 가져올 수 있게 하면 title이라는 변수가 안전하게 저장,수정될 수 있다는 것이다.


---


## 4. 클로저의 응용
<br>
<br>
클로저를 활용하는 것에서 실수하기 쉬운 예제를 보자. Javascript에서는 오로지 함수의 괄호 안에서만 지역변수로서 할당되고 그 외 모든 장소는 전역변수로 취급을 받는다. 우리가 예상하는 결과는 0,1,2,3,4 일것이다. 하지만 그렇지 않다. 첫번째 for문이 반복되는 동안 점점 증가되는 i의 값이 arr라는 배열에 저장될 것 같지만, 실제로 저장되는 것은 함수 그 자체이다. i는 반복이 끝난후 5라는 값이되고 return i 의 값은 5가된다. 그리고 다음 for in문에서 arr[index]는 해당 인덱스의 값으로서의 함수이고 ()를 붙였음으로 해당 함수가 호출된다. i 값은 첫번째 for문을 돌아 5가된 상태이기 때문에 5, 5, 5, 5, 5가 출력된다. 


~~~javascript

var arr = []
for(var i = 0; i < 5; i++){
    arr[i] = function(){
        return i;
    }
}
for(var index in arr) {
    console.log(arr[index]());
}
~~~

그렇다면 정상출력 0, 1, 2, 3, 4을 얻기위해선 어떻게 해야할까? 위의 코드에서 달라진 점은 그전의 코드를 외부 함수로 감싸주어서 원래 함수는 내부 함수가 된다는 것아다. 그리고 외부 함수는 내부 함수를 값으로 반환하는데 그 자리에서 바로 그 외부 함수를 호출하기 때문에 내부 함수가 값으로서 반환되어 바로 변수에 할당이 된다. 


~~~javascript

var arr = []
for(var i = 0; i < 5; i++){
    arr[i] = function(id) {
        return function(){
            return id;
        }
    }(i);
}
for(var index in arr) {
    console.log(arr[index]());
}

/* 결과
0
1
2
3
4
*/

~~~

위의 두 예제에서 첫번째 for문을 비교한 것이다.


~~~javascript

var arr = [];
for(var i = 0; i < 5; i++){
  arr[i] = function(){
    return i;
  }
}


  arr[0] = function(){
    return i;
  }
  arr[1] = function(){
    return i;
  }
  arr[2] = function(){
    return i;
  }
  arr[3] = function(){
    return i;
  }
  arr[4] = function(){
    return i;
  }


for(var i = 0 ; i < 5; i++){
  arr[i] = function(id){  //외부함수.
    return function(){    //내부함수.
      return id;
    }
  }(i);  //외부함수 호출
}

  arr[0] = function(){
      return 0;
  }
  arr[1] = function(){
      return 1;
  }
  arr[2] = function(){
      return 2;
  }
  arr[3] = function(){
      return 3;
  }
  arr[4] = function(){
      return 4;
  }

~~~