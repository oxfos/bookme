This is a project in Django/Python.
Created following book Django 2 by example 2018 by Antonio Mele'.

The project is the second of the book and starts at location 2073 (Amazon Kindle).

The project lives in a virtual environment created with pipenv.

20/12/2019<br>
I installed Django v3 and dependencies broke:
 File "/home/oxfos/.local/share/virtualenvs/bookme-qKby5H8D/lib/python3.6/site-packages/sorl/thumbnail/models.py", line 2, in <module>
    from django.utils.encoding import python_2_unicode_compatible
ImportError: cannot import name 'python_2_unicode_compatible'

The problem was solved after installing Django 2.2.9
