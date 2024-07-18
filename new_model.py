import random
import pandas as pd
import nltk
import tensorflow as tf
from transformers import BertTokenizer, TFAutoModelForCausalLM
from sklearn.preprocessing import MinMaxScaler

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Initialize the BERT tokenizer and model for text generation
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
text_generator = TFAutoModelForCausalLM.from_pretrained("gpt-2")

# Define the RNN model (LSTM)
class PRIDEModel(tf.keras.Model):
    def __init__(self):
        super(PRIDEModel, self).__init__()
        self.lstm = tf.keras.layers.LSTM(128, return_sequences=True)
        self.dense = tf.keras.layers.Dense(1, activation='linear')
        self.text_generator = text_generator
        self.tokenizer = tokenizer

    def call(self, inputs):
        x = self.lstm(inputs)
        return self.dense(x)

    def calculate_scores(self, accuracy, speed, consistency):
        """Calculate MPI score, growth percentage, and MPC."""
        mpi_score = (accuracy + speed + consistency) / 3
        mpi_growth_percentage = ((mpi_score - 7.5) / 7.5) * 100
        mpc = accuracy * ((2 * 30 - speed) / 30) if speed != 0 else 0  # Avoid division by zero
        return mpi_score, mpi_growth_percentage, mpc

    def classify_mpi_score(self, mpi_score):
        """Classify MPI score into a descriptive category."""
        categories = [
            "Gradually Potential", "Moderately Potential", "Steadily Potential", "Highly Potential",
            "Gradually Preparing", "Moderately Preparing", "Steadily Preparing", "Highly Preparing",
            "Gradually Promising", "Moderately Promising", "Steadily Promising", "Highly Promising",
            "Gradually Progressing", "Moderately Progressing", "Steadily Progressing", "Highly Progressing",
            "Gradually Performing", "Moderately Performing", "Steadily Performing", "Highly Performing"
        ]
        index = min(int(mpi_score // 5), len(categories) - 1)
        return categories[index]

    def generate_dynamic_section(self, score, section):
        """Generate a section of the report dynamically based on the score."""
        content_options = {
            "PRIDE Distribution": [
                "Your balanced personality is reflected in a high PRIDE score of {score:.2f}. This indicates a strong foundation in various key traits.",
                "A PRIDE score of {score:.2f} highlights your holistic development, showcasing strengths in explaining intentions, knowing details, making wise decisions, solving problems, and building relationships.",
                "With a PRIDE score of {score:.2f}, you exhibit remarkable personal traits across different areas, contributing to a well-rounded personality."
            ],
            "Intelligence Distribution": [
                "Your intelligence metrics reveal a profound understanding of core concepts and the ability to adapt plans based on situational needs.",
                "The intelligence distribution indicates a robust capability in grasping fundamental ideas and adjusting processes accordingly, reflective of your score of {score:.2f}.",
                "A score of {score:.2f} in intelligence distribution underscores your ability to understand, adapt, and apply knowledge effectively."
            ],
            "PRIDE Skill Activities Polarity Level": [
                "Your skill activities are highlighted by a high proficiency in innovative thinking, clear communication, and precise memory recall.",
                "Excelling in PRIDE skill activities, you demonstrate significant abilities in articulating intentions, remembering crucial information, and planning innovatively.",
                "The activities reveal your strengths in thinking creatively and communicating effectively, aligning with a score of {score:.2f}."
            ],
            "Cognitive Performance": [
                "Your cognitive performance is commendable, with {accuracy}% accuracy, {speed}% speed, and {consistency}% consistency, reflecting a balanced and effective cognitive process.",
                "Exhibiting {accuracy}% accuracy and {speed}% speed, you maintain a consistent performance at {consistency}%, indicating strong cognitive capabilities.",
                "With impressive metrics of {accuracy}% accuracy and {consistency}% consistency, your cognitive performance is highly efficient and reliable."
            ],
            "Mental Productivity": [
                "Your mental productivity profile showcases an MPI score of {mpi_score:.2f} and an MPC of {mpc:.2f}%, indicating robust growth and productive capabilities.",
                "An MPI growth percentage of {mpi_growth_percentage:.2f}% reflects your notable productivity, contributing to an overall score of {mpi_score:.2f}.",
                "The metrics of mental productivity reveal a solid MPI score of {mpi_score:.2f}, highlighting your continuous growth and efficiency."
            ],
            "Mental Processing and Decision Making": [
                "You process decisions with an impressive average response time of {speed:.2f} seconds, demonstrating quick and consistent decision-making abilities.",
                "Your decision-making consistency is evidenced by your speed and accuracy, showing a well-balanced approach to processing information.",
                "With a strong performance in speed and accuracy, your decision-making skills are notably effective and reliable."
            ],
            "Ranking Order": [
                "In daily activities, you excel in explaining intentions, making decisions, and solving problems, ranking high in these areas.",
                "Your strengths include clear communication, precise knowledge, and effective problem-solving, placing you at a top ranking in these skills.",
                "You consistently demonstrate strong decision-making and relationship-building skills, achieving high rankings in these areas."
            ],
            "Action Plan and Way Forward": [
                "Focus on enhancing your decision-making process and maintaining high accuracy in tasks to continue your growth trajectory.",
                "To further develop, work on refining your learning styles and deepening your understanding of fundamental concepts.",
                "Build on your existing strengths and aim to cultivate a positive and adaptive mindset for continued excellence."
            ],
            "Productivity Capacity": [
                "A productivity capacity of {score}% is exceptional, indicating a highly productive student. Continuously engage in new challenges and advanced projects to maintain and further improve productivity.",
                "Your productivity capacity of {score}% is very high. To sustain this level, set new challenges and participate in advanced coursework or projects.",
                "A productivity capacity of {score}% suggests good productivity with room for improvement. Focus on identifying areas for enhancement and seek feedback for continuous growth.",
                "A productivity capacity of {score}% reflects a need for significant improvement. Work on identifying weaknesses and develop a strategic plan for better performance."
            ]
        }

        # Select a random template and format it with the appropriate score
        content_template = random.choice(content_options[section])
        return content_template.format(
            score=score,
            mpi_score=score,
            mpi_growth_percentage=((score - 7.5) / 7.5) * 100,
            mpc=score * ((2 * 30 - score) / 30) if score != 0 else 0,  # Avoid division by zero
            accuracy=score,
            speed=score,
            consistency=score
        )

    def generate_suggestions(self, scores):
        """Generate suggestions based on scores."""
        suggestions = []
        for category, score in scores.items():
            if score < 5:
                suggestions.append(f"For {category}, consider focusing on foundational improvements.")
            elif score < 10:
                suggestions.append(f"In {category}, work on enhancing your basic skills.")
            elif score < 15:
                suggestions.append(f"Your {category} skills are developing well; aim for consistency.")
            elif score < 20:
                suggestions.append(f"Strengthen your {category} abilities to reach higher proficiency.")
            else:
                suggestions.append(f"Continue to excel in {category}; your performance is impressive.")
        return "\n".join(suggestions)

    def advanced_text_generation(self, prompt, max_length=200):
        """Generate advanced text using the text generation model."""
        inputs = self.tokenizer(prompt, return_tensors="tf")
        generated_texts = self.text_generator.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(generated_texts[0], skip_special_tokens=True)

    def generate_report(self, name, accuracy, speed, consistency):
        """Generate a comprehensive report for the student."""
        mpi_score, mpi_growth_percentage, mpc = self.calculate_scores(accuracy, speed, consistency)
        classification = self.classify_mpi_score(mpi_score)

        scores = {
            "PRIDE Distribution": mpi_score,
            "Intelligence Distribution": mpi_score,
            "PRIDE Skill Activities Polarity Level": mpi_score,
            "Cognitive Performance": accuracy,
            "Mental Productivity": mpi_score,
            "Mental Processing and Decision Making": speed,
            "Ranking Order": mpi_score,
            "Action Plan and Way Forward": mpi_score,
            "Productivity Capacity": accuracy  # Assuming Productivity Capacity is based on accuracy
        }

        report_sections = {
            "PRIDE Distribution": self.generate_dynamic_section(mpi_score, "PRIDE Distribution"),
            "Intelligence Distribution": self.generate_dynamic_section(mpi_score, "Intelligence Distribution"),
            "PRIDE Skill Activities Polarity Level": self.generate_dynamic_section(mpi_score, "PRIDE Skill Activities Polarity Level"),
            "Cognitive Performance": self.generate_dynamic_section(accuracy, "Cognitive Performance"),
            "Mental Productivity": self.generate_dynamic_section(mpi_score, "Mental Productivity"),
            "Mental Processing and Decision Making": self.generate_dynamic_section(speed, "Mental Processing and Decision Making"),
            "Ranking Order": self.generate_dynamic_section(mpi_score, "Ranking Order"),
            "Action Plan and Way Forward": self.generate_dynamic_section(mpi_score, "Action Plan and Way Forward"),
            "Productivity Capacity": self.generate_dynamic_section(accuracy, "Productivity Capacity")
        }

        suggestions = self.generate_suggestions(scores)

        report = f"""
        # Student Performance Report: {name}

        ## PRIDE Distribution
        {report_sections['PRIDE Distribution']}

        ## Intelligence Distribution
        {report_sections['Intelligence Distribution']}

        ## PRIDE Skill Activities Polarity Level
        {report_sections['PRIDE Skill Activities Polarity Level']}

        ## Cognitive Performance
        {report_sections['Cognitive Performance']}

        ## Mental Productivity
        {report_sections['Mental Productivity']}

        ## Mental Processing and Decision Making
        {report_sections['Mental Processing and Decision Making']}

        ## Ranking Order
        {report_sections['Ranking Order']}

        ## Action Plan and Way Forward
        {report_sections['Action Plan and Way Forward']}

        ## Productivity Capacity
        {report_sections['Productivity Capacity']}

        ## Suggestions for Improvement
        {suggestions}
        """

        return report

# Sample data
data = {
    "Name": ["Student A", "Student B", "Student C", "Student D"],
    "Accuracy": [18, 15, 12, 7],
    "Speed": [10, 7, 5, 2],
    "Consistency": [12, 10, 8, 4]
}
df = pd.DataFrame(data)

# Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df[["Accuracy", "Speed", "Consistency"]])
df[["Accuracy", "Speed", "Consistency"]] = scaled_data

# Generate reports for each student
pride_model = PRIDEModel()
for index, row in df.iterrows():
    report = pride_model.generate_report(row["Name"], row["Accuracy"], row["Speed"], row["Consistency"])
    print(report)
    print("\n" + "="*50 + "\n")
