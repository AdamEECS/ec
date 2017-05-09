let sendMailCode = function() {

}

$('#id-button-mail-code').click(function(event) {
    let mailCodeButton = $(event.target)
    t = 5
    mailCodeButton.text(`获取（ ${t} ）`)
    mailCodeButton.attr('disabled', true)
    let timer = setInterval(function() {
        t -= 1
        mailCodeButton.text(`获取（ ${t} ）`)
        if (t <= 0) {
            clearInterval(timer)
            mailCodeButton.removeAttr('disabled')
            mailCodeButton.text(`获取`)
        }
    }, 1000);
    return false
})
