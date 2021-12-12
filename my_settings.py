DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'westarbucks',
        'USER': 'root',
        'PASSWORD': '13245095',
        'HOST': '127.0.0.1',
        'PORT': '3306',
				'OPTIONS': {'charset': 'utf8mb4'}
    }
}

SECRET_KEY = 'django-insecure-2)ylahy^)tus)jw4e!7vjn&sff5%@#+2l+co!%*juhis^@0)mr'
#settings.py에 있는 secret_key 를 사용합니다.