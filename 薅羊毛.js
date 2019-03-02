
//页面引入jquery
var src="https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/js/lib/jquery-1.10.2_1c4228b8.js"

var head = document.getElementsByTagName('head')[0];
var script = document.createElement('script');
script.type = 'text/javascript';
script.src = src;
head.appendChild(script);

//-----------------------薅猪毛代码-------------------

var methon=function(){
    console.log("执行")
    $(".box-button p").click();
    if($(".buttion-invitation")){
        $(".buttion-invitation").click();
    }
}
var reloadInterval = window.setInterval(function(){
    setTimeout(methon,Math.random()*50*1000)     
},1000*1000);



//----------------抢购程序代码----------------------
//1.进入商品页面
//2.判断秒杀是否已经开始 $(".spike-coming") ！= undifine == 尚未开始
//      a.如果秒杀未开始，每隔100ms刷新页面
//      b.如果秒杀已经开始，
//          1.是否存在已经开始拼单的人，$(".local-group-item").click()=>开始拼单 =>$(".g-group-footer button").click()=>进入商品选择界面
//          2.不存在时候,选择开始拼单，$(".goods-group-btn-new").click()
//          3.选择商品属性：var types=$(".sku-specs");遍历types ：$(types[0]).find(".sku-spec-value-list div:first")[0].click()
//          4.确定购买：$(".sku-selector-bottom").click()

function check(){
    //轮询是否已经可以购买
    function methon(){
       var isBegin=$(".spike-coming")
       if(isBegin[0]&&isBegin[0].innerText=="即将开抢"){
           console.log("尚未开抢")
           window.location.reload()
           return;
       }
    }
    var reloadInterval = window.setInterval(function(){
        setTimeout(methon,Math.random()*50)     
    },100);
}

//选择第一个人开始拼单，进入属性选择界面
function pindan(){
    $(".local-group-item").click();
    $(".g-group-footer button").click()
}

//选择商品属性，默认选择第一个,下一步进行确定
function selectTypes(){
    var types=$(".sku-specs");
    for(var i=0;i<types.length;i++){
        $(types[i]).find(".sku-spec-value-list div:first")[0].click()
    }

}

//确定购买
function buy(){
    $(".sku-selector-bottom").click()
    //延时100ms付款  //已经跳转了新页面，方法无用了
    // setTimeout(function(){$(".oc-pay-btn").click()},100)
}
