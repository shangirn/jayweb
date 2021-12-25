from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import NameForm

# Create your views here.
#from .models import Book, Author, BookInstance, Genre

from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")

@csrf_exempt
#@ensure_csrf_cookie
def translate(request):
    """View function for home page of site."""
    article_en = ""
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            article_en = form.cleaned_data[ 'to_translate' ]
            model_inputs = tokenizer(article_en, return_tensors="pt")
            # translate from English to Hindi
            generated_tokens = model.generate(
                **model_inputs,
                forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"]
            )
            translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        else:
            translation = ""
    else:
        translation = ""

    context = {
        'Result': translation,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'translate.html', context=context)