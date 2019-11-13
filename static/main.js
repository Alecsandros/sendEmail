$('#contact-form').submit(function(e){
    event.preventDefault();

    let name = $("input[name=name]").val();
    let mail = $("input[name=mail]").val();
    let subject = $("input[name=subject]").val();
    let message = $("input[name=message]").val();

    let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    console.log(csrftoken);

    $.ajax({
        type: 'POST',
        url: '/contato/',
        data: {
            'csrfmiddlewaretoken': csrftoken,
            'name': name,
            'mail': mail,
            'subject': subject,
            'message': message
        },
        success: function(data){
            alert('funcionou')
        },
        error: function(data){
            alert('não funciou')
        }
    })
})