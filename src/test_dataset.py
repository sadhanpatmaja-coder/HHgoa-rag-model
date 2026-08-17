from datasets import load_dataset

print("Connecting to MSMARCO-XI...")

dataset = load_dataset(
    "ai4bharat/MSMARCO-XI",
    split="validation",
    streaming=True
)

print("Connected!")

print("\nDataset information:")
print(dataset)

print("\nFeatures:")
print(dataset.features)

print("\nGetting first example...")

example = next(iter(dataset))

print("\nFirst example:")
print(example)