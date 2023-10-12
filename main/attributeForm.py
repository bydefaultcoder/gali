from django.forms import modelformset_factory
from django.shortcuts import redirect, render

from .ProductAttributeForm import ProductAttributeForm
from .ProductForm import ProductForm
from .models import ProductAttribute as Attribute
ProductAttributeFormSet = modelformset_factory(Attribute, form=ProductAttributeForm, extra=0)

def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, prefix='product')
        attribute_formset = ProductAttributeFormSet(request.POST, prefix='attributes')

        if product_form.is_valid() and attribute_formset.is_valid():
            # Save the product
            product = product_form.save()

            # Add selected attributes to the product
            for attribute in attribute_formset.cleaned_data:
                if attribute.get('attributes'):
                    product.attributes.add(*attribute['attributes'])

            return redirect('product_list')  # Redirect to the product list page or a success page

    else:
        product_form = ProductForm(prefix='product')
        attribute_formset = ProductAttributeFormSet(queryset=Attribute.objects.none(), prefix='attributes')

    return render(request, 'add_product.html', {
        'product_form': product_form,
        'attribute_formset': attribute_formset,
    })
