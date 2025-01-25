DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'russian_restaurant',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Authentication Settings
AUTH_USER_MODEL = 'yourapp.User'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# Add traditional Russian menu items and drink items to the database
MenuItem.objects.bulk_create([
    MenuItem(name="Borscht", description="Traditional beet soup served with sour cream.", price=6.99),
    MenuItem(name="Pelmeni", description="Russian dumplings filled with minced meat.", price=9.99),
    MenuItem(name="Beef Stroganoff", description="Tender beef strips in a creamy mushroom sauce.", price=14.99),
    MenuItem(name="Blini", description="Thin Russian pancakes served with jam or sour cream.", price=5.99),
    MenuItem(name="Olivier Salad", description="Classic Russian potato salad with vegetables and mayonnaise.", price=4.99),
    MenuItem(name="Kvass", description="Traditional fermented beverage made from rye bread.", price=2.99),
    # Drinks
    MenuItem(name="Vodka", description="Premium Russian vodka served chilled.", price=8.99),
    MenuItem(name="Mors", description="Refreshing berry drink made from cranberries.", price=3.99),
    MenuItem(name="Russian Tea", description="Traditional black tea served with lemon and sugar.", price=2.99),
    MenuItem(name="Kompot", description="Sweet drink made from boiled fruits.", price=3.49)
])
