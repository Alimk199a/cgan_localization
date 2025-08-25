# CGAN Localization (Baseline + Improved)

این پروژه یک پیاده‌سازی ساده از CGAN برای داده‌سازی (data augmentation) در مکان‌یابی است.  
دو حالت دارد:
- baseline: مدل بدون بهبود
- improved: مدل بهبودیافته با *one-sided label smoothing*

## 📂 ساختار پروژه
- requirements.txt → لیست وابستگی‌ها
- run_experiment.py → کد اصلی
- پوشه data/ → شامل دیتاست مصنوعی (train/test CSV)
- پوشه results/ → شامل نمودارها و لاگ‌های نتایج

## ▶️ نحوه اجرا
`powershell
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt

# اجرای نسخه پایه
python run_experiment.py --mode baseline --regen-data

# اجرای نسخه بهبود یافته
python run_experiment.py --mode improved
