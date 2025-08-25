@echo off
echo ==== ایجاد محیط مجازی ====
python -m venv .venv
call .venv\Scripts\activate

echo ==== نصب کتابخانه ها ====
pip install -r requirements.txt

echo ==== تولید دیتاست ====
python run_experiment.py --mode baseline --regen-data

echo ==== اجرای مدل baseline ====
python run_experiment.py --mode baseline

echo ==== اجرای مدل improved ====
python run_experiment.py --mode improved

echo ==== همه کارها تمام شد ✅ ====
pause
