// $('#id-button-verify').click(function(event) {
//     let mailCodeButton = $(event.target)
//     let form = mailCodeButton.closest('form')
//     console.log(form)
//     t = 60
//     mailCodeButton.text(`获取验证邮件（ ${t} ）`)
//     mailCodeButton.attr('disabled', true)
//     let timer = setInterval(function() {
//         t -= 1
//         mailCodeButton.text(`获取验证邮件（ ${t} ）`)
//         if (t <= 0) {
//             clearInterval(timer)
//             mailCodeButton.removeAttr('disabled')
//             mailCodeButton.text(`获取验证邮件`)
//         }
//     }, 1000);
//     return false
// })

$('.button-re-verify').click(function() {
    $('#id-div-email-info').toggle()
    $('#id-div-email-update').toggle()
})

let ajaxFormSubmit = function() {
    let ajaxForm = $(event.target)
    let img = ajaxForm.find('img')
    img.click()
    let mailCodeButton = ajaxForm.find('#id-button-verify')
    ajaxForm.ajaxSubmit(function(message) {
        if(message.success == true){
        }
    });
    t = 60
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
    return false;
}
