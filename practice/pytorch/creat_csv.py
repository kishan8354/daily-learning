
import pandas as pd
from pathlib import Path

# Dataset folders
base_dir = Path("dataset/catsAndDogs/PetImages")
cat_dir = base_dir / "Cat"
dog_dir = base_dir / "Dog"

data = []

# Cats: label 0
for image in cat_dir.iterdir():
    if image.is_file() and image.suffix.lower() in [".jpg", ".jpeg", ".png"]:
        data.append([f"Cat/{image.name}", 0])

# Dogs: label 1
for image in dog_dir.iterdir():
    if image.is_file() and image.suffix.lower() in [".jpg", ".jpeg", ".png"]:
        data.append([f"Dog/{image.name}", 1])

# Create CSV
df = pd.DataFrame(data, columns=["Animal", "Label"])
df.to_csv(base_dir / "cats_dogs.csv", index=False)

print("CSV created successfully!")
print("Total images:", len(df))
print(df.head())
