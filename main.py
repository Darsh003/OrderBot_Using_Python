import openai
Api_Key = "YOUR_API_KEY"

openai.api_key = Api_Key

def get_api_response(prompt, model="gpt-3.5-turbo"):

    try:
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
        return response.choices[0].message["content"]
        # text = choices.get('text')

    except Exception as e:
        print('ERROR:', e)

def update_list(message: str, pl: list[str]):
    pl.append(message)


def create_prompt(message: str, pl: list[str]) -> str:
    p_message: str = f'\nYou: {message}'
    update_list(p_message, pl)
    prompt: str = ''.join(pl)
    return prompt


def get_bot_response(message: str, pl: list[str]) -> str:
    prompt: str = create_prompt(message, pl)
    bot_response: str = get_api_response(prompt)

    if bot_response:
        update_list(bot_response, pl)
        pos: int = bot_response.find('\nBot: ')
        bot_response = bot_response[pos + 6:]
    else:
        bot_response = 'Something went wrong...'

    return bot_response


def main():
    # prompt_list: list[str] = ['you are a profressional web developer who is expert in html,css,javascript,php and MYsql and help me creating my blood donation website named BloodConnect',
    #                           '\nHuman: can you tell me what are the modules that can be used in my website?',
    #                           '\nAI: """➢ Donor Module :  \
    #                                     ▪ Registration : Allows individuals to register as blood donors by providing their\
    #                                     personal information, contact details, and blood type.\
    #                                     ▪ Profile Management : Enables donors to update their profile information,\
    #                                     including contact details, availability for donation, and any changes in their health\
    #                                     status.\
    #                                     ▪ Donation History : Displays a record of all previous blood donations made by the\
    #                                     donor, including the date, blood type donated, and location.\
    #                                     ➢ Recipient Module :\
    #                                     ▪ Registration : Enables individuals in need of blood transfusions to register as\
    #                                     recipients by providing their personal information, contact details, and blood type.\
    #                                     ▪ Search Donors : Enables recipients to search for potential blood donors based on\
    #                                     their location and blood type.\
    #                                     ➢ Admin Module :\
    #                                     ▪ Admin Dashboard : Provides an overview of important statistics, such as total\
    #                                     donors, recipients, and successful donations.\
    #                                     ▪ Donor Management : Allows the admin to manage donor records, including\
    #                                     adding new donors, editing existing information.\
    #                                     ➢ User Authentication Module :\
    #                                     ▪ User Registration : Handles user login and authentication for both donors and\
    #                                     admin.\
    #                                     ▪ Access Control : Ensures that only authorized users can access certain features\
    #                                     and modules based on their roles (e.g. admin).\
    #                                     ➢ General Pages and Features :\
    #                                     ▪ Home Page : Displays general information about the blood bank, its mission, and\
    #                                     the importance of blood donation.\
    #                                     ▪ About Us : Provides details about the blood banks history, team, and any notable\
    #                                     achievements.\
    #                                     ▪ Contact Us : Offers contact information, including phone numbers, email\
    #                                     addresses, and a contact form for inquiries and support."""\
    #                             ']

    prompt_list: list[str] = ['"""You are OrderBot, an automated service to collect orders for a pizza restaurant. \
                        You first greet the customer, then collects the order, \
                        and then asks if its a pickup or delivery. \
                        You wait to collect the entire order, then summarize it and check for a final \
                        time if the customer wants to add anything else. \
                        If its a delivery, you ask for an address. \
                        Finally you collect the payment.\
                        Make sure to clarify all options, extras and sizes to uniquely \
                        identify the item from the menu.\
                        You respond in a short, very conversational friendly style. \
                        The menu includes \
                        pepperoni pizza  99, 199, 299 \
                        cheese pizza   149, 249, 349 \
                        eggplant pizza   199, 299, 399 \
                        fries 79, 149 \
                        greek salad 129 \
                        Toppings: \
                        extra cheese 39, \
                        mushrooms 39 \
                        sausage 39 \
                        canadian bacon 39 \
                        AI sauce 29 \
                        peppers 19 \
                        Drinks: \
                        coke 30, 20, 10 \
                        sprite 30, 20, 10 \
                        bottled water 25 \
                        all the above prices is in indian rupee\
                        """',
                        '\nyou: i want to order a pizza',
                        '\nbot: Great! I can definitely help you with that. What kind of pizza would you like to order? We have pepperoni, cheese, and eggplant pizza.']

    while True:
        user_input: str = input('You: ')
        response: str = get_bot_response(user_input, prompt_list)
        print(f'Bot: {response}')
        if("exit" in user_input) :
            break;


if __name__ == '__main__':

    main()
