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

    # Sample data extraction
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
    The PRIDE Holistic Personality assessment evaluates {student_name} across various dimensions, measuring their potential and preparedness in multiple skill areas. Based on {student_name}'s PRIDE score, {student_name} can be categorized into different potential and performance levels. Here's a detailed breakdown of the assessment components and scoring metrics.

    1. PRIDE Score Interpretation
    The PRIDE score is a holistic measure that determines where {student_name} stands in terms of their capabilities. This score categorizes {student_name}'s performance and preparedness across different areas into five main categories: Potential, Preparing, Promising, Progressing, and Performing.

    PRIDE Score Categories:
    {category_description}

    2. Personality Type and PRIDE Performance
    Each {student_name}'s PRIDE score places them into a unique personality type, indicating their proficiency in various abilities and their readiness to take on new challenges. {student_name}'s current personality type, "{personality_type}", suggests a nuanced understanding of their abilities and developmental stage.

    Detailed Description: {detailed_description}

    3. Detailed Metrics and Algorithms
    Mental Performance Index (MPI): {mpi_score}
    MPI Growth Percentage: {mpi_growth_percentage}
    Mental Productivity Capacity (MPC): {mpc_score}
    PRIDE Accuracy Percentage: {accuracy_percentage}
    Mental Processing Speed: {processing_speed}
    Appropriate Decision Consistency: {consistency_ratio}

    The MPI is a comprehensive indicator of {student_name}'s mental agility and efficiency, showing how swiftly and effectively they can process and utilize information. Their growth percentage reflects the incremental improvements in {student_name}'s mental performance, demonstrating the continuous effort they put into enhancing their cognitive capabilities. The MPC measures {student_name}'s capacity to generate productive mental output, a critical factor in achieving high performance. Their PRIDE accuracy percentage indicates the precision of {student_name}'s responses, which is a testament to their focused and diligent approach. Mental processing speed is the rate at which {student_name} can understand and act on information, an essential skill for quick and effective decision-making. Lastly, the consistency ratio evaluates the steadiness of {student_name}'s performance, highlighting their reliability and dependability in maintaining high standards over time.

    4. Ranking Order
    The Ranking Order metric arranges activities based on the Index scores of PRIDE, Skills, and Intelligence Domains. Activities with higher Index scores are ranked higher, providing insight into {student_name}'s strengths and areas for improvement. This ranking helps identify {student_name}'s key strengths and pinpoint areas where additional focus and effort may yield significant improvements.

    Conclusion
    This comprehensive PRIDE Holistic Personality assessment provides a detailed view of {student_name}'s capabilities and areas for development. It highlights their potential, preparation, promise, progress, and performance across various dimensions, guiding them towards holistic growth and success. By understanding their unique personality type and interpreting the detailed metrics, {student_name} can strategically plan their personal and academic growth, ensuring a well-rounded and successful future.
    """

    category_description = """
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
    Based on {student_name}'s PRIDE score, their personality type is "{personality_type}". This suggests that they exhibit the characteristics and abilities associated with this category. Here are some insights specific to their personality type:

    - As someone who is "{personality_type}", {student_name} demonstrates a strong foundation in their PRIDE abilities. They are likely to approach tasks with a strategic mindset, ensuring that they thoroughly understand and address the requirements.

    - Their mental agility and efficiency, as indicated by their MPI score of {converted_mpi_score}, show that they are capable of processing and utilizing information effectively. This is a valuable trait that will help them excel in various academic and personal endeavors.

    - With a PRIDE accuracy percentage of {pride_accuracy_score_percentage}%, {student_name} exhibits a high level of precision in their responses. This indicates that they pay close attention to detail and strive for accuracy in their work.

    - {student_name}'s mental processing speed of {mental_processing_speed} reflects their ability to quickly understand and act on information. This is crucial for effective decision-making and problem-solving.

    - The consistency ratio of {mpi_consistency} highlights {student_name}'s reliability and dependability. Maintaining consistent performance over time is a key indicator of their commitment and discipline.

    Overall, {student_name}'s PRIDE assessment results provide a comprehensive view of their strengths and areas for development. By focusing on the insights and recommendations provided in this report, they can continue to build on their existing skills and achieve greater success in the future.
    """

    mpi_score = converted_mpi_score
    mpi_growth_percentage = pride_growth_percentage
    mpc_score = mental_productivity_capacity
    accuracy_percentage = pride_accuracy_score_percentage
    processing_speed = mental_processing_speed
    consistency_ratio = mpi_consistency

    report = format_template(template, student_name=data["student_name"],
                             category_description=category_description,
                             personality_type=personality_type,
                             detailed_description=detailed_description,
                             mpi_score=mpi_score,
                             mpi_growth_percentage=mpi_growth_percentage,
                             mpc_score=mpc_score,
                             accuracy_percentage=accuracy_percentage,
                             processing_speed=processing_speed,
                             consistency_ratio=consistency_ratio)

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
