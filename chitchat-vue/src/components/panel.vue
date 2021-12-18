<template>

<div>

    <el-tabs type="border-card" id="el-tabs-style-tmp">

        <div id="login-box">
                        <span style="color: red"><router-link v-if="login_flag" to="/">已登录</router-link>
                        <router-link v-else to="/login">未登陆</router-link>
                        </span>
            &nbsp;|&nbsp;

            <span><button @click="login_out">退出</button>
                        </span>
        </div>


        <el-tab-pane label="聊天机器人系统演示">
            <h1>简单测试</h1>
            <div class="main-content">
<!--修改机器翻译请求为对话请求-->

                <translateForm @my_submit="getText"></translateForm>

                <translateResult :result="translated_text"></translateResult>
<!--                <img src="../assets/icon.png" alt="">-->

            </div>

                    <el-row class="elrow" type="flex" justify="center" align="middle" :gutter="15">
                        <el-col :span="15">
                        <el-card  shadow="hover">
<!--                            <img src="../assets/icon.png" alt="">-->
                            <span id="textchat" style="text-align: center" >多轮对话测试页面</span>
                            <el-button  @click="go_chat" id="tiaozhuan"  type="primary" round>点击跳转</el-button>
<!--                            <div style="background-color: blue;color: #fff;">多轮对话测试</div>-->
                        </el-card>
                        </el-col>

                    </el-row>


        </el-tab-pane>


        <el-tab-pane label="初始训练">
            <el-steps :active="active" finish-status="success" id="el-step-style">
                <el-step title="模型创建" icon="el-icon-edit" description="创建模型目录"></el-step>
                <el-step title="文件上传" icon="el-icon-upload" description="上传文件并进行处理"></el-step>
                <el-step title="开始训练" icon="el-icon-time" description="训练模型"></el-step>
            </el-steps>
            <el-collapse id="el-collapse-item-style" v-model="activeNames" @change="handleChange">

                <el-collapse-item title="初始化模型" name="1">
                    <br>
                    <div>模型目录唯一，请使用英文</div>
                    <div>微调训练模型目录需使用已存在模型目录且包含finetuning字符串，如：modelName_finetuning</div>
<!--                    <div>训练模型名称为源语言和目标语言代码。源语言英文，目标语言中文：en2cn_step_{step}.pt</div>-->
                    <div id="trainPanel">
                        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">

                            <el-form-item label="模型目录" prop="name">
                                <el-input v-model="ruleForm.name"></el-input>
                            </el-form-item>

                            <el-form-item label="epoch" prop="region">
                                <el-select v-model="ruleForm.src" placeholder="epoch">
                                    <el-option label="30" value="30"></el-option>
                                    <el-option label="40" value="40"></el-option>
                                    <el-option label="50" value="50"></el-option>
                                    <el-option label="70" value="70"></el-option>
                                    <el-option label="100" value="100"></el-option>
                                </el-select>
                            </el-form-item>

                            <el-form-item label="batch_size" prop="region">
                                <el-select v-model="ruleForm.tgt" placeholder="batch size">
                                    <el-option label="8" value="8"></el-option>
                                    <el-option label="16" value="16"></el-option>
                                    <el-option label="32" value="32"></el-option>
                                    <el-option label="64" value="64"></el-option>
                                    <el-option label="256" value="256"></el-option>
                                    <el-option label="1024" value="1024"></el-option>
                                </el-select>
                            </el-form-item>
                            <el-form-item>
                                <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
                                <el-button @click="resetForm('ruleForm')">重置</el-button>
                            </el-form-item>
                        </el-form>
                    </div>
                </el-collapse-item>

                <el-collapse-item title="训练文件处理" name="2">
                    <br>
                    <div>上传训练文件，保存在上一步模型文件夹/data目录</div>
                    <strong>文件名需要和模型名相同</strong>

                    <el-upload
                        action="#"
                        :file-list="fileList"
                        :on-change="changeData"
                        :http-request="handleRequest"
                        multiple>
                        <!--                        :before-upload="beforeUpload"-->
                        <el-button class="btn upload-btn" type="primary">上传训练文件</el-button>

                        <div slot="tip" class="el-upload__tip">不限制大小</div>
                        <!--                        <el-progress :stroke-width="16" :percentage="progressPercent"></el-progress>-->
                    </el-upload>
                    <el-progress :stroke-width="16" :percentage="progressPercent"></el-progress>


<!--                    对原始训练文件进行标准处理-->
                    <el-form :inline="true" ref="form" :model="form" label-width="80px" id="filepreprocess">
<!--                        <div>输入上传的文件名，对数据预处理。</div>-->
<!--                        <el-form-item label="文件名称">-->
<!--                            <el-input v-model="file_name"></el-input>-->
<!--                        </el-form-item>-->
<!--                        <el-form-item>-->
<!--                            <el-button v-if="raw_file_progress_flag" type="primary" @click="datapreprocess">立即处理</el-button>-->
<!--                            <el-button v-else type="primary" :loading="true" size="small">正在处理</el-button>-->
<!--                        </el-form-item>-->
                    </el-form>
                </el-collapse-item>

                <el-collapse-item title="训练" name="3">
                    <br>
                    <el-button type="primary" @click="train_model">开始训练</el-button>
                    <el-button type="primary" @click="tensorboard_r">tensorboard可视化</el-button>
<!--                    <el-button type="primary" @click="test_model">模型测试</el-button>-->

<!--                    <div id="el_progress_style">-->
<!--                        <el-progress :text-inside="true" :stroke-width="18" :percentage="train_process" status="success"></el-progress>-->
<!--                    </div>-->
<!--                    <div>测试结果：{{test_result}}</div>-->
                </el-collapse-item>

            </el-collapse>


        </el-tab-pane>



        <el-tab-pane label="训练日志查看">
            <el-button type="info" @click="get_log_info">获取日志</el-button>
            <div id="log_look_content_style" v-html="log_info">
            </div>
        </el-tab-pane>

<!--        <el-tab-pane label="定时任务补偿">-->
<!--            <div>-->
<!--                <el-upload-->
<!--                    class="upload-demo"-->
<!--                    ref="upload"-->
<!--                    :multiple="false"-->
<!--                    action="void"-->
<!--                    :http-request="customUpload"-->
<!--                    :on-remove="handleRemove"-->
<!--                    :on-progress="progressA"-->
<!--                    :file-list="fileList"-->
<!--                    multiple-->
<!--                    :auto-upload="true">-->
<!--                    <el-button slot="trigger" size="small" type="primary">选取文件</el-button>-->
<!--                </el-upload>-->
<!--            </div>-->

<!--        </el-tab-pane>-->

    </el-tabs>
</div>
</template>

<script>
import translateForm from "./translateForm";
import translateResult from "./translateResult";
import login from "./Login"
export default {
    name: "test",
    components: {
        translateForm,
        translateResult,
    },
    data: function () {
        return {
            // 模型生成调整参数
            p_max_len: 25,
            p_repetition_penalty: 1.0,
            p_temperature: 1,
            p_topk: 8,
            p_topp: 0,


            test_result:'',
            log_info:'',
            // 模型训练进度条百分比数
            train_process:0,
            // 登陆状态
            login_flag:false,
            // 步骤条测试变量
            active:0,
            //原始数据文件处理标志
            raw_file_progress_flag:true,
            // 上传文件名字
            file_name:'',
            // 模型目录名称,源语言，目标语言
            model_info:{},
            // 折叠面板参数
            activeNames: ['3'],
            // 删除文件变量
            files: [],
            msg: "",
            showFlag: false,

            // 翻译变量
            translateing_text: "",
            progressPercent:0,
            language: "",
            showflag:false,
            translated_text: "",

            ruleForm: {
                name: '',
                src: '',
                tgt:'',
            },
            fileList: [],
            rules: {
                name: [
                    { required: true, message: '请输入模型名称', trigger: 'blur' },
                    { min: 3, max: 20, message: '长度在 3 到 30 个字符', trigger: 'blur' }
                ],
                src: [
                    { required: true, message: '请选择epoch', trigger: 'change' }
                ],
                tgt: [
                    { required: true, message: '请选择batch size', trigger: 'change' }
                ],
            },
        }
    },
    methods: {
        tensorboard_r(){
            let href = "http://localhost:6006/#scalars"
            window.open(href, '_blank')
        },
        // 测试模型评分
        test_model(){
            let token = this.check_user_login()
            this.$axios({
                url: this.BASE_URL + "v1/model/test",
                method: "post",
                auth:{username: token}
            }).then(res =>{
                this.test_result = res.data['msg']
                this.$message({
                    message:"测试成功",
                    duration:1000,
                    type:"success"
                })
            }).catch(error => {
                console.log(error)
                this.$message({
                    message:'测试文件不存在',
                    duration:1000,
                    type:"error"
                })
            })
        },
        // 获取日志
        get_log_info(){
            let token = this.check_user_login()
            this.$axios({
                url: this.BASE_URL + "v1/file/log",
                method: "post",
                data: {
                    folder:this.model_info['model_name'],
                    src:this.model_info['src'],
                    tgt:this.model_info['tgt']
                },
                auth:{username: token}
            }).then(res =>{
                this.log_info = res.data['msg']
                this.$message({
                    message:"获取日志成功",
                    duration:1000,
                    type:"success"
                })
            }).catch(error => {
                this.$message({
                    message:"获取日志失败",
                    duration:1000,
                    type:"error"
                })
            })
        },
        change_login_status(){
            let token = localStorage.token || sessionStorage.token;
            if (token) {
                this.login_flag=true
            }

        },
        // 检查用户登陆
        check_user_login() {
            let token = localStorage.token || sessionStorage.token;
            if (!token) {
                let self = this;
                this.$confirm("未登陆系统", {
                    callback() {
                        self.$router.push("/login");
                    }
                });
                return false
            }
            return token;
        },
        login_out(){
            // sessionStorage.removeItem('token')
            // sessionStorage.removeItem('user')
            sessionStorage.clear()
            localStorage.clear()
            this.login_flag = false
            this.$message({
                message:"退出系统成功",
                duration:1000,
                type:"success"
            })

        },
        // 对训练数据进行数据预处理的请求
        datapreprocess() {
            this.raw_file_progress_flag=false
            let token = this.check_user_login()
            this.$axios({
                url: this.BASE_URL + "v1/data/preprocessing",
                method: "post",
                data: {
                    file_name:this.file_name,
                },
                auth:{username: token}
            }).then(res =>{
                // console.log("数据预处理成功",res.data.msg)
                // if(response.code === 1){
                //   this.$router.push({path: '/main'})
                // }
                this.raw_file_progress_flag=true
                if (this.active++ > 2) this.active = 0;
                this.$message({
                    message:"数据处理成功",
                    duration:1000,
                    type:"success"
                })
            }).catch(error => {
                    console.log(error);
                    this.raw_file_progress_flag=true
                    this.$message({
                        message:"数据处理失败",
                        duration:1000,
                        type:"error"
                    })
        })},
        customUpload(file) {
            let FormDatas = new FormData();
            FormDatas.append('file', file.file);
            this.$axios({
                url: 'http://192.168.1.5:8889/upload',
                method: 'post',
                data: FormDatas,
                //上传进度
                onUploadProgress: (progressEvent) => {
                    let num = progressEvent.loaded / progressEvent.total * 100 | 0;  //百分比
                    file.onProgress({percent: num})     //进度条
                }
            }).then(data => {
                file.onSuccess(); //上传成功(打钩的小图标)
            })
        },
        /**     文件正在上传时的钩子    **/
        progressA(event, file) {},
        /**     移除上传文件    **/
        handleRemove(file) {
            this.$refs.upload.abort(); //取消上传
            this.$message({message: '成功移除' + file.name, type: 'success'});
        },



        // 发送训练模型请求
        train_model: function (){
            let token = this.check_user_login()
            this.$axios({
                url: this.BASE_URL + "v1/model/train",
                method: "post",

                data: {
                    folder:this.model_info['model_name'],
                    epoch:this.model_info['src'],
                    batch_size:this.model_info['tgt']
                },
                auth:{username: token}
            }).then(res =>{
                // console.log("创建模型成功",res.data.msg)
                // if(response.code === 1){
                //   this.$router.push({path: '/main'})
                // }
                this.model_info['model_name'] = this.ruleForm['name']
                this.model_info['src'] = this.ruleForm['src']
                this.model_info['tgt'] = this.ruleForm['tgt']
                if (this.active++ > 2) this.active = 0;
                this.$message({
                    message:"模型创建成功",
                    duration:1000,
                    type:"success"
                })
                // this.test_tmp()
            }).catch(error => {
                console.log(error);
                this.$message({
                    message:"模型创建失败",
                    duration:1000,
                    type:"error"
                })
        })},


        // 对话请求
        getText: function (text, src, tgt) {
            this.translateing_text = text;

            // this.language = lan;
            console.log(this.translateing_text)
            let token = this.check_user_login()
            // 初始化要传递给API的数据
            this.$axios({
                url:this.BASE_URL + "v1/chat",
                method:'post',
                data:{
                    text: text,
                },
                auth:{username: token}
            }).then(res=>{
                // console.log(res.data);
                console.log('对话成功')
                console.log(res.data)
                this.$message({
                    message:"回复成功",
                    duration:1000,
                    type:"success"
                })
                this.translated_text = res.data['msg']
            }).catch(error=>{
                console.log(error.response.data['msg']);
                this.$message({
                    message:error.response.data['msg'],
                    duration: 1000,
                    type: "error"
                })
            })
        },

        // 提交模型请求
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    if (!this.ruleForm.src || !this.ruleForm.tgt){
                        this.$message({
                            duration:1000,
                            message:"完善相关参数",
                            type:"error"
                        })
                    }else{
                        let token = this.check_user_login()
                    this.$axios({
                        url: this.BASE_URL + "v1/model/initialize",
                        method: "post",

                        data: {
                            folder:this.ruleForm['name'],
                            epoch:this.ruleForm['src'],
                            batch_size:this.ruleForm['tgt']
                        },
                        auth:{username: token}
                    }).then(res =>{
                        console.log("创建模型成功",res.data)
                        // if(response.code === 1){
                        //   this.$router.push({path: '/main'})
                        // }
                        this.model_info['model_name'] = this.ruleForm['name']
                        this.model_info['src'] = this.ruleForm['src']
                        this.model_info['tgt'] = this.ruleForm['tgt']
                        if (this.active++ > 2) this.active = 0;
                        this.$message({
                            message:"创建模型成功",
                            duration:1000,
                            type:"success"
                        })
                    }).catch(err => {
                        console.log(err.data);
                        this.$message({
                            message:'创建模型出错',
                            duration:1000,
                            type:"error"
                        })
                })}} else {
                    console.log('error submit!!');
                    return false;
                }
            });
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
        },


        // 文件上传

        //上传前对文件大小进行校验
        // beforeUpload(file) {
        //     const isLt2M = file.size / 1024 / 1024 < 500;
        //     if (!isLt2M) {
        //         this.$message.error('上传文件大小大小不能超过 500MB!');
        //         return isLt2M;
        //     }
        // },
        changeData (file, fileList) {
            // 数据小于0.1M的时候按KB显示
            const size = file.size/1024/1024 > 0.1 ? `(${(file.size/1024/1024).toFixed(1)}M)` : `(${(file.size/1024).toFixed(1)}KB)`
            file.name.indexOf('M')>-1 || file.name.indexOf('KB')>-1 ? file.name : file.name += size
        },
        // 文件上传
        handleRequest (data) {
            let formdata = new FormData()
            console.log('data file',data.file)
            formdata.append('file', data.file)
            let token = this.check_user_login()
            const config = {
                onUploadProgress: progressEvent => {
                    // progressEvent.loaded:已上传文件大小
                    // progressEvent.total:被上传文件的总大小
                    this.progressPercent = Number((progressEvent.loaded / progressEvent.total * 100).toFixed(2))
                    // console.log(this.progressPercent)
                },
                auth:{username: token},
            }
            this.$axios.post(this.BASE_URL + "v1/file",formdata,config,).then(res => {
                console.log('上传成功')
                console.log(res.data)
                this.$message({
                    message:"上传成功",
                    duration:1000,
                    type:"success"
                })
                this.getfiles()
            }).catch(error=>{
                this.$message({
                    message:"上传失败",
                    duration:1000,
                    type:"error"
                })
            })
        },


        // data目录文件函数
        // 删除文件
        delNote(index,file){
            console.log(index);
            let token = this.check_user_login()
            this.files.splice(index, 1)
            this.$axios({
                url:this.BASE_URL + "v1/file",
                method: 'delete',
                data:{
                    filename:file
                },
                auth:{username:token}
            }).then(res=>{
                this.$message({
                    message:res.data.msg,
                    duration:1000,
                    type:"success"
                })
            }).catch(err=>{
                this.$message({
                    message:err.data.msg,
                    duration:1000,
                    type:"error"
                })
            })
        },
        // 获取文件列表
        getfiles(){
            this.$axios({
                url:this.BASE_URL + "v1/file",
                method:"get",
                auth:{username:sessionStorage.token}
            }).then(res=>{
                console.log(res.data.msg)
                this.files = res.data.msg
            }).catch(err=>{
                this.showFlag= true
            })
        },
        go_chat(){
            let token = localStorage.token || sessionStorage.token;
            if (!token) {
                let self = this;
                this.$confirm("未登陆系统", {
                    callback() {
                        self.$router.push("/login");
                    }
                });
                return false
            }else {
                window.location.href = 'http://127.0.0.1:8000/'
            }

        },
        handleChange(val) {
            console.log(val);
        },
    },


    created() {
        this.change_login_status()
        console.log(this.BASE_URL)
    },
}
</script>

<style scoped>
#log_look_content_style{
    width: 70%;
    display: table;
    margin: 0 auto;
}
#el_progress_style {
    margin-top: 5px;
}
#login-box {
    /*width: ;*/
    position: absolute;
    top: 0px;
    right: 0px;
}
#filepreprocess {
    margin-top: 15px;
}
/*#el-tabs-style-tmp {*/
/*    margin-right: 60px;*/
/*}*/


#el-collapse-item-style {
    width: 70%;
    display: table;
    margin: 0 auto;
}
#el-step-style {
    margin-top: 15px;
}
h1 {
    text-align: center;
    letter-spacing: 5px;
    margin-top: 20px;
    font-size:35px;
    color: black;
}

h4 {
    color: gray;
    text-align: center;
}

.main-content {
    width: 80%;
    margin: 0 auto;
    display: flex;
    justify-content: space-around;
    align-items: flex-end;
    flex-wrap: wrap;
}
#trainPanel {
    width: 80%;
    display: flex;
    justify-content:center;
    /*align-items: center;*/

}

#tiaozhuan{
    margin-left: 10px;
}
</style>
