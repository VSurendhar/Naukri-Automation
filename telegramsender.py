import os
import urllib.parse
import urllib.request

from dotenv import load_dotenv


def send_telegram_logs():

    load_dotenv()
    
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    
    if not telegram_token or not chat_id:
        # Silently fail or log locally if credentials are missing
        return

    log_file_path = "/Users/novosoftsolutions/CodingProjects/PythonProjects/NaukriAutomation/cron.log"
    if not os.path.exists(log_file_path):
        return

    try:
        with open(log_file_path, "r") as f:
            log_content = f.read().strip()
        
        if log_content:
            url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
            data = urllib.parse.urlencode({
                "chat_id": chat_id,
                "text": f"Naukri Automation Logs:\n\n{log_content}"
            }).encode("utf-8")
            
            request = urllib.request.Request(url, data=data)
            with urllib.request.urlopen(request) as response:
                pass

        # Clear the log file regardless of whether logs were sent
        with open(log_file_path, "w") as f:
            f.truncate(0)
            
    except Exception:
        # Standalone script, avoid cluttering stdout if possible
        pass

if __name__ == "__main__":
    send_telegram_logs()
