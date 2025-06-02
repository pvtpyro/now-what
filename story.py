
story = {
    "start": {
        "text": "You graduated High School! Now what?",
        "choices": [
            {"text": "Go straight to college. You already know what you want to study, and you're passionate about it.", "next": "college"},
            {"text": "Join the military.", "next": "military"},
            {"text": "Enter the workforce. You can always go to college later.", "next": "workforce"}
        ]
    },


    # military path
    "military": {
        "text": "Select a branch of the military:",
        "choices": [
            {"text": "Join the Army.", "next": "military_goals"},
            {"text": "Join the Navy.", "next": "military_goals"},
            {"text": "Join the Air Force if you don't mind being picked on by the other branches.", "next": "military_goals"},
            {"text": "Join the Marines. Be sure to pick your favorite Crayola flavor before you sign up.", "next": "military_goals"},
            {"text": "Join the Space Force.", "next": "military_goals"}
        ]
    },
    "military_goals": {
        "text": "You've reached the end of your first 4 year tour.",
        "choices": [
            {"text": "This is too much. Get out now.", "next": "military_civilian"},
            {"text": "Complete another tour or two, then move back into the civilian world.", "next": "military_civilian"},
            {"text": "Do a full 20 years in the military and retire with a pension.", "next": "military_retirement"}
        ]
    },
    "military_civilian": {
        "text": "You are a civilian now. It's a culture shock for you. You can ease into civilian life, or you can jump right in.",
        "choices": [
            {"text": "Use your G.I. Bill and go to college for free.", "next": "college"},
            {"text": "Use your G.I. Bill and go to trade school.", "next": "tradeschool"},
            {"text": "Get a job.", "next": "workforce_military"},
            {"text": "Take some time off. Get your health in order and maybe do some traveling.", "next": "mental_health"}
        ]
    },
    "military_retirement": {
        "text": "You're 38 years old. You can now retire from the military.",
        "choices": [
            {"text": "Start a van life and travel the country.", "next": "van_life"},
            {"text": "Start a new career in the civilian world and retire from that too.", "next": "workforce_military"}
        ]
    },
    "van_life": {
        "text": "You live in a van and travel the country. You sign up for a gym membership so you can shower and use the bathroom. You love it!",
        "choices": [
            {"text": "You travel for the rest of your life. Maybe earning extra cash sharing your adventures on Tiktok.", "next": "end"}
        ]
    },
    "tradeschool": {
        "text": "You went to trade school. You mastered your craft and you have no debts.", 
        "choices": [
            {"text": "You are debt free. You own your own. And you can choose when to retire. You've won at life.", "next": "end"}
        ]  
    },
    "mental_health": {
        "text": "You took some time off. You got your health in order and did some traveling. Now you're ready to get back to work.",
        "choices": [
            {"text": "Use your G.I. Bill and go to college for free.", "next": "college"},
            {"text": "Use your G.I. Bill and go to trade school.", "next": "tradeschool"},
            {"text": "Get a job.", "next": "workforce_military"},
            {"text": "You feel like life is just too hard. Give up on everyone and everything.", "next": "homeless"}

        ]
    },
    "workforce_military": {
        "text": "You got a job. You have no debts and you have military experience. A lot of companies want to hire you so you chose what made you happiest.",
        "choices": [
            {"text": "Job hop to widen your experiences while adding to a 401k and retire", "next": "retire"},
            {"text": "Stay at a company you love, climb the ladder and retire happy.", "next": "retire"}
        ]
    },



    # straight to workforce path
    "workforce": {
        "text": "You got a job. You've avoided the debt trap. You don't make much money, yet.",
        "choices": [
            {"text": "Job hop to widen your experiences, or until you find something you love, while adding to a 401k and retire", "next": "retire"},
            {"text": "Stay at a company you love, climb the ladder and retire happy.", "next": "retire"},
            {"text": "Job hob until you find something you love. They offer big promotions if you go get a degree", "next": "workforce_college"}
        ]
    },
    "workforce_college": {
        "text": "Good news. You already have a job so you don't need to take out a loan.",
        "choices": [
            {"text": "Go to college part-time while you work.", "next": "college_part_time"},
            {"text": "You don't have any other priorities. You can handle college full time while working.", "next": "college_full_time"}
        ]
    },
    "college_part_time": {
        "text": "You went to college part-time while you worked. It took a long time, but you got your degree.",
        "choices": [
            {"text": "Your company gave you the promotion they promised you. You're able to buy a home and retire.", "next": "retire"}
        ]
    },
    "college_full_time": {
        "text": "You went to college full-time while you worked. You sacrificed ALL of your social life, but you got your degree.",
        "choices": [
            {"text": "Your company gave you the promotion they promised you. You're able to buy a home and retire.", "next": "retire"}
        ]
    },



    # straight to college path
    "college": {
        "text": "X number have years have gone by. You have a degree and a lot of debt. It's time to get to work!",
        "choices": [
            {"text": "Find an internship in your field for low or no pay.", "next": "internship"},
            {"text": "Get any job you can while you hold out for a good job in your field", "next": "job_not_in_field"}
        ]
    },
    "internship": {
        "text": "You got an internship! You worked hard and learned a lot. Now you have a job in your field.",
        "choices": [
            {"text": "The company loves you and wants to keep you permanently. Stay with the company", "next": "promotion"},
            {"text": "You have the experience needed, it's time to move on to another company", "next": "switch_company"}
        ]
    },
    "job_not_in_field": {
        "text": "You got a job, but it's not in your field. 5-10 years have gone by and you're still working at your \"temp\" job.",
        "choices": [
            {"text": "The company loves you and wants to keep you permanently. Stay with the company", "next": "promotion_manager"},
            {"text": "You've had enough. You're not living up to your potential. You want to work in your field, even if that means a temporary pay-cut.", "next": "switch_company_downgrade"},
        ]
    },
    "promotion": {
        "text": "You got a promotion! You have worked your way up. You make great money and can pay off your debts quickly.",
        "choices": [
            {"text": "It's time to retire", "next": "retire"}
        ]
    },
    "promotion_manager": {
        "text": "You've been promoted to manager! You're not in the field you wanted, but you're doing okay. You're are slowly paying off your debts, but it's hard to keep up with the interest.",
        "choices": [
            {"text": "You can keep working here, but you won't be able to pay off your debts for a long time.", "next": "stay_manager"},
            {"text": "You now have manager experience, and a degree. Find a new job in the field you wanted originally", "next": "switch_company_related_field"},
            {"text": "It's time to retire", "next": "retire"}
        ]
    },
    "switch_company": {
        "text": "You're making decent cash now and you're chipping away at your debts.",
        "choices": [
            {"text": "Pay off all your debts, buy a house, then retire", "next": "retire"},
            {"text": "Refuse to pay your debts. Live above your means and enjoy life.", "next": "failure"},
        ]
    },
    "switch_company_related_field": {
        "text": "You got a job in your field and you're starting a lot higher on the ladder than you expected. You love your job and the pay is great.",
        "choices": [
            {"text": "Pay off all your debts, buy a house, then retire", "next": "retire"},
            {"text": "Refuse to pay your debts. Live above your means and enjoy life.", "next": "failure"},
        ]
    },
    "switch_company_downgrade": {
        "text": "You took a pay-cut to work in your field. You love your job, but you're not making enough to pay off your debts. Yet.",
        "choices": [
            {"text": "Stay. Work your way up the ladder. Pay off debts, buy a house, retire", "next": "retire"},
            {"text": "You're frustrated that you're not where you wanted to be. Give up.", "next": "homeless"},
        ]
    },


    # endings
    "retire": {
        "text": "Congratulations! You've lived your best life. Now that you're retired you can do whatever you want.",
        "choices": []
    },
    "failure": {
        "text": "You enjoyed life for a while. Until the IRS came knocking on your door. You ignored them, but they took everything you had. You're older now. You take any job you can get. Since you've hit the bottom you've learned to love and appreciate your job and everything you have.",
        "choices": []
    },
    "homeless": {
        "text": "You gave up. You lost everything. You live on the streets now. Take any job you can get. Since you've hit the bottom you've learned to love and appreciate your job and everything you have.",
        "choices": []
    },
    "end": {
        "text": "The end.",
        "choices": []
    },

}
