from django.core.management.base import BaseCommand, CommandError
from videos.models import Topic


class Command(BaseCommand):
    help = "Creates default topic objects"

    def handle(self, *args, **options):
        Topic.objects.all().delete()
        Topic(
            topic="Positive Role Models: Highlight stories of successful Black individuals who have overcome adversity to achieve their dreams. This could include entrepreneurs, athletes, artists, activists, and more. Showcasing these role models can inspire young Black boys and girls to believe in themselves and their potential.",
            search_prompt="successful black individuals who achieved their dreams",
        ).save()
        Topic(
            topic="Life Skills: Offer practical advice and tips on important life skills such as financial literacy, communication skills, time management, goal setting, and conflict resolution. These skills are essential for success in both personal and professional life.",
            search_prompt="advice on important life skills like financial literacy, communication skills, time management, goal setting, and conflict resolution",
        ).save()
        Topic(
            topic="Cultural Heritage: Explore and celebrate the rich cultural heritage of Black Americans, including their contributions to art, music, literature, science, and history. Teaching young people about their cultural roots can help them develop a strong sense of identity and pride.",
            search_prompt="rich cultural heritage of black americans, contributions to art, music, literature, science, and history",
        ).save()
        Topic(
            topic="Mental Health and Well-being: Provide resources and support for addressing mental health issues such as stress, anxiety, depression, and trauma. Many young Black boys and girls may face unique challenges related to systemic racism and discrimination, so it's important to address these issues in a supportive and understanding way.",
            search_prompt="support for young black individuals for addressing mental health issues such as stress, anxiety, depression, and trauma",
        ).save()
        Topic(
            topic="Education and Career Guidance: Offer guidance on education and career paths, including information about different professions, college and vocational training options, scholarship opportunities, and mentorship programs. Empowering young people with the knowledge and resources they need to pursue their dreams can make a significant difference in their lives.",
            search_prompt="education and career guidance, information about different professions, college and vocational training options, scholarship opportunities, and mentorship programs",
        ).save()
        Topic(
            topic="Community Support: Create a supportive online community where young Black boys and girls can connect with each other, share their experiences, and provide mutual support and encouragement. Building a sense of belonging and camaraderie can help combat feelings of isolation and alienation.",
            search_prompt="young black individuals online community for mutual support and encouragement",
        ).save()
        Topic(
            topic="Fashion and Sneakers: Many young folks, regardless of their background, are into fashion and sneakers. They want to rock the latest trends, whether it's streetwear brands, designer labels, or limited-edition sneakers. They're willing to save up their allowances or even hustle to afford these items because they see them as status symbols and ways to express themselves.",
            search_prompt="young folks fashion and sneakers latest trends streetwear brands designer labels limited-edition sneakers",
        ).save()
        Topic(
            topic="Technology and Gaming: Kids these days are glued to their screens, whether it's smartphones, tablets, gaming consoles, or computers. They're always on the lookout for the latest gadgets, video games, and accessories. Anything that enhances their gaming experience or helps them stay connected with friends online is highly sought after.",
            search_prompt="technology and gaming latest gadgets video games accessories gaming experience stay connected with friends online",
        ).save()
        Topic(
            topic="Music and Entertainment: Music plays a huge role in the lives of many young people, shaping their identities and influencing their tastes. They might be willing to spend money on concert tickets, merchandise from their favorite artists, or subscriptions to streaming services that offer exclusive content.",
            search_prompt="how music influences young black people",
        ).save()
        Topic(
            topic="Sports and Fitness: Whether it's basketball, football, or track and field, sports are a big part of many young African Americans' lives. They might be interested in athletic gear, training equipment, or tickets to sporting events featuring their favorite teams or athletes.",
            search_prompt="how sports and fitness influences young black people",
        ).save()
        Topic(
            topic="Self-Expression and Creativity: Many teenagers are exploring their identities and passions, whether it's through art, photography, writing, or other creative outlets. They might be drawn to products that allow them to express themselves or develop their skills, such as art supplies, cameras, or online courses.",
            search_prompt="self-expression and creativity in young black people",
        ).save()
        Topic(
            topic="Personal Development: Provide resources on self-confidence, self-esteem, and resilience. Many miseducated youth may lack belief in themselves due to societal pressures or inadequate support systems.",
            search_prompt="personal development: self-confidence, self-esteem, and resilience",
        ).save()
        Topic(
            topic="Educational Resources: Offer materials that supplement their schooling, covering topics like mathematics, science, history, and literature. Many schools may not provide comprehensive education, and supplemental resources can fill those gaps.",
            search_prompt="mathematics, science, history, and literature educational resources for black youth",
        ).save()
        Topic(
            topic="Financial Literacy: Teach basic financial management skills such as budgeting, saving, and investing. Many children from low-income families may not have access to this knowledge, which could empower them to make better financial decisions in the future.",
            search_prompt="basic financial management skills: budgeting, saving, and investing for black youth",
        ).save()
        Topic(
            topic="Entrepreneurship: Inspire entrepreneurial thinking and provide guidance on starting small businesses. Encourage creativity and resourcefulness, showing them that they can create their own opportunities even with limited resources.",
            search_prompt="entrepreneurial thinking and starting small businesses for black youth",
        ).save()
        Topic(
            topic="Mental Health Awareness: Address the importance of mental health and provide coping mechanisms for dealing with stress, anxiety, and depression. Many children may face challenges at home or in their communities that affect their mental well-being.",
            search_prompt="mental health awareness for black youth: dealing with stress, anxiety, and depression",
        ).save()
        Topic(
            topic="Positive Role Models: Highlight stories of successful individuals from similar backgrounds who have overcome obstacles to achieve their goals. Representation matters and seeing people who look like them succeed can be incredibly motivating.",
            search_prompt="stories of successful individuals from similar backgrounds who have overcome obstacles to achieve their goals",
        ).save()
        Topic(
            topic="Critical Thinking Skills: Teach them how to analyze information critically, question assumptions, and form their own opinions. In a world full of misinformation, this skill is essential for making informed decisions and navigating complex issues.",
            search_prompt="how to analyze information critically, question assumptions, and form own opinion",
        ).save()
        Topic(
            topic="Digital Literacy: Provide guidance on using technology responsibly and safely, including tips on privacy, online etiquette, and avoiding online scams. As the internet becomes increasingly integrated into daily life, these skills are crucial for personal and professional success.",
            search_prompt="guide on using technology responsibly and safely: privacy, online etiquette, and avoiding online scams",
        ).save()
        Topic(
            topic="Healthy Relationships: Offer resources on communication skills, conflict resolution, and consent. Many children may not have positive role models for healthy relationships, and providing guidance in this area can help break cycles of abuse and dysfunction.",
            search_prompt="communication skills, conflict resolution, and consent for healthy relationships",
        ).save()
        Topic(
            topic="Cultural Pride and Identity: Celebrate Black culture and history, fostering a sense of pride and belonging. Many miseducated youth may not have access to accurate representations of their cultural heritage, and providing this knowledge can help strengthen their sense of identity.",
            search_prompt="black culture and history: fostering a sense of pride and belonging",
        ).save()
        Topic(
            topic="Black History and Achievement: Providing content that highlights the rich history and contributions of African Americans throughout the years can be both empowering and educational. This can include profiles of influential figures in various fields such as science, art, sports, and activism.",
            search_prompt="contributions of african americans throughout the years: science, art, sports, and activism",
        ).save()
        Topic(
            topic="Self-Esteem and Identity: Addressing issues related to self-esteem, identity, and cultural pride can be crucial for young Black adolescents who may struggle with societal stereotypes and discrimination. Content that celebrates diversity and encourages self-love and confidence can be highly beneficial.",
            search_prompt="addressing issues related to self-esteem, identity, and cultural pride for young black adolescents",
        ).save()
        Topic(
            topic="Financial Literacy: Offering guidance on basic financial concepts such as budgeting, saving, and investing can equip young individuals with essential life skills for economic empowerment. This can include practical tips on managing money effectively and setting financial goals.",
            search_prompt="basic financial concepts: budgeting, saving, and investing for economic empowerment",
        ).save()
        Topic(
            topic="Entrepreneurship and Business Skills: Providing resources and advice on entrepreneurship and business skills can inspire young minds to explore opportunities for success. This can include topics such as starting a business, marketing strategies, and the importance of innovation and perseverance.",
            search_prompt="advise on entrepreneurship and business skills: starting a business, marketing strategies, and the importance of innovation and perseverance",
        ).save()
        Topic(
            topic="Health and Wellness: Addressing health-related issues specific to the African American community, such as disparities in healthcare access and mental health stigma, can raise awareness and promote positive habits for overall well-being.",
            search_prompt="disparities in healthcare access and mental health stigma in the african american community",
        ).save()
        Topic(
            topic="Education and Academic Success: Offering support and resources to help young students navigate the education system, excel academically, and pursue their academic goals can be invaluable. This can include study tips, mentorship programs, and information on scholarships and educational opportunities.",
            search_prompt="how to excel academically and pursue academic goals",
        ).save()
        Topic(
            topic="Social Justice and Activism: Providing information on social justice issues, historical struggles for civil rights, and avenues for activism can empower young individuals to advocate for positive change in their communities.",
            search_prompt="social justice issues, historical struggles for civil rights, and avenues for activism",
        ).save()
        Topic(
            topic="Technology and Digital Skills: Equipping young people with essential digital skills and knowledge about technology trends can prepare them for the increasingly digital world. This can include coding basics, digital literacy, and tips for responsible internet use.",
            search_prompt="coding basics, digital literacy, and tips for responsible internet use",
        ).save()
        Topic(
            topic="Self-Respect and Dignity: Regardless of our circumstances, it's crucial to maintain self-respect and dignity. No matter how tough things may seem, we should always carry ourselves with pride and integrity.",
            search_prompt="how to maintain self-respect and dignity in tough circumstances",
        ).save()
        Topic(
            topic="Importance of Education: While I may not have had the opportunity to receive a formal education, I understand the importance of learning and knowledge. Education opens doors and provides the tools necessary to succeed in life.",
            search_prompt="importance of education and learning for success in life",
        ).save()
        Topic(
            topic="Entrepreneurship and Business Ownership: Despite starting from humble beginnings, I've learned the value of entrepreneurship and owning your own business. It's a path to financial independence and allows you to have more control over your destiny.",
            search_prompt="value of entrepreneurship and business ownership for financial independence",
        ).save()
        Topic(
            topic="Financial Literacy: Understanding how money works and how to manage it effectively is crucial for success. Learning about budgeting, saving, investing, and avoiding debt can set you on the path towards financial stability and wealth accumulation.",
            search_prompt="understanding money management: budgeting, saving, investing, and avoiding debt",
        ).save()
        Topic(
            topic="Community and Support Networks: Building strong relationships within your community and fostering a support network is essential. Surrounding yourself with positive influences and mentors can provide guidance and assistance on your journey.",
            search_prompt="community and support networks for guidance and assistance",
        ).save()
        Topic(
            topic="Resilience and Perseverance: Life will inevitably present challenges and setbacks, but it's important to stay resilient and persevere through adversity. Success often requires hard work, determination, and the ability to bounce back from failures.",
            search_prompt="resilience and perseverance through adversity for success",
        ).save()
        Topic(
            topic="Giving Back: As you achieve success, it's important to give back to your community and uplift others who may be facing similar challenges. Whether through mentorship, philanthropy, or advocacy, making a positive impact on the lives of others is incredibly fulfilling.",
            search_prompt="how to give back to your community and uplift others",
        ).save()
        Topic(
            topic="Financial Literacy: Despite my initial circumstances, I took it upon myself to learn about finances. I understand the importance of budgeting, investing, and managing money wisely. This knowledge has helped me grow my wealth and secure a stable future for my family.",
            search_prompt="importance of budgeting, investing, and managing money wisely for financial stability",
        ).save()
        Topic(
            topic="Networking Skills: Building strong relationships and networks is crucial in the business world. I've learned how to effectively network, cultivate valuable connections, and leverage them to open doors of opportunity.",
            search_prompt="how to effectively network and cultivate valuable connections",
        ).save()
        Topic(
            topic="Emotional Intelligence: Success isn't just about making money; it's also about understanding people and their motivations. Developing emotional intelligence has allowed me to navigate complex situations, build trust, and inspire others to work towards common goals.",
            search_prompt="how to develop emotional intelligence to navigate complex situations",
        ).save()
        Topic(
            topic="Strategic Thinking: In business, it's essential to think long-term and strategically. I've honed my ability to analyze market trends, anticipate challenges, and make calculated decisions that position me for success.",
            search_prompt="how to think long-term and strategically in business",
        ).save()
        Topic(
            topic="Adaptability: The world is constantly changing, and so is the business landscape. I've learned to embrace change, adapt to new technologies and trends, and stay ahead of the curve.",
            search_prompt="how to embrace change and adapt to new technologies and trends",
        ).save()
        Topic(
            topic="Ethical Leadership: True success is about more than just making money; it's about making a positive impact on the world. I lead by example, prioritizing integrity, honesty, and social responsibility in all my business dealings.",
            search_prompt="how to lead with integrity, honesty, and social responsibility",
        ).save()
        Topic(
            topic="Continuous Learning: Despite my achievements, I understand that there's always room for growth. I remain humble and committed to learning, whether it's through formal education, mentorship, or self-directed study.",
            search_prompt="how to remain humble and committed to continuous learning",
        ).save()

        self.stdout.write(
            self.style.SUCCESS('Successfully created "%s" topics' % Topic.objects.count())
        )
