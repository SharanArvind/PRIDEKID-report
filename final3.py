def generate_ranking_order(data):
    skills = {
        "Perceive": float(data["perceiveContribution"]),
        "Resolve": float(data["resolveContribution"]),
        "Influence": float(data["influenceContribution"]),
        "Deliver": float(data["deliverContribution"]),
        "Engage": float(data["engageContribution"]),
        "Attention": float(data["attentionContribution"]),
        "Memory": float(data["memoryContribution"]),
        "Critical Thinking": float(data["criticalContribution"]),
        "Creative Thinking": float(data["creativeContribution"]),
        "Mindset": float(data["mindsetContribution"]),
        "Attitude": float(data["attitudeContribution"]),
        "Expression": float(data["expressionContribution"]),
        "Communication": float(data["communicationContribution"]),
        "Collaboration": float(data["collaborationContribution"]),
        "Leadership": float(data["leadershipContribution"]),
        "Awareness": float(data["awarenessContribution"]),
        "Application": float(data["applicationContribution"]),
        "Advantage": float(data["advantageContribution"])
    }

    ranked_skills = sorted(skills.items(), key=lambda x: x[1], reverse=True)
    ranking_order = "\n".join(f"{ranked_skills.index(skill) + 1}. {skill[0]}: {skill[1]}" for skill in ranked_skills)

    return ranking_order


def generate_polarity_order(data):
    skills = {
        "Perceive": float(data["perceiveContribution"]),
        "Resolve": float(data["resolveContribution"]),
        "Influence": float(data["influenceContribution"]),
        "Deliver": float(data["deliverContribution"]),
        "Engage": float(data["engageContribution"]),
        "Attention": float(data["attentionContribution"]),
        "Memory": float(data["memoryContribution"]),
        "Critical Thinking": float(data["criticalContribution"]),
        "Creative Thinking": float(data["creativeContribution"]),
        "Mindset": float(data["mindsetContribution"]),
        "Attitude": float(data["attitudeContribution"]),
        "Expression": float(data["expressionContribution"]),
        "Communication": float(data["communicationContribution"]),
        "Collaboration": float(data["collaborationContribution"]),
        "Leadership": float(data["leadershipContribution"]),
        "Awareness": float(data["awarenessContribution"]),
        "Application": float(data["applicationContribution"]),
        "Advantage": float(data["advantageContribution"])
    }

    sorted_skills = sorted(skills.items(), key=lambda x: x[1], reverse=True)
    polarity_order = "\n".join(f"{skill[0]}: {'Positive' if skill[1] >= 50 else 'Negative'}" for skill in sorted_skills)

    return polarity_order


def generate_areas_for_improvement(data):
    improvement_paragraphs = {
        "Perceive": f"To enhance perception skills, {data['student_name']} should actively engage in exercises that sharpen observation and interpretation abilities. By practicing mindfulness techniques and paying closer attention to details in various situations, {data['student_name']} can improve their perceptual acuity. Additionally, seeking diverse perspectives and actively listening to others' viewpoints can broaden their understanding and enhance overall perceptual skills.",
        "Resolve": f"Improving resolution skills requires {data['student_name']} to develop effective decision-making strategies and enhance their problem-solving abilities. To achieve this, {data['student_name']} should practice evaluating multiple options before making decisions, considering different perspectives, and analyzing potential outcomes. Building resilience in handling challenges and seeking mentorship or guidance in complex situations can also foster growth in resolution skills.",
        "Influence": f"Enhancing influence skills involves {data['student_name']} refining their communication strategies and understanding the impact of their actions on others. By cultivating empathy and actively listening to others' needs, {data['student_name']} can build stronger relationships and effectively communicate ideas. Taking leadership roles in group projects or community activities can provide opportunities to practice influencing others positively and developing persuasive communication skills.",
        "Deliver": f"To enhance delivery skills, {data['student_name']} should focus on improving organization and time management abilities. Setting clear goals, prioritizing tasks effectively, and maintaining a structured approach to projects can significantly enhance delivery efficiency. Additionally, practicing effective presentation techniques, such as maintaining audience engagement and clarity in communication, will further refine {data['student_name']}'s delivery skills.",
        "Engage": f"Improving engagement skills requires {data['student_name']} to actively participate in discussions, listen attentively, and contribute meaningfully to group interactions. By fostering a collaborative environment and valuing diverse perspectives, {data['student_name']} can enhance their ability to engage effectively with others. Building empathy and understanding the impact of their contributions on group dynamics will further strengthen {data['student_name']}'s engagement skills.",
        "Attention": f"To improve attention skills, {data['student_name']} should practice concentration exercises and minimize distractions during tasks. Setting specific goals and deadlines can help maintain focus and improve productivity. Developing strategies to handle interruptions and implementing time management techniques will further enhance {data['student_name']}'s ability to sustain attention and avoid distractions.",
        "Memory": f"Enhancing memory skills involves {data['student_name']} employing mnemonic devices, visualization techniques, and active recall methods. Creating associations between new information and existing knowledge can aid in retention. Regular review of material and practicing retrieval exercises will strengthen memory recall and improve overall memory retention capabilities.",
        "Critical Thinking": f"Improving critical thinking skills requires {data['student_name']} to evaluate information objectively, analyze different perspectives, and develop reasoned judgments. By practicing questioning assumptions, seeking evidence, and considering alternative viewpoints, {data['student_name']} can enhance their analytical abilities. Engaging in debates, solving complex problems, and discussing current issues can further refine {data['student_name']}'s critical thinking skills.",
        "Creative Thinking": f"To enhance creative thinking, {data['student_name']} should explore new ideas, experiment with different approaches, and embrace unconventional solutions. Engaging in activities that foster creativity, such as brainstorming sessions, artistic pursuits, or interdisciplinary projects, can stimulate innovative thinking. Embracing failures as learning opportunities and seeking feedback from peers or mentors will further nurture {data['student_name']}'s creative potential.",
        "Mindset": f"Developing a growth mindset involves {data['student_name']} embracing challenges, persisting through setbacks, and viewing failures as opportunities for growth. By cultivating resilience, maintaining a positive outlook, and seeking constructive feedback, {data['student_name']} can foster a growth-oriented mindset. Setting achievable goals, celebrating successes, and learning from setbacks will further strengthen {data['student_name']}'s mindset.",
        "Attitude": f"To improve attitude, {data['student_name']} should focus on maintaining a positive outlook, demonstrating resilience in adversity, and fostering a proactive approach to challenges. By practicing gratitude, staying optimistic, and adopting a solution-oriented mindset, {data['student_name']} can cultivate a positive attitude. Embracing collaboration, supporting peers, and seeking opportunities for personal growth will further enhance {data['student_name']}'s attitude.",
        "Expression": f"Enhancing expression skills involves {data['student_name']} practicing clear and concise communication. By refining verbal and written communication techniques, using appropriate language, and structuring ideas logically, {data['student_name']} can convey thoughts effectively. Seeking opportunities to present ideas confidently, actively listening to feedback, and adjusting communication style based on audience needs will further develop {data['student_name']}'s expressive capabilities.",
        "Communication": f"Improving communication skills requires {data['student_name']} to listen actively, convey ideas clearly, and adapt communication style to diverse audiences. By practicing empathy, using effective listening techniques, and fostering open dialogue, {data['student_name']} can enhance interpersonal communication. Engaging in group discussions, delivering persuasive presentations, and seeking constructive criticism will further refine {data['student_name']}'s communication skills.",
        "Collaboration": f"To enhance collaboration skills, {data['student_name']} should develop teamwork abilities, foster trust among team members, and improve conflict resolution techniques. By valuing diverse perspectives, promoting open communication, and respecting team dynamics, {data['student_name']} can build effective collaborative relationships. Taking leadership roles in group projects, facilitating team discussions, and mediating conflicts will further strengthen {data['student_name']}'s collaboration skills.",
        "Leadership": f"Improving leadership skills involves {data['student_name']} setting a vision, motivating team members, and making informed decisions. By developing emotional intelligence, delegating tasks effectively, and providing constructive feedback, {data['student_name']} can inspire others and achieve common goals. Taking initiative in group activities, mentoring peers, and seeking leadership opportunities will further cultivate {data['student_name']}'s leadership abilities.",
        "Awareness": f"Enhancing awareness requires {data['student_name']} staying informed about current events, trends, and industry developments. By engaging in self-reflection, seeking feedback, and maintaining curiosity, {data['student_name']} can deepen their understanding of personal strengths and areas for growth. Developing cultural awareness, staying updated on relevant topics, and networking with industry professionals will further expand {data['student_name']}'s awareness.",
        "Application": f"To improve application skills, {data['student_name']} should focus on applying theoretical knowledge in practical scenarios, evaluating outcomes, and refining strategies based on results. By participating in hands-on projects, internships, or real-world simulations, {data['student_name']} can gain practical experience and enhance application capabilities. Seeking mentorship, receiving feedback on performance, and reflecting on lessons learned will further strengthen {data['student_name']}'s application skills.",
        "Advantage": f"Developing competitive advantage involves {data['student_name']} leveraging strengths, identifying unique capabilities, and capitalizing on opportunities. By conducting SWOT analysis, setting SMART goals, and differentiating themselves in the market, {data['student_name']} can gain a competitive edge. Networking with industry professionals, staying updated on market trends, and showcasing skills through projects or portfolios will further enhance {data['student_name']}'s competitive advantage."
    }

def generate_areas_for_improvement(data):
    scores = {
        "Perceive": float(data.get('Perceive_score', 0)),
        "Resolve": float(data.get('Resolve_score', 0)),
        "Influence": float(data.get('Influence_score', 0)),
        "Deliver": float(data.get('Deliver_score', 0)),
        "Engage": float(data.get('Engage_score', 0)),
        "Attention": float(data.get('Attention_score', 0)),
        "Memory": float(data.get('Memory_score', 0)),
        "Critical Thinking": float(data.get('Critical_Thinking_score', 0)),
        "Creative Thinking": float(data.get('Creative_Thinking_score', 0)),
        "Mindset": float(data.get('Mindset_score', 0)),
        "Attitude": float(data.get('Attitude_score', 0)),
        "Expression": float(data.get('Expression_score', 0)),
        "Communication": float(data.get('Communication_score', 0)),
        "Collaboration": float(data.get('Collaboration_score', 0)),
        "Leadership": float(data.get('Leadership_score', 0)),
        "Awareness": float(data.get('Awareness_score', 0)),
        "Application": float(data.get('Application_score', 0)),
        "Advantage": float(data.get('Advantage_score', 0))
    }

    improvement_paragraphs = {
        "Perceive": f"To enhance perception skills, {data.get('student_name', 'the student')} should actively engage in exercises that sharpen observation and interpretation abilities. By practicing mindfulness techniques and paying closer attention to details in various situations, {data.get('student_name', 'the student')} can improve their perceptual acuity. Additionally, seeking diverse perspectives and actively listening to others' viewpoints can broaden their understanding and enhance overall perceptual skills.",
        "Resolve": f"Improving resolution skills requires {data.get('student_name', 'the student')} to develop effective decision-making strategies and enhance their problem-solving abilities. To achieve this, {data.get('student_name', 'the student')} should practice evaluating multiple options before making decisions, considering different perspectives, and analyzing potential outcomes. Building resilience in handling challenges and seeking mentorship or guidance in complex situations can also foster growth in resolution skills.",
        "Influence": f"Enhancing influence skills involves {data.get('student_name', 'the student')} refining their communication strategies and understanding the impact of their actions on others. By cultivating empathy and actively listening to others' needs, {data.get('student_name', 'the student')} can build stronger relationships and effectively communicate ideas. Taking leadership roles in group projects or community activities can provide opportunities to practice influencing others positively and developing persuasive communication skills.",
        "Deliver": f"To enhance delivery skills, {data.get('student_name', 'the student')} should focus on improving organization and time management abilities. Setting clear goals, prioritizing tasks effectively, and maintaining a structured approach to projects can significantly enhance delivery efficiency. Additionally, practicing effective presentation techniques, such as maintaining audience engagement and clarity in communication, will further refine {data.get('student_name', 'the student')}'s delivery skills.",
        "Engage": f"Improving engagement skills requires {data.get('student_name', 'the student')} to actively participate in discussions, listen attentively, and contribute meaningfully to group interactions. By fostering a collaborative environment and valuing diverse perspectives, {data.get('student_name', 'the student')} can enhance their ability to engage effectively with others. Building empathy and understanding the impact of their contributions on group dynamics will further strengthen {data.get('student_name', 'the student')}'s engagement skills.",
        "Attention": f"To improve attention skills, {data.get('student_name', 'the student')} should practice concentration exercises and minimize distractions during tasks. Setting specific goals and deadlines can help maintain focus and improve productivity. Developing strategies to handle interruptions and implementing time management techniques will further enhance {data.get('student_name', 'the student')}'s ability to sustain attention and avoid distractions.",
        "Memory": f"Enhancing memory skills involves {data.get('student_name', 'the student')} employing mnemonic devices, visualization techniques, and active recall methods. Creating associations between new information and existing knowledge can aid in retention. Regular review of material and practicing retrieval exercises will strengthen memory recall and improve overall memory retention capabilities.",
        "Critical Thinking": f"Improving critical thinking skills requires {data.get('student_name', 'the student')} to evaluate information objectively, analyze different perspectives, and develop reasoned judgments. By practicing questioning assumptions, seeking evidence, and considering alternative viewpoints, {data.get('student_name', 'the student')} can enhance their analytical abilities. Engaging in debates, solving complex problems, and discussing current issues can further refine {data.get('student_name', 'the student')}'s critical thinking skills.",
        "Creative Thinking": f"To enhance creative thinking, {data.get('student_name', 'the student')} should explore new ideas, experiment with different approaches, and embrace unconventional solutions. Engaging in activities that foster creativity, such as brainstorming sessions, artistic pursuits, or interdisciplinary projects, can stimulate innovative thinking. Embracing failures as learning opportunities and seeking feedback from peers or mentors will further nurture {data.get('student_name', 'the student')}'s creative potential.",
        "Mindset": f"Developing a growth mindset involves {data.get('student_name', 'the student')} embracing challenges, persisting through setbacks, and viewing failures as opportunities for growth. By cultivating resilience, maintaining a positive outlook, and seeking constructive feedback, {data.get('student_name', 'the student')} can foster a growth-oriented mindset. Setting achievable goals, celebrating successes, and learning from setbacks will further strengthen {data.get('student_name', 'the student')}'s mindset.",
        "Attitude": f"To improve attitude, {data.get('student_name', 'the student')} should focus on maintaining a positive outlook, demonstrating resilience in adversity, and fostering a proactive approach to challenges. By practicing gratitude, staying optimistic, and adopting a solution-oriented mindset, {data.get('student_name', 'the student')} can cultivate a positive attitude. Embracing collaboration, supporting peers, and seeking opportunities for personal growth will further enhance {data.get('student_name', 'the student')}'s attitude.",
        "Expression": f"Enhancing expression skills involves {data.get('student_name', 'the student')} practicing clear and concise communication. By refining verbal and written communication techniques, using appropriate language, and structuring ideas logically, {data.get('student_name', 'the student')} can convey thoughts effectively. Seeking opportunities to present ideas confidently, actively listening to feedback, and adjusting communication style based on audience needs will further develop {data.get('student_name', 'the student')}'s expressive capabilities.",
        "Communication": f"Improving communication skills requires {data.get('student_name', 'the student')} to listen actively, convey ideas clearly, and adapt communication style to diverse audiences. By practicing empathy, using effective listening techniques, and fostering open dialogue, {data.get('student_name', 'the student')} can enhance interpersonal communication. Engaging in group discussions, delivering persuasive presentations, and seeking constructive criticism will further refine {data.get('student_name', 'the student')}'s communication skills.",
        "Collaboration": f"To enhance collaboration skills, {data.get('student_name', 'the student')} should develop teamwork abilities, foster trust among team members, and improve conflict resolution techniques. By valuing diverse perspectives, promoting open communication, and respecting team dynamics, {data.get('student_name', 'the student')} can contribute effectively to collaborative efforts. Taking initiative in group projects, assuming leadership roles, and supporting team cohesion will further strengthen {data.get('student_name', 'the student')}'s collaboration skills.",
        "Leadership": f"Improving leadership skills involves {data.get('student_name', 'the student')} demonstrating integrity, inspiring others, and fostering a collaborative team environment. By setting a positive example, providing guidance, and empowering team members, {data.get('student_name', 'the student')} can lead with confidence. Developing decision-making abilities, delegating tasks effectively, and seeking feedback from peers will further enhance {data.get('student_name', 'the student')}'s leadership skills.",
        "Awareness": f"To enhance awareness skills, {data.get('student_name', 'the student')} should practice mindfulness, cultivate self-awareness, and develop empathy for others. By reflecting on personal strengths and weaknesses, seeking feedback, and embracing continuous learning, {data.get('student_name', 'the student')} can deepen their awareness. Engaging in cultural activities, participating in community service, and exploring diverse perspectives will further broaden {data.get('student_name', 'the student')}'s awareness.",
        "Application": f"Improving application skills involves {data.get('student_name', 'the student')} demonstrating practical knowledge, applying theoretical concepts, and solving real-world problems effectively. By engaging in hands-on experiences, seeking internships or project opportunities, and collaborating with industry professionals, {data.get('student_name', 'the student')} can enhance their application abilities. Developing technical proficiency, adapting to new technologies, and staying updated with industry trends will further refine {data.get('student_name', 'the student')}'s application skills.",
        "Advantage": f"To enhance advantage skills, {data.get('student_name', 'the student')} should leverage strengths, identify opportunities, and develop competitive strategies. By conducting market research, analyzing trends, and exploring innovative solutions, {data.get('student_name', 'the student')} can gain a competitive edge. Networking with industry professionals, attending conferences, and pursuing certifications relevant to their field of interest will further strengthen {data.get('student_name', 'the student')}'s advantage."
    }

    
    # Sort skills by scores in ascending order and select top 5
    sorted_skills = sorted(scores.items(), key=lambda x: float(x[1]), reverse=False)[:5]

    improvement_order = "\n\n".join(improvement_paragraphs[skill[0]] for skill in sorted_skills if skill[0] in improvement_paragraphs)

    return improvement_order

def generate_recommendations(data):
    recommendations = []

    # Perceive
    recommendations.append("### Perceive")
    if data.get('Perceive_score', 0) < 50:
        recommendations.append("- Practice mindfulness techniques daily to improve observation skills.")
        recommendations.append("- Engage in activities that require acute attention to detail.")
    elif data.get('Perceive_score', 0) >= 50 and data.get('Perceive_score', 0) < 70:
        recommendations.append("- Continue practicing mindfulness exercises to enhance perception skills.")
        recommendations.append("- Explore new hobbies that stimulate observational abilities, such as photography or painting.")
    else:
        recommendations.append("- Maintain consistent mindfulness practices to sustain high levels of perception.")
        recommendations.append("- Mentor peers in developing effective observation techniques.")

    # Resolve
    recommendations.append("\n### Resolve")
    if data.get('Resolve_score', 0) < 50:
        recommendations.append("- Focus on decision-making exercises to improve resolution skills.")
        recommendations.append("- Seek guidance from mentors or professionals when faced with complex problems.")
    elif data.get('Resolve_score', 0) >= 50 and data.get('Resolve_score', 0) < 70:
        recommendations.append("- Practice evaluating multiple options before making decisions.")
        recommendations.append("- Participate in workshops on problem-solving strategies.")
    else:
        recommendations.append("- Take on leadership roles to further develop decision-making abilities.")
        recommendations.append("- Mentor others in effective problem-solving techniques.")

    # Influence
    recommendations.append("\n### Influence")
    if data.get('Influence_score', 0) < 50:
        recommendations.append("- Develop active listening skills to better understand others' perspectives.")
        recommendations.append("- Practice assertiveness in communicating ideas and opinions.")
    elif data.get('Influence_score', 0) >= 50 and data.get('Influence_score', 0) < 70:
        recommendations.append("- Engage in group activities that require teamwork and collaboration.")
        recommendations.append("- Seek opportunities to lead discussions or group projects.")
    else:
        recommendations.append("- Mentor peers in effective communication strategies.")
        recommendations.append("- Take on roles that require influencing team decisions.")

    # Deliver
    recommendations.append("\n### Deliver")
    if data.get('Deliver_score', 0) < 50:
        recommendations.append("- Improve time management skills to meet project deadlines effectively.")
        recommendations.append("- Practice structuring presentations to enhance clarity and impact.")
    elif data.get('Deliver_score', 0) >= 50 and data.get('Deliver_score', 0) < 70:
        recommendations.append("- Use feedback to refine presentation skills and maintain audience engagement.")
        recommendations.append("- Develop organizational skills to streamline project delivery.")
    else:
        recommendations.append("- Mentor peers in effective presentation techniques.")
        recommendations.append("- Seek opportunities to lead presentations or workshops.")

    # Engage
    recommendations.append("\n### Engage")
    if data.get('Engage_score', 0) < 50:
        recommendations.append("- Actively participate in group discussions and activities.")
        recommendations.append("- Develop empathy to understand and address team dynamics.")
    elif data.get('Engage_score', 0) >= 50 and data.get('Engage_score', 0) < 70:
        recommendations.append("- Foster a collaborative environment by encouraging diverse opinions.")
        recommendations.append("- Take initiative in organizing team-building exercises.")
    else:
        recommendations.append("- Mentor peers in fostering collaboration within teams.")
        recommendations.append("- Lead initiatives that promote teamwork and mutual support.")

    # Attention
    recommendations.append("\n### Attention")
    if data.get('Attention_score', 0) < 50:
        recommendations.append("- Minimize distractions during tasks by creating a conducive work environment.")
        recommendations.append("- Use time-blocking techniques to allocate focused time for different tasks.")
    elif data.get('Attention_score', 0) >= 50 and data.get('Attention_score', 0) < 70:
        recommendations.append("- Practice mindfulness exercises to improve concentration.")
        recommendations.append("- Implement strategies to manage interruptions effectively.")
    else:
        recommendations.append("- Mentor peers in maintaining focus and productivity.")
        recommendations.append("- Lead workshops on effective time management strategies.")

    # Memory
    recommendations.append("\n### Memory")
    if data.get('Memory_score', 0) < 50:
        recommendations.append("- Use mnemonic devices and visualization techniques to aid memory retention.")
        recommendations.append("- Review information regularly to reinforce learning.")
    elif data.get('Memory_score', 0) >= 50 and data.get('Memory_score', 0) < 70:
        recommendations.append("- Practice active recall methods to strengthen memory.")
        recommendations.append("- Engage in activities that require memorization, such as quizzes or flashcards.")
    else:
        recommendations.append("- Mentor peers in memory enhancement techniques.")
        recommendations.append("- Lead study groups focused on improving memory recall.")

    # Critical Thinking
    recommendations.append("\n### Critical Thinking")
    if data.get('Critical_Thinking_score', 0) < 50:
        recommendations.append("- Evaluate information critically by questioning assumptions and biases.")
        recommendations.append("- Engage in debates or discussions on complex topics to develop analytical skills.")
    elif data.get('Critical_Thinking_score', 0) >= 50 and data.get('Critical_Thinking_score', 0) < 70:
        recommendations.append("- Seek opportunities to analyze diverse perspectives on current issues.")
        recommendations.append("- Participate in problem-solving activities that require critical reasoning.")
    else:
        recommendations.append("- Mentor peers in developing critical thinking abilities.")
        recommendations.append("- Lead workshops on logical reasoning and decision-making.")

    # Creative Thinking
    recommendations.append("\n### Creative Thinking")
    if data.get('Creative_Thinking_score', 0) < 50:
        recommendations.append("- Explore creative outlets such as writing, art, or music to stimulate innovative thinking.")
        recommendations.append("- Embrace failure as a learning opportunity to foster creativity.")
    elif data.get('Creative_Thinking_score', 0) >= 50 and data.get('Creative_Thinking_score', 0) < 70:
        recommendations.append("- Participate in brainstorming sessions to generate new ideas.")
        recommendations.append("- Experiment with different approaches to problem-solving.")
    else:
        recommendations.append("- Mentor peers in cultivating creative thinking skills.")
        recommendations.append("- Lead creative projects that encourage innovative solutions.")

    # Mindset
    recommendations.append("\n### Mindset")
    if data.get('Mindset_score', 0) < 50:
        recommendations.append("- Cultivate a growth mindset by embracing challenges and learning from setbacks.")
        recommendations.append("- Seek feedback to identify areas for personal growth.")
    elif data.get('Mindset_score', 0) >= 50 and data.get('Mindset_score', 0) < 70:
        recommendations.append("- Maintain a positive outlook during challenges to sustain a growth mindset.")
        recommendations.append("- Encourage others to adopt a growth-oriented mindset.")
    else:
        recommendations.append("- Mentor peers in developing resilience and perseverance.")
        recommendations.append("- Lead workshops on fostering a growth mindset.")

    # Attitude
    recommendations.append("\n### Attitude")
    if data.get('Attitude_score', 0) < 50:
        recommendations.append("- Practice gratitude to maintain a positive attitude in all situations.")
        recommendations.append("- Foster a supportive environment by offering help to peers.")
    elif data.get('Attitude_score', 0) >= 50 and data.get('Attitude_score', 0) < 70:
        recommendations.append("- Demonstrate resilience in overcoming challenges.")
        recommendations.append("- Encourage optimism and proactive problem-solving approaches.")
    else:
        recommendations.append("- Mentor peers in developing a positive attitude and proactive mindset.")
        recommendations.append("- Lead initiatives that promote a culture of positivity and collaboration.")

    # Expression
    recommendations.append("\n### Expression")
    if data.get('Expression_score', 0) < 50:
        recommendations.append("- Practice clear and concise communication to convey ideas effectively.")
        recommendations.append("- Seek opportunities to present ideas confidently.")
    elif data.get('Expression_score', 0) >= 50 and data.get('Expression_score', 0) < 70:
        recommendations.append("- Use feedback to refine communication skills and adapt to audience needs.")
        recommendations.append("- Engage in activities that require persuasive communication, such as debates or presentations.")
    else:
        recommendations.append("- Mentor peers in improving verbal and written communication skills.")
        recommendations.append("- Lead workshops on effective communication strategies.")

    # Communication
    recommendations.append("\n### Communication")
    if data.get('Communication_score', 0) < 50:
        recommendations.append("- Actively listen to others to understand their perspectives.")
        recommendations.append("- Practice empathy in communication to build stronger relationships.")
    elif data.get('Communication_score', 0) >= 50 and data.get('Communication_score', 0) < 70:
        recommendations.append("- Foster open dialogue by encouraging diverse viewpoints.")
        recommendations.append("- Seek opportunities to lead discussions or facilitate group interactions.")
    else:
        recommendations.append("- Mentor peers in developing effective interpersonal communication skills.")
        recommendations.append("- Lead workshops on fostering communication skills within teams.")

    # Collaboration
    recommendations.append("\n### Collaboration")
    if data.get('Collaboration_score', 0) < 50:
        recommendations.append("- Develop teamwork skills by collaborating on group projects.")
        recommendations.append("- Build trust among team members to improve collaboration.")
    elif data.get('Collaboration_score', 0) >= 50 and data.get('Collaboration_score', 0) < 70:
        recommendations.append("- Promote inclusive teamwork by valuing diverse perspectives.")
        recommendations.append("- Encourage mutual support and respect within teams.")
    else:
        recommendations.append("- Mentor peers in fostering collaborative relationships.")
        recommendations.append("- Lead initiatives that strengthen teamwork and cohesion.")

    # Leadership
    recommendations.append("\n### Leadership")
    if data.get('Leadership_score', 0) < 50:
        recommendations.append("- Develop leadership skills by taking initiative in group activities.")
        recommendations.append("- Seek feedback from peers and mentors to improve leadership abilities.")
    elif data.get('Leadership_score', 0) >= 50 and data.get('Leadership_score', 0) < 70:
        recommendations.append("- Lead by example to inspire others and foster team collaboration.")
        recommendations.append("- Encourage team members to take ownership of their roles and responsibilities.")
    else:
        recommendations.append("- Mentor peers in developing effective leadership qualities.")
        recommendations.append("- Lead initiatives that promote leadership development within groups.")

    # Emotional Intelligence
    recommendations.append("\n### Emotional Intelligence")
    if data.get('Emotional_Intelligence_score', 0) < 50:
        recommendations.append("- Practice self-awareness to recognize and manage emotions effectively.")
        recommendations.append("- Develop empathy to understand others' feelings and perspectives.")
    elif data.get('Emotional_Intelligence_score', 0) >= 50 and data.get('Emotional_Intelligence_score', 0) < 70:
        recommendations.append("- Use emotional intelligence to build positive relationships.")
        recommendations.append("- Foster a supportive environment by empathizing with team members.")
    else:
        recommendations.append("- Mentor peers in developing emotional intelligence.")
        recommendations.append("- Lead workshops on emotional intelligence and its impact on teamwork.")

    # Adaptability
    recommendations.append("\n### Adaptability")
    if data.get('Adaptability_score', 0) < 50:
        recommendations.append("- Embrace change as an opportunity for growth and learning.")
        recommendations.append("- Develop resilience to overcome challenges.")
    elif data.get('Adaptability_score', 0) >= 50 and data.get('Adaptability_score', 0) < 70:
        recommendations.append("- Remain flexible and open to new ideas and approaches.")
        recommendations.append("- Seek opportunities to learn from different experiences.")
    else:
        recommendations.append("- Mentor peers in adapting to changing circumstances.")
        recommendations.append("- Lead initiatives that promote adaptability and innovation.")

    # Innovation
    recommendations.append("\n### Innovation")
    if data.get('Innovation_score', 0) < 50:
        recommendations.append("- Foster a creative environment that encourages new ideas.")
        recommendations.append("- Experiment with innovative solutions to solve problems.")
    elif data.get('Innovation_score', 0) >= 50 and data.get('Innovation_score', 0) < 70:
        recommendations.append("- Collaborate with others to develop and refine innovative concepts.")
        recommendations.append("- Seek feedback to improve and implement innovative ideas.")
    else:
        recommendations.append("- Mentor peers in fostering a culture of innovation.")
        recommendations.append("- Lead projects that require innovative thinking and problem-solving.")

    # Resilience
    recommendations.append("\n### Resilience")
    if data.get('Resilience_score', 0) < 50:
        recommendations.append("- Develop coping strategies to manage stress and adversity.")
        recommendations.append("- Practice optimism to maintain a positive outlook during challenges.")
    elif data.get('Resilience_score', 0) >= 50 and data.get('Resilience_score', 0) < 70:
        recommendations.append("- Build resilience by learning from setbacks and failures.")
        recommendations.append("- Seek support from peers and mentors during difficult times.")
    else:
        recommendations.append("- Mentor peers in developing resilience and perseverance.")
        recommendations.append("- Lead workshops on building resilience and overcoming adversity.")

    # Problem-Solving
    recommendations.append("\n### Problem-Solving")
    if data.get('Problem_Solving_score', 0) < 50:
        recommendations.append("- Develop systematic approaches to analyze and solve problems.")
        recommendations.append("- Practice breaking down complex problems into manageable tasks.")
    elif data.get('Problem_Solving_score', 0) >= 50 and data.get('Problem_Solving_score', 0) < 70:
        recommendations.append("- Use analytical skills to evaluate multiple solutions before making decisions.")
        recommendations.append("- Seek feedback to improve problem-solving techniques.")
    else:
        recommendations.append("- Mentor peers in developing effective problem-solving strategies.")
        recommendations.append("- Lead workshops on critical thinking and decision-making.")

    # Ethics
    recommendations.append("\n### Ethics")
    if data.get('Ethics_score', 0) < 50:
        recommendations.append("- Uphold ethical principles in all professional and personal decisions.")
        recommendations.append("- Seek guidance from mentors or ethical experts when faced with moral dilemmas.")
    elif data.get('Ethics_score', 0) >= 50 and data.get('Ethics_score', 0) < 70:
        recommendations.append("- Continuously reflect on ethical implications of actions and decisions.")
        recommendations.append("- Discuss ethical dilemmas with peers to gain diverse perspectives.")
    else:
        recommendations.append("- Mentor peers in ethical decision-making.")
        recommendations.append("- Lead discussions on ethical practices and responsibilities.")

    return "\n".join(recommendations)

def generate_action_plan(data):
    scores = {
        "Perceive": float(data.get('perceiveContribution', 0)),
        "Resolve": float(data.get('resolveContribution', 0)),
        "Influence": float(data.get('influenceContribution', 0)),
        "Deliver": float(data.get('deliverContribution', 0)),
        "Engage": float(data.get('engageContribution', 0)),
        "Attention": float(data.get('attentionContribution', 0)),
        "Memory": float(data.get('memoryContribution', 0)),
        "Critical Thinking": float(data.get('criticalContribution', 0)),
        "Creative Thinking": float(data.get('creativeContribution', 0)),
        "Mindset": float(data.get('mindsetContribution', 0)),
        "Attitude": float(data.get('attitudeContribution', 0)),
        "Expression": float(data.get('expressionContribution', 0)),
        "Communication": float(data.get('communicationContribution', 0)),
        "Collaboration": float(data.get('collaborationContribution', 0)),
        "Leadership": float(data.get('leadershipContribution', 0)),
        "Awareness": float(data.get('awarenessContribution', 0)),
        "Application": float(data.get('applicationContribution', 0)),
        "Advantage": float(data.get('advantageContribution', 0))
    }

    # Sort skills by their contribution scores in ascending order
    sorted_skills = sorted(scores.items(), key=lambda x: x[1])

    action_plan = "### EXPERT NOTE\n\nAction Plan and Way Forward\n\n"

    # Iterate over the top 5 lowest skills
    for skill, value_points in sorted_skills[:5]:
        expert_note = {
            "Perceive": "Sharpen your ability to perceive and interpret subtle cues and signals, enhancing your decision-making.",
            "Resolve": "Strengthen your problem-solving abilities to navigate challenges effectively and achieve optimal outcomes.",
            "Influence": "Master the art of influencing decisions and outcomes positively through persuasive communication and strategic negotiation.",
            "Deliver": "Refine your task management skills to consistently deliver high-quality results on time and within budget.",
            "Engage": "Enhance your interpersonal skills to build strong relationships and foster a collaborative team environment.",
            "Attention": "Improve your focus and concentration to boost productivity and minimize errors in your work.",
            "Memory": "Develop effective memory retention techniques to facilitate learning and recall of critical information.",
            "Critical Thinking": "Cultivate your analytical reasoning skills to evaluate complex problems and make informed decisions.",
            "Creative Thinking": "Foster innovative thinking to generate unique solutions and approaches to challenges.",
            "Mindset": "Embrace a growth mindset, believing in your ability to learn and develop skills through dedication and effort.",
            "Attitude": "Cultivate a positive mindset to navigate challenges with resilience and optimism.",
            "Expression": "Hone your communication skills to articulate ideas clearly and persuasively across various platforms.",
            "Communication": "Enhance your ability to convey information effectively and build meaningful connections through communication.",
            "Collaboration": "Strengthen your collaborative skills to work effectively within teams and achieve collective goals.",
            "Leadership": "Develop your leadership capabilities to inspire and guide others toward achieving shared objectives.",
            "Awareness": "Expand your awareness of global issues and trends to make informed decisions and drive positive change.",
            "Application": "Apply your knowledge and skills effectively in practical situations to achieve tangible results.",
            "Advantage": "Leverage your unique strengths and capabilities to gain a competitive edge and create opportunities for success."
        }

        action_plan += f"PRIDE: {skill}\n\n"
        action_plan += f"{expert_note.get(skill, 'Insightful expert note')}\n\n"

        if value_points < 50:
            action_plan += f"{data.get('student_name', 'The student')} needs to focus on building a strong foundation in {skill.lower()}.\n\n"
        elif value_points >= 50 and value_points < 70:
            action_plan += f"{data.get('student_name', 'The student')} has shown some progress in {skill.lower()}, but there's room for significant improvement.\n\n"
        else:
            action_plan += f"While {data.get('student_name', 'the student')} demonstrates proficiency in most areas, {skill.lower()} could be further optimized.\n\n"

        # Detailed action plan recommendations for each skill:
        if skill == "Perceive":
            action_plan += "- Develop skills in perceiving and interpreting subtle cues and signals.\n"
            action_plan += "- Practice active listening and observation to enhance perception accuracy.\n"
            action_plan += "- Engage in activities that require attention to detail and the ability to detect patterns.\n\n"

        elif skill == "Resolve":
            action_plan += "- Enhance decision-making abilities by considering multiple perspectives and possible outcomes.\n"
            action_plan += "- Practice problem-solving techniques to efficiently resolve issues and challenges.\n"
            action_plan += "- Develop resilience to overcome obstacles and setbacks effectively.\n\n"

        elif skill == "Influence":
            action_plan += "- Work on decision-making processes by validating information based on motives, triggers, holistic benefits, process hurdles, and positive growth potential.\n"
            action_plan += "- Enhance negotiation skills to influence outcomes positively and build productive relationships.\n"
            action_plan += "- Develop strategies to effectively communicate ideas and gain buy-in from stakeholders.\n\n"

        elif skill == "Deliver":
            action_plan += "- Improve task management skills to meet deadlines and deliver high-quality results.\n"
            action_plan += "- Enhance organizational skills to streamline workflows and optimize productivity.\n"
            action_plan += "- Develop strategies to manage resources effectively and minimize wastage.\n\n"

        elif skill == "Engage":
            action_plan += "- Enhance interpersonal skills to build rapport and connect with others effectively.\n"
            action_plan += "- Develop empathy and active listening skills to understand perspectives and respond appropriately.\n"
            action_plan += "- Practice conflict resolution techniques to address differences and foster collaboration.\n\n"

        elif skill == "Attention":
            action_plan += "- Practice techniques to improve focus and concentration, such as mindfulness or meditation.\n"
            action_plan += "- Minimize distractions in your environment to enhance productivity and accuracy.\n"
            action_plan += "- Take regular breaks to maintain mental clarity and avoid cognitive fatigue.\n\n"

        elif skill == "Memory":
            action_plan += "- Develop mnemonic devices or memory aids to enhance retention and recall.\n"
            action_plan += "- Practice spaced repetition techniques to reinforce learning and memory retention.\n"
            action_plan += "- Engage in activities that challenge your memory, such as puzzles or learning new languages.\n\n"

        elif skill == "Critical Thinking":
            action_plan += "- Evaluate information critically by questioning assumptions and examining evidence.\n"
            action_plan += "- Practice logical reasoning and problem-solving techniques to analyze complex issues.\n"
            action_plan += "- Seek diverse perspectives and consider alternative solutions before making decisions.\n\n"

        elif skill == "Creative Thinking":
            action_plan += "- Cultivate curiosity and explore new ideas or approaches to problem-solving.\n"
            action_plan += "- Engage in activities that stimulate creativity, such as brainstorming sessions or artistic endeavors.\n"
            action_plan += "- Embrace ambiguity and risk-taking to foster innovative thinking.\n\n"

        elif skill == "Mindset":
            action_plan += "- Develop resilience to overcome setbacks and challenges with a positive outlook.\n"
            action_plan += "- Challenge limiting beliefs and cultivate a growth mindset focused on continuous learning.\n"
            action_plan += "- Set ambitious yet achievable goals to stretch your capabilities and expand your potential.\n\n"

        elif skill == "Attitude":
            action_plan += "- Practice gratitude and positivity to maintain a constructive attitude in challenging situations.\n"
            action_plan += "- Cultivate emotional intelligence to regulate your emotions and respond effectively to setbacks.\n"
            action_plan += "- Foster a supportive and inclusive environment that promotes teamwork and collaboration.\n\n"

        elif skill == "Expression":
            action_plan += "- Refine your verbal and written communication skills to convey ideas clearly and persuasively.\n"
            action_plan += "- Tailor your message to the audience's needs and preferences to enhance engagement.\n"
            action_plan += "- Use storytelling techniques to make your communications more compelling and memorable.\n\n"

        elif skill == "Communication":
            action_plan += "- Develop active listening skills to understand others' perspectives and respond empathetically.\n"
            action_plan += "- Practice assertiveness and clarity in your communication to express ideas effectively.\n"
            action_plan += "- Foster open dialogue and transparency to build trust and strengthen relationships.\n\n"

        elif skill == "Collaboration":
            action_plan += "- Enhance your ability to work collaboratively in diverse teams and leverage collective strengths.\n"
            action_plan += "- Build trust and rapport with team members through effective communication and mutual respect.\n"
            action_plan += "- Foster a culture of cooperation and shared responsibility to achieve common goals.\n\n"

        elif skill == "Leadership":
            action_plan += "- Develop your leadership skills by inspiring and motivating others to achieve shared objectives.\n"
            action_plan += "- Delegate tasks effectively and empower team members to take ownership of their responsibilities.\n"
            action_plan += "- Continuously refine your leadership style based on feedback and self-reflection.\n\n"

        elif skill == "Awareness":
            action_plan += "- Stay informed about current trends and developments in your field of expertise.\n"
            action_plan += "- Expand your knowledge of global issues and their potential impact on your work or community.\n"
            action_plan += "- Actively seek diverse perspectives to broaden your understanding and decision-making.\n\n"

        elif skill == "Application":
            action_plan += "- Apply theoretical knowledge to practical situations to gain hands-on experience.\n"
            action_plan += "- Seek opportunities to implement innovative solutions and contribute to organizational goals.\n"
            action_plan += "- Reflect on your experiences and continuously refine your skills based on lessons learned.\n\n"

        elif skill == "Advantage":
            action_plan += "- Identify and leverage your unique strengths and capabilities to gain a competitive edge.\n"
            action_plan += "- Explore opportunities for professional growth and advancement based on your strengths.\n"
            action_plan += "- Develop a strategic plan to capitalize on your advantages and achieve long-term success.\n\n"

    return action_plan


def generate_pride_report(data):
    def get_category(score):
        if score <= 20:
            return "Potential"
        elif score <= 40:
            return "Preparing"
        elif score <= 60:
            return "Promising"
        elif score <= 80:
            return "Progressing"
        else:
            return "Performing"

    def get_personality_type(pride_score):
        if pride_score <= 20:
            return "Uniquely Potential"
        elif pride_score <= 40:
            return "Uniquely Preparing"
        elif pride_score <= 60:
            return "Uniquely Promising"
        elif pride_score <= 80:
            return "Uniquely Progressing"
        else:
            return "Uniquely Performing"

    def format_template(template, student_name, **kwargs):
        kwargs['student_name'] = student_name
        return template.format(**kwargs)

    # Extracting required data
    total_marks = data["totalMarks"]
    count_of_5_pointers = data["countOf5Pointers"]
    total_time = data["totalTime"]
    total_assessment = data["totalAssesment"]
    pride_accuracy_score_percentage = float(data["prideAccuracyScorePercentage"])
    consistency_percentage = data["consistencyPercentage"]
    mental_processing_speed = data["MentalProcessingSpeed"]
    mental_speed_in_sec = float(data["mentalSpeedInSec"])
    converted_mpi_score = float(data["convertedMpiScore"])
    mental_productivity_capacity = data["mentalProductivityCapacity"]
    pride_growth_percentage = data["prideGrowthPercentage"]
    mpi_consistency = float(data["mpiConsistency"])
    total_option_time = data["totalOptionTime"]
    latest_exam_date = data["latestExamDateofStudent"]
    next_exam_date = data["nextExamDate"]

    # Additional contributions
    perceive_contribution = data["perceiveContribution"]
    resolve_contribution = data["resolveContribution"]
    influence_contribution = data["influenceContribution"]
    deliver_contribution = data["deliverContribution"]
    engage_contribution = data["engageContribution"]
    attention_contribution = float(data["attentionContribution"])
    memory_contribution = float(data["memoryContribution"])
    critical_contribution = float(data["criticalContribution"])
    creative_contribution = float(data["creativeContribution"])
    mindset_contribution = float(data["mindsetContribution"])
    attitude_contribution = float(data["attitudeContribution"])
    expression_contribution = float(data["expressionContribution"])
    communication_contribution = float(data["communicationContribution"])
    collaboration_contribution = float(data["collaborationContribution"])
    leadership_contribution = float(data["leadershipContribution"])
    awareness_contribution = float(data["awarenessContribution"])
    application_contribution = float(data["applicationContribution"])
    advantage_contribution = float(data["advantageContribution"])

    # Calculating PRIDE score and categories
    pride_score = round(pride_accuracy_score_percentage)
    category = get_category(pride_score)
    personality_type = get_personality_type(pride_score)

    # Generating detailed descriptions for sections
    category_description = f"""
    0-20: Potential
    - Students in this category show initial stages of skill development and have significant room for growth. They are at the beginning of their learning journey and have the opportunity to build a strong foundation.

    21-40: Preparing
    - Students in this category are actively preparing and enhancing their skills. They have a basic understanding and are working towards solidifying their knowledge and abilities.

    41-60: Promising
    - Students in this category demonstrate promising capabilities and show good progress. They have a solid grasp of the fundamentals and are starting to excel in certain areas.

    61-80: Progressing
    - Students in this category are progressing well and showing considerable improvement. They are developing advanced skills and are on the path to high performance.

    81-100: Performing
    - Students in this category are performing at an exceptional level. They have mastered various skills and consistently deliver high-quality results.
    """

    detailed_description = f"""
    Based on {data["student_name"]}'s PRIDE score, their personality type is "{personality_type}". This suggests that they exhibit the characteristics and abilities associated with this category. Here are some insights specific to their personality type:

    - As someone who is "{personality_type}", {data["student_name"]} demonstrates a strong foundation in their PRIDE abilities. They are likely to approach tasks with a strategic mindset, ensuring that they thoroughly understand and address the requirements.

    - Their mental agility and efficiency, as indicated by their MPI score of {converted_mpi_score}, show that they are capable of processing and utilizing information effectively. This is a valuable trait that will help them excel in various academic and personal endeavors.

    - With a PRIDE accuracy percentage of {pride_accuracy_score_percentage}%, {data["student_name"]} exhibits a high level of precision in their responses. This indicates that they pay close attention to detail and strive for accuracy in their work.

    - {data["student_name"]}'s mental processing speed of {mental_processing_speed} reflects their ability to quickly understand and act on information. This is crucial for effective decision-making and problem-solving.

    - The consistency ratio of {mpi_consistency} highlights {data["student_name"]}'s reliability and dependability. Maintaining consistent performance over time is a key indicator of their commitment and discipline.

    Overall, {data["student_name"]}'s PRIDE assessment results provide a comprehensive view of their strengths and areas for development. By focusing on the insights and recommendations provided in this report, they can continue to build on their existing skills and achieve greater success in the future.
    """

    # Generating the report template
    template = f"""
    PRIDE Holistic Personality Summary for {data["student_name"]}

    The PRIDE Holistic Personality assessment evaluates {data["student_name"]} across various dimensions, measuring their potential and preparedness in multiple skill areas. Based on {data["student_name"]}'s PRIDE score, {data["student_name"]} can be categorized into different potential and performance levels. Here's a detailed breakdown of the assessment components and results:

    1. Overview of Performance

    - Total Marks: {total_marks}
    - Count of 5 Pointers: {count_of_5_pointers}
    - Total Time: {total_time}
    - Total Assessment: {total_assessment}
    - PRIDE Accuracy Score Percentage: {pride_accuracy_score_percentage}%
    - Consistency Percentage: {consistency_percentage}
    - Mental Processing Speed: {mental_processing_speed}
    - Mental Speed in Seconds: {mental_speed_in_sec}
    - Converted MPI Score: {converted_mpi_score}
    - Mental Productivity Capacity: {mental_productivity_capacity}
    - PRIDE Growth Percentage: {pride_growth_percentage}
    - MPI Consistency: {mpi_consistency}
    - Total Option Time: {total_option_time}
    - Latest Exam Date of Student: {latest_exam_date}
    - Next Exam Date: {next_exam_date}

    2. Detailed Description

    {detailed_description}

    3. Category Description

    The Category Description metric arranges activities based on the Index scores of PRIDE, Skills, and Intelligence Domains. Activities with higher Index scores are ranked higher, providing insight into {data["student_name"]}'s strengths and areas for improvement. This ranking helps identify {data["student_name"]}'s key strengths and pinpoint areas where additional focus and effort may yield significant improvements.

    {category_description}

    4. Ranking Order

    The Ranking Order metric arranges activities based on the Index scores of PRIDE, Skills, and Intelligence Domains. Activities with higher Index scores are ranked higher, providing insight into {data["student_name"]}'s strengths and areas for improvement. This ranking helps identify {data["student_name"]}'s key strengths and pinpoint areas where additional focus and effort may yield significant improvements.

    {generate_ranking_order(data)}

    5. Polarity Order

    The Polarity Order section highlights the positive and negative aspects of each skill contribution, ranked in descending order based on their values.

    {generate_polarity_order(data)}

    6. Areas for Improvement

    Areas for Improvement are identified based on contributions that fall below the optimal threshold. Focusing on these areas can help {data["student_name"]} enhance their overall performance and achieve greater success.

    {generate_areas_for_improvement(data)}

    7. Recommendations

    Based on the assessment results, here are specific recommendations for {data["student_name"]} to further develop their skills and capabilities:

    {generate_recommendations(data)}

    8.Future Outlook

    Looking ahead, {data["student_name"]} has great potential to continue progressing in their personal and academic journey. Continued focus on their strengths and targeted improvements in identified areas will pave the way for {data["student_name"]} to achieve even greater success.

    Conclusion

    This PRIDE Holistic Personality Summary provides {data["student_name"]} with valuable insights into their current capabilities and areas for development. By leveraging these insights, {data["student_name"]} can focus on enhancing their strengths and addressing areas that require improvement, ultimately achieving their academic and personal goals.

    Action Plan and Way Forward

    {generate_action_plan(data)}

    """

    report = format_template(template, student_name=data["student_name"])

    return report


# Sample input data with student name included
data = {
    "totalMarks": 249,
    "countOf5Pointers": 28,
    "totalTime": 4392,
    "totalAssesment": 1,
    "prideAccuracyScorePercentage": "55.33",
    "consistencyPercentage": 40,
    "MentalProcessingSpeed": 100,
    "mentalSpeedInSec": "25.27",
    "convertedMpiScore": "6.51",
    "mentalProductivityCapacity": 34286,
    "prideGrowthPercentage": 0,
    "mpiConsistency": "2.00",
    "totalOptionTime": 2274,
    "latestExamDateofStudent": "2024-05-22",
    "nextExamDate": "2024-09-06",
    "perceiveContribution": 68,
    "resolveContribution": 52,
    "influenceContribution": 45,
    "deliverContribution": 47,
    "engageContribution": 37,
    "attentionContribution": "14.06",
    "memoryContribution": "13.25",
    "criticalContribution": "8.84",
    "creativeContribution": "12.05",
    "mindsetContribution": "10.84",
    "attitudeContribution": "7.23",
    "expressionContribution": "9.24",
    "communicationContribution": "9.64",
    "collaborationContribution": "6.43",
    "leadershipContribution": "8.43",
    "awarenessContribution": "24.50",
    "applicationContribution": "39.76",
    "advantageContribution": "35.74",
    "attentionAccuracy": "77.78",
    "memoryAccuracy": "73.33",
    "criticalThinkingAccuracy": "48.89",
    "creativeThinkingAccuracy": "66.67",
    "mindsetAccuracy": "60.00",
    "attitudeAccuracy": "40.00",
    "expressionAccuracy": "51.11",
    "communicationAccuracy": "53.33",
    "collaborationAccuracy": "35.56",
    "leadershipAccuracy": "46.67",
    "awarenessAccuracy": "40.67",
    "applicationAccuracy": "66.00",
    "advantageAccuracy": "59.33",
    "perceiveAccuracy": "75.56",
    "resolveAccuracy": "57.78",
    "influenceAccuracy": "50.00",
    "deliverAccuracy": "52.22",
    "engageAccuracy": "41.11",
    "student_name": "Sharan"
}
# Sample student name
student_name = "Sharan"


# Generate the report
report = generate_pride_report(data)
print(report)
