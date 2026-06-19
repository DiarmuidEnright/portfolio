ABOUT = {
    "name": "Diarmuid Enright",
    "tagline": "Data Science student & SDE Intern @ AWS",  # change this if you'd prefer something else
    # Drop your photo in app/static/img/ and point to it here.
    # TODO: replace 'logo.jpg' with your own photo file name.
    "photo": "logo.jpg",
    "bio": (
        "My name is Diarmuid and I am a Data Science student studying in Cork, "
        "Ireland. Right now I am working in AWS as part of the CloudWatch metrics "
        "team. In my free time I like to play chess and play the Cello."
    ),
}

EXPERIENCES = [
    {
        "role": "Software Development Intern",
        "company": "Amazon Web Services",
        "period": "February 2026 - Present",
        "description": "Improved telemetry pipelines and automated agent deployment.",
    },
    {
        "role": "Research Engineer, ADA Lab",
        "company": "Huawei Research",
        "period": "September 2025 - January 2026",
        "description": "Optimized Rust toolchains for LLM integrations.",
    },
    {
        "role": "AI Research Engineer",
        "company": "Huawei Research",
        "period": "June 2025 - September 2025",
        "description": "Built Rust-based ML tooling and ETL pipelines.",
    },
]

EDUCATION = [
    {
        "qualification": "BSc Data Science and Artificial Intelligence",
        "institution": "University College Cork",
        "period": "2023 – 2027",  # CONFIRM: I used your example dates — fix if wrong
        "description": "Head SysAdmin or SysAdmin of literally every tech society on campus.",
    },
]

# Each hobby can have an image. Put images in app/static/img/ and reference the
# file name in "image". TODO: replace the logo.jpg images with real photos.
HOBBIES = [
    {
        "name": "Chess",
        "description": (
            "I was super antisocial when I was a kid and just going to weekly chess "
            "helped me meet new people."
        ),
        "image": "logo.jpg",  # TODO: replace with your own image file name
    },
    {
        "name": "Cello",
        "description": (
            "Grew up going to lessons and it just became ingrained in my life. Played "
            "with the national youth orchestra for a few years, but now it's something I "
            "can do on the side to de-stress from college or work."
        ),
        "image": "logo.jpg",  # TODO: replace with your own image file name
    },
]

# Used to drop pins on the map. Find coordinates by right-clicking a spot in
# Google Maps. Add more entries to drop more pins.
LOCATIONS = [
    {"name": "Copenhagen, Denmark", "lat": 55.6761, "lng": 12.5683},
]
