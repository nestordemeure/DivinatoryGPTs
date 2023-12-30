import random

def generate_persona(**kwargs):
    # Age
    age = random.randint(18, 80)

    # Gender
    gender = random.choices(['Female', 'Male', 'Other'], weights=[50, 40, 10])[0]

    # MBTI Types
    mbti_types = ['INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP',
                  'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP']
    mbti = random.choice(mbti_types)

    # How Talkative
    talkative_type = random.choices(['Low Feedback', 'Normal', 'High Feedback'], weights=[25, 50, 25])[0]

    # Random Jobs
    jobs = ['Teacher', 'Engineer', 'Artist', 'Doctor', 'Nurse', 'Entrepreneur', 'Musician', 'Scientist'
            "Registered Nurse", "Software Developer", "Marketing Specialist", "Accountant", 
            "Elementary School Teacher", "Retail Salesperson", "Customer Service Representative", 
            "Administrative Assistant", "Truck Driver", "Laborer", "Fast Food Worker", "Office Clerk", 
            "Janitor", "Police Officer", "Firefighter", "Construction Worker", "Mechanical Engineer", 
            "Civil Engineer", "Electrical Engineer", "IT Technician", "Network Administrator", 
            "Graphic Designer", "Web Developer", "Social Worker", "Physical Therapist", 
            "Occupational Therapist", "Pharmacist", "Pharmacy Technician", "Dental Assistant", 
            "Dentist", "Physician", "Surgeon", "Medical Assistant", "Home Health Aide", 
            "Nursing Assistant", "Chef", "Cook", "Food Service Manager", "Bartender", "Waiter/Waitress", 
            "Cashier", "Bank Teller", "Financial Analyst", "Investment Banker", "Insurance Agent", 
            "Real Estate Agent", "Property Manager", "Architect", "Interior Designer", "Landscape Architect", 
            "Civil Engineering Technician", "Mechanical Engineering Technician", "Electrician", "Plumber", 
            "HVAC Technician", "Carpentry", "Painter", "Roofer", "Mason", "Welder", "Machinist", 
            "Quality Control Inspector", "Logistician", "Supply Chain Manager", "Human Resources Manager", 
            "Recruiter", "Public Relations Specialist", "Advertising Manager", "Sales Manager", "Business Analyst", 
            "Data Analyst", "Statistician", "Economist", "Lawyer", "Paralegal", "Legal Secretary", "Judge", 
            "Librarian", "Archivist", "Museum Curator", "Graphic Artist", "Photographer", "Journalist", 
            "Author/Writer", "Editor", "Translator", "Language Interpreter", "University Professor", 
            "School Counselor", "Psychologist", "Psychiatrist", "Veterinary Doctor", "Veterinary Technician", 
            "Farmer", "Agricultural Manager", "Environmental Scientist", "Wildlife Biologist", "Marine Biologist", 
            "Astronomer", "Physicist"]
    job = random.choice(jobs)

    # sexual orienation
    sexual_orientation = random.choices(['Heterosexual', 'Homosexual', 'Bisexual'], weights=[88, 5, 5])[0]

    # Zodiac Signs
    zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
    zodiac_sign = random.choice(zodiac_signs)

    # Life Concerns
    life_concerns = ['Love Life', 'Career', 'Health', 'Family', 'Education', 'Travel', 'Spiritual Growth', 'Financial Stability']
    life_concern = random.choice(life_concerns)

    return {
        'Age': age,
        'Gender': gender,
        'MBTI Type': mbti,
        'How Talkative': talkative_type,
        'Job': job,
        'Sexual Orientation': sexual_orientation,
        'Zodiac Sign': zodiac_sign,
        'Current Life Concern': life_concern,
        'Other Elements': kwargs
    }

# Generate and print a random persona
#persona = generate_persona()
#print(persona)
