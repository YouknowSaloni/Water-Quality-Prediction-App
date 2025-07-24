import joblib

# Load your original large model
model = joblib.load("pollution_model.pkl")

# Save a compressed version
joblib.dump(model, "pollution_model_compressed.pkl", compress=3)

print("✅ Compression complete! Saved as pollution_model_compressed.pkl")
