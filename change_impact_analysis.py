from transformers import pipeline

def analyze_changes(file_path):
    # Load a pre-trained model from Hugging Face
    classifier = pipeline('sentiment-analysis', model='yangheng/deberta-v3-large-absa-v1.1')
    
    # Read the Java code changes
    with open(file_path, 'r') as file:
        changes = file.read()
    
    # Perform analysis
    result = classifier(changes)
    print(f"Results for {file_path}: {result}")

if __name__ == "__main__":
    # List of Java files to analyze
    java_files = ['src/main/java/com/example/Calculator.java', 'src/main/java/com/example/Calculator.java']
    for file_path in java_files:
        analyze_changes(file_path)
