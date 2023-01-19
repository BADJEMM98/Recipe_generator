clear
echo "Loading..."
gunicorn --reload  src.app --bind 0.0.0.0:5000 --access-logfile - --reload  # live-reload (development only!)
