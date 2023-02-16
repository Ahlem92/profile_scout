import numpy as np
import pandas as pd
from sklearn.preprocessing import RobustScaler

def preprocess_features(data: pd.DataFrame) -> np.ndarray:
    Features = ['Age', 'Height(in cm)','Weak Foot Rating','Skill Moves',
            'International Reputation','Pace Total','Shooting Total','Passing Total','Dribbling Total',
            'Defending Total','Physicality Total','Crossing','Finishing','Heading Accuracy','Short Passing','Volleys','Dribbling',
            'Curve','Freekick Accuracy','LongPassing','BallControl','Acceleration','Sprint Speed','Agility','Reactions','Balance','Shot Power',
            'Jumping', 'Stamina','Strength','Long Shots','Aggression','Interceptions','Positioning','Vision','Penalties','Composure',
            'Marking','Sliding Tackle','Shooting Foot']

    X = data[Features]

    scaler = RobustScaler()
    X_scaled = scaler.fit_transform(X)

    data[Features] = X_scaled
    print("\n✅ data processed")
    return pd.DataFrame(X_scaled)
