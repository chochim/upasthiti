jQuery.validator.addMethod("entrynum", function(value, element) {
	return this.optional(element) || 
	/^20[0-9][1-9][a-zA-Z][a-zA-Z][0-9]{5}$/.test(value);
}, "Enter correct entry number");

function checkEntryNum(entryNum)
{
	return /^20[0-9][1-9][a-zA-Z][a-zA-Z][0-9]{5}$/.test(entryNum);
}

$('input').change(function() {
	if (checkEntryNum($('#username').val()) &&
		$('#attendance').val().length==6) {
		$('#sbmt').removeClass('disabled');
    } else {
    	$('#sbmt').addClass('disabled');
	}
});

$(document).ready(function() {
	$('#attendanceForm').validate({
        rules: {
            username: {
                minlength: 11,
                maxlength: 11,
                required: true,
                entrynum: true
            },
            attendance: {
            	minlength: 6,
            	maxlength: 6,
            	required: true
            }
        },
        highlight: function(element) {
            $(element).closest('.form-group').addClass('has-error');
        },
        unhighlight: function(element) {
            $(element).closest('.form-group').removeClass('has-error');
        },
        errorElement: 'span',
        errorClass: 'help-block',
        errorPlacement: function(error, element) {
            if(element.parent('.input-group').length) {
                error.insertAfter(element.parent());
            } else {
                error.insertAfter(element);
            }
        }
    });
});