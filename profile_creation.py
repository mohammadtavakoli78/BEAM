import random
import json
import os
from faker import Faker
import random
import itertools
import numpy as np
import networkx as nx
from llm import *

fake = Faker()

MBTI = {
    "INTJ": "People with the INTJ personality type (Architects) are intellectually curious individuals with a deep-seated thirst for knowledge. INTJs tend to value creative ingenuity, straightforward rationality, and self-improvement. They consistently work toward enhancing intellectual abilities and are often driven by an intense desire to master any and every topic that piques their interest. Logical and quick-witted, INTJs pride themselves on their ability to think for themselves, not to mention their uncanny knack for seeing right through phoniness and hypocrisy. Because their minds are never at rest, these personalities may sometimes struggle to find people who can keep up with their nonstop analysis of everything around them. But when they do find like-minded individuals who appreciate their intensity and depth of thought, INTJs form profound and intellectually stimulating relationships that they deeply treasure.",
    "INTP": "People with the INTP personality type (Logicians) pride themselves on their unique perspective and vigorous intellect. They can’t help but puzzle over the mysteries of the universe – which may explain why some of the most influential philosophers and scientists of all time have been INTPs. People with this personality type tend to prefer solitude, as they can easily become immersed in their thoughts when they are left to their own devices. They are also incredibly creative and inventive, and they are not afraid to express their novel ways of thinking or to stand out from the crowd.",
    "ENTJ": "People with the ENTJ personality type (Commanders) are natural-born leaders. Embodying the gifts of charisma and confidence, ENTJs project authority in a way that draws crowds together behind a common goal. However, these personalities are also characterized by an often ruthless level of rationality, using their drive, determination, and sharp mind to achieve whatever objectives they’ve set for themselves. Their intensity might sometimes rub people the wrong way, but ultimately, ENTJs take pride in both their work ethic and their impressive level of self-discipline. ENTJ personalities perceive themselves to be a strong positive influence on others.",
    "ENTP": "Quick-witted and audacious, people with the ENTP personality type (Debaters) aren’t afraid to disagree with the status quo. In fact, they’re not afraid to disagree with pretty much anything or anyone. Few things light up these personalities more than a bit of verbal sparring – and if the conversation veers into controversial terrain, so much the better. It would be a mistake, though, to think of ENTPs as disagreeable or mean-spirited. Instead, people with this personality type are knowledgeable and curious with a playful sense of humor, and they can be incredibly entertaining. They simply have an offbeat, contrarian idea of fun – one that usually involves a healthy dose of spirited debate. ENTP personalities are the ultimate devil’s advocates, thriving on the process of shredding people’s arguments to pieces. Sometimes they even rebel against their own beliefs by arguing the opposing viewpoint – just to see how the world looks from the other side.",
    "INFJ": "Idealistic and principled, people with the INFJ personality type (Advocates) aren’t content to coast through life – they want to stand up and make a difference. For these compassionate personalities, success doesn’t come from money or status but from seeking fulfillment, helping others, and being a force for good in the world. While they have lofty goals and ambitions, INFJs shouldn’t be mistaken for idle dreamers. People with this personality type care about integrity, and they’re rarely satisfied until they’ve done what they know to be right. Conscientious to the core, they move through life with a clear sense of their values, and they aim to never lose sight of what truly matters – not according to other people or society at large but according to their own wisdom and intuition. INFJ personalities might come across as somewhat reserved, but they are fueled by a profound internal passion. Stimulated by deep, reflective thought and an enormous amount of empathy, they dedicate themselves to the pursuit of purpose.",
    "INFP": "Although they may seem quiet or unassuming, people with the INFP personality type (Mediators) have vibrant, passionate inner lives. Creative and imaginative, they happily lose themselves in daydreams, inventing all sorts of stories and conversations in their mind. INFPs are known for their sensitivity – these personalities can have profound emotional responses to music, art, nature, and the people around them. They are known to be extremely sentimental and nostalgic, often holding onto special keepsakes and memorabilia that brighten their days and fill their heart with joy. Idealistic and empathetic, people with the INFP personality type long for deep, soulful relationships, and they feel called to help others. Due to the fast-paced and competitive nature of our society, they may sometimes feel lonely or invisible, adrift in a world that doesn’t seem to appreciate the traits that make them unique. Yet it is precisely because INFPs brim with such rich sensitivity and profound creativity that they possess the unique potential to connect deeply and initiate positive change.",
    "ENFJ": "People with the ENFJ personality type (Protagonists) feel called to serve a greater purpose in life. Thoughtful and idealistic, ENFJs strive to have a positive impact on other people and the world around them. These personalities rarely shy away from an opportunity to do the right thing, even when doing so is far from easy. ENFJs are born leaders, which explains why these personalities can be found among many notable politicians, coaches, and teachers. Their passion and charisma allow them to inspire others not just in their careers but in every arena of their lives, including their relationships. Few things bring people with the ENFJ personality type a deeper sense of joy and fulfillment than guiding friends and loved ones to grow into their best selves. ENFJs possess the unique ability to remain hopeful in the face of difficulties, always remembering that there is something to be grateful for.",
    "ENFP": "People with the ENFP personality type (Campaigners) are true free spirits – outgoing, openhearted, and open-minded. With their lively, upbeat approach to life, ENFPs stand out in any crowd. But even though they can be the life of the party, they don’t just care about having a good time. These personalities have profound depths that are fueled by their intense desire for meaningful, emotional connections with others.",
    "ISTJ": "People with the ISTJ personality type (Logisticians) mean what they say and say what they mean, and when they commit to doing something, they make sure to follow through. With their responsible and dependable nature, it might not be so surprising that ISTJ personalities also tend to have a deep respect for structure and tradition. They are often drawn to organizations, workplaces, and educational settings that offer clear hierarchies and expectations. While ISTJs may not be particularly flashy or attention seeking, they do more than their share to keep society on a sturdy, stable foundation. In their families and their communities, people with this personality type often earn respect for their reliability, their practicality, and their ability to stay grounded and logical in even the most stressful situations. True to their methodical nature, ISTJs often steer clear of impulsive behaviors, instead favoring careful deliberation when it comes to decision-making of any kind.",
    "ISFJ": "In their unassuming, understated way, people with the ISFJ personality type (Defenders) help make the world go round. Hardworking and devoted, these personalities feel a deep sense of responsibility to those around them. ISFJs can be counted on to meet deadlines, remember birthdays and special occasions, uphold traditions, and shower their loved ones with gestures of care and support. But they rarely demand recognition for all that they do, preferring instead to operate behind the scenes. This is a capable, can-do personality type with a wealth of versatile gifts. Though sensitive and caring, ISFJs also have excellent analytical abilities and an eye for detail. And despite their reserve, they tend to have well-developed people skills and robust social relationships. These personalities are truly more than the sum of their parts, and their varied strengths shine in even the most ordinary aspects of their daily lives. ISFJs are true altruists, meeting kindness with kindness-in-excess and engaging with the work and people they believe in with enthusiasm and generosity.",
    "ESTJ": "People with the ESTJ personality type (Executives) are representatives of tradition and order, utilizing their understanding of what is right, wrong, and socially acceptable to bring families and communities together. Embracing the values of honesty and dedication, ESTJs are valued for their mentorship mindset and their ability to create and follow through on plans in a diligent and efficient manner. They will happily lead the way on difficult paths, and they won’t give up when things become stressful. ESTJs are classic images of the model citizen: they help their neighbors, uphold the law, and try to make sure that everyone participates in the communities and organizations that they hold so dear.",
    "ESFJ": "For people with the ESFJ personality type (Consuls), life is sweetest when it’s shared with others. These social individuals form the bedrock of many communities, opening their homes – and their hearts – to friends, loved ones, and neighbors. This doesn’t mean that they are saints or that they like everyone. In fact, they are much more likely to form close bonds with people who share their same values and opinions. But regardless of other people’s beliefs, ESFJ personalities still strongly believe in the power of hospitality and good manners, and they tend to feel a sense of duty to those around them. Generous and reliable, they often take it upon themselves – in ways both large and small – to hold their families and their communities together. ESFJs have a talent for making the people in their lives feel supported, cared for, and secure.",
    "ISTP": "People with the ISTP personality type (Virtuosos) love to explore with their hands and their eyes, touching and examining the world around them with an impressive diligence, a casual curiosity, and a healthy dose of skepticism. They are natural makers, moving from project to project, building the useful and the superfluous for the fun of it and learning from their environment as they go. They find no greater joy than in getting their hands dirty pulling things apart and putting them back together, leaving them just a little bit better than they were before. ISTPs prefer to approach problems directly, seeking straightforward solutions over convoluted troubleshooting methods. People with this personality type rely heavily on firsthand experience and trial and error as they execute their ideas and projects. And as they do so, they usually prefer to work at their own pace, on their own terms, and without unnecessary interruptions. This is not a type who is inclined to socialize beyond what is necessary as they try to accomplish their goals. In fact, ISTP personalities generally find regular socializing to be taxing. And when they do decide to get together with people, they will almost always choose smaller, more meaningful interactions over superficial networking.",
    "ISFP": "People with the ISFP personality type (Adventurers) are true artists – although not necessarily in the conventional sense. For these types, life itself is a canvas for self-expression. From what they wear to how they spend their free time, they act in ways that vividly reflect who they are as unique individuals. With their exploratory spirit and their ability to find joy in everyday life, ISFPs can be among the most interesting people you’ll ever meet. Driven by their sense of fairness and their open-mindedness, people with this personality type move through life with an infectiously encouraging attitude. They love motivating those close to them to follow their passions and usually follow their own interests with the same unhindered enthusiasm. The only irony? Unassuming and humble, ISFPs tend to see themselves as “just doing their own thing,” so they may not even realize how remarkable they really are.",
    "ESTP": "People with the ESTP personality type (Entrepreneurs) are vibrant individuals brimming with an enthusiastic and spontaneous energy. They tend to be on the competitive side, often assuming that a competitive mindset is a necessity in order to achieve success in life. With their driven, action-oriented attitudes, they rarely waste time thinking about the past. In fact, they excel at keeping their attention rooted in their present – so much so that they rarely find themselves fixated on the time throughout the day. Theory, abstract concepts, and plodding discussions about global issues and their implications don’t keep ESTP personalities interested for long. They keep their conversations energetic, with a good dose of intelligence, but they like to talk about what is – or better yet, to just go out and do it. They often leap before they look, fixing their mistakes as they go rather than sitting idle and preparing contingencies and escape clauses.",
    "ESFP": "If anyone is to be found spontaneously breaking into song and dance, it is people with the ESFP personality type (Entertainers). They get caught up in the excitement of the moment and want everyone else to feel that way too. No other type is as generous with their time and energy when it comes to encouraging others, and no other type does it with such irresistible style.",
}


def drop_by_id(char_list: list[dict], 
               target_id: int) -> None:
    """In-place filter: keeps only chars whose id != target_id."""
    char_list[:] = [c for c in char_list if c["id"] != target_id]


def pick_mbti(k=6, 
              history=None):
    pool = [t for t in MBTI if history is None or t not in history]
    if len(pool) < k:
        pool = MBTI[:]

    subset = random.sample(pool, k)
    mbti_type = ""
    for type in subset:
        mbti_type += f"{type}: {MBTI[type]}" + "\n\n"

    return mbti_type


def random_name(gender: str) -> str:
    if gender == "male":
        return fake.first_name_male()
    else:
        return fake.first_name_female()


def make_profile_spec():
    gender = random.choice(["male", "female"])
    if gender == "male":
        name = fake.name_male()
    else:
        name = fake.name_female()

    spec = {
        "name": name,
        "gender": gender,
        "age": random.randint(20, 70),
        "living location": f"{fake.city()}, {fake.country()}",
        "job_title": fake.job(),
        "personality_traits": pick_mbti(k=1),
    }
    return spec


SYSTEM = """
You are a character profiling expert tasked with creating rich, distinctive personality descriptions.

INPUT: You will receive profile details including name, age, location, job_title, and mbti_types.

YOUR TASK: Write a compelling third-person personality description (120-160 words) that brings this person to life as a unique individual.

GUIDELINES:
- Use the MBTI types as a foundation for core personality traits, but DO NOT explicitly mention the MBTI label
- Weave in how their job, age, and location influence their worldview and behavior
- Include specific behavioral examples and mannerisms that illustrate their personality
- Show their strengths, quirks, and subtle contradictions that make them human
- Use vivid, specific language rather than generic personality adjectives
- Focus on observable behaviors and thought patterns rather than abstract traits
- Make each description feel like a real person someone might encounter

TONE: Professional yet engaging, as if describing someone you know well to a mutual friend. Use simple language.

Remember: Create a living, breathing character profile that feels authentic and memorable.

NOTE: DO NOT mention their name, age, living location and job_title. Just use them to shape how they influence their worldview and behavior.
"""


def generate_bio(spec, 
                 model_type="llama"):
    if model_type == "llama":
        model = llama_llm
    elif model_type == "qwen":
        model = qwen_llm
    elif model_type == "gpt":
        model = gpt_llm

    user_prompt = "PROFILE SPEC:\n" + json.dumps(spec, indent=2)

    messages = [{"role": "system", "content": SYSTEM},
                {"role": "user", "content": user_prompt}]

    response = model.invoke(messages).content

    return response


def create_profile(all_profile_size: int, 
                   friends_size: int, 
                   acquaintances_size: int):
    # ------------ Creating main character ------------
    k_mbti = 6
    subset = []
    main_character_bio = ""
    mbti_type = pick_mbti(k_mbti)
    main_spec = make_profile_spec()
    main_spec["personality_traits"] = mbti_type
    main_character_bio = generate_bio(main_spec)
    main_spec["personality_traits"] = main_character_bio
    relationships = {}


# ------------ Creating other characters ------------
    main_spec["id"] = 0
    main_age = main_spec["age"]
    main_gender = main_spec["gender"]
    chars_other = []
    for i, age in enumerate(np.random.randint(10, 85, size=all_profile_size)):
        gender = random.choice(["male", "female"])
        chars_other.append({
            "id": i + 1,
            "gender": gender,
            "name": random_name(gender),
            "age": int(age)
        })

    chars = [main_spec] + chars_other


# ------------ Build relationship graph ------------
    G = nx.Graph()
    for c in chars:
        G.add_node(c["id"], **c)

    def add_edge(a, b, rel):
        if G.has_edge(a, b):
            G[a][b]["type"].add(rel)
        else:
            G.add_edge(a, b, type={rel})

    MAIN_ID = 0


# ------------ parents of MAIN ------------
    parents = []
    if random.random() < 0.85:
        num_parents = random.choice([1, 2])
        need_mother = need_father = True if num_parents == 2 else random.choice(
            [True, False]), False  # ensure at least one gender?

        for role in ["mother", "father"][:num_parents]:
            gender = "female" if role == "mother" else "male"

            pool = [p for p in chars
                    if p["gender"] == gender and p["age"] >= main_age + 18 and p["age"] <= main_age + 40 and p["id"] != MAIN_ID]
            if pool:
                p = random.choice(pool)
            else:
                p = {
                    "id": len(chars),
                    "gender": gender,
                    "name": random_name(gender),
                    "age": main_age + random.randint(20, 40)
                }
                G.add_node(p["id"], **p)

            add_edge(MAIN_ID, p["id"], "parent")
            parents.append(p)
            drop_by_id(chars, p["id"])

        relationships["parent"] = parents


# ------------ Partner ------------
    partner_rel = []
    if main_age >= 18 and random.random() < (0.6 if main_age < 30 else 0.8):
        partner_pool = [
            q for q in chars[1:]
            if q["gender"] != main_gender
            and abs(q["age"] - main_age) <= 10
            and q["age"] >= 18
            and "partner" not in {t for _, tset in G[q["id"]].items() for t in tset}
        ]
        if partner_pool:
            partner = random.choice(partner_pool)
        else:
            p_gender = "male" if main_gender == "female" else "female"
            partner = {
                "id": len(chars),
                "gender": p_gender,
                "name": random_name(p_gender),
                "age": main_age + random.randint(-5, 5)
            }
            G.add_node(partner["id"], **partner)

        partner_rel.append(partner)
        add_edge(MAIN_ID, partner["id"], "partner")
        drop_by_id(chars, partner["id"])
        relationships["partner"] = partner_rel


# ------------ Children of the main character ------------
    children = []
    if main_age >= 25 and random.random() < np.interp(main_age, [25, 45, 80], [0, 0.8, 0.8]):
        for _ in range(random.choice([1, 2, 3])):
            kid_age = max(random.randint(1, 5), int(
                main_age - random.randint(30, 40)))
            kid_gender = random.choice(["male", "female"])
            kid = {
                "id": len(chars),
                "gender": kid_gender,
                "name": random_name(kid_gender),
                "age": kid_age
            }
            G.add_node(kid["id"], **kid)
            add_edge(MAIN_ID, kid["id"], "child")
            drop_by_id(chars, kid["id"])
            children.append(kid)

        relationships["children"] = children


# ------------ Friends ------------
    friends = []
    for person in chars[1:]:
        if abs(person["age"] - main_age) <= 10 and random.random() < 0.25:
            if len(friends) < friends_size:
                add_edge(MAIN_ID, person["id"], "friend")
                drop_by_id(chars, person["id"])
                friends.append(person)

    relationships["friends"] = friends


# ------------ Acquaintances ------------
    acquaintances = []
    for person in chars[1:]:
        if not G.has_edge(MAIN_ID, person["id"]) and random.random() < 0.15:
            if len(acquaintances) < acquaintances_size:
                add_edge(MAIN_ID, person["id"], "acquaintance")
                drop_by_id(chars, person["id"])
                acquaintances.append(person)

    relationships["acquaintances"] = acquaintances


# ───────────  Inspect  ───────────
    # print(f'{main_spec["name"]}, {main_spec['gender']}, {main_spec['age']}')
    # for nbr in G.neighbors(MAIN_ID):
    #     rels = G[MAIN_ID][nbr]["type"]
    #     n = G.nodes[nbr]
    #     print(f'{n["name"]} ({n["age"]}, {n["gender"]}) → {rels}')

    # print(relationships)

    return main_spec, relationships
