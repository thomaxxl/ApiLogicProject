```
git clone https://github.com/thomaxxl/ApiLogicProject 
cd ApiLogicProject
mkdir venv
virtualenv venv
source venv/bin/activate
gunicorn -w 4 app:application -b 0.0.0.0:5656  --threads 5 --error-logfile - --access-logfile - --reload

GitHub - thomaxxl/ApiLogicProject
https://github.com
```
