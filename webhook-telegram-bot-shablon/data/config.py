from environs import Env

# Env
env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("IP")
NGROK_URL = env.str("NGROK_URL")