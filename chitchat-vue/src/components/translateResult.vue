<template>


    <div class="translateResult">
        <div>{{result}}</div>
    </div>
</template>

<script>
export default {
    name: 'translateResult',
    props:[
        "result"
    ],
    data() {
        return {}
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.translateResult{
    width: 45%;
    height: 200px;
    min-width: 300px;
    margin: 10px 10px;
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
</style>
