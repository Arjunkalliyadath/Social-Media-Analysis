from datasets import load_dataset

dataset = load_dataset("tweet_eval", "sentiment")

print("Training Samples:", len(dataset["train"]))
print("Validation Samples:", len(dataset["validation"]))
print("Test Samples:", len(dataset["test"]))

print("\nExample Tweet:")
print(dataset["train"][0])

print("\nLabels:")
print(dataset["train"].features["label"].names)