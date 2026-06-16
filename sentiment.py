from datasets import load_dataset

dataset = load_dataset("tweet_eval", "sentiment")

print(dataset["train"][0])

print(dataset["train"].features["label"].names)