function bindCaptchaBtnClick(){
    $("#captcha-btn").on("click",function (event) {
        var $this = $(this);
        var email = $("input[name='email']").val();
        if (!email) {
            alert("请先输入邮箱")
            return;
        }
        //通过js发送请求：ajax - Async JavaScript And XML
        else{
            $.ajax({
                url:"/user/captcha",
                method:"POST",
                data:{
                    "email":email
                },
                success: function (res) {
                    var code = res['code'];
                    if (code == 200) {
                        //取消点击事件
                        $this.off("click");
                        //开始倒计时
                        var countDown = 60;
                        setInterval(function(){
                            if (countDown > 0) {
                                $this.text(countDown+"秒后重新发送");
                            }
                            else{
                                $this.text("获取验证码");
                                bindCaptchaBtnClick();
                                //如果不需要倒计时了，记得清除倒计时
                                clearInterval(timer);
                            }
                            countDown--;
                        }, 1000)
                        alert("验证码发送成功！");
                    }
                    else if(code == 400) {
                        alert(res["message"]);
                    }

                }
            })
        }
    })
}

//等网页文档所有元素都加载完成后再执行
$(function () {
    bindCaptchaBtnClick()
})