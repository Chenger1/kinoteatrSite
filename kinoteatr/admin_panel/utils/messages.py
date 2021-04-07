from django.contrib import messages


def beautify_inline_error_messages(errors, request):
    for error in errors:
        for key, item in error.as_data().items():
            for elem in item:
                messages.error(request, f'{key}-{elem.message}')


def beautify_error_messages(errors):
    result = []
    for error, text in errors.items():
        result.append(f'{error} - {text[0]}')
    return result
