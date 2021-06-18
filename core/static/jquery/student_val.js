$( document ).ready(function() {
    alert('in jquery')

    errorClass: 'errors',
    $("#login").validate({
        
        rules: {
            email: {
                required : true,
                email: true
            },
            password : {
                required : true,
                minlength : 4,
                maxlength : 8
            },

        },

        messages: {
            email : {
                required : "Please enter the email id",
                email : "Please enter valid email id"
            },
            password : {
                required : "Please enter the Password",
                minlength : "Password length must be at least 4 characters",
                maxlength : "Password too long. not more than 8 characters"
            },
            
        }
    })

    $("#registration").validate({
        
        rules: {
            email: {
                required : true,
                email: true
            },
            c_email: {
                required : true,
                email: true
            },
            password : {
                required : true,
                minlength : 4,
                maxlength : 8
            },
            c_password : {
                required : true,
                minlength : 4,
                maxlength : 8
            },
            name : "required",
            c_name : "required",
            university : "required",

            confirm_password : {
                required : true,
                equalTo: '#password'
            },
            c_confirm_password : {
                required : true,
                equalTo: '#c_password'
            }

        },

        messages: {
            email : {
                required : "Please enter the email id",
                email : "Please enter valid email id"
            },
            password : {
                required : "Please enter the Password",
                minlength : "Password length must be at least 4 characters",
                maxlength : "Password too long. not more than 8 characters"
            },
            name : {
                required : "Please enter your name"
            },
            university : {
                required : "Please enter your Institution name"
            },
            confirm_password : {
                required : "Please re enter the password for confirmation",
                equalTo : "Password doesn't match. Kindly re-enter"
            }
        }
    })

    $(window).scroll(function() {
        $(".slideanim").each(function(){
          var pos = $(this).offset().top;
    
          var winTop = $(window).scrollTop();
            if (pos < winTop + 600) {
              $(this).addClass("slide");
            }
        })
    })
    //validation for complaint form..
    $("#student_complaint").validate({
        rules: {
            category: "required",
            description: {
                required : true,
                minlength : 50,
                maxlength : 2000
            },
            priority: "required",
        },
        messages:{
            category: "Please select your category",
            description: {
                required: "Please write your description",
                minlength : "Description should be a minimum of 50 characters.",
                maxlength : "Description should not exceed 2000 characters."
            },
            priority: "Please select your priority"
        }
    })

})

// on click function to hide or show the register button and clearing out the text box fields when inputs are collapsed // 

$(document).on("click","#student, #committee_member",function(){
    var is_student_expanded = $("#student").attr("aria-expanded")
    var is_committee_member_expanded = $("#committee_member").attr("aria-expanded")
    $("#email").val("")
    $("#password").val("")
    $("#confirm_password").val("")
    $("#university").val("")
    $("#name").val("")
    if (is_student_expanded == 'false' && is_committee_member_expanded =='false')
    {
        $("#register").hide()
    }
    else
    {
        $("#register").show()
    }
})

