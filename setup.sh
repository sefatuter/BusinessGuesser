mkdir -p %SefaPc%/.streamlit

echo "[server]
headless = true
port = $PORT
enableCORS = false
" > %SefaPc%/.streamlit/config.toml