
echo "  BUILD START"

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py collectstatic --noinput --clear
python manage.py migrate
deactivate

echo "  BUILD END"
