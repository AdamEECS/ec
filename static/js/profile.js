let sendMailCode = function() {

}

$('#id-button-verify').click(function(event) {
    let mailCodeButton = $(event.target)
    t = 5
    mailCodeButton.text(`获取验证邮件（ ${t} ）`)
    mailCodeButton.attr('disabled', true)
    let timer = setInterval(function() {
        t -= 1
        mailCodeButton.text(`获取验证邮件（ ${t} ）`)
        if (t <= 0) {
            clearInterval(timer)
            mailCodeButton.removeAttr('disabled')
            mailCodeButton.text(`获取验证邮件`)
        }
    }, 1000);
    return false
})

$('.button-re-verify').click(function() {
    $('#id-div-email-info').toggle()
    $('#id-div-email-update').toggle()
})
