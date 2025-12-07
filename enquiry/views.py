from django.shortcuts import render
from django.contrib import messages
from .forms import EnquiryRequestForm


def enquiry_us(request):
    """
    Renders the enquiry request
    """
    if request.method == "POST":
        enquiry_form = EnquiryRequestForm(data=request.POST)
        if enquiry_form.is_valid():
            enquiry_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your Enquiry request received! I endeavour to respond within 2 working days.",
            )

    enquiry_form = EnquiryRequestForm()

    return render(
        request,
        "enquiry/enquiry.html",
        {
            "enquiry_form": enquiry_form,
        },
    )
