import requests
from passwords import return_credentials
from datetime import datetime
import os

my_ip = requests.get('https://myip.dnsomatic.com/')
my_ip = str(my_ip.text)

def update_ip():
    credentials = return_credentials()
    for domain in credentials:
        url = f'https://{domain["username"]}:{domain["password"]}@domains.google.com/nic/update?hostname={domain["hostname"]}&myip={my_ip}'
        response = requests.post(url)
        print(response.text)
        if os.path.exists('/home/deploy/Projects/ip_update_v2/'):
            with open(os.path.join(os.getcwd(), '/home/deploy/Projects/ip_update_v2/ip_log.txt'), 'a', encoding='utf-8') as file:
                file.write(f'{datetime.now()}       {domain["hostname"]}          {response.text} \n')


if __name__ == "__main__":
    update_ip()