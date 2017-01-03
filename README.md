# climb_tracker
Tool for tracking climbing &amp; bouldering progress.
Built with Django/Django Rest Framework.

TODO:
  Add Auth to allow multiple users.
  Add React/Redux client.

To start
```
git clone git@github.com:AliSkinner/climb_tracker.git
cd climb_tracker
pip install -r requirements.txt
python climb_tracker/manage.py migrate
python climb_tracker/manage.py createsuperuser
python climb_tracker/manage.py runserver
```
open `http://127.0.0.1:8000/` in your browser.
