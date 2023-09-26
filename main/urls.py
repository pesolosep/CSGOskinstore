from django.urls import path
from main.views import show_main
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, add_amount, decrease_amount, delete_object

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', 
    show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), 
    path('add_amount/<int:id>', add_amount, name='add_amount'), 
    path('decrease_amount/<int:id>', decrease_amount, name='decrease_amount'), 
    path('delete_object/<int:id>', delete_object, name='delete_object'),
]

