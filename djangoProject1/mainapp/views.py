from django.shortcuts import render
from requests import post
from .forms import DesignForm, ContactForm
from mainapp import image2dots, image2lines
import os
from django.conf import settings
import requests

def design_create_view(request):
    flag = False
    curve = False
    filenameResult = ''
    form = DesignForm()
    contact_form = ContactForm()


    if request.method == 'POST':
        form = DesignForm(request.POST, request.FILES)
        if form.is_valid():
            data_instance = form.save(commit=False)
            data_dict = form.cleaned_data
            print(data_dict)
            filename = data_instance.image.name
            filename = filename.replace(' ', '_').replace(':', '')
            data_instance.image.name = filename
            data_instance.save()
            data_instance.delete()

            if data_dict['style'] == 'id_dots':
                filenameResult = image2dots.image2dots(filename,
                                      data_dict['width'],
                                      data_dict['length'],
                                      hex_to_rgb(data_dict['bg_color']),
                                      hex_to_rgb(data_dict['main_color']))
                # filenameResult = image2dots.getOutputPath_dots(filename)
                flag = True
            elif data_dict['style'] == 'id_lines':
                image2lines.image2lines(filename,
                                        data_dict['width'],
                                        data_dict['length'],
                                        hex_to_rgb(data_dict['bg_color']),
                                        hex_to_rgb(data_dict['main_color']))
                filenameResult = image2lines.getOutputPath_lines(filename)
                flag = True
            elif data_dict['style'] == 'id_curves':
                filenameResult = '/static/images/curveImg.png'
                curve = True
                flag = True

            combined_data = {
                'width': data_dict['width'],
                'length': data_dict['length'],
                'bg_color': data_dict['bg_color'],
                'main_color': data_dict['main_color'],
                'style': data_dict['style'],
                'image': filenameResult,
                'imageOrig': 'media/images/' + filename
            }
            request.session['design_data'] = combined_data


        elif 'name' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_data = contact_form.cleaned_data
                print(contact_data)
                design_data = request.session.get('design_data', {})
                combined_data = {**contact_data, **design_data}
                print(combined_data)
                message = (f"Заказ новой панели:\n\n\nЗаказчик: {combined_data['name']}\n"
                           f"Связь с заказчиком: {combined_data['phone']},\n{combined_data['email']}\n\n\nШирина: {combined_data['width']}мм\n"
                           f"Высота: {combined_data['length']}мм\nЦвет фона: {combined_data['bg_color']}\n"
                           f"Цвет узора: {combined_data['main_color']}\nУзор: {'Точки' if combined_data['style'] == 'id_dots' else 'Линии'}")
                image_paths = [
                    combined_data['image'],
                    combined_data['imageOrig']
                ]
                send_telegram_photos(image_paths, message)
                delete_file(combined_data['imageOrig'])
                delete_file(combined_data['image'])

    return render(request, 'page32586937.html',
                  {'form': form, 'contact_form': contact_form, 'flag': flag, 'curve': curve,
                   'pathOutput': filenameResult})


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return (r, g, b)


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def send_telegram_photos(photo_paths: list, caption: str):
    bot_token = ''
    chat_id = ''
    url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
    for photo_path in photo_paths:
        with open(photo_path, 'rb') as photo_file:
            payload = {'chat_id': chat_id, 'caption': caption}
            files = {'photo': photo_file}
            post(url, data=payload, files=files)

