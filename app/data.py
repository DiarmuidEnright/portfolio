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
        "description": (
            "Engineered tightly coupled integrations between the CloudWatch Agent and "
            "hoststore systems, improving telemetry ingestion pipelines to process 5M+ "
            "daily system-level metrics and logs. Introduced and streamlined "
            "multi-platform installation procedures utilizing AWS Systems Manager and "
            "custom scripting to automate agent deployment across 500+ diverse hoststore "
            "compute environments. Architected advanced monitoring profiles within the "
            "agent to collect and aggregate critical host performance data, maximizing "
            "observability while maintaining a minimal CPU and memory footprint. Designed "
            "and executed robust end-to-end benchmarking configurations to stress-test "
            "agent-hoststore interaction, identifying and resolving resource bottlenecks "
            "under high-concurrency traffic simulation."
        ),
    },
    {
        "role": "Research Engineer, ADA Lab",
        "company": "Huawei Research",
        "period": "September 2025 - January 2026",
        "description": (
            "Facilitated Huawei's Advanced Language Engineering lab's joint research with "
            "Peking University to advance Rust for memory-safe, highly performant and "
            "concrete systems, impacting 3 major LLM integration tools. Evaluated advanced "
            "Rust features for internal adoption, raising concurrency, I/O, and build-time "
            "ergonomics for 10+ core systems. Collaborated with the Rust Foundation "
            "community across 15+ PRs and issues; work focused on optimizing the Rust "
            "language and toolchain for trusted, production systems. Produced 5+ prototypes "
            "and internal benchmarks that informed ADA Lab's Rust adoption roadmap and "
            "trustworthy programming practices."
        ),
    },
    {
        "role": "AI Research Engineer",
        "company": "Huawei Research",
        "period": "June 2025 - September 2025",
        "description": (
            "Authored performant Rust-based tooling supporting 20+ ML and deep learning "
            "workflows, enhancing concurrency and memory safety. Architected scalable ETL "
            "pipelines using Polars, Apache Arrow, and Parquet, processing 10M+ records "
            "daily. Implemented Rust-Python bindings via PyO3 and maturin, decreasing "
            "runtime for batch jobs by 40%."
        ),
    },
]

# TODO: STILL EMPTY — fill in your real education (school, course, dates).
EDUCATION = [
    {
        "qualification": "TODO: Degree / course (e.g. BSc Data Science)",
        "institution": "TODO: University in Cork (e.g. University College Cork)",
        "period": "TODO: e.g. 2022 – 2026",
        "description": "TODO: focus areas, achievements, etc.",
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
