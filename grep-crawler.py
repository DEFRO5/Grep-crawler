import os
import requests
from datetime import datetime
from typing import Optional

from dotenv import load_dotenv
load_dotenv()

class URLMonitorBot:
    def __init__(self):
        self.telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
        self.monitor_url = os.getenv('MONITOR_URL')
        self.search_word = os.getenv('SEARCH_WORD')
        
        self._validate_env_vars()
    
    def _validate_env_vars(self):
        required_vars = {
            'TELEGRAM_BOT_TOKEN': self.telegram_bot_token,
            'TELEGRAM_CHAT_ID': self.telegram_chat_id,
            'MONITOR_URL': self.monitor_url,
            'SEARCH_WORD': self.search_word
        }
        
        missing_vars = [var for var, value in required_vars.items() if not value]
        
        if missing_vars:
            error_msg = f"Missing required environment variables: {', '.join(missing_vars)}"
            raise ValueError(error_msg)
    
    def send_telegram_message(self, message: str) -> bool:
        try:
            telegram_api_url = f"https://api.telegram.org/bot{self.telegram_bot_token}/sendMessage"
            
            payload = {
                'chat_id': self.telegram_chat_id,
                'text': message,
                'parse_mode': 'HTML'
            }
            
            response = requests.post(telegram_api_url, json=payload, timeout=10)
            response.raise_for_status()
            
            return True
            
        except requests.exceptions.RequestException:
            return False
    
    def fetch_url_content(self) -> Optional[str]:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(self.monitor_url, headers=headers, timeout=10)
            response.raise_for_status()
            
            return response.text
            
        except requests.exceptions.RequestException:
            return None
    
    def check_word_in_content(self, content: str) -> bool:
        return self.search_word.lower() in content.lower()
    
    def run_single_check(self):
        content = self.fetch_url_content()
        if content is None:
            return
        
        word_found = self.check_word_in_content(content)
        
        if word_found:
            message = (
                f"<b>ALERT: \"{self.search_word}\" found in the url</b>\n\n"
                f"{self.monitor_url}\n"
            )
            
            self.send_telegram_message(message)

def main():
    try:
        bot = URLMonitorBot()
        bot.run_single_check()
    except Exception as e:
        print(f"Failed to run bot: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())