# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class SurreyuniversityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #1.course Name
    course_name=scrapy.Field()

    #2.category Name
    category = scrapy.Field()

    #3.sub Category
    sub_category = scrapy.Field()

    #4.course Website
    course_website = scrapy.Field()

    #5.duration
    duration = scrapy.Field()

    #6.duration term
    duration_term = scrapy.Field()

    #7.study mode
    study_mode = scrapy.Field()

    #8.degree level
    degree_level = scrapy.Field()

    #9.monthly_intake
    monthly_intake = scrapy.Field()

    #10.intake day
    intake_day = scrapy.Field()

    #11.intake month
    intake_month = scrapy.Field()

    #12.apply day
    apply_day = scrapy.Field()

    #13.apply month
    apply_month = scrapy.Field()

    #14.city
    city = scrapy.Field()

    #15 domestic only
    domestic_only = scrapy.Field()

    #16.international fee
    international_fee = scrapy.Field()

    #17.domestic fee
    domestic_fee = scrapy.Field()

    #18.fee term
    fee_term = scrapy.Field()

    #19.fee year
    fee_year = scrapy.Field()

    #20.currency
    currency = scrapy.Field()

    #21.study load
    study_load = scrapy.Field()

    #22.IELTS listening
    IELTS_listening = scrapy.Field()

    #23.IELTS speaking
    IELTS_speaking = scrapy.Field()

    #24.Ielts writing
    IELTS_writing = scrapy.Field()

    #25.IELTS reading
    IELTS_reading = scrapy.Field()

    #26.IELTS overall
    IELTS_overall = scrapy.Field()

    #27.PTE listening
    PTE_listening = scrapy.Field()

    #28.PTE speaking
    PTE_speaking = scrapy.Field()

    #29.PTE writing
    PTE_writing = scrapy.Field()

    #30.PTE reading
    PTE_reading = scrapy.Field()

    #31.PTE overall
    PTE_overall = scrapy.Field()

    #32.TOFEL Listening
    TOFEL_listening = scrapy.Field()

    #33.TOFEL Speaking
    TOFEL_speaking = scrapy.Field()

    #34.TOFEL Writing
    TOFEL_writing = scrapy.Field()

    #35.TOFEL reading
    TOFEL_reading = scrapy.Field()

    #36.TOFEL overall
    TOFEL_overall = scrapy.Field()

    #37.english test
    english_test = scrapy.Field()

    #38.reading
    reading = scrapy.Field()

    #39.listening
    listening = scrapy.Field()

    #40.speaking
    speaking = scrapy.Field()

    #41.writing
    writing = scrapy.Field()

    #42.overall
    overall = scrapy.Field()

    #43.academic level
    academic_level = scrapy.Field()

    #44.academic score
    academic_score = scrapy.Field()

    #45.score type
    score_type = scrapy.Field()

    #46.academic country
    academic_country = scrapy.Field()

    #47.other test
    other_test = scrapy.py()

    #48.score
    score = scrapy.Field()

    #49.other requirements
    other_requirements = scrapy.py()

    #50.course description
    course_description = scrapy.Field()

    #51.course structure
    course_structure = scrapy.Field()

    #52.career
    career = scrapy.Field()

    #53.scholarship
    scholarship = scrapy.Field()


    pass
