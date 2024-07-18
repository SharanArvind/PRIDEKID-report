import json

def generate_pride_report(student_name, data):
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

    def format_template(template, **kwargs):
        return template.format(**kwargs)

    # Extracting data
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

    # Additional data
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

    # Generating the PRIDE report
    pride_score = round(pride_accuracy_score_percentage)
    category = get_category(pride_score)
    personality_type = get_personality_type(pride_score)

    template = """
    PRIDE Holistic Personality Summary for {student_name}
    ---------------------------------------------------

    The PRIDE Holistic Personality assessment evaluates students across various dimensions, measuring their potential and preparedness in multiple skill areas. Based on the PRIDE score, students can be categorized into different potential and performance levels. Here's a detailed breakdown of the assessment components and scoring metrics for {student_name}.

    1. PRIDE Score Interpretation
    ---------------------------------
    The PRIDE score is a holistic measure that determines where a student stands in terms of their capabilities. This score categorizes {student_name}'s performance and preparedness across different areas into five main categories: Potential, Preparing, Promising, Progressing, and Performing.

    PRIDE Score Categories:
    {category_description}

    Based on the score, {student_name} falls into the "{category}" category, which signifies {category_meaning}.

    2. Personality Type and PRIDE Performance
    ------------------------------------------
    Each student's PRIDE score places them into a unique personality type, indicating their proficiency in various abilities and their readiness to take on new challenges.

    Personality Type: {personality_type}

    Detailed Description: {detailed_description}

    3. Detailed Metrics and Algorithms
    -----------------------------------
    Here are the detailed metrics that contribute to the overall PRIDE score:

    - Mental Performance Index (MPI): {mpi_score}
    - MPI Growth Percentage: {mpi_growth_percentage}
    - Mental Productivity Capacity (MPC): {mpc_score}
    - PRIDE Accuracy Percentage: {accuracy_percentage}
    - Mental Processing Speed: {processing_speed}
    - Appropriate Decision Consistency: {consistency_ratio}

    4. Ranking Order
    -----------------
    The Ranking Order metric arranges activities based on the Index scores of PRIDE, Skills, and Intelligence Domains. Activities with higher Index scores are ranked higher, providing insight into {student_name}'s strengths and areas for improvement.

    Conclusion
    -----------
    This comprehensive PRIDE Holistic Personality assessment provides a detailed view of {student_name}'s capabilities and areas for development. It highlights their potential, preparation, promise, progress, and performance across various dimensions, guiding them towards holistic growth and success.
    """

    category_description = """
    0-20: Potential
    21-40: Preparing
    41-60: Promising
    61-80: Progressing
    81-100: Performing
    """

    category_meaning_map = {
        "Potential": "that the student has a lot of potential but needs to focus on converting this into consistent action.",
        "Preparing": "that the student is preparing well and making progress, but there is still room for improvement.",
        "Promising": "that the student shows promising abilities and is on the right track towards higher performance.",
        "Progressing": "that the student is progressing well and demonstrating strong capabilities across various dimensions.",
        "Performing": "that the student is performing exceptionally well, showcasing high levels of proficiency and readiness."
    }

    category_meaning = category_meaning_map[category]

    detailed_description = f"{student_name} demonstrates {category_meaning}"

    mpi_score = converted_mpi_score
    mpi_growth_percentage = pride_growth_percentage
    mpc_score = mental_productivity_capacity
    accuracy_percentage = pride_accuracy_score_percentage
    processing_speed = mental_processing_speed
    consistency_ratio = mpi_consistency

    report = format_template(template, student_name=student_name, category_description=category_description,
                             category=category, category_meaning=category_meaning,
                             personality_type=personality_type,
                             detailed_description=detailed_description,
                             mpi_score=mpi_score,
                             mpi_growth_percentage=mpi_growth_percentage,
                             mpc_score=mpc_score,
                             accuracy_percentage=accuracy_percentage,
                             processing_speed=processing_speed,
                             consistency_ratio=consistency_ratio)

    return report

# Sample input data
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
    "engageAccuracy": "41.11"
}

# Sample student name
student_name = "John Doe"

# Generate the report
report = generate_pride_report(student_name, data)
print(report)
