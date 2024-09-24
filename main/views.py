from django.shortcuts import render
from .models import Previous_work, profile_pic, CV, contact  # Use Contact instead of contact
from django.contrib import messages

# Home view for form submission
def home(request):
    work = Previous_work.objects.all()  # Load previous work
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        # Validate the form data
        if len(name) > 3 and len(phone) <= 11:
            # Save contact
            new_contact = contact(name=name, phone=phone)
            new_contact.save()
            messages.success(request, 'Form submitted successfully!')
        else:
            messages.error(request, 'Please fill out the form correctly.')

    # Render the template with context
    return render(request, 'index.html', {'works': work})

# About page view to show profile pic and CV
def about(request):
    pic = profile_pic.objects.get(id=1)
    Cv = CV.objects.get(id=1)
    return render(request, 'about.html', {'pic': pic, 'Cv': Cv})
