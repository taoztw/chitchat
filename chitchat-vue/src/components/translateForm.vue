<template>
    <div id="translateForm">

        <!-- 用户选择的翻译模式 -->
        <div class="option-box">
<!--            <span class="option-result" v-on:click="showList">{{ option_result }}</span>-->
<!--            <span class="option-result" v-on:click="showList">{{ option_result }}</span>-->
<!--            <div class="option-list">-->
<!--                <p v-for="(option,index) in option_list" v-on:click="selectOption(index)">{{ option }}</p>-->
<!--            </div>-->
<!--            <el-select class="option-result" v-model="src"  placeholder="源语言">-->
<!--                <el-option-->
<!--                    v-for="item in options"-->
<!--                    :key="item.label"-->
<!--                    :label="item.value"-->
<!--                    :value="item.value">-->
<!--                </el-option>-->
<!--            </el-select>-->

<!--            <el-select class="option-result"-->
<!--                v-model="tgt"-->
<!--                collapse-tags-->
<!--                style="margin-left: 20px;"-->
<!--                placeholder="目标语言">-->
<!--                <el-option-->
<!--                    v-for="item in options"-->
<!--                    :key="item.label"-->
<!--                    :label="item.value"-->
<!--                    :value="item.value">-->
<!--                </el-option>-->
<!--            </el-select>-->


            <input id="" type="button" value="发送" v-on:click="my_translate()">
        </div>

        <!-- 用户输入的要翻译的文字 -->
        <form class="my-form">
            <textarea class="my-textarea" v-model="translating_text" placeholder="请输入对话内容"
                      v-on:keydown.enter="my_translate"></textarea>
        </form>

    </div>




</template>


<script>
import $ from 'jquery'
import translateResult from "./translateResult";
export default {
    name: 'translateForm',
    data() {
        return {
            data:"",
            translating_text: "",
            translated_text:"",
            language: "en",
            // option_result: "中文 > 英文",
            // option_list: ["中文 > 英文", "中文 > 日文", "中文 > 韩文", "中文 > 法文", "中文 > 泰文", "中文 > 德文", "中文 > 阿拉伯文", "中文 > 俄文", "中文 > 意大利文", "中文 > 丹麦文"],
            // language_list: ["en", "jp", "kor", "fra", "th", "de", "ara", "ru", "it", "dan"],
            options: [{
                value: '简体中文',
                label: '1'
            }, {
                value: '繁体中文',
                label: '2'
            }, {
                value: '英语',
                label: '3'
            }, {
                value: '日语',
                label: '4'
            }, {
                value: '韩语',
                label: '5'
            },{value: '法语', label: '6'},{value: '西班牙语', label: '7'},{value: '意大利语', label: '8'}
                ,{value: '德语', label: '9'},{value: '土耳其语', label: '10'},{value: '俄语', label: '11'}
                ,{value: '葡萄牙语', label: '12'},{value: '越南语', label: '13'},{value: '印尼语', label: '14'}
                ,{value: '泰语', label: '15'},{value: '马来西亚语', label: '16'},{value: '阿拉伯语', label: '17'}
                ,{value: '印地语', label: '18'}],
            src: '',
            tgt: ''
        }
    },
    methods: {
        // 用户点击【翻译】，触发自定义事件，将数据传递给父组件
        my_translate: function () {
            this.$emit("my_submit", this.translating_text, this.src, this.tgt)
            // event.preventDefault();
        },
        // 获取日志
        get_data(){
            // let token = this.check_user_login()
            // this.$rout('https://127.0.0.1:8000/api/chat?message=1234')
            window.open('https://127.0.0.1:8000','_blank') // 新窗口打开外链接
        },
    //     screenFuc: function () {
    //         var topHeight = $(".chatBox-head").innerHeight();//聊天头部高度
    //         //屏幕小于768px时候,布局change
    //         var winWidth = $(window).innerWidth();
    //         if (winWidth <= 768) {
    //             var totalHeight = $(window).height(); //页面整体高度
    //             $(".chatBox-info").css("height", totalHeight - topHeight);
    //             var infoHeight = $(".chatBox-info").innerHeight();//聊天头部以下高度
    //             //中间内容高度
    //             $(".chatBox-content").css("height", infoHeight - 46);
    //             $(".chatBox-content-demo").css("height", infoHeight - 46);
    //
    //             $(".chatBox-list").css("height", totalHeight - topHeight);
    //             $(".chatBox-kuang").css("height", totalHeight - topHeight);
    //             $(".div-textarea").css("width", winWidth - 42);
    //         } else {
    //             $(".chatBox-info").css("height", 525);
    //             $(".chatBox-content").css("height", 448);
    //             $(".chatBox-content-demo").css("height", 478);
    //             $(".chatBox-list").css("height", 495);
    //             $(".chatBox-kuang").css("height", 495);
    //             $(".div-textarea").css("width", 328);
    //         }
    //     },
    //
    //     sendMessage(){
    //         let _this = this;
    //         var textContent = $(".div-textarea").html().replace(/[\n\r]/g, '<br>')
    //         if (textContent != "") {
    //             $(".chatBox-content-demo").append("<div class=\"clearfloat\">" +
    //                 "<div class=\"author-name\"><small class=\"chat-date\">"+this.getTime()+"</small> </div> " +
    //                 "<div class=\"right\"> <div class=\"chat-message\"> " + textContent + " </div> " +
    //                 "<div class=\"chat-avatars\"><img src=\"../assets/icon02.png\" alt=\"头像\" /></div> </div> </div>");
    //             //发送后清空输入框
    //             $(".div-textarea").html("");
    //             //聊天框默认最底部
    //             $(document).ready(function () {
    //                 $("#chatBox-content-demo").scrollTop($("#chatBox-content-demo")[0].scrollHeight);
    //             });
    //
    //             let url = "http://127.0.0.1:8000/api/chat?message="+encodeURIComponent(textContent)
    //             $.ajax({
    //                 type:"GET",
    //                 url:url,
    //                 timeout : 10000, //超时时间设置，单位毫秒
    //                 // dataType:"html",
    //                 success:function(result){
    //                     // alert(result)
    //                     _this.getMessage(result);
    //                 },
    //                 error:function(jqXHR){
    //                     console.log("Error: "+jqXHR.status);
    //                 }
    //             });
    //
    //         }
    //     },
    //     getMessage(result){
    //         var textContent = $(".div-textarea").html().replace(/[\n\r]/g, '<br>')
    //         $(".chatBox-content-demo").append("<div class=\"clearfloat\">" +
    //             "<div class=\"author-name\"><small class=\"chat-date\">"+this.getTime()+"</small> </div> " +
    //             "<div class=\"left\"> <div class=\"chat-avatars\"><img src=\"../assets/icon01.png\" alt=\"头像\" /></div>" +
    //             "<div class=\"chat-message\"> " + result + " </div>  </div> </div>");
    //         //发送后清空输入框
    //         $(".div-textarea").html("");
    //         //聊天框默认最底部
    //         $(document).ready(function () {
    //             $("#chatBox-content-demo").scrollTop($("#chatBox-content-demo")[0].scrollHeight);
    //         });
    //     },
    //     getTime() {
    //         var date = new Date();
    //         var seperator1 = "-";
    //         var seperator2 = ":";
    //         var month = date.getMonth() + 1;
    //         var strDate = date.getDate();
    //         if (month >= 1 && month <= 9) {
    //             month = "0" + month;
    //         }
    //         if (strDate >= 0 && strDate <= 9) {
    //             strDate = "0" + strDate;
    //         }
    //         var currentdate = date.getFullYear() + seperator1 + month + seperator1 + strDate
    //             + " " + date.getHours() + seperator2 + date.getMinutes()
    //             + seperator2 + date.getSeconds();
    //         return currentdate;
    //     },
    //
    //     // 下使用jQuery库来个翻译选项加一些下拉的动画
    //     showList: function () {
    //         if ($('.option-list').css('display') != 'none') {
    //             $('.option-list').slideUp();
    //         }
    //         else {
    //             $('.option-list').slideDown();
    //         }
    //     },
    //     // 通过用户选择的翻译模式，设置相应的数据
    //     selectOption: function (index) {
    //         $('.option-list').slideUp();
    //         this.language = this.language_list[index];
    //         this.option_result = this.option_list[index];
    //     }
    // },

    //页面加载完自动加载区域
    mounted(){
        let _this = this;//赋值vue的this
        // window.onresize = ()=>{
        //     //调用methods中的事件
        //     _this.screenFuc();
        _this.get_data()
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.chatContainer,.chatContainer div, .chatContainer ul, .chatContainer li, .chatContainer p{
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
}
/* 设置滚动条的样式 */
::-webkit-scrollbar {
    width:5px;
}
/* 滚动槽 */
::-webkit-scrollbar-track {
    border-radius:10px;
}
/* 滚动条滑块 */
::-webkit-scrollbar-thumb {
    border-radius:10px;
    background:#8C85E6;
    -webkit-box-shadow:#8C85E6;
}
::-webkit-scrollbar-thumb:window-inactive {
    background: rgba(175, 190, 255, 0.4);
}
/*按钮样式*/
.btn-default-styles {
    outline: none;
    resize: none;
    border: none;
    display: inline-block;
    padding: 5px 10px;
    margin-bottom: 0;
    font-size: 14px;
    font-weight: 400;
    line-height: 1.42857143;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    -ms-touch-action: manipulation;
    touch-action: manipulation;
    cursor: pointer;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    background-image: none;
    background: #bbb;
    color: #fff;
    border-radius: 4px;
}
.btn-default-styles:focus {
    outline: none;
}
.btn-default-styles:hover {
    background: #c5c5c5;
    animation: anniu 1s infinite;
}
.btn-default-styles:active {
    box-shadow: 0 2px 3px rgba(0, 0, 0, .2) inset;
}


.chatContainer{
    position: fixed;
    bottom: 20px;
    right: 20px;
}
.chatBtn{
    width: 50px;
    height: 50px;
    background: #01bef0;
    color: #fff;
    line-height: 50px;
    text-align: center;
    border-radius: 50%;
    box-shadow: 2px 2px 2px #d4d4d4;
    cursor: pointer;
    position: absolute;
    bottom: 0;
    right: 0;
    overflow: hidden;
}
.chatBtn:hover{
    background: #01b3df;
    box-shadow: none;
}
.chatBtn>i{
    font-size: 25px;
}
.chatBox{
    width: 370px;
    min-width: 320px;
    height: 570px;
    border-radius: 10px;
    background: #f5ecff;
    position: fixed;
    top: 5%;
    left: 40%;

    overflow: hidden;
    border: solid 1px #d5d5d5;
    box-shadow: 1px 1px 2px #c0c0c0;
    z-index: 1005;
}
.chatBox-head{
    width: 100%;
    height: 45px;
    background: #01aee0;
    position: absolute;
    top: 0;
    left: 0;
}
.chatBox-head-one{
    width: 100%;
    height: 45px;
    line-height: 45px;
    color: #fff;
    font-size: 20px;
    text-align: center;
    position: absolute;
    top: 0;
    left: 0;
}
.chatBox-head-two{
    width: 100%;
    height: 75px;
    color: #fff;
    padding: 10px 10px;
    display: none;
    position: absolute;
    top: 0;
    left: 0;
}
.chat-return{
    float: left;
    width: 55px;
    height: 55px;
    line-height: 55px;
    border-radius: 10px;
    cursor: pointer;
    text-align: center;
}

.chat-return:hover{
    background: #0188b7;
}
.chat-close{
    float: right;
    width: 55px;
    height: 55px;
    line-height: 55px;
    border-radius: 10px;
    cursor: pointer;
    text-align: center;
}
.chat-close:hover{
    background: #0188b7;
}
.chat-people{
    float: left;
}
.chat-people>div{
    height: 55px;
    display: inline-block;
    vertical-align: middle;
    line-height: 55px;
    margin-left: 5px;
}
.chat-people>div:nth-of-type(1){
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: #eee;
    overflow: hidden;
}
.chat-people>div:nth-of-type(1)>img{
    width: 50px;
    height: 50px;
}
.chat-people>div:nth-of-type(2){
    width: 165px;
    text-align: left;
    height: 55px;
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
}

.chatBox-info{
    width: 100%;
    height: 495px;
    background: #fff;
    text-align: left;
    position: absolute;
    top: 45px;
    left: 0;
}

.chatBox-list{
    width: 100%;
    height: 495px;
    overflow-y: scroll;
}
.chat-list-people:hover{
    cursor: pointer;
    background: #f8f8f8;
}
.chat-list-people>div{
    height: 55px;
    display: inline-block;
    vertical-align: middle;
    margin-left: 10px;
}
.chat-list-people>div:nth-of-type(1){
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: #eee;
    overflow: hidden;
}
.chat-list-people>div:nth-of-type(1)>img{
    width: 40px;
    height: 40px;
}


.chat-name{
    width: 230px;
}
.chat-name>p{
    margin: 0;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}
.chat-name>p:nth-of-type(1){
    line-height: 55px;
}
.chat-list-people>div.message-num{
    display: inline-block;
    height: auto;
    min-width: 10px;
    padding: 3px 5px;
    font-size: 12px;
    font-weight: 700;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    border-radius: 10px;
    margin-right: 15px;
    margin-top: 14px;
    color: #fff;
    background: #f46266;
    float: right;
}
.chat-message-num{
    display: inline-block;
    height: auto;
    min-width: 10px;
    padding: 3px 5px;
    font-size: 12px;
    font-weight: 700;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    border-radius: 10px;
    margin-right: 15px;
    margin-top: 14px;
    color: #fff;
    background: #f46266;
    position: absolute;
    bottom: 40px;
    right: -24px;
}
.chatBox-kuang{
    width: 100%;
    height: 495px;
    display: none;
}
.chatBox-content{
    width: 100%;
}
.chatBox-content-demo{
    width: 100%;
    overflow-y: scroll;
}

.clearfloat:after{
    display:block;
    clear:both;
    content:"";
    visibility:hidden;
    height:0
}
.clearfloat{
    zoom:1;
    margin: 10px 10px;
}
.clearfloat .right{
    float: right;
}
.author-name{
    text-align: center;
    margin: 15px 0 5px 0;
    color: #888;
}

.clearfloat .chat-message{
    max-width: 252px;
    text-align: left;
    padding: 8px 12px;
    border-radius: 6px;
    word-wrap:break-word;
    display: inline-block;
    position: relative;
}


.clearfloat .left .chat-message{
    background: #D9D9D9;
    min-height: 36px;
}
.clearfloat .left .chat-message:before{
    position: absolute;
    content: "";
    top: 8px;
    left: -6px;
    border-top: 10px solid transparent;
    border-bottom: 10px solid transparent;
    border-right: 10px solid #D9D9D9;
}

.clearfloat .right{
    text-align: right;
}
.clearfloat .right .chat-message{
    background: #8c85e6;
    color: #fff;
    text-align: left;
    min-height: 36px;
}
.clearfloat .right .chat-message:before{
    position: absolute;
    content: "";
    top: 8px;
    right: -6px;
    border-top: 10px solid transparent;
    border-bottom: 10px solid transparent;
    border-left: 10px solid #8c85e6;
}

.clearfloat .chat-avatars{
    display: inline-block;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: #eee;
    vertical-align: top;
    overflow: hidden;
}
.clearfloat .chat-avatars>img{
    width: 30px;
    height: 30px;
}
.clearfloat .left .chat-avatars{
    margin-right: 10px;
}
.clearfloat .right .chat-avatars{
    margin-left: 10px;
}

.chatBox-send{
    width: 100%;
    padding: 10px 5px;
    background: #eee;
    border-top: 1px #D0D0D0 solid;
    position: absolute;
    bottom: 0;
    left: 0;
}
.div-textarea{
    width: 260px;
    min-height: 20px;
    max-height: 100px;
    _height: 120px;
    padding: 3px;
    outline: 0;
    background: #fff;
    font-size: 14px;
    line-height: 20px;
    word-wrap: break-word;
    overflow-x: hidden;
    overflow-y: auto;
    user-modify: read-write-plaintext-only;    /*纯文本*/
    -webkit-user-modify: read-write-plaintext-only;
    -moz-user-modify: read-write-plaintext-only;
}
.div-textarea:focus{
    box-shadow: 0 0 15px rgba(82, 168, 236, 0.6);
}
.chatBox-send>div{
    float: left;
}
.chatBox-send>div:nth-of-type(2){
    font-size: 0;
}
.chatBox-send>div button{
    padding: 1px 5px;
    margin-left: 3px;
}
.chatBox-send>div label{
    padding: 1px 5px;
    margin-left: 3px;
}
#chat-biaoqing{
    position: relative;

}
.hidden{
    display: none;
}
.biaoqing-photo{
    width: 200px;
    height: 160px;
    background: #ffffff;
    position: absolute;
    top: -160px;
    right: 40px;
    text-align: left;
    border-radius: 5px;
    border: solid 1px #c5c5c5;
    display: none;
}
.biaoqing-photo::before{
    content: '';
    position: absolute;
    border-top: solid 7px #c5c5c5;
    border-left: solid 9px transparent;
    border-right: solid 9px transparent;
    bottom: -7px;
    right: 36px;
}
.biaoqing-photo::after{
    content: '';
    position: absolute;
    border-top: solid 7px #fff;
    border-left: solid 10px transparent;
    border-right: solid 10px transparent;
    bottom: -5px;
    right: 35px;
}
.biaoqing-photo>ul{
    margin: 0;
    width: 200px;
    height: 160px;
    padding: 3px 2px;
    list-style: none;
}
.biaoqing-photo>ul>li{
    float: left;
    height: 30px;
    margin-left: 2px;
}
.emoji-picker-image{
    display: inline-block;
    width: 30px;
    height: 30px;
    background: url(../assets/bqxtb01.png) no-repeat;
    background-size: 200px auto;
    cursor: pointer;
}
.biaoqing-photo>ul>li span.emoji-picker-image:hover{
    border: solid 1px #f5f5f5;
}
.chat-message img{
    width: 220px;
    height:auto;
}

@media all and (max-width: 768px) {
    .chatBox{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
}
@media all and (max-width: 370px){
    .chat-name{
        width: 185px;
    }
    .chat-people>div:nth-of-type(2){
        width: 120px;
    }
    .clearfloat .chat-message{
        max-width: 240px;
    }
}
#translateForm {
    width: 45%;
    min-width: 300px;
    margin: 10px 10px;
    /*background-color: #0049ff;*/
}
.option-box {
    width: 100%;
    min-width: 300px;
    height: 50px;
    position: relative;
    z-index: 99;
}
.option-result {
    width: 23%;
    height: 38px;
    display: inline-block;
    text-align: center;
    line-height: 38px;
    border-radius: 5px;
    /*border: 1px solid #666;*/
    color: #666;
    box-sizing: border-box;
    font-size: 18px;
    font-family: "微软雅黑";
    cursor: pointer;
}
.option-list {
    width: 300px;
    position: absolute;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-content: flex-start;
    top: 50px;
    left: 0px;
    background-color: #fff;
    border-radius: 10px;
    display: none;
}
.option-list p {
    display: inline-block;
    width: 45%;
    height: 30px;
    text-align: center;
    line-height: 30px;
    border-radius: 5px;
    margin: 10px 5px;
    cursor: pointer;
}
.option-list p:hover {
    background-color: rgba(255, 50, 50, 0.5);
}
input[type='button'] {
    display: inline-block;
    width: 108px;
    height: 40px;
    background-color: #e02433;
    border: none;
    border-radius: 5px;
    color: #fff;
    font-size: 20px;
    font-family: "微软雅黑";
    box-sizing: border-box;
    cursor: pointer;
    margin-left: 5px;
}
.my-form {
    width: 100%;
    position: relative;
    top: 4px;
    border-radius: 5px;
    margin: 0 auto;
}
.my-textarea {
    width: 100%;
    height: 200px;
    min-width: 300px;
    margin: 0 auto;
    border: none;
    border-radius: 10px;
    font-size: 17px;
    color: #666;
    padding: 40px 20px;
    box-sizing: border-box;
    font-family: "微软雅黑";
    resize: none;
    background-color: rgb(242, 242, 242);
}


@font-face {font-family: "iconfont";
    src: url('../assets/iconfont.eot?t=1515469903495'); /* IE9*/
    src: url('../assets/iconfont.eot?t=1515469903495#iefix') format('embedded-opentype'), /* IE6-IE8 */
    url('data:application/x-font-woff;charset=utf-8;base64,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') format('woff'),
    url('../assets/iconfont.ttf?t=1515469903495') format('truetype'); /* chrome, firefox, opera, Safari, Android, iOS 4.2+*/
    /*url('../assets/iconfont.svg?t=1515469903495#iconfont') format('svg'); !* iOS 4.1- *!*/
}

.iconfont {
    font-family:"iconfont" !important;
    font-size:16px;
    font-style:normal;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

.icon-gouwuche2:before { content: "\e610"; }

.icon-verylarger-view:before { content: "\e622"; }

.icon-tehui:before { content: "\e60c"; }

.icon-gengduo1:before { content: "\e606"; }

.icon-xiaoxi:before { content: "\e609"; }

.icon-houtui:before { content: "\e607"; }

.icon-gouwuche:before { content: "\e60d"; }

.icon-guojia:before { content: "\e6c0"; }

.icon-xiaoxi1:before { content: "\e62d"; }

.icon-shoucang:before { content: "\e60f"; }

.icon-tuxiang:before { content: "\e645"; }

.icon-yushou:before { content: "\e644"; }

.icon-icon05:before { content: "\e630"; }

.icon-jiadian:before { content: "\e670"; }

.icon-shoucang1:before { content: "\e6a2"; }

.icon-dingdan:before { content: "\e682"; }

.icon-shuaxin:before { content: "\e6fc"; }

.icon-kefu:before { content: "\e6df"; }

.icon-shoucang2:before { content: "\e71a"; }

.icon-wode2:before { content: "\e6f3"; }

.icon-gengduo:before { content: "\e617"; }

.icon-larger-view:before { content: "\e655"; }

.icon-tuxiang1:before { content: "\e63d"; }

.icon-geren2-copy:before { content: "\e657"; }

.icon-jiushui:before { content: "\e61b"; }

.icon-shuji:before { content: "\e61e"; }

.icon-fasong:before { content: "\e625"; }

.icon-xuanzhuan:before { content: "\e614"; }

.icon-shouye:before { content: "\e60e"; }

.icon-guanbi:before { content: "\e72c"; }

.icon-wode:before { content: "\e61d"; }

.icon-app:before { content: "\e62c"; }

.icon-fanhui:before { content: "\e6d6"; }

.icon-guanbi1:before { content: "\e705"; }

.icon-yingyangbaojian:before { content: "\e639"; }

.icon-fenlei:before { content: "\e60a"; }

.icon-xiaoxi2:before { content: "\e69a"; }

.icon-shanchu:before { content: "\e642"; }

.icon-qian:before { content: "\e624"; }

.icon-shoucangjia:before { content: "\e618"; }

.icon-meishi:before { content: "\e7af"; }

.icon-larger-view2:before { content: "\e627"; }

.icon-dingbu:before { content: "\e67d"; }

.icon-pingjia:before { content: "\e619"; }

.icon-xiaoxi3:before { content: "\e61a"; }

.icon-wode1:before { content: "\e621"; }

.icon-wode4:before { content: "\e611"; }

.icon-yingerfeng:before { content: "\e620"; }

.icon-xiaoxi4:before { content: "\e623"; }

.icon-xiaoxi5:before { content: "\e67e"; }

.icon-ccgl-shouhuoguanli-3:before { content: "\e601"; }

.icon-liwu_gift:before { content: "\e604"; }

.icon-shoucang3:before { content: "\e613"; }

.icon-jiaju:before { content: "\e65d"; }

.icon-shoucang4:before { content: "\e602"; }

.icon-sousuo2:before { content: "\e61c"; }

.icon-biaoqing:before { content: "\e605"; }

.icon-kouhong:before { content: "\e60b"; }

.icon-gengduo2:before { content: "\e728"; }

.icon-gift:before { content: "\e600"; }

.icon-lingquan:before { content: "\e61f"; }

.icon-jifen:before { content: "\e674"; }

.icon-qianjin:before { content: "\e608"; }

.icon-shoucang11:before { content: "\e603"; }

.icon-shuaxin1:before { content: "\e626"; }

.icon-zhongxin:before { content: "\e650"; }

.icon-list-view:before { content: "\e628"; }

.icon-fushi:before { content: "\e63c"; }

.icon-saoyisao:before { content: "\e612"; }

.icon-double-vertical:before { content: "\e615"; }

.icon-up-down:before { content: "\e66f"; }

.icon-sousuo1:before { content: "\e66e"; }

.icon-double-cross:before { content: "\e616"; }

.icon-left-right:before { content: "\e7b0"; }


</style>
